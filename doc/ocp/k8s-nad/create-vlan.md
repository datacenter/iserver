# Network Attachment Definition - Create VLAN

## Workflow

- create network attachment definition of [type:vlan](./overview-vlan.md)

## Requirements

None

## Configurable options

```
# iserver create k8s vlan
  --cluster TEXT              Cluster Name
  --namespace TEXT            Namespace
  --name TEXT                 Name
  --master TEXT               Master interface
  --vlan INTEGER              VLAN ID
  --ipam [static|local]  IPAM mode [default: static]
  --address TEXT              Address
  --gateway TEXT              Gateway CIDR
  --no-confirm                Confirmation mode
```

## Example (static)

```
# iserver create k8s nad vlan \
    --namespace default \
    --name test \
    --master eth10 \
    --vlan 100 \
    --ipam static \
    --address 10.10.10.1 \
    --gateway 10.10.10.254/24

Kubernetes Workflow - Network Attachment Definition - Create VLAN
=================================================================

OpenShift Cluster: bm3

Create VLAN NAD
---------------
- namespace: default
- name: test
- master: eth10
- vlan: 100
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
      "type": "vlan",
      "master": "eth10",
      "vlanId": 100,
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

+-------------------------------+------+-----------------+-------------------------------------+------+
| Network Attachment Definition | Type | SR-IOV Resource | Config                              | Age  |
+-------------------------------+------+-----------------+-------------------------------------+------+
| default/test                  | vlan | --              | {                                   | 1h0m |
|                               |      |                 |   "cniVersion": "0.3.1",            |      |
|                               |      |                 |   "type": "vlan",                   |      |
|                               |      |                 |   "master": "eth10",                |      |
|                               |      |                 |   "vlanId": 100,                    |      |
|                               |      |                 |   "ipam": {                         |      |
|                               |      |                 |     "type": "static",               |      |
|                               |      |                 |     "addresses": [                  |      | 
|                               |      |                 |       {                             |      |
|                               |      |                 |         "address": "10.10.10.1/24", |      |
|                               |      |                 |         "gateway": "10.10.10.254"   |      |
|                               |      |                 |       }                             |      |
|                               |      |                 |     ]                               |      |
|                               |      |                 |   }                                 |      |
|                               |      |                 | }                                   |      |
+-------------------------------+------+-----------------+-------------------------------------+------+
```

## Example (host-local)

```
# iserver create k8s nad vlan \
    --namespace default \
    --name test \
    --master eth10 \
    --vlan 100 \
    --ipam local \
    --address 10.10.10.1-10.10.10.253 \
    --gateway 10.10.10.254/24

Kubernetes Workflow - Network Attachment Definition - Create VLAN
=================================================================

OpenShift Cluster: bm3

Create VLAN NAD
---------------
- namespace: default
- name: test
- master: eth10
- vlan: 100
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
      "type": "vlan",
      "master": "eth10",
      "vlanId": 100,
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

+-------------------------------+------+-----------------+---------------------------------+------+
| Network Attachment Definition | Type | SR-IOV Resource | Config                          | Age  |
+-------------------------------+------+-----------------+---------------------------------+------+
| default/test                  | vlan | --              | {                               | 1h0m |
|                               |      |                 |   "cniVersion": "0.3.1",        |      |
|                               |      |                 |   "type": "vlan",               |      |
|                               |      |                 |   "master": "eth10",            |      |
|                               |      |                 |   "vlanId": 100,                |      |
|                               |      |                 |   "ipam": {                     |      |
|                               |      |                 |     "type": "host-local",       |      |
|                               |      |                 |     "subnet": "10.10.10.0/24",  |      |
|                               |      |                 |     "rangeStart": "10.10.10.1", |      |
|                               |      |                 |     "rangeEnd": "10.10.10.253", |      |
|                               |      |                 |     "gateway": "10.10.10.254"   |      |
|                               |      |                 |   }                             |      |
|                               |      |                 | }                               |      |
+-------------------------------+------+-----------------+---------------------------------+------+
```

[[Back]](./README.md)