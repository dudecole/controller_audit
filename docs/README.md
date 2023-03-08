# controller_audit

This module allows for auditing Ansible Automation Platform Controller resources utilizing the `ansible.controller` collection.

This source code includes a playbook with the tasks to `ansible.controller.export` Controller resources into a register, then using this module, `controller_audit` to format the data in a more user-friendly API response schema.

## Building and Installing
There is no additional configuration required to implement this into a pre-existing AAP Controller environment, or even just using this from `ansible-core` CLI.

### Variables and Creds
In the `./group_vars/creds.yml` vaulted file, contains three variables for `ansible.controller.export` to consume, and creating this credentials file will eliminate the need to run this from AAP Controller.  

*./group_vars/creds.yml*
```yaml

controller_host: "< ip-address >"
controller_username: "< controller-user >"
controller_password: "< controller-password >"

```

### Vaulting The Creds File

After creating the credentials file, encrypt the `./group_vars/creds.yml` file using the following steps:

*vaulting ./group_vars/creds.yml*
```yaml
ansible-vault encrypt ./group_vars/creds.yml

```

*enter a vault password*
```console

New Vault password:          
Confirm New Vault password:

Encryption successful   
```

### Alternatives to Vaulting Creds File

If preferred, the alternative to running this playbook with the `./group_vars/creds.yml` file, the other option is to create either the credential in AAP Controller Web UI.  The credentials that can be created and consumed would be:

- `vault` AAP Credential
- `custom` AAP Credential

For help on creating a custom AAP Credential, please check the docs [here.](https://docs.ansible.com/automation-controller/latest/html/userguide/credential_types.html)

## Running

To run this source locally, you will need to make sure the requirments are met first.  They are here as follows:

### Run Locally
    
`ansible-playbook`

*install ansible.controller collection*
```console
[root@something]# ansible-galaxy collection install ansible.controller

```

`ansible-navigator`

*install ansible-navigator*
```console
[root@something]# python3 -m virtualenv venv
[root@something]# source venv/bin/activate
[root@something]# pip install ansible-navigator
```

### Run on Controller Web UI
- create an AAP Project with [this source code](https://github.com/dudecole/controller_audit)
- create a job template with the `query_users.yml` playbook
- Specify to run certain parts of the play; `tags: format or export`
- Attach the AAP credential to the job_template to decrypt the vaulted `./group_vars/creds.yml` file












