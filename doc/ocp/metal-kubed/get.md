# Metal Kubed - Get

[[Back]](./README.md)

## Workflow

- show `BareMetalHost` crds incl
    - [provisioning state](./kb/provisioning_state.md)
    - [operational state](./kb/operational_state.md)
    - bmc details used for [registration](./kb/register.md)

## Requirements

None

## Example

```
# iserver get ocp bmh --cluster bm1

OpenShift Workflow - Bare Metal Host - Get state
================================================

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
```

[[Back]](./README.md)