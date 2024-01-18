module.exports = {
  semanticLayerSync: () => {
    return [{
      type: "preset",
      name: "Preset Sync",
      config: {
        api_token: process.env.PRESET_API_TOKEN,
        api_secret: process.env.PRESET_API_SECRET,
        workspace_url: process.env.PRESET_WORKSPACE_URL
      }
    }, {
      type: "powerbi",
      name: "Powerbi Sync",
      config: {
        database: "Cube Cloud: cube_demo"
      }
    }];
  }
};
