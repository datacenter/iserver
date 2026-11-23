# Network Attachment Definition - Create Bridge

## Workflow

- create network attachment definition of [type:bridge](./overview-bridge.md)

## Requirements

None

## Configurable options

```
# iserver create k8s bridge
  --cluster TEXT         Cluster Name
  --namespace TEXT       Namespace
  --name TEXT            Name
  --bridge TEXT          Bridge name
  --ipam [static|local]  IPAM mode  [default: static]
  --address TEXT         Address
  --gateway TEXT         Gateway CIDR
  --route TEXT           Route
  --no-confirm           Confirmation mode
```

## Example (static)

```
# iserver create k8s nad bridge \
    --namespace default \
    --name test \
    --bridge br1 \
    --ipam local \
    --address 10.10.10.2 \
    --gateway 10.10.10.1/28 \
    --route 10.20.20.0/24 \
    --route 10.30.30.0/24

Kubernetes Workflow - Network Attachment Definition - Create Bridge
===================================================================

OpenShift Cluster: bm3

Create IPVLAN NAD
-----------------
- namespace: default
- name: test
- bridge: br1
- ipam: static
- address: 10.10.10.2
- gateway: 10.10.10.1/28
- route: 10.20.20.0/24, 10.30.30.0/24

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
      "type": "bridge",
      "name": "br1",
      "bridge": "br1",
      "isDefaultGateway": true,
      "isMasq": true,
      "ipam": {
        "type": "static",
        "addresses": [
          {
            "address": "10.10.10.2/28",
            "gateway": "10.10.10.1"
          }
        ],
        "routes": [
          {
            "dst": "10.20.20.0/24",
            "gw": "10.10.10.1"
          },
          {
            "dst": "10.30.30.0/24",
            "gw": "10.10.10.1"
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
| default/test                  | bridge | --              | {                                   | 60m | 
|                               |        |                 |   "cniVersion": "0.3.1",            |     |
|                               |        |                 |   "type": "bridge",                 |     |
|                               |        |                 |   "name": "br1",                    |     |
|                               |        |                 |   "bridge": "br1",                  |     |
|                               |        |                 |   "isDefaultGateway": true,         |     |
|                               |        |                 |   "isMasq": true,                   |     |
|                               |        |                 |   "ipam": {                         |     |
|                               |        |                 |     "type": "static",               |     |
|                               |        |                 |     "addresses": [                  |     |
|                               |        |                 |       {                             |     |
|                               |        |                 |         "address": "10.10.10.2/28", |     |
|                               |        |                 |         "gateway": "10.10.10.1"     |     |
|                               |        |                 |       }                             |     |
|                               |        |                 |     ],                              |     |
|                               |        |                 |     "routes": [                     |     |
|                               |        |                 |       {                             |     |
|                               |        |                 |         "dst": "10.20.20.0/24",     |     |
|                               |        |                 |         "gw": "10.10.10.1"          |     |
|                               |        |                 |       },                            |     |
|                               |        |                 |       {                             |     | 
|                               |        |                 |         "dst": "10.30.30.0/24",     |     |
|                               |        |                 |         "gw": "10.10.10.1"          |     |
|                               |        |                 |       }                             |     |
|                               |        |                 |     ]                               |     |
|                               |        |                 |   }                                 |     |
|                               |        |                 | }                                   |     |
+-------------------------------+--------+-----------------+-------------------------------------+-----+
```

## Example (host-local)

```
# iserver create k8s nad bridge \
    --namespace default \
    --name test \
    --bridge br1 \
    --ipam local \
    --address 10.10.10.2-10.10.10.15 \
    --gateway 10.10.10.1/28 \
    --route 10.20.20.0/24 \
    --route 10.30.30.0/24

Kubernetes Workflow - Network Attachment Definition - Create Bridge
===================================================================

OpenShift Cluster: bm3

Create IPVLAN NAD
-----------------
- namespace: default
- name: test
- bridge: br1
- ipam: local
- address: 10.10.10.2-10.10.10.15
- gateway: 10.10.10.1/28
- route: 10.20.20.0/24, 10.30.30.0/24

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
      "type": "bridge",
      "name": "br1",
      "bridge": "br1",
      "isDefaultGateway": true,
      "isMasq": true,
      "ipam": {
        "type": "host-local",
        "subnet": "10.10.10.0/28",
        "rangeStart": "10.10.10.2",
        "rangeEnd": "10.10.10.15",
        "gateway": "10.10.10.1",
        "routes": [
          {
            "dst": "10.20.20.0/24",
            "gw": "10.10.10.1"
          },
          {
            "dst": "10.30.30.0/24",
            "gw": "10.10.10.1"
          }
        ]
      }
    }

~~~
Continue [Y/N]? y

Network attachment definition created

Wait for nad...

+-------------------------------+--------+-----------------+---------------------------------+-----+
| Network Attachment Definition | Type   | SR-IOV Resource | Config                          | Age |
+-------------------------------+--------+-----------------+---------------------------------+-----+
| default/test                  | bridge | --              | {                               | 60m |
|                               |        |                 |   "cniVersion": "0.3.1",        |     |
|                               |        |                 |   "type": "bridge",             |     |
|                               |        |                 |   "name": "br1",                |     | 
|                               |        |                 |   "bridge": "br1",              |     |
|                               |        |                 |   "isDefaultGateway": true,     |     |
|                               |        |                 |   "isMasq": true,               |     |
|                               |        |                 |   "ipam": {                     |     |
|                               |        |                 |     "type": "host-local",       |     |
|                               |        |                 |     "subnet": "10.10.10.0/28",  |     |
|                               |        |                 |     "rangeStart": "10.10.10.2", |     |
|                               |        |                 |     "rangeEnd": "10.10.10.15",  |     |
|                               |        |                 |     "gateway": "10.10.10.1",    |     |
|                               |        |                 |     "routes": [                 |     |
|                               |        |                 |       {                         |     | 
|                               |        |                 |         "dst": "10.20.20.0/24", |     |
|                               |        |                 |         "gw": "10.10.10.1"      |     |
|                               |        |                 |       },                        |     |
|                               |        |                 |       {                         |     |
|                               |        |                 |         "dst": "10.30.30.0/24", |     |
|                               |        |                 |         "gw": "10.10.10.1"      |     |
|                               |        |                 |       }                         |     |
|                               |        |                 |     ]                           |     |
|                               |        |                 |   }                             |     |
|                               |        |                 | }                               |     |
+-------------------------------+--------+-----------------+---------------------------------+-----+
```

[[Back]](./README.md)