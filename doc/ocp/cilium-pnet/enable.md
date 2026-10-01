# Private Network - Enable feature

[[Back]](./README.md) [[kb]](./kb/enable.md)

## Workflow

- check cilium cni operator state
- check current cilium configuration
- enable private network feature 
- restart cilium operators and agents
- wait for cilium resources to be back up
- check expected private network crd
- optional workaround (fixup)

## Requirements

None

## Expected outcome

Private network CRDs available
- ClusterwidePrivateNetwork
- PrivateNetworkEndpointSlice
- PrivateNetworkExternalEndpoint

## Configurable options

```
# iserver set ocp cilium pnet --mode feature
  --cluster TEXT                        Cluster Name
  --pnet [default|bridge|local-access]  Private network mode  [default: default]
  --no-confirm                          Confirmation mode
```

## Example

```
# iserver set ocp cilium pnet --cluster bm1 --mode feature 

OpenShift Workflow - Isovalent Private Network - Enable
=======================================================

OpenShift Cluster: bm1
Cilium cni found
~~~
cni:
  binPath: /var/lib/cni/bin
  chainingMode: portmap
  confPath: /var/run/multus/cni/net.d
  exclusive: false
enterprise:
  featureGate:
    strict: false
  privateNetworks:
    enabled: true
    mode: default
~~~

Cilium config update
--------------------
~~~
apiVersion: cilium.io/v1alpha1
kind: CiliumConfig
...
~~~
CiliumConfig CRD patched
Take a nap to check cilium config state and detect automatic deployment restart...
Cilium configuration valid
Forced agent reload
Forced operator reload

Patch Deployment
----------------
- namespace: cilium
- name: cilium-operator

~~~
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cilium-operator
  namespace: cilium
spec:
  template:
    metadata:
      annotations:
        kubectl.kubernetes.io/restartedAt: '2026-05-13T15:53:19.130873Z'
~~~
Deployment [cilium/cilium-operator] patched
Daemon set [cilium/cilium] patch successful

Wait for Cilium resources
-------------------------
- pod: cilium-6l5zj
- pod: cilium-envoy-lk4fs
- pod: cilium-envoy-rn9gt
- pod: cilium-envoy-szrqn
- pod: cilium-operator-67cccbc47-m7rfc
- pod: cilium-operator-67cccbc47-mjmdt
- pod: cilium-w2b2w
- pod: cilium-xmkvd
- pod: clife-controller-manager-57f789f995-qzk6f
- deployment: cilium-operator
- deployment: clife-controller-manager

Completed tasks
- Private Network feature enabled
- CRD ready

+----+---------+-------------+----------------+---------+---------+--------------+
| ID | Target  | Scope       | Workflow       | Changes | Success | Duration [s] |
+----+---------+-------------+----------------+---------+---------+--------------+
| 1  | ocp:bm1 | cilium-pnet | create feature | 3       | ✓       | 110          | 
+----+---------+-------------+----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[kb]](./kb/enable.md)