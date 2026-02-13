# Network Attachment Definition - Create MacVLAN

## Workflow

- create network attachment definition of [type:macvlan](./overview-macvlan.md)

## Requirements

None

## Configurable options

```
# iserver create k8s macvlan
  --cluster TEXT                          Cluster Name
  --namespace TEXT                        Namespace
  --name TEXT                             Name
  --master TEXT                           Master interface
  --mode [bridge|passthru|private|vepa]   MacVLAN mode [default: bridge]
  --ipam [dhcp|static|local]              IPAM mode [default: dhcp]
  --address TEXT                          Address
  --gateway TEXT                          Gateway CIDR
  --no-confirm                            Confirmation mode
```

## Example (dhcp)

```
# iserver create k8s nad macvlan --namespace default --name test --master eth10 --mode bridge

Kubernetes Workflow - Network Attachment Definition - Create MacVLAN
====================================================================

OpenShift Cluster: bm3

Create MacVLAN NAD
------------------
- namespace: default
- name: test
- master: eth10
- mode: bridge
- ipam: dhcp

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
      "type": "macvlan",
      "master": "eth10",
      "mode": "bridge",
      "ipam": {
        "type": "dhcp"
      }
    }

~~~
Continue [Y/N]? y

Network attachment definition created

Wait for nad...

+-------------------------------+---------+-----------------+--------------------------+------+
| Network Attachment Definition | Type    | SR-IOV Resource | Config                   | Age  |
+-------------------------------+---------+-----------------+--------------------------+------+
| default/test                  | macvlan | --              | {                        | 1h0m |
|                               |         |                 |   "cniVersion": "0.3.1", |      |
|                               |         |                 |   "type": "macvlan",     |      |
|                               |         |                 |   "master": "eth10",     |      | 
|                               |         |                 |   "mode": "bridge",      |      |
|                               |         |                 |   "ipam": {              |      |
|                               |         |                 |     "type": "dhcp"       |      |
|                               |         |                 |   }                      |      |
|                               |         |                 | }                        |      |
+-------------------------------+---------+-----------------+--------------------------+------+
```

## Example (static)

```
# iserver create k8s nad macvlan \
    --namespace default \
    --name test \
    --master eth10 \
    --mode bridge \
    --ipam static \
    --address 10.10.10.1 \
    --gateway 10.10.10.254/24

Kubernetes Workflow - Network Attachment Definition - Create MacVLAN
====================================================================

OpenShift Cluster: bm3

Create MacVLAN NAD
------------------
- namespace: default
- name: test
- master: eth10
- mode: bridge
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
      "type": "macvlan",
      "master": "eth10",
      "mode": "bridge",
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

+-------------------------------+---------+-----------------+-------------------------------------+-----+
| Network Attachment Definition | Type    | SR-IOV Resource | Config                              | Age |
+-------------------------------+---------+-----------------+-------------------------------------+-----+
| default/test                  | macvlan | --              | {                                   | 60m |
|                               |         |                 |   "cniVersion": "0.3.1",            |     |
|                               |         |                 |   "type": "macvlan",                |     |
|                               |         |                 |   "master": "eth10",                |     |
|                               |         |                 |   "mode": "bridge",                 |     |
|                               |         |                 |   "ipam": {                         |     |
|                               |         |                 |     "type": "static",               |     |
|                               |         |                 |     "addresses": [                  |     |
|                               |         |                 |       {                             |     |
|                               |         |                 |         "address": "10.10.10.1/24", |     |
|                               |         |                 |         "gateway": "10.10.10.254"   |     |
|                               |         |                 |       }                             |     |
|                               |         |                 |     ]                               |     |
|                               |         |                 |   }                                 |     |
|                               |         |                 | }                                   |     |
+-------------------------------+---------+-----------------+-------------------------------------+-----+
```

## Example (host-local)

```
# iserver create k8s nad macvlan \
    --namespace default \
    --name test \
    --master eth10 \
    --mode bridge \
    --ipam local \
    --address 10.10.10.1-10.10.10.253 \
    --gateway 10.10.10.254/24

Kubernetes Workflow - Network Attachment Definition - Create MacVLAN
====================================================================

OpenShift Cluster: bm3

Create MacVLAN NAD
------------------
- namespace: default
- name: test
- master: eth10
- mode: bridge
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
      "type": "macvlan",
      "master": "eth10",
      "mode": "bridge",
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

+-------------------------------+---------+-----------------+---------------------------------+-----+
| Network Attachment Definition | Type    | SR-IOV Resource | Config                          | Age |
+-------------------------------+---------+-----------------+---------------------------------+-----+
| default/test                  | macvlan | --              | {                               | 60m |
|                               |         |                 |   "cniVersion": "0.3.1",        |     |
|                               |         |                 |   "type": "macvlan",            |     |
|                               |         |                 |   "master": "eth10",            |     |
|                               |         |                 |   "mode": "bridge",             |     |
|                               |         |                 |   "ipam": {                     |     |
|                               |         |                 |     "type": "host-local",       |     |
|                               |         |                 |     "subnet": "10.10.10.0/24",  |     |
|                               |         |                 |     "rangeStart": "10.10.10.1", |     |
|                               |         |                 |     "rangeEnd": "10.10.10.253", |     |
|                               |         |                 |     "gateway": "10.10.10.254"   |     |
|                               |         |                 |   }                             |     |
|                               |         |                 | }                               |     |
+-------------------------------+---------+-----------------+---------------------------------+-----+
```

[[Back]](./README.md)