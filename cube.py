from cube import config, file_repository
import json
import os

config.base_path = '/cube-api'

config.schema_path = 'models'

config.telemetry = False

# Access Control

# Fix query_rewrite compatibility with SQL push down

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

def get_schema_for_user(user):
    # Here we would reach out to a service or query a table with the user->schema mappings    
    schema = ''
    
    if user == 'auth0|66230a8321e009a9c2d58b02': #tony+demo1@cube.dev
        schema = 'MULTITENANCY_CUBE_DEMO.NYC_ECOM'

    elif user == 'auth0|66230ac3b71a509d7fe0f59c': #tony+demo2@cube.dev
        schema = 'MULTITENANCY_CUBE_DEMO.AUSTIN_ECOM'

    elif user == 'google-oauth2|101269788254543291787': #tony@cube.dev
        schema = 'CUBE_DEMO.ECOM'

    # elif user == 'cube':
    #     schema = 'CUBE_DEMO.ECOM'

    return schema

@config('context_to_app_id')
def context_mapping(ctx: dict):
  return ctx['securityContext'].setdefault('schema')

@config('check_sql_auth')
def check_sql_auth(query: dict, username: str, password: str) -> dict:
  print(username)
  print(get_schema_for_user(username))
  security_context = {
    'schema': get_schema_for_user(username)
  }
  

  return {
    'password': os.environ['CUBEJS_SQL_PASSWORD'],
    'securityContext': security_context
  }

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


# contextToOrchestratorId
# canSwitchUser 
@config('can_switch_sql_user')
def can_switch_sql_user(current_user: str, new_user: str) -> dict:
  if current_user == 'cube':
    return True 
  return False


# Custom check auth. TODO: not sure it is working
#
# @config('check_auth')
# def check_auth(ctx: dict, token: str) -> None:
#   if token == 'my_secret_token':
#     ctx['securityContext'] = {}
#     return 

#   raise Exception('Access denied')



@config('repository_factory')
def repository_factory(ctx: dict) -> list[dict]:
  return file_repository('models')

@config('logger')
def logger(message: str, params: dict) -> None:
  print(f'MY CUSTOM LOGGER --> {message}: {params}')

@config('context_to_api_scopes')
def context_to_api_scopes(context: dict, default_scopes: list[str]) -> list[str]:
  return ['meta', 'data', 'graphql']


@config('semantic_layer_sync')
def sls(ctx: dict) -> list:
    return [
      {
  "name": "Preset Sync",
  "type": "preset",
  "config": {
    "database": "Cube Cloud: Multitenancy Demo",
    "api_token": os.environ['CUBEJS_PRESET_TONY_MT_TOKEN'],
    "api_secret": os.environ['CUBEJS_PRESET_TONY_MT_SECRET'],
    "workspace_url": "5276833d.us2a.app.preset.io"
  }
}
    ]
              