# Cilium Cluster Mesh - Create cluster

## Workflow

- check cilium cni operator state
- check current cilium configuration if cilium mesh is enabled
- patch clusters with new cluster definition
- update cilium configuration
- restart cilium operators and agents
- wait for cilium resources to be back up
- wait for new cluster to be ready

## Requirements

None

## Configurable options

```
# iserver delete ocp cilium mesh --mode cluster
  --cluster TEXT            Cluster Name
  --mesh-name TEXT          Cluster mesh name
  --mesh-ip TEXT            Cluster mesh ip
  --mesh-port INTEGER       Cluster mesh port
  --no-wait                 No-wait for cluster mesh up
  --no-confirm              Confirmation mode
```

## Non-configurable defaults

```
{
    "namespace": "cilium",
    "package": "clife"
}
```

## Example

```
# iserver set ocp cilium mesh --cluster bm1 --mode cluster --mesh-ip 10.10.10.100 --mesh-port 32380 --mesh-name inb --no-confirm

OpenShift Workflow - Cilium - Add Cluster to Mesh
=================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "mesh-name": "inb",
    "mesh-ip": "10.10.10.100",
    "mesh-port": 32380,
    "wait": true,
    "confirmation": false,
    "check-verbose": true,
    "namespace": "cilium",
    "package": "clife"
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:*****]
- api [*****]: ok
- dns resolution: ok



Operator
--------
- subscription          : cilium/clife
- package               : openshift-marketplace/certified-operators/clife
- channel               : 1.17
- install plan          : cilium/install-v6tpt
- install plan approved : ✓
- installed csv         : clife.v1.17.9-cee.1
- latest_csv            : ✓


Cluster mesh enabled


Cilium config update
--------------------
CiliumConfig CRD patched
Take a nap to detect automatic deployment restart...
Automatic pods rollout detected

Wait for Cilium resources
-------------------------
- pod: cilium-8gmkp
- pod: cilium-envoy-7c2z7
- pod: cilium-envoy-sm8bk
- pod: cilium-envoy-th29g
- pod: cilium-h5mlm
- pod: cilium-lm2jp
- pod: cilium-operator-9cd8c7b85-dgskz
- pod: cilium-operator-9cd8c7b85-xljgk
- pod: clife-controller-manager-7b4dd4bb46-nslcj
- pod: clustermesh-apiserver-869796877-k6h7h
- deployment: cilium-operator
- deployment: clife-controller-manager
- deployment: clustermesh-apiserver

Wait for cluster [inb] connected...

+----+--------------+------------+--------------+--------------+---------+--------------+-------+-------------+-------+
| ID | Cluster Name | Cluster ID | Cluster IP   | Cluster Port | Summary | Cilium Agent | Node  | Node IP     | Ready |
+----+--------------+------------+--------------+--------------+---------+--------------+-------+-------------+-------+
| 1  | inb          | 2          | 10.10.10.100 | 32380        | 3/3     | cilium-h5mlm | bm1-1 | 10.20.20.17 | ✓     | 
|    |              |            |              |              |         | cilium-8gmkp | bm1-2 | 10.20.20.18 | ✓     | 
|    |              |            |              |              |         | cilium-lm2jp | bm1-3 | 10.20.20.19 | ✓     | 
+----+--------------+------------+--------------+--------------+---------+--------------+-------+-------------+-------+

Completed tasks
- Cluster mesh added
```

[[Back]](./README.md)