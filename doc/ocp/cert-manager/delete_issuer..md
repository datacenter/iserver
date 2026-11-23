# Certificate Manager - Delete issuer or cluster issuer

[[Back]](./README.md)

## Workflow

- if namespace is defined, delete `Issuer` selected by name or all issuers
- if namespace is not defined, delete `ClusterIssuer` selected by name or all cluster issuers
- delete associated `Secret`

## Requirements

- Certificate manager [installed](./enable.md)

## Configurable options

```
# iserver delete ocp cert-manager --mode issuer
  --cluster TEXT           Cluster name
  --namespace TEXT         CRD namespace
  --name TEXT              CRD name
```

## Example

```
# iserver delete ocp cert-manager \
    --cluster bm1 \
    --mode issuer \
    --namespace cilium \
    --name cilium-root-ca 

OpenShift Workflow - Certificate Manager - Delete issuer
========================================================

OpenShift Cluster: bm1

+----+----------------+------------------+----------------------------------------------------+-------+
| ID | Issuer         | Secret           | Certificate                                        | Ready |
+----+----------------+------------------+----------------------------------------------------+-------+
| 1  | cilium         | ✓ cilium-root-ca | "version": "v3",                                   | ✓     | 
|    | cilium-root-ca |                  | "serial": ...,                                     |       | 
|    |                |                  | "issuer": "CN=cilium-ca-root",                     |       | 
|    |                |                  | "subject": "CN=cilium-ca-root",                    |       | 
|    |                |                  | "sign_algo": "sha256WithRSAEncryption",            |       | 
|    |                |                  | "hash_algo": "sha256",                             |       | 
|    |                |                  | "valid_from": "2025-04-29T12:57:23.000000",        |       | 
|    |                |                  | "valid_to": "2027-02-05T04:57:23.000000"           |       | 
+----+----------------+------------------+----------------------------------------------------+-------+

Delete Issuer
-------------
- namespace: cilium
- name: cilium-root-ca
- deleted
Wait for no Issuer cilium/cilium-root-ca [timeout:60s]

Delete Secret
-------------
- namespace: cilium
- name: cilium-root-ca
- deleted
Wait for no Secret cilium/cilium-root-ca [timeout:60s]

Completed tasks
- issuer deleted

+----+---------+--------------+---------------+---------+---------+--------------+
| ID | Target  | Scope        | Workflow      | Changes | Success | Duration [s] |
+----+---------+--------------+---------------+---------+---------+--------------+
| 1  | ocp:bm1 | cert-manager | delete issuer | 2       | ✓       | 1            | 
+----+---------+--------------+---------------+---------+---------+--------------+
```

[[Back]](./README.md)