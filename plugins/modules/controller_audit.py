#!/usr/python
import pprint as p



from aap_export import resources


new_dict = {}
my_list = []

p.pprint(resources, indent=0)

# List user roles
for resource in resources: 
    if type(resource['related']['roles']) == list: 
        print("yep we have some roles, in a list")
        print("resource['related']['roles]': {}".format(resource['username']))
        my_dict = {
            "name": resource['first_name'] + resource['last_name'],
            "email": resource['email'],
            "is_superuser": resource['is_superuser'],
            "is_system_auditor": resource['is_system_auditor'],
            "username": resource['username'],
            }
        my_list.append(my_dict)
# Need to loop for this
#            "roles": [{ "name": resource['related']['roles']['content_object']['name'],
#                        "role_type": resource['related']['roles']['content_object']['type'],
#                        "permission_level": resource['related']['roles']['name'],
#                        "type": resource['related']['roles']['type']
#                     }]
    else:
        print("nope, no roles found in the 'related' section thats a list")


p.pprint("------------")
p.pprint("---my_list---")
p.pprint(my_list)




# for resource in resources:
#            # loop through each list in `primary_key_name` (assets)
#            for asset in input_dict[primary_key_name]:
#                # compare if asset is same as 'resource' passed in
#                if asset == resource:
#                    my_list = []
#                    # loop through each resource and append items found
#                    for item in input_dict[primary_key_name][resource]: 
#                        # check if the `search_string` in the `search_key` field
#                        if search_string.lower() in item[search_key].lower(): 
#                            # add to the list of that resource
#                            my_list.append(item) 
#                    # append the list to this cache dictionary 
#                    cache_dict = {resource: my_list}
#                    # update the final_dict with the cache_dict
#                    final_dict.update({resource: my_list})
#

#def main:


## DOCS
#  - name: import and format the teams_export    
#    controller_audit:
#      resource: 
#      - users
#    register: user_roles

#def run_module():
#    # define available arguments/parameters a user can pass to the module
#    module_args = dict(
#        secret_key=dict(type='str', required=True),
#        credential_data=dict(type='list', required=True, default=None),
#        primary_key_column=dict(type='str', required=False, default='id'),
#        database_table_name=dict(type='str', required=False, default='main_credential'),
#        state=dict(type='str', required=False, default='decrypt')
#    )
#
#    # seed the result dict in the object
#    result = dict(
#        changed=False,
#        original_message='',
#        message=''
#    )
#
#    # the AnsibleModule object for working with Ansible
#    # this includes instantiation, a couple of common attr would be the
#    # args/params passed to the execution, as well as if the module
#    # supports check mode
#    module = AnsibleModule(
#        argument_spec=module_args,
#        supports_check_mode=True
#    )
#
#    if module.check_mode:
#        module.exit_json(**result)
#
#    # For cleaner referencing, using variables for module.params[] values 
#    secret_key = module.params['secret_key']
#    credential_data = module.params['credential_data']
#    primary_key_column = module.params['primary_key_column']
#    database_table_name = module.params['database_table_name']
#    state = module.params['state']
#   
#    # vars for parsing and decrypting the '$encrypted$' string
#    encrypted_dict = {}
#    final_dict = {}
#    encrypt_string = "encrypted"
#
#    if 'decrypt' in state.lower():
#        for cred in credential_data:
#            for k, v in cred['inputs'].items():
#                if encrypt_string in str(v):
#                    # if `$encrypted$` resides in the str'ing value of the secret in the credential
#                    # then assign the (k)ey, (v)alue to a new dictionary to reference later
#                    encrypted_dict[k] = v
#
#                    # Generate an encryption key based on the following:
#                    # 1. The (k)ey or 'field' name of k,v from above
#                    # 2. `secret_key` is the CAT'd data from the `/etc/tower/SECRET_KEY` on [controller[0]] 
#                    #    ansible inventory group.
#                    # 3. The primary key of the main_credential table (pgadmin):
#                    #    in this case the default is ['id']...
#                    key = get_encryption_key(k, secret_key, cred['id'])
#                    
#
#                    # Create a python dictionary with the found matches {(k): (v)}
#                    data = {k:v} 
#                    decrypted_item = decrypt_value(key, data[k])
#
#                    cred['inputs'][k] = decrypted_item
#        result['message'] = credential_data 
#        
#    if 'encrypt' in state.lower():
#        encrypt_list = ['$encrypted', 'AESCBC']
#        for cred in credential_data:
#            for k, v in cred['inputs'].items(): #<-looping through the credential_data, outside of 'inputs' dictionary
#            # looking for the key that contains 'encrypted', and then decrypting that secret INSIDE of the 
#            # 'inputs' dictionary
#                if 'decrypted' in str(v):
#                    # get encryption key
#                    key = get_encryption_key(k, secret_key, cred['id'])
#                    decrypted_item = str(v).split('$')[-1]
#
#                    encrypted_item = encrypt_value(key, decrypted_item)                    
#
#                    cred['inputs'][k] = '$'.join(["$encrypted","UTF8","AESCBC", encrypted_item]) 
#
#        result['message'] = credential_data #encrypt_list #credential_data #encrypted_item 
#
#    if 'export' in state.lower():
#        for cred in credential_data:
#            for k, v in cred['inputs'].items():
#                if encrypt_string in str(v):
#                    # split secret value to retrieve encoded/encrypted value
#                    # for encryption
#                    key = get_encryption_key(k, secret_key, cred['id'])
#                    data = {k:v} #json.loads('{k.quote(): v.quote() }') #, "ssh_key_data": "$encrypted$UTF8$AESCBC$..."}');
#                    decrypted_item = decrypt_value(key, data[k])
#                    # structure original inputs into cred_data dictionary
#                    #original_inputs = {k: '$'.join(["hi-there","$encrypted","UTF8","AESCBC",decrypted_item])} #v}
#                    # update dict (that is outside of 'inputs') with original 'inputs' containing '$encrypted$'
#                    #cred.update(original_inputs) 
#                    cred['inputs'][k] = '$'.join(["$decrypted","UTF8","AESCBC",decrypted_item]) 
#
#        result['message'] = credential_data 
#    
#    module.exit_json(**result) #**result)
#
#def main():
#    run_module()
#
#
#if __name__ == '__main__':
#    main()
