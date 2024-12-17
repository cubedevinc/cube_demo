cube(`orders`, {
  sql_table: `"ECOM"."ORDERS"`,
  
  joins: {
    
  },
  
  dimensions: {
    id: {
      sql: `${CUBE}."ID"`,
      type: `number`,
      primary_key: true
    },
    
    status: {
      sql: `${CUBE}."STATUS"`,
      type: `string`
    },
    
    created_at: {
      sql: `${CUBE}."CREATED_AT"`,
      type: `time`
    },
    
    completed_at: {
      sql: `${CUBE}."COMPLETED_AT"`,
      type: `time`
    }
  },
  
  measures: {
    count: {
      type: `count`
    }
  },
  
  pre_aggregations: {
    // Pre-aggregation definitions go here.
    // Learn more in the documentation: https://cube.dev/docs/caching/pre-aggregations/getting-started
  }
});
