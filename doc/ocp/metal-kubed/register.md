# Metal Kubed - Node registration

[[Back]](./README.md) [[kb]](./kb/register.md)

## Workflow

Checks
- selected node provisioning state must be [unmanaged](./kb/unmanaged.md) or registering or [detached](./kb/detach.md) annotation should not be defined

HTTP Proxy
- if http proxy is configured, check if bmc address is defined in noProxy
- add it otherwise

Registration
- add `Secret` object with username and password
- patch `BareMetalHost` object with secret, bmc address and certificate check settings

Bmc address depends on bmc endpoint type:
- ucsc: redfish-virtualmedia://bmc-ip/redfish/v1/Systems/server-serial where server-serial is collected from BareMetalHost object

> [!CAUTION]
> it may take several minutes for provisioning state to change from unmanaged to registering

## Configurable options

```
# iserver set ocp bmh --mode bmc
  --cluster TEXT     Cluster Name
  --bmc TEXT         node:address
  --type [ucsc]      server type  [default: ucsc]
  --username TEXT    bmc username
  --password TEXT    bmc password
  --cert             Certificate mode
  --no-wait          Wait mode
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp bmh --cluster bm1 --mode bmc --bmc bm1-1:10.10.10.10 --username admin --password secret

OpenShift Workflow - Bare Metal Host - Enable (register)
========================================================

OpenShift Cluster: bm1

Collecting proxy settings...

Checkin noproxy match for [10.10.10.10]
- .bm1.ocp.domain.com
- .cluster.local
- .svc
- 10.128.0.0/14
- 127.0.0.1
- 172.30.0.0/16
- api-int.bm1.domain.com
- domain.com
- localhost

noproxy [10.10.10.10] currently not configured

Replace Proxy
-------------
- name: cluster

~~~
apiVersion: config.openshift.io/v1
kind: Proxy
metadata:
  name: cluster
  resourceVersion: ...
spec:
  httpProxy: ...
  httpsProxy: ...
  noProxy: ...'

~~~
Proxy [cluster] replaced

Wait for desired proxy status...

Create Secret
--------------
- namespace: openshift-machine-api
- name: bm1-1-bmc-secret

~~~
apiVersion: v1
data:
  password: cGFzc3dvcmQ=
  username: YWRtaW4=
kind: Secret
metadata:
  labels:
    environment.metal3.io: baremetal
  name: bm1-1-bmc-secret
  namespace: openshift-machine-api
type: Opaque

~~~
Secret [openshift-machine-api/bm1-1-bmc-secret] replaced
- wait for Secret openshift-machine-api/bm1-1-bmc-secret [timeout:60s]

Patch BareMetalHost
-------------------
- namespace: openshift-machine-api
- name: bm1-1

~~~
apiVersion: metal3.io/v1alpha1
kind: BareMetalHost
metadata:
  labels:
    installer.openshift.io/role: control-plane
  name: bm1-1
  namespace: openshift-machine-api
  resourceVersion: ...
spec:
  bmc:
    address: redfish-virtualmedia://10.10.10.10/redfish/v1/Systems/AAAAAA
    credentialsName: bm1-1-bmc-secret
    disableCertificateVerification: true

~~~
BareMetalHost [openshift-machine-api/bm1-1] patched
- wait for BareMetalHost openshift-machine-api/bm1-1 [timeout:600s] with {"operational_state": "OK"}
- wait for BareMetalHost openshift-machine-api/bm1-1 [timeout:180s] with {"provisioning_state": "externally provisioned"}

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
- bare metal hosts configured
```

[[Back]](./README.md) [[kb]](./kb/register.md)