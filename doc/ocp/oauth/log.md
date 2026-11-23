# OpenShitf Authentication (OAuth) - Set log level

[[Back]](./README.md) [[Prev]](./restart.md) [[Next]](./get.md)

## Workflow

- get `Authentication` object
- change spec.logLevel to one of: Normal, Debug, Trace, TraceAll

## Requirements

None

## Configurable options

```
# iserver set ocp oauth --mode log
  --cluster TEXT   Cluster Name
```

## Example

```
# iserver set ocp oauth --cluster bm1 --mode log --level Debug


OpenShift Workflow - OAuth - Log Level
======================================

OpenShift Cluster: trinity


Authentication Operator
-----------------------
- Name             : cluster
- Log Level        : Normal
- Error Conditions : ---


Patch Authentication
--------------------
- name: cluster

~~~
apiVersion: operator.openshift.io/v1
kind: Authentication
metadata:
  name: cluster
spec:
  logLevel: Debug

~~~
Authentication [cluster] patched


Authentication Operator
-----------------------
- Name             : cluster
- Log Level        : Debug
- Error Conditions : ---


OAuth restart
- wait for no Pod openshift-authentication/oauth-openshift-55f74b6ccd-8rf8q [timeout:180s]
- wait for no Pod openshift-authentication/oauth-openshift-55f74b6ccd-hl7lf [timeout:180s]
- wait for no Pod openshift-authentication/oauth-openshift-55f74b6ccd-sr9mv [timeout:180s]
- wait for deployment openshift-authentication/oauth-openshift ready state [timeout:180s]
```

[[Back]](./README.md) [[Prev]](./restart.md) [[Next]](./get.md)