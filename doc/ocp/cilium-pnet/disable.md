# Private Network - Disable feature

[[Back]](./README.md)

## Workflow

- check cilium cni operator state
- check current cilium configuration
- delete all private network crds if --wipe option
- break if private network crds are defined
- disable private network feature 
- restart cilium operators and agents
- wait for cilium resources to be back up
- check expected private network crd are no longer available

## Configurable options

```
# iserver delete ocp cilium pnet --mode feature
  --cluster TEXT     Cluster Name
  --wipe             Wipe crds
  --no-confirm       Confirmation mode
```

## Example

```
# iserver delete ocp cilium pnet --cluster bm1 --mode feature --wipe

OpenShift Workflow - Isovalent Private Network - Disable
========================================================

OpenShift Cluster: bm1
Cilium cni found

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
        kubectl.kubernetes.io/restartedAt: '2026-05-13T15:47:04.010554Z'
~~~
Deployment [cilium/cilium-operator] patched
Daemon set [cilium/cilium] patch successful

Wait for Cilium resources
-------------------------
- pod: cilium-5mscd
- pod: cilium-6znx2
- pod: cilium-envoy-lk4fs
- pod: cilium-envoy-rn9gt
- pod: cilium-envoy-szrqn
- pod: cilium-operator-65f79bbc87-kjth8
- pod: cilium-operator-65f79bbc87-t7zcv
- pod: cilium-q9wcs
- pod: clife-controller-manager-57f789f995-qzk6f
- deployment: cilium-operator
- deployment: clife-controller-manager

Completed tasks
- Private Network feature disabled

+----+---------+-------------+----------------+---------+---------+--------------+
| ID | Target  | Scope       | Workflow       | Changes | Success | Duration [s] |
+----+---------+-------------+----------------+---------+---------+--------------+
| 1  | ocp:bm1 | cilium-pnet | delete feature | 3       | ✓       | 125          | 
+----+---------+-------------+----------------+---------+---------+--------------+
```

[[Back]](./README.md)