# Trident Operator

NetApp Trident is an open source storage provisioner and orchestrator maintained by NetApp. It enables you to create storage volumes for containerized applications managed by Docker and Kubernetes. For full release information, including patch release changes, see [documentation](https://docs.netapp.com/us-en/trident/trident-rn.html).

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp trident | check the trident operator | [Link](./get.md)
iserver set ocp trident --mode operator | install trident operator | [Link](./create_operator.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp trident --mode operator | delete trident operator | [Link](./delete_operator.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)