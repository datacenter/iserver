# Metal Kubed - Delete node

[[Back]](./README.md)

## Workflow

Checks
- selected node must exist

Action
- delete `BareMetalHost` object
- wait for resource gone
- delete `Secret` object
- wait for resource gone


## Configurable options

```
# iserver delete ocp bmh --mode node
  --cluster TEXT     Cluster Name
  --node TEXT        Node name
  --no-wait          Wait mode
```

## Example

```
# iserver delete ocp bmh --cluster bm1 --mode node --node test

OpenShift Workflow - Bare Metal Host - Delete host
==================================================

OpenShift Cluster: bm1

+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+
| ID | Bare Metal Host       | Provisioning           | Operational | Power | Server                                                     |
+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+
| 1  | openshift-machine-api | externally provisioned | OK          | V     | redfish-virtualmedia://10.10.10.10/redfish/v1/Systems/AAAA | 
|    | bm1-1                 |                        |             |       | bm1-1-bmc-secret                                           | 
|    |                       |                        |             |       | Cert verification: X                                       | 
|    |                       |                        |             |       | UCSC-C240-M6SN                                             |
|    |                       |                        |             |       | AAAA                                                       |
+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+
| 2  | openshift-machine-api | externally provisioned | OK          | V     | redfish-virtualmedia://10.10.10.11/redfish/v1/Systems/BBBB |
|    | bm1-2                 |                        |             |       | bm1-2-bmc-secret                                           |
|    |                       |                        |             |       | Cert verification: X                                       |
|    |                       |                        |             |       | UCSC-C240-M6SN                                             |
|    |                       |                        |             |       | BBBB                                                       |
+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+
| 3  | openshift-machine-api | externally provisioned | OK          | V     | redfish-virtualmedia://10.10.10.12/redfish/v1/Systems/CCCC |
|    | bm1-3                 |                        |             |       | bm1-3-bmc-secret                                           |
|    |                       |                        |             |       | Cert verification: X                                       |
|    |                       |                        |             |       | UCSC-C240-M6SN                                             |
|    |                       |                        |             |       | CCCC                                                       |
+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+
| 4  | openshift-machine-api | inspecting             | OK          | V     | redfish-virtualmedia://10.10.10.13/redfish/v1/Systems/DDDD |
|    | test                  |                        |             |       | test-bmc-secret                                            |
|    |                       |                        |             |       | Cert verification: X                                       |
|    |                       |                        |             |       | Product: ---                                               |
|    |                       |                        |             |       | Serial: ---                                                |
+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+

Delete BareMetalHost
--------------------
- namespace: openshift-machine-api
- name: test
- deleted
- wait for no BareMetalHost openshift-machine-api/test [timeout:180s]

Delete Secret
-------------
- namespace: openshift-machine-api
- name: test-bmc-secret
- already deleted

+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+
| ID | Bare Metal Host       | Provisioning           | Operational | Power | Server                                                     |
+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+
| 1  | openshift-machine-api | externally provisioned | OK          | V     | redfish-virtualmedia://10.10.10.10/redfish/v1/Systems/AAAA | 
|    | bm1-1                 |                        |             |       | bm1-1-bmc-secret                                           | 
|    |                       |                        |             |       | Cert verification: X                                       | 
|    |                       |                        |             |       | UCSC-C240-M6SN                                             |
|    |                       |                        |             |       | AAAA                                                       |
+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+
| 2  | openshift-machine-api | externally provisioned | OK          | V     | redfish-virtualmedia://10.10.10.11/redfish/v1/Systems/BBBB |
|    | bm1-2                 |                        |             |       | bm1-2-bmc-secret                                           |
|    |                       |                        |             |       | Cert verification: X                                       |
|    |                       |                        |             |       | UCSC-C240-M6SN                                             |
|    |                       |                        |             |       | BBBB                                                       |
+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+
| 3  | openshift-machine-api | externally provisioned | OK          | V     | redfish-virtualmedia://10.10.10.12/redfish/v1/Systems/CCCC |
|    | bm1-3                 |                        |             |       | bm1-3-bmc-secret                                           |
|    |                       |                        |             |       | Cert verification: X                                       |
|    |                       |                        |             |       | UCSC-C240-M6SN                                             |
|    |                       |                        |             |       | CCCC                                                       |
+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+

Completed tasks
- bare metal host deleted
```

[[Back]](./README.md)