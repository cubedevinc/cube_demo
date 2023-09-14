module.exports = {
  // Mapping of security contexts to data model versions
  // https://cube.dev/docs/reference/configuration/config#contexttoappid
  contextToAppId: ({
    securityContext
  }) => {
    //return securityContext.team;
    return securityContext;
  },
  // Security hook which is run before a query is executed
  // https://cube.dev/docs/reference/configuration/config#queryrewrite
  // queryRewrite: (query, {
  //   securityContext
  // }) => {
  //   if (!securityContext.team) {
  //     securityContext.team = 'public';
  //   }
  //   return query;
  // },
  checkSqlAuth: (query, username) => {
    const securityContext = {
      team: username
    };
    return {
      password: process.env.CUBEJS_SQL_PASSWORD,
      securityContext: securityContext
    };
  },
  semanticLayerSync: () => {
    return [{
      type: "preset",
      name: "828 Sync",
      config: {
        database: "828 Take 2",
        api_token: "448d9518-3d7a-41e3-9bda-e626b1646c32",
        api_secret: "e5e5374a64e12b0f7907e417f0d93ad11e7cbe0046181ba1896671d9949c7120",
        workspace_url: "5276833d.us2a.app.preset.io"
      }
    }, {
      type: "tableau",
      name: "Tableau Sync",
      config: {
        database: "Cube Cloud",
        region: "10ax",
        site: "tonycube",
        personalAccessToken: "cube demo",
        personalAccessTokenSecret: process.env.CUBEJS_TABLEAU_PAT_SECRET
      }
    }];
  }
};