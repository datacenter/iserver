# UDN and POD - CRD

[[Back]](../README.md) [[Prev]](../overview/pod.md) [[Next]](../create/pod_task.md)

Example with netshoot container connected to
- primary user defined network based on namespace state
- secondary user defined network based on annotation

```
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: s1-l2,s2-l2
  name: p1-3
  namespace: island
spec:
  containers:
  - command:
    - sleep
    - infinite
    image: nicolaka/netshoot:latest
    name: netshoot
    securityContext:
      capabilities:
        add:
        - IPC_LOCK
        - SYS_RESOURCE
        - NET_RAW
      runAsUser: 0
  nodeName: bm1-3
```

[[Back]](../README.md) [[Prev]](../overview/pod.md) [[Next]](../create/pod_task.md)