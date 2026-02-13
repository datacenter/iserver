# Network Attachment Definition - Delete

## Workflow

- get network attachment definitions selected by namespace, name or all
- delete nads one-by-one

## Requirements

None

## Configurable options

```
# iserver delete k8s nad 
  --cluster TEXT    Cluster Name
  --namespace TEXT  Filter by namespace
  --name TEXT       Filter by name
  --no-confirm      No confirmation mode
```

## Example

```
# iserver delete k8s nad --cluster bm1 --namespace default


Kubernetes Workflow - Network Attachment Definition - Delete
============================================================

OpenShift Cluster: bm3

+-------------------------------+------+-----------------+--------------------------+------+
| Network Attachment Definition | Type | SR-IOV Resource | Config                   | Age  |
+-------------------------------+------+-----------------+--------------------------+------+
| default/test                  | vlan | --              | {                        | 2h5m | 
|                               |      |                 |   "cniVersion": "0.3.1", |      | 
|                               |      |                 |   "type": "vlan",        |      | 
|                               |      |                 |   "master": "eth10",     |      | 
|                               |      |                 |   "vlanId": 100,         |      | 
|                               |      |                 |   "ipam": {              |      | 
|                               |      |                 |     "type": "dhcp"       |      | 
|                               |      |                 |   }                      |      | 
|                               |      |                 | }                        |      | 
+-------------------------------+------+-----------------+--------------------------+------+
Continue [Y/N]? y

Delete Network Attachment Definition
------------------------------------
- namespace: default
- name: test
- wait for no nad
```

[[Back]](./README.md)