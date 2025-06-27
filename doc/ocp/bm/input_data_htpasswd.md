# httpasswd

OpenShift cluster installation creates kubeadmin user with generated password. iserver supports optional [task](./input_data_tasks.md) that runs after OpenShift cluster is successfully installed to add identity provider with htpasswd authentication file as an input.

## Example

Task definition in tasks.json file

```
[
    {
        "identity": {
            "provider": "htpasswd",
            "filename": "myhtpasswd",
            "admin": [
                "__ALL__"
            ]
        }
    }
]
```

myhtpasswd file content create offline, check [here](https://docs.redhat.com/en/documentation/openshift_container_platform/4.10/html-single/authentication_and_authorization/index#identity-provider-creating-htpasswd-file-linux_configuring-htpasswd-identity-provider) for guidance

```
user1:$2y$05$xo...
user2:$2y$05$xo...
```

[Back](../BareMetalCluster.md)
