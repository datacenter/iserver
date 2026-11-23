# Certificate Manager - Create certificate

[[Back]](./README.md)

## Workflow

- check `Certificate` object based on user inputs
- wait until ready

## Requirements

- Certificate manager [installed](./enable.md)

## Configurable options

```
# iserver set ocp cert-manager --mode crt
  --cluster TEXT               Cluster name
  --namespace TEXT             CRD namespace
  --name TEXT                  CRD name
  --cn TEXT                    Common name
  --issuer TEXT                Issuer name
```

## Example 

```
# iserver set ocp ocp cert-manager \
    --cluster bm1 \
    --mode crt \
    --namespace default \
    --name test \
    --cn abc \
    --issuer cilium-root-ca

OpenShift Workflow - Certificate Manager - Create certificate
=============================================================

OpenShift Cluster: bm1

Create Certificate
------------------
- namespace: default
- name: test

~~~
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: test
  namespace: default
spec:
  commonName: test
  isCA: true
  issuerRef:
    group: cert-manager.io
    kind: ClusterIssuer
    name: cilium-root-ca
  secretName: test
~~~
Certificate [default/test] created
Wait for Certificate default/test [timeout:60s]
Wait for Certificate default/test [timeout:60s] with {"ready": true}

+----+-------------+-----------------------------+--------+-------------------------------------------------------------+-------+
| ID | Certificate | Issuer                      | Secret | Certificate                                                 | Ready |
+----+-------------+-----------------------------+--------+-------------------------------------------------------------+-------+
| 1  | default     | "group": "cert-manager.io", | ✓ test | "version": "v3",                                            | ✓     | 
|    | test        | "kind": "ClusterIssuer",    |        | "serial": 111,                                              |       | 
|    |             | "name": "cilium-root-ca"    |        | "issuer": "CN=cilium-ca-root",                              |       | 
|    |             |                             |        | "subject": "CN=test",                                       |       | 
|    |             |                             |        | "sign_algo": "sha256WithRSAEncryption",                     |       | 
|    |             |                             |        | "hash_algo": "sha256",                                      |       | 
|    |             |                             |        | "valid_from": "2026-06-26T10:17:11.000000",                 |       | 
|    |             |                             |        | "valid_to": "2026-09-24T10:17:11.000000"                    |       | 
+----+-------------+-----------------------------+--------+-------------------------------------------------------------+-------+

Completed tasks
- certificate created

+----+---------+--------------+------------+---------+---------+--------------+
| ID | Target  | Scope        | Workflow   | Changes | Success | Duration [s] |
+----+---------+--------------+------------+---------+---------+--------------+
| 1  | ocp:bm1 | cert-manager | create crt | 1       | ✓       | 8            | 
+----+---------+--------------+------------+---------+---------+--------------+
```

[[Back]](./README.md)