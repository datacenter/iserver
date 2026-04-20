# Metal Kubed - Power on

[[Back]](./README.md) [[kb]](./kb/power_on.md)

## Workflow

Checks
- selected node provisioning state must be one of: 'available', 'externally provisioned', 'provisioned'
- `spec.online` should be false

Action
- patch `BareMetalHost` resource with `spec.online` set to true value

## Configurable options

```
# iserver set ocp bmh --mode on
  --cluster TEXT     Cluster Name
  --node TEXT        Node name
  --no-wait          Wait mode
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp bmh --cluster bm1 --node bm1-1 --mode on

OpenShift Workflow - Bare Metal Host - Power on
===============================================

OpenShift Cluster: bm1

Patch BareMetalHost
-------------------
- namespace: openshift-machine-api
- name: bm1-1

~~~
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: bm1-1
  namespace: openshift-machine-api
spec:
  online: true

~~~
BareMetalHost [openshift-machine-api/bm1-1] patched
- wait for BareMetalHost openshift-machine-api/bm1-1 [timeout:600s] with {"power": true}
- wait for BareMetalHost openshift-machine-api/bm1-1 [timeout:600s] with {"online": true}

+----+-----------------------+------------------------+-------------+--------+-------+------------------------------------------------------------+
| ID | Bare Metal Host       | Provisioning           | Operational | Online | Power | Server                                                     |
+----+-----------------------+------------------------+-------------+--------+-------+------------------------------------------------------------+
| 1  | openshift-machine-api | externally provisioned | OK          | V      | V     | redfish-virtualmedia://10.10.10.10/redfish/v1/Systems/AAAA | 
|    | bm1-1                 |                        |             |        |       | bm1-1-bmc-secret                                           | 
|    |                       |                        |             |        |       | Cert verification: X                                       | 
|    |                       |                        |             |        |       | UCSC-C240-M6N                                              | 
|    |                       |                        |             |        |       | AAAA                                                       | 
+----+-----------------------+------------------------+-------------+--------+-------+------------------------------------------------------------+

Completed tasks
- bare metal hosts powered on
```

[[Back]](./README.md) [[kb]](./kb/detach.md)