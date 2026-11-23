# Network Attachment Definition - Get

## Workflow

- get network attachment definitions

## Configurable options

```
# iserver get k8s nad
  --cluster TEXT                  Cluster name
  --namespace TEXT                Filter by namespace
  --name TEXT                     Filter by name
  -v, --view TEXT                 [state]  [default: state]
  -o, --output [default|mo|json]  [default: default]
```

## Example

```
# iserver get k8s nad --cluster bm1 --namespace default
Cluster: bm1 (type: ocp)

+----+-------------------------------+--------+-----------------+-------------------------------------------+------+
| ID | Network Attachment Definition | Type   | SR-IOV Resource | Config                                    | Age  |
+----+-------------------------------+--------+-----------------+-------------------------------------------+------+
| 1  | default                       |        | ---             | {                                         | 51d  |
|    | primary-udn-kubevirt-binding  |        |                 |   "cniVersion": "1.0.0",                  |      |
|    |                               |        |                 |   "name": "primary-udn-kubevirt-binding", |      |
|    |                               |        |                 |   "plugins": [                            |      |
|    |                               |        |                 |     {                                     |      |
|    |                               |        |                 |       "type": "network-passt-binding"     |      |
|    |                               |        |                 |     }                                     |      |
|    |                               |        |                 |   ]                                       |      |
|    |                               |        |                 | }                                         |      |
+----+-------------------------------+--------+-----------------+-------------------------------------------+------+
| 2  | default                       | bridge | ---             | {                                         | 1h7m |
|    | test                          |        |                 |   "cniVersion": "0.3.1",                  |      |
|    |                               |        |                 |   "type": "bridge",                       |      |
|    |                               |        |                 |   "name": "br1",                          |      |
|    |                               |        |                 |   "bridge": "br1",                        |      |
|    |                               |        |                 |   "isDefaultGateway": true,               |      |
|    |                               |        |                 |   "isMasq": true,                         |      |
|    |                               |        |                 |   "ipam": {                               |      | 
|    |                               |        |                 |     "type": "static",                     |      |
|    |                               |        |                 |     "addresses": [                        |      |
|    |                               |        |                 |       {                                   |      |
|    |                               |        |                 |         "address": "10.10.10.2/28",       |      |
|    |                               |        |                 |         "gateway": "10.10.10.1"           |      |
|    |                               |        |                 |       }                                   |      |
|    |                               |        |                 |     ],                                    |      |
|    |                               |        |                 |     "routes": [                           |      |
|    |                               |        |                 |       {                                   |      |
|    |                               |        |                 |         "dst": "10.20.20.0/24",           |      |
|    |                               |        |                 |         "gw": "10.10.10.1"                |      |
|    |                               |        |                 |       },                                  |      |
|    |                               |        |                 |       {                                   |      |
|    |                               |        |                 |         "dst": "10.30.30.0/24",           |      |
|    |                               |        |                 |         "gw": "10.10.10.1"                |      |
|    |                               |        |                 |       }                                   |      |
|    |                               |        |                 |     ]                                     |      |
|    |                               |        |                 |   }                                       |      |
|    |                               |        |                 | }                                         |      |
+----+-------------------------------+--------+-----------------+-------------------------------------------+------+
```

[[Back]](./README.md)