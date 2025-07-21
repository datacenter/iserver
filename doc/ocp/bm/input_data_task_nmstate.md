# Task: nmstate

nmstate operator installation with the following defaults

```
    "nmstate": {
        "namespace": "openshift-nmstate",
        "name": "kubernetes-nmstate-operator",
        "channel": "stable",
        "instance": "nmstate",
        "confirmation": false,
        "check-fqdn": true,
        "break-on-error": false,
        "lldp": {
            "nic-fw-disable": false,
            "enable": false,
            "include-down": true,
            "delete-nncp": true
        }
    }
```

The minimum task definition

```
    "nmstate": {}
```

Workflow details
- operator installed from package manifest nmstate.name and nmstate.channel into nmstate.namespace
- wait until operator installation completes
- nmstate.instance created with default empty spec
- wait until nns available per node
- if lldp.nic-fw-disable
    - for every physical ethernet interface
    - check priv flags with ethtools
    - if lldp enabled on fw level, then disable it
    - Intel NIC 700/800 series supported
- if lldp.enable
    - check nns for every physical ethernet interface
    - if lldp disabled then enable it with extra check on interface state vs nmstate.lldp.include-down flag
    - lldp is enabled on interface using nncp
    - nmstate.lldp.delete-nncp control if nncp policies are deleted

```
    deployments = [
        {'namespace': 'openshift-nmstate', 'name': 'nmstate-cert-manager'},
        {'namespace': 'openshift-nmstate', 'name': 'nmstate-console-plugin'},
        {'namespace': 'openshift-nmstate', 'name': 'nmstate-operator'},
        {'namespace': 'openshift-nmstate', 'name': 'nmstate-webhook'}
    ]
```

[Back](./input_data_tasks.md)