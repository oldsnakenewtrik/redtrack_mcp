Below is a concrete, end‑to‑end development plan for a **portable Model‑Context‑Protocol (MCP) server that exposes RedTrack™ data and is deployed exclusively on Railway**.
The design eliminates any need for local or persistent files; every artefact (manifest, schemas, etc.) is generated at runtime and served from memory, so the service can be used from *any* device with nothing more than a browser or IDE.

---

## 1. Technical foundations

| Layer       | Choice                                                       | Rationale                                                                                 |
| ----------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| Runtime     | **Node 18 LTS** (supported natively by Railway)              | Fast boot, abundant examples, easy to stream JSON.                                        |
| Framework   | **Express 4**                                                | Tiny footprint, compatible with Railway’s “Web service” template. ([Railway Docs][1])     |
| Deployment  | **Railway “Deploy Node/Express” template** (one‑click or CI) | No containers to build; auto‑detects `package.json`. ([Railway][2])                       |
| Protocol    | **Model Context Protocol v0.6**                              | Defines `/manifest`, `/run`, error model, etc. ([Model Context Protocol][3], [Medium][4]) |
| Data source | **RedTrack Public REST API**                                 | Endpoints such as `GET /conversions`, `GET /campaigns`. ([api.redtrack.io][5])            |

---

## 2. High‑level architecture

```text
┌───────────┐   HTTP   ┌─────────────────────┐   HTTPS    ┌──────────────────────┐
│ IDE / LLM │ ───────▶ │ MCP Server (Railway)│ ─────────▶ │ RedTrack REST API    │
└───────────┘          │  /manifest          │            │  (api.redtrack.io)   │
                       │  /run               │◀────────── │                      │
                       └─────────────────────┘            └──────────────────────┘
```

*Everything* in the shaded box is stateless; data lives only in RAM for the lifetime of the request.

---

## 3. Repository skeleton (5 files)

```
.
├─ server.mjs          // Express bootstrap + routes
├─ redtrack.mjs        // Thin client for RedTrack endpoints
├─ manifest.mjs        // JS object exporting MCP manifest
├─ package.json
└─ README.md           // Docs only; optional for users
```

> **No YAML/JSON assets on disk:** `manifest.mjs` returns a JS object which Express serialises to JSON on the fly, satisfying the “no local files” requirement.

---

## 4. Key implementation steps

### 4.1 Bootstrap Express

```js
import express from 'express';
import { manifest } from './manifest.mjs';
import { runTool }  from './redtrack.mjs';

const app = express();
app.use(express.json());

// MCP endpoints
app.get('/manifest', (_, res) => res.json(manifest));
app.post('/run', async (req, res) => {
  try { res.json(await runTool(req.body)); }
  catch (e) { res.json({ isError: true, content: [`${e.message}`]}); }
});

app.listen(process.env.PORT || 3000);
```

### 4.2 Build RedTrack client

```js
const BASE = 'https://api.redtrack.io/rest/v1';
export async function getConversions({ startDate, endDate }) {
  const rsp = await fetch(
      `${BASE}/conversions?startDate=${startDate}&endDate=${endDate}`,
      { headers: { Authorization: `ApiKey ${process.env.REDTRACK_KEY}` }});
  if (!rsp.ok) throw new Error(`RedTrack error ${rsp.status}`);
  return rsp.json();
}
```

### 4.3 Generate MCP manifest in memory

```js
export const manifest = {
  schema_version: 'v0.6',
  name: 'redtrack_attribution',
  description: 'Query RedTrack conversions and campaigns',
  tools: [{
    name: 'get_conversions',
    description: 'Return a list of conversions in a date range',
    input_schema: {
      type: 'object',
      properties: {
        startDate: { type: 'string', format: 'date' },
        endDate:   { type: 'string', format: 'date' }
      },
      required: ['startDate','endDate']
    }
  }]
};
```

### 4.4 Implement `/run`

```js
export async function runTool({ tool, input }) {
  if (tool === 'get_conversions') {
    const rows = await getConversions(input);
    return { content: [rows] };      // MCP expects `content` array
  }
  throw new Error('Unknown tool');
}
```

---

## 5. Railway deployment walkthrough

1. **Fork / push** the repository to GitHub.
2. **Create project** → *New* → *Deploy from GitHub* → select repo.
3. When Railway asks for environment variables, add:

   | Key            | Value                   | Notes                 |
   | -------------- | ----------------------- | --------------------- |
   | `REDTRACK_KEY` | *Your RedTrack API key* | Do **not** hard‑code. |
   | `NODE_ENV`     | `production`            |                       |
4. Railway auto‑installs dependencies & exposes your service at
   `https://redtrack‑mcp.up.railway.app` (example).
5. **Verify**: `curl https://…/manifest` returns the JSON manifest.

*(No Dockerfile is needed; Railway’s Node builder handles everything.)*

---

## 6. Consuming from an IDE

Many AI‑enhanced IDEs (Cursor, Continue, Codeium, etc.) accept an *array* of MCP endpoints.
Once deployed, you can copy‑paste the following array into the IDE’s “Model Context Protocol servers” setting:

```json5
[
  "https://redtrack-mcp.up.railway.app"
]
```

The IDE will:

1. Fetch `/manifest` to learn available tools.
2. POST to `/run` whenever the model invokes `get_conversions`, etc.

Because the manifest is self‑describing and served dynamically, **no additional configuration** is required on client machines.

---

## 7. Optional enhancements

| Feature                          | How to add                                                    | Keeps “no files” guarantee? |
| -------------------------------- | ------------------------------------------------------------- | --------------------------- |
| **More tools** – campaigns, logs | Add entries in `manifest.mjs` and handlers in `redtrack.mjs`. | ✔                           |
| **Rate‑limit caching**           | In‑memory `Map` keyed by query string for 60 s.               | ✔                           |
| **Auth proxy**                   | Accept IDE‑side JWT, verify, then call RedTrack.              | ✔                           |
| **CI/CD**                        | Enable Railway‑triggered deploy on push (`railway up`).       | ✔                           |

---

## 8. Checklist before shipping

1. ✅ `npm run lint && npm test` passes.
2. ✅ `curl /manifest` & `curl -X POST /run …` return expected JSON.
3. ✅ Railway “Health check” configured to call `/manifest`.
4. ✅ Secrets stored only in Railway’s *Variables* pane.
5. ✅ README includes quick‑start and the IDE array snippet.

---

### You now have a **stateless, single‑click‑deploy MCP server** that bridges any LLM‑powered tool or IDE with RedTrack attribution data—portable, reproducible, and zero‑setup on every device.

[1]: https://docs.railway.com/guides/express?utm_source=chatgpt.com "Deploy an Express App | Railway Docs"
[2]: https://railway.com/deploy/Abo1zu?utm_source=chatgpt.com "Deploy Node.js on Railway"
[3]: https://modelcontextprotocol.io/docs/concepts/tools?utm_source=chatgpt.com "Tools - Model Context Protocol"
[4]: https://medium.com/%40sainitesh/model-context-protocol-mcp-how-to-build-your-own-mcp-server-d1dd172aea02?utm_source=chatgpt.com "Model Context Protocol (MCP): How to Build Your Own MCP Server?"
[5]: https://api.redtrack.io/docs/index.html?utm_source=chatgpt.com "Swagger UI - Redtrack API latest"
