module.exports = {
  semanticLayerSync: () => {
    return [{
      type: "tableau",
      name: "Tableau Server Sync",
      useRlsFilters: true,
      config: {
        database: "Cube Cloud: Treadwell Cube Demo",
        region: "us-west-2b",
        site: "cubedev",
        personalAccessToken: "treadwell_cube_demo",
        personalAccessTokenSecret: process.env.CUBEJS_TABLEAU_PAT_SECRET
      }
    }];
  },

  checkSqlAuth: (req, user_name, password) => {
    console.log(user_name);
    
    return {
      password: process.env.CUBEJS_SQL_PASSWORD,
      securityContext: {
        user_name: user_name
      },
    };
  },

  canSwitchSqlUser: (current_user, new_user) => {
    return true;
  }
};
