# Metal Kubed - Inspect host

[[Back]](./README.md) [[kb]](./kb/inspect.md)

## Workflow

Checks
- inspection annotation should not be defined

Action
- add inspect.metal3.io='' annotation
- wait for provisioning state to reach `inspecting` 

## Configurable options

```
# iserver set ocp bmh --mode inspect
  --cluster TEXT     Cluster Name
  --node TEXT        Node name
  --no-wait          Wait mode
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp bmh --cluster bm1 --node bm1-1 --mode inspect


OpenShift Workflow - Bare Metal Host - Inspection
=================================================

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
    inspect.metal3.io: ''
  name: bm1-1
  namespace: openshift-machine-api

~~~
BareMetalHost [openshift-machine-api/bm1-1] patched
- wait for BareMetalHost openshift-machine-api/bm1-1 [timeout:180s] with {"provisioning_state": "inspecting"}
- wait for BareMetalHost openshift-machine-api/bm1-1 [timeout:180s] with {"operational_state": "OK"}

+----+-----------------------+--------------+-------------+--------+-------+------------------------------------------------------------+
| ID | Bare Metal Host       | Provisioning | Operational | Online | Power | Server                                                     |
+----+-----------------------+--------------+-------------+--------+-------+------------------------------------------------------------+
| 1  | openshift-machine-api | inspecting   | OK          | V      | X     | redfish-virtualmedia://10.10.10.10/redfish/v1/Systems/AAAA | 
|    | bm1-1                 |              |             |        |       | bm1-1-bmc-secret                                           | 
|    |                       |              |             |        |       | Cert verification: X                                       | 
|    |                       |              |             |        |       | Product: ---                                               | 
|    |                       |              |             |        |       | Serial: ---                                                | 
+----+-----------------------+--------------+-------------+--------+-------+------------------------------------------------------------+

Completed tasks
- bare metal host inspection initiatied
```

[[Back]](./README.md) [[kb]](./kb/detach.md)