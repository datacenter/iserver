# CUDN w/Localnet Topology - Step 4: POD

[[Back]](./overview.md) [[Prev](./cudn.md)] [[Next]](./vm.md)

## Connection to POD CIDR

- POD **always** connects to Kubernetes POD CIDR
- the default route configuration depends on connection to CUDN

## Connection to primary CUDN

- POD **may** connect to cudn as primary interface
- [namespace](./namespace.md) must be labeled as primary enabled
- [cudn](./cudn.md) must be configured with role:Primary
- no definition required on the Pod CRD level
- localnet topology **cannot** be used

## Connection to secondary CUDN w/localnet topology

- POD **may** connect to cudn and that can be localnet
- no namespace label required
- [cudn](./cudn.md) must be configured with role:Secondary
- pod select nad created by cudn

```
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: ysphy
```

## CIDR example

```
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: ysphy
  name: p1-1
  namespace: island-y2
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
  nodeName: bm7-1
```

## POD state example

```
# iserver get k8s pod --namespace island-y2 -v net

+----+-----------+---------+----------+-----------------+-----+-------------------+-------------+
| ID | Pod       | HostNet | Intf     | Network         | Def | MAC               | IP          |
+----+-----------+---------+----------+-----------------+-----+-------------------+-------------+
| 1  | island-y2 | X       | eth0     | ovn-kubernetes  | X   | 0a:58:0a:80:01:30 | 10.128.1.48 | 
|    | p1-1      |         | ovn-udn1 | ovn-kubernetes  | V   | 0a:58:42:42:00:0a | 66.66.0.10  | 
|    |           |         | net1     | island-y2/ysphy | X   | 0a:58:42:42:01:07 | 66.66.1.7   | 
+----+-----------+---------+----------+-----------------+-----+-------------------+-------------+
```

[[Back]](./overview.md) [[Prev](./cudn.md)] [[Next]](./vm.md)