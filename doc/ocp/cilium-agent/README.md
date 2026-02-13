# Cilium Agent

## Overview

The [Cilium agent](https://docs.cilium.io/en/stable/overview/component-overview/) runs on each node in the cluster. At a high-level, the agent accepts configuration via Kubernetes or APIs that describes networking, service load-balancing, network policies, and visibility & monitoring requirements.

The Cilium agent listens for events from orchestration systems such as Kubernetes to learn when containers or workloads are started and stopped. It manages the eBPF programs which the Linux kernel uses to control all network access in / out of those containers.

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp cilium agent -v pod | get cilium agent pods | [Link](./get_agent_pod.md)
iserver get ocp cilium agent -v logs | get cilium agent logs | [Link](./get_agent_logs.md)
iserver set ocp cilium restart --mode agent | restart cilium agents | [Link](./restart.md)

[[Back]](../Operations.md)