# Tetragon - Alert Rule

[[Back]](../README.md) [[Tracing]](./tracing_policy.md) [[Sandbox]](./sandbox_policy.md) [[Alert]](./alert_rule.md) [[PodInfo]](./pod_info.md)

`AlertRule` enables users to define custom alert rules based on Tetragon events, triggering real-time notifications when suspicious activity is detected.

References
- [blog](https://isovalent.com/blog/post/isovalent-runtime-security-116/#flexible-lightweight-alert-rules)
- [official documentation](https://docs.isovalent.com/iep/latest/tetragon/policies/alertrule/index.html)

## Example

```yaml
apiVersion: cilium.io/v1alpha1
kind: AlertRule
metadata:
  name: aws-credential-hunting
spec:
  message: "AWS credential hunting detected"
  tags: ["security", "aws", "credential"]
  severity: "high"
  expression: |
    process_exec.process != null && (
      (
        process_exec.process.binary.endsWith("grep") ||
        process_exec.process.binary.endsWith("egrep") ||
        process_exec.process.binary.endsWith("fgrep")
      ) &&
      (
        process_exec.process.arguments.contains("AWS_ACCESS_KEY_ID") ||
        process_exec.process.arguments.contains("AWS_SECRET_ACCESS_KEY") ||
        process_exec.process.arguments.contains("AWS_SESSION_TOKEN")
      )
    ) || (
      process_exec.process != null && (
        (
          process_exec.process.binary.endsWith("find") ||
          process_exec.process.binary.endsWith("fd")
        ) &&
        (
          process_exec.process.arguments.contains("AWS_ACCESS_KEY_ID") ||
          process_exec.process.arguments.contains("AWS_SECRET_ACCESS_KEY") ||
          process_exec.process.arguments.contains("config")
        )
      )
    )
```

[[Back]](../README.md) [[Tracing]](./tracing_policy.md) [[Sandbox]](./sandbox_policy.md) [[Alert]](./alert_rule.md) [[PodInfo]](./pod_info.md)