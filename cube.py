# Cube configuration options: https://cube.dev/docs/config

from cube import config

import requests
import json
import os


def branchregion_policy(groups):
  if '15805cbe-a32b-4ce7-ac63-d3a9b7238300' in groups:
    return {
      'member': 'order_info.users_city',
      'operator': 'equals',
      'values': ['Los Angeles'],  
    }
  elif 'c7c68de9-d937-4a79-92c0-daa83966fc47' in groups:
    return None
  else:
    return {
      'member': 'order_info.users_city',
      'operator': 'equals',
      'values': [''],  
    }

def get_groups(user_id: str, access_token: str):
    url = f"https://graph.microsoft.com/v1.0/users/{user_id}/memberOf/microsoft.graph.group"

    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    print(response.text)

    data = json.loads(response.text)
    return list(map(lambda x: x['id'], data['value']))

def get_user_by_id(user_id: str, access_token: str):
    url = f"https://graph.microsoft.com/v1.0/users/{user_id}"

    headers = {
        'Authorization': f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)

    return json.loads(response.text)

def get_access_token():
    url = 'https://login.microsoftonline.com/57149b7d-be9e-4534-bd60-cc835252a462/oauth2/v2.0/token'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'client_id': os.getenv('ENTRA_ID_CLIENT_ID'),
        'scope': os.getenv('ENTRA_ID_SCOPE'),
        'client_secret': os.getenv('ENTRA_ID_CLIENT_SECRET'),
        'grant_type': 'client_credentials'
    }

    response = requests.post(url, headers=headers, data=data)
    access_token = json.loads(response.text)['access_token']
    return access_token

@config('context_to_app_id')
def context_mapping(ctx: dict):
  return ctx['securityContext'].setdefault('team')

 
@config('query_rewrite')
def query_rewrite(query: dict, ctx: dict) -> dict:
  if 'admin' in ctx["securityContext"] and ctx["securityContext"]['admin']:
    return query
  access_token = get_access_token()
  groups = get_groups(ctx["securityContext"]["user_id"], access_token)
  filters = branchregion_policy(groups)
  if filters:
    query['filters'].append(filters)
  print(query)
  return query

@config('check_sql_auth')
def check_sql_auth(query: dict, username: str, password: str) -> dict:
  security_context = {
    'user_id': username
  }

  return {
    'password': password,
    'securityContext': security_context
  }