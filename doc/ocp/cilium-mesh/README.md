# Cilium Cluster Mesh

Cluster Mesh is the Isovalent Networking for Kubernetes multi-cluster solution, which extends Cilium's networking datapath across multiple clusters.

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp cilium mesh | get cluster mesh configuration and state | [Link](./get.md)
iserver set ocp cilium mesh --mode feature | enable cluster mesh feature | [Link](./enable.md)
iserver set ocp cilium mesh --mode cluster | add cluster to mesh | [Link](./create_cluster.md)
iserver set ocp cilium mesh --mode timescape | enable timescape for cluster mesh | [Link](./enable_timescape.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp cilium mesh --mode feature | delete cluster mesh feature | [Link](./disable.md)
iserver delete ocp cilium mesh --mode cluster | delete cluster from mesh | [Link](./delete_cluster.md)
iserver delete ocp cilium mesh --mode timescape | disable timescape for cluster mesh | [Link](./disable_timescape.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)