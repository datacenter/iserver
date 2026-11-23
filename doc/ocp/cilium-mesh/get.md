# Cilium Cluster Mesh - Get

## Workflow

- check cilium cni operator state
- check current cilium configuration
- get cilium mesh configuration
- get cilium cluster mesh state on every cilium agent

## Requirements

None

## Configurable options

```
# iserver get ocp cilium mesh
  --cluster TEXT     Cluster Name
```

## Non-configurable defaults

```
{
    "namespace": "cilium"
}
```

## Example

```
# iserver get ocp cilium mesh --cluster bm1 

OpenShift Workflow - Cilium - Get Mesh
======================================


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok


Cluster mesh configuration

~~~
apiserver:
  kvstoremesh:
    enabled: false
  nodePort: 32379
  replicas: 1
  service: {}
  tls:
    authMode: cluster
    auto:
      certManagerIssuerRef:
        group: cert-manager.io
        kind: Issuer
        name: cilium
      certValidityDuration: 1
      enabled: true
      method: certmanager
  type: NodePort
config:
  clusters:
  - ips:
    - 10.10.10.100
    name: inb
    port: 32380
  enabled: true
useAPIServer: true

~~~

+----+--------------+------------+--------------+--------------+---------+--------------+-------+-------------+-------+
| ID | Cluster Name | Cluster ID | Cluster IP   | Cluster Port | Summary | Cilium Agent | Node  | Node IP     | Ready |
+----+--------------+------------+--------------+--------------+---------+--------------+-------+-------------+-------+
| 1  | inb          | 2          | 10.10.10.100 | 32380        | 3/3     | cilium-sx24v | bm3-1 | 10.10.20.17 | ✓     |
|    |              |            |              |              |         | cilium-nkxhl | bm3-2 | 10.10.20.18 | ✓     |
|    |              |            |              |              |         | cilium-84g4v | bm3-3 | 10.10.20.19 | ✓     |
+----+--------------+------------+--------------+--------------+---------+--------------+-------+-------------+-------+
```

[[Back]](./README.md)