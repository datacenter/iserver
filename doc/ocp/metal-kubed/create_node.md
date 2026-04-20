# Metal Kubed - Create node

[[Back]](./README.md)

## Workflow

Checks
- selected node must not exist

Action
- add noProxy settings if required
- create `BareMetalHost` object
- wait for [inspecting](./kb/inspect.md) state

## Configurable options

```
# iserver set ocp bmh --mode node
  --cluster TEXT                  Cluster Name
  --node TEXT                     Node name
  --bmc TEXT                      node:address
  --type [ucsc]                   server type  [default: ucsc]
  --username TEXT                 bmc username
  --password TEXT                 bmc password
  --cert                          Certificate mode
  --mac TEXT                      Boot mac address
  --serial TEXT                   Serial number
  --boot [uefi|secure|legacy]     Boot mode  [default: uefi]
  --no-wait                       Wait mode
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver set ocp bmh --cluster bm1 --mode node --node test --bmc 10.10.10.13 --username admin --password secret --serial DDDD --mac aa:aa:aa:aa:aa:aa --boot uefi --no-confirm

OpenShift Workflow - Bare Metal Host - Create host
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

Collecting proxy settings...

Checkin noproxy match for [10.10.10.13]
- .bm1.ocp.domain.com
- .cluster.local
- .svc
- 10.128.0.0/14
- 127.0.0.1
- 172.30.0.0/16
- 10.10.10.13
- api-int.bm1.domain.com
- domain.com
- localhost

Create Secret
-------------
- namespace: openshift-machine-api
- name: test-bmc-secret

~~~
apiVersion: v1
data:
  password: cGFzc3dvcmQ=
  username: YWRtaW4=
kind: Secret
metadata:
  labels:
    environment.metal3.io: baremetal
  name: test-bmc-secret
  namespace: openshift-machine-api
type: Opaque

~~~
Secret [openshift-machine-api/test-bmc-secret] created
- wait for Secret openshift-machine-api/test-bmc-secret [timeout:60s]

Create BareMetalHost
--------------------
- namespace: openshift-machine-api
- name: test

~~~
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  name: test
  namespace: openshift-machine-api
spec:
  bmc:
    address: redfish-virtualmedia://10.10.10.13/redfish/v1/Systems/DDDD
    credentialsName: test-bmc-secret
    disableCertificateVerification: true
  bootMACAddress: aa:aa:aa:aa:aa:aa
  bootMode: UEFI
  online: true

~~~
BareMetalHost [openshift-machine-api/test] created
- wait for BareMetalHost openshift-machine-api/test [timeout:60s]
- wait for BareMetalHost openshift-machine-api/test [timeout:180s] with {"provisioning_state": "registering"}
- wait for BareMetalHost openshift-machine-api/test [timeout:180s] with {"provisioning_state": "inspecting"}

+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+
| ID | Bare Metal Host       | Provisioning           | Operational | Power | Server                                                     |
+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+
| 1  | openshift-machine-api | inspecting             | OK          | X     | redfish-virtualmedia://10.10.10.13/redfish/v1/Systems/DDDD |
|    | test                  |                        |             |       | test-bmc-secret                                            |
|    |                       |                        |             |       | Cert verification: X                                       |
|    |                       |                        |             |       | Product: ---                                               |
|    |                       |                        |             |       | Serial: ---                                                |
+----+-----------------------+------------------------+-------------+-------+------------------------------------------------------------+

Completed tasks
- bare metal host created
```

[[Back]](./README.md)