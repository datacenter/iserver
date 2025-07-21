# Task: identity

- adds identity provider of HTPasswd type with user credentials defined in input file located in root directory
- selected or all users defined in the htpasswd file are configured with cluster-admin role
- htpasswd file has to be created offline, check [here](https://docs.redhat.com/en/documentation/openshift_container_platform/4.10/html-single/authentication_and_authorization/index#identity-provider-creating-htpasswd-file-linux_configuring-htpasswd-identity-provider) for guidance
- kubeadmin user is by default created by assisted installer workflow, you may decide to delete it automatically

```
    "tasks": [
        {
            "identity": {
                "provider": "htpasswd",
                "filename": "htpasswd",
                "admin": [
                    "__ALL__"
                ]
            }
        },
        {
            "identity": {
                "provider": "kubeadmin",
                "delete": false
            }
        }
```

[Back](./input_data_tasks.md)