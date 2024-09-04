from cube import config, file_repository
import json
import os

# config.base_path = '/cube-api'

# config.schema_path = 'models'

# config.telemetry = False

# Access Control

# @config('query_rewrite')
# def query_rewrite(query: dict, ctx: dict) -> dict:
#   if 'user_id' in ctx['securityContext']:
#     query['filters'].append({
#       'member': 'orders_view.users_id',
#       'operator': 'equals',
#       'values': [ctx['securityContext']['user_id']]
#     })
#   return query

# Dynamic Data Model

# @config('context_to_app_id')
# def context_mapping(ctx: dict):
#   return ctx['securityContext'].setdefault('team')

@config('can_switch_sql_user')
def can_switch_sql_user(current_user: str, new_user: str) -> dict:
  return True

@config('check_sql_auth')
def check_sql_auth(query: dict, username: str, password: str) -> dict:
  print(f"username from thoughtspot: {username}")
  print(f"pw from thoughtspot: {password}")
  return {
    'password': os.environ.get('CUBEJS_SQL_PASSWORD', 'no_password'),
    'securityContext': {'tsu': username}
  }

@config('context_to_app_id')
def context_to_app_id(ctx: dict) -> str:
  sc = ctx.get('securityContext', {})
  u = sc.get('tsu', 'none')
  return f"app_id_{u}"

@config('context_to_orchestrator_id')
def context_to_orchestrator_id(ctx: dict) -> str:
  sc = ctx.get('securityContext', {})
  u = sc.get('tsu', 'none')
  return f"orchestrator_id_{u}"

# @config('driver_factory')
# def driver_factory(ctx: dict) -> None:
#   context = ctx['securityContext']
#   data_source = ctx['dataSource']
 
#   if data_source == 'postgres':
#     return {
#       'type': 'postgres',
#       'host': 'demo-db-examples.cube.dev',
#       'user': 'cube',
#       'password': '12345',
#       'database': 'ecom'
#     }


# Other

# @config('repository_factory')
# def repository_factory(ctx: dict) -> list[dict]:
#   return file_repository('models')

# @config('logger')
# def logger(message: str, params: dict) -> None:
#   print(f'MY CUSTOM LOGGER --> {message}: {params}')

# @config('context_to_api_scopes')
# def context_to_api_scopes(context: dict, default_scopes: list[str]) -> list[str]:
#   return ['meta', 'data', 'graphql']

@config('semantic_layer_sync')
def sls(ctx: dict) -> list:
    return [{
  "type": "tableau-cloud",
  "name": "Tableau Cloud Sync",
  "config": {
    "database": "Cube Cloud: Treadwell Cube Demo",
    "region": "us-west-2b",
    "site": "cubedev",
    "personalAccessToken": "treadwell_cube_demo",
    "personalAccessTokenSecret": os.environ["CUBEJS_TABLEAU_PAT_SECRET"]
  }
}, 
{
  "type": "preset",
  "name": "Preset Sync",
  "config": {
    "database": "Cube Cloud: Treadwell Cube Demo",
    "api_token": "8fc4f74e-7940-46d1-9ae6-77343f482f70",
    "api_secret": os.environ["CUBEJS_PRESET_PAT_SECRET"],
    "workspace_url": "aea9b11a.us2a.app.preset.io"
  }
}, 
{
  "type": "powerbi",
  "name": "Power BI Sync",
  "config": {
    "database": "Cube Cloud: Treadwell Cube Demo"
  }
}, 
{
  "type": "metabase",
  "name": "Metabase Sync",
  "config": {
    "database": "Cube Cloud: Treadwell Cube Demo",
    "user": "mike@cube.dev",
    "password": os.environ["CUBEJS_METABASE_PAT_SECRET"],
    "url": "partner-cube.metabaseapp.com"
  }
}]