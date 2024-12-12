from cube import config
import os

@config('semantic_layer_sync')
def semantic_layer_sync(ctx: dict) -> list[dict]:
  return [
    {
      'type': 'tableau',
      'name': 'Tableau Cloud Sync',
      'useRlsFilters': True,
      'config': {
        'region': 'us-west-2b',
        'site': 'cubedev',
        'personalAccessToken': 'treadwell_cube_demo',
        'personalAccessTokenSecret': os.environ['CUBEJS_TABLEAU_PAT_SECRET'],
        'database': 'Cube Cloud: Treadwell Cube Demo',
      },
    },
    {
      "name": "Preset Sync",
      "type": "preset",
      "config": {
        "api_secret": os.environ['CUBEJS_PRESET_PAT_SECRET'],
        "api_token": "04988220-0955-487b-b656-08b8c9c6450f",
        "database": "Cube Cloud: Treadwell Cube Demo",
        "workspace_url": "5276833d.us2a.app.preset.io"
      }
    }
  ]

@config('check_sql_auth')
def check_sql_auth(req: dict, user_name: str, password: str) -> dict:
  print(user_name)
  
  return {
    'password': os.environ['CUBEJS_SQL_PASSWORD'],
    'securityContext': {
      'user_name': user_name,
      'manager_state': "us-la"
    }
  }

@config('query_rewrite')
def query_rewrite(query: dict, ctx: dict) -> dict:
  user_name = ctx.get('securityContext', {}).get('user_name', 'cube')
 
  # if user_name != 'cube':
  #   query['filters'].append({
  #     'member': 'users.user_name',
  #     'operator': 'equals',
  #     'values': [user_name],
  #   })
 
  return query

@config('can_switch_sql_user')
def can_switch_sql_user(current_user: str, new_user: str) -> dict:
  return True


@config('context_to_app_id')
def context_to_app_id(ctx: dict) -> str:
  user_name = ctx.get('securityContext', {}).get('user_name', 'cube')
  return f"CUBE_APP_{user_name}"
 
@config('context_to_orchestrator_id')
def context_to_orchestrator_id(ctx: dict) -> str:
  user_name = ctx.get('securityContext', {}).get('user_name', 'cube')
  return f"CUBE_APP_{user_name}"

@config('scheduled_refresh_contexts')
def scheduled_refresh_contexts() -> list[object]:
  return [
    {
      'securityContext': {
        'user_name': 'mike@cube.dev'
      }
    },
    {
      'securityContext': {
        'user_name': 'cube'
      }
    }
  ]

@config('context_to_roles')
def context_to_roles(context):
    if context.get("securityContext", {}).get("user_name", "cube") == "mike@cube.dev":
      return ["sales_manager"]
    else:
      return context.get("securityContext", {}).get("roles", [])
