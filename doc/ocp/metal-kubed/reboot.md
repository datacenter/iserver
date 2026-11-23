# Metal Kubed - Reboot

[[Back]](./README.md) [[kb]](./kb/reboot.md)

## Workflow

Checks
- selected node provisioning state must be one of: 'available', 'externally provisioned', 'provisioned'
- reboot annotation not expected

Action
- annotate `BareMetalHost` resource with `reboot.metal3.io=''`
- wait until annotation is removed
- wait until server operationa state shows power and online status

> [!CAUTION]
> this is **not** kubernetes friendly way of rebooting the node

## Configurable options

```
# iserver set ocp bmh --mode reboot
  --cluster TEXT     Cluster Name
  --node TEXT        Node name
  --no-wait          Wait mode
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp bmh --cluster bm1 --node bm1-1 --mode reboot


OpenShift Workflow - Bare Metal Host - Reboot
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
    reboot.metal3.io: ''
  name: bm1-1
  namespace: openshift-machine-api

~~~
BareMetalHost [openshift-machine-api/bm1-1] patched
- wait for BareMetalHost openshift-machine-api/bm1-1 [timeout:180s] with {"annotation:reboot.metal3.io": null}
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
- bare metal hosts rebooted
```

[[Back]](./README.md) [[kb]](./kb/reboot.md)