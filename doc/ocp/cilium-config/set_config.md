# Cilium Configuration - Set configuration

## Workflow

- get current `cilium config`
- update spec of based on the filename content
- if no wait mode then exit
- check state transitions for value or processing errors
- if errors detected and no rollback, exit with error
- else rollback configuration
- detect automatic agent restarts or force restart daemon set
- wait for agents to come up

## Requirements

None

## Configurable options

```
# iserver set ocp cilium config
  --cluster TEXT   Cluster Name
  --filename TEXT  Target configuration
  --no-wait        Wait mode
  --no-confirm     Confirmation mode
  --no-rollback    Rollback mode
```

Note: 
- file content must be in yaml format
- if kube yaml detected then kind CiliumConfig expected and content is based on spec
- else yaml content is desired spec

## Example (success)

```
# iserver set ocp cilium config --cluster bm1 --filename /tmp/config.yaml

OpenShift Workflow - Cilium - Set configuration
===============================================

OpenShift Cluster: bm1

Cilium config update
--------------------
~~~
apiVersion: cilium.io/v1alpha1
kind: CiliumConfig
metadata:
  labels:
    app.kubernetes.io/name: clife
  name: ciliumconfig
  resourceVersion: '83133176'
spec:
  cluster:
    id: 1
    name: ocp
...
~~~
Continue [Y/N]? y
CiliumConfig CRD patched
Take a nap to check cilium config state and detect automatic deployment restart...
Cilium configuration valid
Fallback to forced agent reload
Daemon set [cilium/cilium] patch successful

Wait for Cilium resources
-------------------------
- pod: cilium-fvlxm
- pod: cilium-jkbgd
- pod: cilium-qqdwf

Configuration updated successfully
```

## Example (rollback)

```
# iserver set ocp cilium config --cluster bm1 --filename /tmp/config-invalid.yaml

OpenShift Workflow - Cilium - Set configuration
===============================================

OpenShift Cluster: bm1

Cilium config update
--------------------
~~~
apiVersion: cilium.io/v1alpha1
kind: CiliumConfig
metadata:
  labels:
    app.kubernetes.io/name: clife
  name: ciliumconfig
  resourceVersion: '83151022'
spec:
  cluster:
    id: 1
    name: ocp
  hubble:
    enabled: it-should-fail
...
~~~
CiliumConfig CRD patched
Take a nap to check cilium config state and detect automatic deployment restart...
[ERROR] cilium configuration invalid
- processing [reason:HelmError]
~~~
helm cannot generate manifests: error processing charts: values don't meet the specifications of the schema(s) in the following chart(s):
cilium:
- at '/hubble/enabled': got string, want boolean

~~~
Rollback to previous configuration
CiliumConfig CRD patched
Extra nap...
Fallback to forced agent reload
Daemon set [cilium/cilium] patch successful

Wait for Cilium resources
-------------------------
- pod: cilium-jgbrt
- pod: cilium-nkpqx
- pod: cilium-xc9fs

Configuration update failed
```

[[Back]](./README.md)