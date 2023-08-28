module.exports = {
  // Mapping of security contexts to data model versions
  // https://cube.dev/docs/reference/configuration/config#contexttoappid
  contextToAppId: ({
    securityContext
  }) => {
    return securityContext.team;
  },
  // Security hook which is run before a query is executed
  // https://cube.dev/docs/reference/configuration/config#queryrewrite
  queryRewrite: (query, {
    securityContext
  }) => {
    if (!securityContext.team) {
      securityContext.team = 'public';
    }
    return query;
  },
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
      name: "Preset Sync",
      config: {
        database: "828 Take 2",
        api_token: "8623f3be-8ab7-466c-a8c3-a312ba440864",
        api_secret: "3bb335ac0b1208350e592f99df007db4f19f3aa81e4e3cecf6202601a0c53eba",
        workspace_url: "5276833d.us2a.app.preset.io"
      }
    }];
  }
};