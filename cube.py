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
  ]

@config('check_sql_auth')
def check_sql_auth(req: dict, user_name: str, password: str) -> dict:
  print(user_name)
  
  return {
    'password': password,
    'securityContext': {
      'user_name': user_name
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
