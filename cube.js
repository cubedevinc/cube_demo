module.exports = {
  // Mapping of security contexts to data model versions
  // https://cube.dev/docs/reference/configuration/config#contexttoappid
  contextToAppId: ({ securityContext }) => {
    return securityContext.team
  },
  
  // Security hook which is run before a query is executed
  // https://cube.dev/docs/reference/configuration/config#queryrewrite
  queryRewrite: (query, { securityContext }) => {
    if (!securityContext.team) {
      securityContext.team = 'public'
    }

    return query
  },

  checkSqlAuth: (query, username) => {
    const securityContext = {
      team: username
    } 

    return {
      password: process.env.CUBEJS_SQL_PASSWORD,
      securityContext: securityContext,
    };
  }

  
};