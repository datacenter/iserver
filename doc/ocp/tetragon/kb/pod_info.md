# Tetragon - POD Info

[[Back]](../README.md) [[Tracing]](./tracing_policy.md) [[Sandbox]](./sandbox_policy.md) [[Alert]](./alert_rule.md) [[PodInfo]](./pod_info.md)

`PodInfo` CRD is a key-value store containing Pod IPs and Workload objects. The Tetragon Operator queries the Kubernetes API server for Pod metadata information and updates the CRD accordingly.

## Example

Basic nginx application

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - image: nginx
    name: nginx
```

Corresponding PodInfo

```yaml
apiVersion: cilium.io/v1alpha1
kind: PodInfo
metadata:
  annotations:
    ...
  name: nginx
  namespace: default
spec:
  nodeName: bm1-1
status:
  podIP: 10.246.0.60
  podIPs:
  - IP: 10.246.0.60
workloadObject:
  name: nginx
  namespace: default
workloadType:
  apiVersion: v1
  kind: Pod
```

[[Back]](../README.md) [[Tracing]](./tracing_policy.md) [[Sandbox]](./sandbox_policy.md) [[Alert]](./alert_rule.md) [[PodInfo]](./pod_info.md)