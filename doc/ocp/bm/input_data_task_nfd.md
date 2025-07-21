# Task: nfd

Node feature discovery (nfd) operator installation with the following defaults

```
    "nfd": {
        "namespace": "openshift-nfd",
        "name": "nfd",
        "channel": "stable",
        "instance": "nfd-instance",
        "confirmation": false,
        "check-fqdn": false,
        "break-on-error": false
    }
```

The minimum task definition

```
    "nfd": {}
```

Workflow details
- operator installed from package manifest nmstate.name and nmstate.channel into nmstate.namespace
- wait until operator installation completes
- wait until nodes annotated with nfd features

```
    deployments = [
        {'namespace': 'openshift-nfd', 'name': 'nfd-controller-manager'},
        {'namespace': 'openshift-nfd', 'name': 'nfd-master'}
    ]

    daemon_sets = [
        {'namespace': 'openshift-nfd', 'name': 'nfd-worker'}
    ]
```

[Back](./input_data_tasks.md)