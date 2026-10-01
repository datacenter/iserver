# Certificate Manager - Wipe

[[Back]](./README.md)

## Workflow

- delete all resources: `Certificate`, `ClusterIssuer`, `Issuer`
- delete all associated `Secret` resources

## Requirements

- Certificate manager [installed](./enable.md)

## Configurable options

```
# iserver delete ocp cert-manager --mode wipe
  --cluster TEXT           Cluster name
```

## Example

```
# iserver delete ocp cert-manager \
    --cluster bm1 \
    --mode wipe

OpenShift Workflow - Certificate Manager - Wipe
===============================================

OpenShift Cluster: bm1


Certificate Manager Resources
-----------------------------
- cluster issuer      : 1
- issuer              : 1
- certificate request : 2
- certificate         : 2


Delete Certificate
------------------
- namespace: default
- name: test1
- deleted
Wait for no Certificate default/test1 [timeout:60s]

Delete Certificate
------------------
- namespace: default
- name: test2
- deleted
Wait for no Certificate default/test2 [timeout:60s]

Delete Issuer
-------------
- namespace: default
- name: default-root-ca
- deleted
Wait for no Issuer default/default-root-ca [timeout:60s]

Delete ClusterIssuer
--------------------
- name: root-ca
- deleted
Wait for no ClusterIssuer root-ca [timeout:60s]

Delete Secret
-------------
- namespace: default
- name: test1
- deleted
Wait for no Secret default/test1 [timeout:60s]

Delete Secret
-------------
- namespace: default
- name: test2
- deleted
Wait for no Secret default/test2 [timeout:60s]

Delete Secret
-------------
- namespace: default
- name: default-root-ca
- deleted
Wait for no Secret default/default-root-ca [timeout:60s]

Delete Secret
-------------
- namespace: cert-manager
- name: root-ca
- deleted
Wait for no Secret cert-manager/root-ca [timeout:60s]

Completed tasks
- resources wiped

+----+---------+--------------+-------------+---------+---------+--------------+
| ID | Target  | Scope        | Workflow    | Changes | Success | Duration [s] |
+----+---------+--------------+-------------+---------+---------+--------------+
| 1  | ocp:bm1 | cert-manager | delete wipe | 8       | ✓       | 5            | 
+----+---------+--------------+-------------+---------+---------+--------------+
```

[[Back]](./README.md)