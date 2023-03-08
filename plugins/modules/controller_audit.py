#!/usr/python
import pprint as p



from aap_export import teams

my_teams = teams

p.pprint(my_teams, indent=0)

for team in my_teams: 
    if team['related']['roles']:
        print("yep we have some roles")
        print("team['related']['roles]': {}".format(team['username']))
    else:
        print("nope, no roles found in the 'related' section")


#def main:


## DOCS
#  - name: import and format the teams_export    
#    controller_audit:
#      resource: 
#      - users
#    register: user_roles
