# Tetragon

[[Back]](../Operations.md)

![Logo](../images/tetragon/logo.png) 

[Tetragon Enterprise Operator](https://docs.isovalent.com/iep/latest/tetragon/index.html/) is a Kubernetes-native synchronous monitoring, filtering & enforcement tool that applies policies and filtering directly in-kernel with eBPF using custom resources

>[!CAUTION]
>Isovalent Registry Access [configuration](./IEP.md) is mandatory for operator installation.

## Knowledge Base

- [Tetragon operator](./kb/operator.md)
- custom resources
    - [TracingPolicy and TracingPolicyNamespaced](./kb/tracing_policy.md)
    - [SandboxPolicy and SandboxPolicyNamespaced](./kb/sandbox_policy.md)
    - [AlertRule](./kb/alert_rule.md)
    - [PodInfo](./kb/pod_info.md)

## Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp tetragon | check the tetragon operator state | [Link](./get.md)
iserver set ocp tetragon --mode operator | install tetragon operator | [Link](./create_operator.md)
iserver set ocp tetragon --mode crd | configure tetragon | [Link](./create_crd.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp tetragon --mode operator | delete tetragon operator | [Link](./delete_operator.md)
iserver delete ocp tetragon --mode crd | delete tetragon crds | [Link](./delete_crd.md)
iserver delete ocp tetragon --mode wipe | delete all tetragon configurations | [Link](./delete_wipe.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)