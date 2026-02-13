# Network Attachment Definition - Create IPVLAN

## Workflow

- create network attachment definition of [type:ipvlan](./overview-ipvlan.md)

## Requirements

None

## Configurable options

```
# iserver create k8s ipvlan
  --cluster TEXT                Cluster Name
  --namespace TEXT              Namespace
  --name TEXT                   Name
  --master TEXT                 Master interface
  --mode [l2|l3|l3s]            IPVLAN mode  [default: l2]
  --ipam [static|local]         IPAM mode  [static]
  --address TEXT                Address
  --gateway TEXT                Gateway CIDR
  --no-confirm                  Confirmation mode
```

## Example (static)

```
# iserver create k8s nad ipvlan \
    --namespace default \
    --name test \
    --master eth10 \
    --mode l2 \
    --ipam static \
    --address 10.10.10.1 \
    --gateway 10.10.10.254/24

Kubernetes Workflow - Network Attachment Definition - Create IPVLAN
===================================================================

OpenShift Cluster: bm3

Create IPVLAN NAD
-----------------
- namespace: default
- name: test
- master: eth10
- mode: l2
- ipam: static
- address: 10.10.10.1
- gateway: 10.10.10.254/24

~~~
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: test
  namespace: default
spec:
  config: |-
    {
      "cniVersion": "0.3.1",
      "type": "ipvlan",
      "master": "eth10",
      "mode": "l2",
      "ipam": {
        "type": "static",
        "addresses": [
          {
            "address": "10.10.10.1/24",
            "gateway": "10.10.10.254"
          }
        ]
      }
    }

~~~
Continue [Y/N]? y

Network attachment definition created

Wait for nad...

+-------------------------------+--------+-----------------+-------------------------------------+-----+
| Network Attachment Definition | Type   | SR-IOV Resource | Config                              | Age |
+-------------------------------+--------+-----------------+-------------------------------------+-----+
| default/test                  | ipvlan | --              | {                                   | 60m |
|                               |        |                 |   "cniVersion": "0.3.1",            |     |
|                               |        |                 |   "type": "ipvlan",                 |     |
|                               |        |                 |   "master": "eth10",                |     |
|                               |        |                 |   "mode": "l2",                     |     |
|                               |        |                 |   "ipam": {                         |     |
|                               |        |                 |     "type": "static",               |     |
|                               |        |                 |     "addresses": [                  |     |
|                               |        |                 |       {                             |     |
|                               |        |                 |         "address": "10.10.10.1/24", |     |
|                               |        |                 |         "gateway": "10.10.10.254"   |     |
|                               |        |                 |       }                             |     |
|                               |        |                 |     ]                               |     |
|                               |        |                 |   }                                 |     |
|                               |        |                 | }                                   |     |
+-------------------------------+--------+-----------------+-------------------------------------+-----+
```

## Example (host-local)

```
# iserver create k8s nad ipvlan \
    --namespace default \
    --name test \
    --master eth10 \
    --mode bridge \
    --ipam local \
    --address 10.10.10.1-10.10.10.253 \
    --gateway 10.10.10.254/24

Kubernetes Workflow - Network Attachment Definition - Create IPVLAN
===================================================================

OpenShift Cluster: bm3

Create IPVLAN NAD
-----------------
- namespace: default
- name: test
- master: eth10
- mode: l2
- ipam: local
- address: 10.10.10.1-10.10.10.253
- gateway: 10.10.10.254/24

~~~
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: test
  namespace: default
spec:
  config: |-
    {
      "cniVersion": "0.3.1",
      "type": "ipvlan",
      "master": "eth10",
      "mode": "l2",
      "ipam": {
        "type": "host-local",
        "subnet": "10.10.10.0/24",
        "rangeStart": "10.10.10.1",
        "rangeEnd": "10.10.10.253",
        "gateway": "10.10.10.254"
      }
    }

~~~
Continue [Y/N]? y

Network attachment definition created

Wait for nad...

+-------------------------------+--------+-----------------+---------------------------------+-----+
| Network Attachment Definition | Type   | SR-IOV Resource | Config                          | Age |
+-------------------------------+--------+-----------------+---------------------------------+-----+
| default/test                  | ipvlan | --              | {                               | 60m |
|                               |        |                 |   "cniVersion": "0.3.1",        |     |
|                               |        |                 |   "type": "ipvlan",             |     |
|                               |        |                 |   "master": "eth10",            |     |
|                               |        |                 |   "mode": "l2",                 |     |
|                               |        |                 |   "ipam": {                     |     | 
|                               |        |                 |     "type": "host-local",       |     |
|                               |        |                 |     "subnet": "10.10.10.0/24",  |     |
|                               |        |                 |     "rangeStart": "10.10.10.1", |     |
|                               |        |                 |     "rangeEnd": "10.10.10.253", |     |
|                               |        |                 |     "gateway": "10.10.10.254"   |     |
|                               |        |                 |   }                             |     |
|                               |        |                 | }                               |     | 
+-------------------------------+--------+-----------------+---------------------------------+-----+
```

[[Back]](./README.md)