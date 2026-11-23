# Tetragon - Tracing Policy

[[Back]](../README.md) [[Tracing]](./tracing_policy.md) [[Sandbox]](./sandbox_policy.md) [[Alert]](./alert_rule.md) [[PodInfo]](./pod_info.md)

`TracingPolicy` and `TracingPoliciesNamespaced` are a user-configurable Kubernetes custom resource (CR) that allows tracing arbitrary events in the kernel and optionally define actions to take on a match.

Refer to [official documentation](https://docs.isovalent.com/iep/latest/tetragon/policies/tracingpolicy/index.html) for details.

## Example

The policy checks for file descriptors being created, and sends a SIGKILL signal to any process that creates a file descriptor to a file named /tmp/tetragon. 

```yaml
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: "fd-install"
spec:
  kprobes:
  - call: "fd_install"
    syscall: false
    args:
    - index: 0
      type: "int"
    - index: 1
      type: "file"
    selectors:
    - matchArgs:
      - index: 1
        operator: "Equal"
        values:
        - "/tmp/tetragon"
      matchActions:
      - action: Sigkill
```

[[Back]](../README.md) [[Tracing]](./tracing_policy.md) [[Sandbox]](./sandbox_policy.md) [[Alert]](./alert_rule.md) [[PodInfo]](./pod_info.md)