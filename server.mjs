import express from 'express';
import { manifest } from './manifest.mjs';
import { runTool } from './redtrack.mjs';

// Helper to support both simple and JSON-RPC 2.0 payloads
async function processRequest(body) {
  let tool, input, id = null, isJsonRpc = false;
  if (body && body.jsonrpc === '2.0' && body.method === 'run') {
    isJsonRpc = true;
    id = body.id ?? null;
    tool = body.params?.tool;
    input = body.params?.input;
  } else {
    tool = body.tool;
    input = body.input;
  }
  const result = await runTool({ tool, input });
  return isJsonRpc ? { jsonrpc: '2.0', id, result } : result;
}

const app = express();
app.use(express.json());

// MCP required endpoints
app.get('/manifest', (_, res) => {
  res.json(manifest);
});

app.post('/run', async (req, res) => {
  try {
    const result = await processRequest(req.body);
    res.json(result);
  } catch (err) {
    console.error(err);
    res.status(500).json({ isError: true, content: [err.message] });
  }
});

// Additional aliases for various IDE expectations
app.get('/', (_, res) => res.json(manifest));
app.post('/', async (req, res) => {
  try {
    const result = await processRequest(req.body);
    res.json(result);
  } catch (err) {
    console.error(err);
    res.status(500).json({ isError: true, content: [err.message] });
  }
});

// /mcp alias (e.g., bigquery example)
app.get('/mcp', (_, res) => res.json(manifest));
app.post('/mcp', async (req, res) => {
  try {
    const result = await processRequest(req.body);
    res.json(result);
  } catch (err) {
    console.error(err);
    res.status(500).json({ isError: true, content: [err.message] });
  }
});

// Nested /mcp/manifest and /mcp/run paths for IDE compatibility
app.get('/mcp/manifest', (_, res) => res.json(manifest));
app.post('/mcp/run', async (req, res) => {
  try {
    const result = await processRequest(req.body);
    res.json(result);
  } catch (err) {
    console.error(err);
    res.status(500).json({ isError: true, content: [err.message] });
  }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`RedTrack MCP server listening on port ${PORT}`);
});
