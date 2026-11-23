# Certificate Manager - Create issuer or cluster issuer

[[Back]](./README.md)

## Workflow

- check input certificate file
- create `Secret` with tls.crt and tls.key based on input files
- if namespace is defined, create `Issuer` with `Secret` reference
- if namespace is not defined, create `ClusterIssuer` with `Secret` reference

## Requirements

- Certificate manager [installed](./enable.md)

## Configurable options

```
# iserver set ocp cert-manager --mode issuer
  --cluster TEXT           Cluster name
  --namespace TEXT         CRD namespace
  --name TEXT              CRD name
  --crt TEXT               Certificate file
  --key TEXT               Private key file
```

## Example (with namespace defined creating Issuer object)

```
# iserver set ocp ocp cert-manager \
    --cluster bm1 \
    --mode issuer \
    --namespace cilium \
    --name cilium-root-ca \
    --crt /tmp/root-ca.crt \
    --key /tmp/root-ca.key

OpenShift Workflow - Certificate Manager - Create issuer
========================================================

OpenShift Cluster: bm1

Root CA Cert
~~~
{
  "version": "v3",
  "serial": ...,
  "issuer": "CN=cilium-ca-root",
  "subject": "CN=cilium-ca-root",
  "sign_algo": "sha256WithRSAEncryption",
  "hash_algo": "sha256",
  "valid_from": "2025-04-29T12:57:23.000000",
  "valid_to": "2027-02-05T04:57:23.000000"
}
~~~

Create Secret
-------------
- namespace: cilium
- name: cilium-root-ca

~~~
apiVersion: v1
data:
  tls.crt: ...
  tls.key: ...
kind: Secret
metadata:
  name: cilium-root-ca
  namespace: cilium
type: kubernetes.io/tls
~~~
Secret [cilium/cilium-root-ca] created

Create Issuer
-------------
- namespace: cilium
- name: cilium-root-ca

~~~
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: cilium-root-ca
  namespace: cilium
spec:
  ca:
    secretName: cilium-root-ca
~~~
Issuer [cilium/cilium-root-ca] created
Wait for Issuer cilium/cilium-root-ca [timeout:60s]

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

Completed tasks
- issuer created

+----+---------+--------------+---------------+---------+---------+--------------+
| ID | Target  | Scope        | Workflow      | Changes | Success | Duration [s] |
+----+---------+--------------+---------------+---------+---------+--------------+
| 1  | ocp:bm1 | cert-manager | create issuer | 2       | ✓       | 27           | 
+----+---------+--------------+---------------+---------+---------+--------------+
```

[[Back]](./README.md)