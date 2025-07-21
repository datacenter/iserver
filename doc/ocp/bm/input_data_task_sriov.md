# Task: sriov

SR-IOV operator installation with the following defaults

```
    "sriov": {
        "namespace": "openshift-sriov-network-operator",
        "name": "sriov-network-operator",
        "channel": "stable",
        "confirmation": false,
        "check-fqdn": false,
        "break-on-error": false,
        "wait_ready": 600,
        "wait_not_ready": 180
    }
```

The minimum task definition

```
    "sriov": {}
```

Workflow details
- operator installed from package manifest nmstate.name and nmstate.channel into nmstate.namespace
- wait until operator installation completes

```
    deployments = [
        {'namespace': 'openshift-sriov-network-operator', 'name': 'sriov-network-operator'}
    ]

    daemon_sets = [
        {'namespace': 'openshift-sriov-network-operator', 'name': 'network-resources-injector'},
        {'namespace': 'openshift-sriov-network-operator', 'name': 'operator-webhook'},
        {'namespace': 'openshift-sriov-network-operator', 'name': 'sriov-network-config-daemon'}
    ]
```

SR-IOV Network Node Policy can be further defined per physical interface

Example

```
    "policy": [
        {
            "interface": "ens1f0",
            "type": "netdevice",
            "name": "ens1f0net",
            "resource": "ens1f0net",
            "vfs": "64",
            "range": "0-31"
        },
        {
            "interface": "ens1f0",
            "type": "vfio-pci",
            "name": "ens1f0dpdk",
            "resource": "ens1f0dpdk",
            "vfs": "64",
            "range": "32-63"
        }
    ]
```

Note:
- sriov.policy.interface must be defined
- sriov.policy.type must be defined and one of ['netdevice', 'vfio-pci']
- sriov.policy.name is optional and defaults to sriov.policy.interface with net or dpdk suffix
- sriov.policy.resource is optional and defaults to sriov.policy.interface with net or dpdk suffix
- sriov.policy.range is optional and must be used in case VF type split on a single interface. defaults to None

Resulting SriovNetworkNodePolicy CR that is applied (if does not exist yet - checked by name)

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: {sriov.policy.name}
  namespace: {sriov.namespace}
spec:
  deviceType: {sriov.policy.type}
  isRdma: false
  nicSelector:
    pfNames:
    - {sriov.policy.interface}#{sriov.policy.range}   -- if range defined
    - {sriov.policy.interface}                        -- if range not defined
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: "true"
  numVfs: {sriov.policy.vfs}
  resourceName: {sriov.policy.resource}
```

Example output

```
Wait for deployments ready...
- openshift-sriov-network-operator/sriov-network-operator
Wait for deamon sets ready...
- openshift-sriov-network-operator/network-resources-injector
- openshift-sriov-network-operator/operator-webhook
- openshift-sriov-network-operator/sriov-network-config-daemon
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: ens1f0net
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: false
  nicSelector:
    pfNames:
    - ens1f0#0-31
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 64
  resourceName: ens1f0net

apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: ens1f0dpdk
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  isRdma: false
  nicSelector:
    pfNames:
    - ens1f0#32-63
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 64
  resourceName: ens1f0dpdk


Completed tasks
- SR-IOV Operator installed
- SR-IOV Node Network Policy created
```

If policy is created, network node reloads may occur
- the workflow waits for sriov.wait_not_ready seconds for any node reload
- if reload is detected, then it waits sriov.wait_ready seconds for all nodes to be ready

[Back](./input_data_tasks.md)