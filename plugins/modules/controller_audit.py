DOCUMENTATION = '''
---
module: controller_audit 
author: "darren cole(@dudecole)"
short_description: query ansible.controller.export'ed resource data, and format for only necessary audit fields.
description:
    - Export Controller resources and format to only include important fields.  See
      U(https://www.ansible.com/tower) for an overview. <-## CHANGE URL
options:
    resources:
      description:
        - Resources/Assets exported using the `Ansible.Controller.Export` module 
      required: True
      type: list
    audit_item:
      description:
        - The Controller/Asset chosen to be exported by the `ansible.controller.export` module 
      type: str
'''


EXAMPLES = '''

- name: Export from controller
  ansible.controller.export:
    controller_host: "{{ controller_host }}"
    controller_username: "{{ controller_username }}"
    controller_password: "{{ controller_password }}"
    users: all
    validate_certs: false
  register: teams_export
  tags: 
  - export
  - format

- name: import and format the teams_export    
  controller_audit:
    audit_item: users
    resources: "{{ teams_export.assets.users }}"
  register: user_roles
  tags: format
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():

    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        audit_item=dict(type='str', required=True, default=None),
        resources=dict(type='list', required=True, default=None)
    )

    # seed the result dict in the object
    result = dict(
        changed=False,
    )

    # the AnsibleModule object for working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    # For cleaner referencing, using variables for module.params[] values 
    audit_item = module.params['audit_item']
    resources = module.params['resources']
   
    # used for the restructuring of dictionaries
    role_list = []
    my_dict = {}
    role_dict = {}

    # List user roles
    if 'user' in audit_item:
        
        for resource in resources: 
            name = str(resource['username'])
            my_dict[name] = { 
                "name": resource['first_name'] +' '+ resource['last_name'],
                "username": resource['username'],
                "email": resource['email'],
                "is_superuser":  resource['is_superuser'],
                "is_system_auditor": resource['is_system_auditor'],
                }
           
            for role in resource['related']['roles']:
                role_dict = {}
                if 'content_object' in role:
                    role_name = str(role['content_object']['type']) 
                    role_dict[role_name] = { 
                        "resource_name": role['content_object']['name'],
                        "role_permission_name": role['name'],
                        }
                else:
                    role_name = "NO CONTENT OBJECT"
                    role_dict[role_name] = { 
                        "role_type": role['type'],
                        "role_permission_name": role['name']
                        }
                role_list.append(role_dict)

            my_dict[name]["roles"] = role_list
            role_list = []
           
        else:
            print("nope, no roles found in the 'related' section thats a list")


        result['msg'] = my_dict
    module.exit_json(**result) 

def main():
    run_module()


if __name__ == '__main__':
    main()
    
