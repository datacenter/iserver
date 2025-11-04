# Tetragon Enterprise Operator

## Overview

[Tetragon Enterprise Operator](https://isovalent.com/blog/post/isovalent-enterprise-for-tetragon-1-14/) is a Kubernetes-native synchronous monitoring, filtering & enforcement tool that applies policies and filtering directly in-kernel with eBPF.

## HowTo by Example

- Grafana observability dashboards visualizing Prometheus metrics exposed by Tetragon ([Link](./observability.md))

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp tetragon | check the tetragon operator state | [Link](./get.md)
iserver set ocp tetragon --mode operator | install tetragon operator | [Link](./create_operator.md)
iserver set ocp tetragon --mode prometheus | enable prometheus integration | [Link](./enable_prometheus.md)
iserver set ocp tetragon --mode crd | configure tetragon | [Link](./create_crd.md)
iserver set ocp tetragon --mode all | install tetragon operator, enable prometheus and apply crds | [Link](./create_all.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp tetragon --mode operator | delete nvidia tetragon operator | [Link](./delete_operator.md)
iserver delete ocp tetragon --mode crd | unconfigure tetragon | [Link](./delete_crd.md)
iserver delete ocp tetragon --mode prometheus | disable prometheus integration | [Link](./disable_prometheus.md)
iserver delete ocp tetragon --mode wipe | delete tetragon crds | [Link](./delete_wipe.md)
iserver delete ocp tetragon --mode all | delete tetragon crds and delete operator | [Link](./delete_all.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)