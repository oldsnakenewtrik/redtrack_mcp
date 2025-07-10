/*
 * Thin client for RedTrack API and MCP tool dispatcher.
 * All functions are stateless and rely on environment variable REDTRACK_KEY.
 */

const BASE = 'https://api.redtrack.io/rest/v1';

/**
 * Fetch conversions within a date range.
 * @param {{startDate:string,endDate:string}} params
 * @returns {Promise<any>}
 */
export async function getConversions({ startDate, endDate }) {
  if (!process.env.REDTRACK_KEY) {
    throw new Error('REDTRACK_KEY env var not set');
  }
  const url = `${BASE}/conversions?startDate=${startDate}&endDate=${endDate}`;
  const rsp = await fetch(url, {
    headers: { Authorization: `ApiKey ${process.env.REDTRACK_KEY}` }
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
    default:
      throw new Error('Unknown tool');
  }
}
