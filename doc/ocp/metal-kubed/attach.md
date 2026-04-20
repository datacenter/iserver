# Metal Kubed - Attaching hosts from provisioner

[[Back]](./README.md) [[kb]](./kb/detach.md)

## Workflow

Checks
- selected node provisioning state must be one of: 'available', 'externally provisioned', 'provisioned'
- detached annotation should be defined

Action
- delete baremetalhost.metal3.io/detached annotation
- wait for operational state to reach `OK` 

## Configurable options

```
# iserver set ocp bmh --mode attach
  --cluster TEXT     Cluster Name
  --node TEXT        Node name or __all__
  --no-wait          Wait mode
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp bmh --cluster bm1 --node bm1-1 --mode attach

OpenShift Workflow - Bare Metal Host - Attach
=============================================

OpenShift Cluster: bm1

Patch BareMetalHost
-------------------
- namespace: openshift-machine-api
- name: bm1-1

~~~
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  annotations:
    baremetalhost.metal3.io/detached: null
  name: bm1-1
  namespace: openshift-machine-api

~~~
BareMetalHost [openshift-machine-api/bm1-1] patched
- wait for BareMetalHost openshift-machine-api/bm1-1 [timeout:180s] with {"operational_state": "OK"}

+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+
| ID | Bare Metal Host       | Provisioning           | Operational | Power | Server                                                     |
+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+
| 1  | openshift-machine-api | externally provisioned | OK          | V     | redfish-virtualmedia://10.10.10.10/redfish/v1/Systems/AAAA | 
|    | bm1-1                 |                        |             |       | bm1-1-bmc-secret                                           | 
|    |                       |                        |             |       | Cert verification: X                                       | 
|    |                       |                        |             |       | UCSC-C240-M6SN                                             |
|    |                       |                        |             |       | AAAA                                                       |
+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+

Completed tasks
- bare metal hosts attached
```

[[Back]](./README.md) [[kb]](./kb/detach.md)