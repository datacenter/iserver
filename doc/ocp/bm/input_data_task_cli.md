# Task: cli

- executes arbitrary list of commands
- configures .bashrc of core user with cluster http proxy or custom http proxy settings
- installs cli tools on the cluster management node selected with kube:true
- cli tools can be enabled with true value and then follow the built-in default
- use '{"enabled": true}' JSON structure with extra configurable options for version and url control

Basic example

```
    "tasks": [
        {
            "cli": {
                "exec": [
                    "oc get node"
                ],
                "bashrc": true,
                "cilium": true,
                "helm": true,
                "hubble": true,
                "virtctl": true
            }
        }
    ]
```


Details:
- [bashrc](./input_data_task_cli_bashrc.md)
- [cilium](./input_data_task_cli_cilium.md)
- [helm](./input_data_task_cli_helm.md)
- [hubble](./input_data_task_cli_hubble.md)
- [virtctl](./input_data_task_cli_virtcl.md)

[Back](./input_data_tasks.md)