# Tetragon - Sandbox Policy

[[Back]](../README.md) [[Tracing]](./tracing_policy.md) [[Sandbox]](./sandbox_policy.md) [[Alert]](./alert_rule.md) [[PodInfo]](./pod_info.md)

`SandboxPolicy` and  `SandboxPolicyNamespaced` enable build “sandboxes” which constrain workloads’ operations. Instead of writing a net new policy for each set of workloads and accompanying system calls to monitor, these high-level policies use a list of system calls as a denylist or allowlist to easily apply.

References
- [blog post](https://isovalent.com/blog/post/isovalent-enterprise-for-tetragon-1-13/#sandbox-policies)
- [official doc](https://isovalent.com/blog/post/isovalent-enterprise-for-tetragon-1-13/#sandbox-policies)

## Example

In sandbox policy, a list of allowed syscalls and prevent all other sensitive syscalls outside this list (operator: "NotIn") from executing by a signal to terminate the disallowed process.

```yaml
apiVersion: cilium.io/v1alpha1
kind: SandboxPolicyNamespaced
metadata:
  name: "syscall-sandbox"
spec:
  syscalls:
    - list:
      - name: "sys_accept"
      - name: "sys_access"
      - name: "sys_adjtimex"
      - name: "sys_alarm"
      op: "NotIn"
      actions:
        - type: "Block"
        - type: "Signal"
```

[[Back]](../README.md) [[Tracing]](./tracing_policy.md) [[Sandbox]](./sandbox_policy.md) [[Alert]](./alert_rule.md) [[PodInfo]](./pod_info.md)