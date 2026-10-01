# Certificate Manager - Get

[[Back]](./README.md)

## Workflow

- check cert manager repo and helm chart
- check cert manager crds incl. referenced secrets

## Requirements

Cluster with [helm cli enabled](../cli/helm.md)

## Configurable options

```
# iserver get ocp cert-manager 
  --cluster TEXT   Cluster name
  -v, --view TEXT  [state|res|all]  [default: state]
```

## Example (view:state)

```
# iserver get ocp ocp cert-manager --cluster bm1 

OpenShift Workflow - Certificate Manager - Get Information
==========================================================

OpenShift Cluster: bm1

+----+--------------+--------------+----------+-----------------------------------------+----------+----------------------+-------------+
| ID | Namespace    | Name         | Revision | Updated                                 | Status   | Chart                | App Version |
+----+--------------+--------------+----------+-----------------------------------------+----------+----------------------+-------------+
| 1  | cert-manager | cert-manager | 1        | 2026-06-23 14:13:42.378064781 +0000 UTC | deployed | cert-manager-v1.20.2 | v1.20.2     | 
+----+--------------+--------------+----------+-----------------------------------------+----------+----------------------+-------------+


Certificate Manager Resources
-----------------------------
- cluster issuer      : 1
- issuer              : 1
- certificate request : 2
- certificate         : 2


View: state (def), res, all
```

## Example (view:res)

```
# iserver get ocp ocp cert-manager --cluster bm1 -v res

OpenShift Workflow - Certificate Manager - Get Information
==========================================================

OpenShift Cluster: bm1


Certificate Manager Resources
-----------------------------
- cluster issuer      : 1
- issuer              : 1
- certificate request : 2
- certificate         : 2


+----+----------------+------------------+----------------------------------------------------+-------+
| ID | Cluster Issuer | Secret           | Certificate                                        | Ready |
+----+----------------+------------------+----------------------------------------------------+-------+
| 1  | cilium-root-ca | ✓ cilium-root-ca | "version": "v3",                                   | ✓     | 
|    |                |                  | "serial": 111,                                     |       | 
|    |                |                  | "issuer": "CN=cilium-ca-root",                     |       | 
|    |                |                  | "subject": "CN=cilium-ca-root",                    |       | 
|    |                |                  | "sign_algo": "sha256WithRSAEncryption",            |       | 
|    |                |                  | "hash_algo": "sha256",                             |       | 
|    |                |                  | "valid_from": "2025-04-29T12:57:23.000000",        |       | 
|    |                |                  | "valid_to": "2027-02-05T04:57:23.000000"           |       | 
+----+----------------+------------------+----------------------------------------------------+-------+

+----+----------------+------------------+----------------------------------------------------+-------+
| ID | Issuer         | Secret           | Certificate                                        | Ready |
+----+----------------+------------------+----------------------------------------------------+-------+
| 1  | cilium         | ✓ cilium-root-ca | "version": "v3",                                   | ✓     | 
|    | cilium-root-ca |                  | "serial": 111,                             |       |       | 
|    |                |                  | "issuer": "CN=cilium-ca-root",                     |       | 
|    |                |                  | "subject": "CN=cilium-ca-root",                    |       | 
|    |                |                  | "sign_algo": "sha256WithRSAEncryption",            |       | 
|    |                |                  | "hash_algo": "sha256",                             |       | 
|    |                |                  | "valid_from": "2025-04-29T12:57:23.000000",        |       | 
|    |                |                  | "valid_to": "2027-02-05T04:57:23.000000"           |       | 
+----+----------------+------------------+----------------------------------------------------+-------+

+----+-----------------------------+----------+-------+------------------------+-------------------------------------------------+
| ID | Certificate Request         | Approved | Ready | Issuer                 | Requester                                       |
+----+-----------------------------+----------+-------+------------------------+-------------------------------------------------+
| 1  | cilium                      | ✓        | ✓     | kind: ClusterIssuer    | system:serviceaccount:cert-manager:cert-manager | 
|    | hubble-relay-client-certs-1 |          |       | name: cilium-root-ca   |                                                 | 
|    |                             |          |       | group: cert-manager.io |                                                 | 
+----+-----------------------------+----------+-------+------------------------+-------------------------------------------------+
| 2  | cilium                      | ✓        | ✓     | kind: ClusterIssuer    | system:serviceaccount:cert-manager:cert-manager | 
|    | hubble-server-certs-1       |          |       | name: cilium-root-ca   |                                                 | 
|    |                             |          |       | group: cert-manager.io |                                                 | 
+----+-----------------------------+----------+-------+------------------------+-------------------------------------------------+

+----+---------------------------+-----------------------------+-----------------------------+-------------------------------------------------------------+-------+
| ID | Certificate               | Issuer                      | Secret                      | Certificate                                                 | Ready |
+----+---------------------------+-----------------------------+-----------------------------+-------------------------------------------------------------+-------+
| 1  | cilium                    | "group": "cert-manager.io", | ✓ hubble-relay-client-certs | "version": "v3",                                            | ✓     | 
|    | hubble-relay-client-certs | "kind": "ClusterIssuer",    |                             | "serial": 222,                                              |       | 
|    |                           | "name": "cilium-root-ca"    |                             | "issuer": "CN=cilium-ca-root",                              |       | 
|    |                           |                             |                             | "subject": "CN=*.hubble-relay.cilium.io",                   |       | 
|    |                           |                             |                             | "sign_algo": "sha256WithRSAEncryption",                     |       | 
|    |                           |                             |                             | "hash_algo": "sha256",                                      |       | 
|    |                           |                             |                             | "valid_from": "2026-06-25T09:08:39.000000",                 |       | 
|    |                           |                             |                             | "valid_to": "2026-06-26T09:08:39.000000"                    |       | 
+----+---------------------------+-----------------------------+-----------------------------+-------------------------------------------------------------+-------+
| 2  | cilium                    | "group": "cert-manager.io", | ✓ hubble-server-certs       | "version": "v3",                                            | ✓     | 
|    | hubble-server-certs       | "kind": "ClusterIssuer",    |                             | "serial": 333,                                              |       | 
|    |                           | "name": "cilium-root-ca"    |                             | "issuer": "CN=cilium-ca-root",                              |       | 
|    |                           |                             |                             | "subject": "CN=*.default.hubble-grpc.cilium.io",            |       | 
|    |                           |                             |                             | "sign_algo": "sha256WithRSAEncryption",                     |       | 
|    |                           |                             |                             | "hash_algo": "sha256",                                      |       | 
|    |                           |                             |                             | "valid_from": "2026-06-25T09:08:39.000000",                 |       | 
|    |                           |                             |                             | "valid_to": "2026-06-26T09:08:39.000000"                    |       | 
+----+---------------------------+-----------------------------+-----------------------------+-------------------------------------------------------------+-------+

View: state (def), res, all
```

[[Back]](./README.md)