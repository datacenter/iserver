# Cilium Cluster Mesh - Enable timescape

## Workflow

- check cilium cni operator state
- check current cilium configuration 
- update cilium configuration with

```
hubble:
  timescape:
    clustermesh:
      primary:
        namespace: ''
```

- restart cilium operators and agents
- wait for cilium resources to be back up
- wait for timescape resources to be back up

## Requirements

Cluster mesh enabled
Timescape enabled

## Configurable options

```
# iserver set ocp cilium mesh --mode timescape
  --cluster TEXT            Cluster Name
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
# iserver set ocp cilium mesh --mode timescape --cluster bm1

OpenShift Workflow - Cilium - Enable Cluster Mesh Timescape
===========================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "confirmation": true,
    "check-verbose": true,
    "namespace": "cilium",
    "package": "clife",
    "secret": "cilium-ca-root",
    "certificate": "cilium-ocp",
    "certificate-admin": "clustermesh-apiserver-admin-cert",
    "certificate-remote": "clustermesh-apiserver-remote-cert",
    "certificate-server": "clustermesh-apiserver-server-cert"
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
Timescape enabled
Timescape currently disabled for cluster mesh
~~~
hubble:
  timescape:
    clustermesh:
      primary:
        namespace: ''

~~~

Cilium config update
--------------------
CiliumConfig CRD patched
Take a nap to detect automatic deployment restart...
Fallback to forced reload
Deployment [cilium/cilium-operator] patch successful
Daemon set [cilium/cilium] patch successful

Wait for Cilium resources
-------------------------
- pod: cilium-4bzvz
- pod: cilium-dm9gd
- pod: cilium-envoy-bwzml
- pod: cilium-envoy-gm8k5
- pod: cilium-envoy-v9jgx
- pod: cilium-operator-b5446b59f-sc2b8
- pod: cilium-operator-b5446b59f-vvrsn
- pod: cilium-sw5l6
- pod: clife-controller-manager-6c79869f6c-gcj6l
- pod: clustermesh-apiserver-5fbcd5b558-gws27
- pod: hubble-timescape-0
- deployment: cilium-operator
- deployment: clife-controller-manager
- deployment: clustermesh-apiserver
Wait for timescape pods...
Wait for timescape endpoints...

Completed tasks
- Timescape enabled for cluster mesh
```

[[Back]](./README.md)