from cube import TemplateContext
import os
 
# template = TemplateContext()

# @template.function('masked')
# def masked(sql, security_context):
#   trusted_teams = ['cx', 'exec' ]
#   is_trusted_team = security_context.setdefault('team') in trusted_teams
#   if is_trusted_team:
#     return sql
#   else:
#     return "\'--- masked ---\'"