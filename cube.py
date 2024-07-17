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

# @config('check_sql_auth')
# def check_sql_auth(query: dict, username: str, password: str) -> dict:
#   security_context = {
#     'team': username
#   }
#   return {
#     'password': os.environ['CUBEJS_SQL_PASSWORD'],
#     'securityContext': security_context
#   }

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
  "type": "preset",
  "name": "Preset Sync",
  "config": {
    "database": "Morgan Cube Cloud Demo",
    "api_token": "e1fe9756-df01-424b-b7d1-b15d46b2f6fa",
    "api_secret": "29e87c9893ea94fc51149adb96c9ce15b30e8923a6f57fa8cf049276445b68db",
    "workspace_url": "5276833d.us2a.app.preset.io"
  }
}, 
{
  "type": "tableau-cloud",
  "name": "Tableau Cloud Sync",
  "config": {
    "database": "Cube Cloud Demo: Morgan",
    "region": "us-west-2b",
    "site": "cubedev",
    "personalAccessToken": "cube500",
    "personalAccessTokenSecret": "mqPr0b1jRBedFOtMNsrwKQ==:obKzFgZoAmEWQdnc00EIsYHI8rFtHPcx"
  }
}]