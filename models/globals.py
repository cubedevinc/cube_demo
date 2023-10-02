from cube import TemplateContext
import os
 
template = TemplateContext()

@template.function
def get_scheduled_refresh():
  name = 'CUSTOM_ENV_PREAGGS_ENABLE'
  if name in os.environ:
    return str(str(os.environ[name]).lower() == 'true').lower()
  return 'false'

@template.function
def masked(sql, security_context):
  trusted_teams = ['cx', 'exec' ]
  is_trusted_team = security_context.setdefault('team') in trusted_teams
  if is_trusted_team:
    return sql
  else:
    return "\"'--- masked ---'\""