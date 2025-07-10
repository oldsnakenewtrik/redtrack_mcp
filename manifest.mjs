/*
 * Model Context Protocol manifest generated at runtime.
 */
export const manifest = {
  schema_version: 'v0.6',
  name: 'redtrack_attribution',
  description: 'Query RedTrack conversions and campaigns',
  tools: [
    {
      name: 'get_conversions',
      description: 'Return a list of conversions between two dates (YYYY-MM-DD)',
      input_schema: {
        type: 'object',
        properties: {
          startDate: { type: 'string', format: 'date' },
          endDate: { type: 'string', format: 'date' }
        },
        required: ['startDate', 'endDate']
      }
    }
  ]
};
