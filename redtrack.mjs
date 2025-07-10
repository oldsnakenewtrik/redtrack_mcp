/*
 * Thin client for RedTrack API and MCP tool dispatcher.
 * All functions are stateless and rely on environment variable REDTRACK_KEY.
 */

const BASE = 'https://api.redtrack.io';

// Helper to fetch all pages (RedTrack pagination via ?page & per)
async function fetchAllPages(endpoint, params = {}, per = 1000) {
  let page = 1;
  let all = [];
  // use URLSearchParams for readability
  const baseParams = new URLSearchParams(params);
  baseParams.set('api_key', process.env.REDTRACK_KEY);
  baseParams.set('per', per);
  while (true) {
    baseParams.set('page', page);
    const url = `${BASE}${endpoint}?${baseParams.toString()}`;
    const rsp = await fetch(url, { headers: { 'Content-Type': 'application/json' } });
    if (!rsp.ok) {
      throw new Error(`RedTrack error ${rsp.status}`);
    }
    const data = await rsp.json();
    if (Array.isArray(data)) {
      all = all.concat(data);
      if (data.length < per) break;
    } else if (Array.isArray(data?.items)) {
      all = all.concat(data.items);
      if (data.items.length < per) break;
    } else {
      // unknown shape, just return
      return data;
    }
    page += 1;
  }
  return all;
}

/**
 * Fetch all campaigns (optionally filtered by date range).
 * @param {{date_from?:string,date_to?:string}} params
 */
export async function getCampaigns(params = {}) {
  if (!process.env.REDTRACK_KEY) throw new Error('REDTRACK_KEY env var not set');
  const { date_from, date_to, ...rest } = params;
  const query = { ...rest };
  if (date_from) query.date_from = date_from;
  if (date_to) query.date_to = date_to;
  return fetchAllPages('/campaigns', query, 1000);
}

/**
 * Fetch conversions within a date range.
 * @param {{startDate:string,endDate:string}} params
 * @returns {Promise<any>}
 */
export async function getConversions({ startDate, endDate }) {
  if (!process.env.REDTRACK_KEY) {
    throw new Error('REDTRACK_KEY env var not set');
  }
  const url = `${BASE}/conversions?date_from=${startDate}&date_to=${endDate}&api_key=${process.env.REDTRACK_KEY}`;
  const rsp = await fetch(url, {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  if (!rsp.ok) {
    throw new Error(`RedTrack error ${rsp.status}`);
  }
  return rsp.json();
}

/**
 * MCP run dispatcher – routes tool calls to implementations.
 * @param {{tool:string,input:any}} body
 * @returns {Promise<{content:any,isError?:boolean}>}
 */
export async function runTool({ tool, input }) {
  if (!tool) {
    return { content: ['pong'] };
  }
  switch (tool) {
    case 'ping':
      return { content: ['pong'] };
    case 'get_conversions':
      return { content: [await getConversions(input)] };
    case 'get_campaigns':
      return { content: [await getCampaigns(input)] };
    default:
      throw new Error('Unknown tool');
  }
}
