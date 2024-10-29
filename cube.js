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
        database: "Cube Cloud: cube_demo",
        api_token: process.env.PRESET_API_TOKEN,
        api_secret: process.env.PRESET_API_SECRET,
        workspace_url: process.env.PRESET_WORKSPACE_URL
      }
    }, {
      type: "tableau",
      name: "Tableau Sync",
      config: {
        database: "Cube Cloud: cube_demo",
        region: "10ax",
        site: "cubedevartyom",
        personalAccessToken: "demo-cube-cloud",
        personalAccessTokenSecret: process.env.TABLEAU_PAT_SECRET
      }
    }, {
      type: "metabase",
      name: "Metabase Sync",
      config: {
        database: "Cube Cloud: cube_demo",
        user: process.env.METABASE_SLS_USER,
        password: process.env.METABASE_SLS_PASSWORD,
        url: process.env.METABASE_SLS_URL
      }
    }, {
      type: "tableau-cloud",
      name: "Cube Tableau Cloud Sync",
      config: {
        database: "Cube Cloud: Cube Cloud Demo",
        region: "us-west-2b",
        site: "cubedev",
        personalAccessToken: "Cube Cloud Demo",
        personalAccessTokenSecret: "V1LqCMCdT8me10fCAJzIkg==:fQgpzthuRCmMiOlTH695HjCC0xceTZeh"
      }
    }];
  }
};