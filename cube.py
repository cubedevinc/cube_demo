from cube import config
import os

@config('can_switch_sql_user')
def can_switch_sql_user(current_user: str, new_user: str) -> dict:
  return True

@config('check_sql_auth')
def check_sql_auth(req: dict, user_name: str, password: str) -> dict:
  valid_password = os.getenv('CUBEJS_SQL_PASSWORD')
  if password and password != valid_password:
    raise Exception('Access denied')
  return {
    'password': valid_password,
    'securityContext': {
      'user_name': user_name
    }
  }

@config('query_rewrite')
def query_rewrite(query: dict, ctx: dict) -> dict:
  user_name = ctx.get('securityContext', {}).get('user_name', 'cube')
  if user_name != "cube": 
    query['filters'].append({
      'member': 'revenue_margin.supplier_region',
      'operator': 'equals',
      'values': regions.get(user_name, {}).get('regions', ['AMERICA']),
    })
  return query

regions = {
  'morgan@cube.dev': {'regions': ['EUROPE']},
  'mike@cube.dev': {'regions': ['MIDDLE EAST']}
}
