# NVIDIA NIM Operator

The NVIDIA NIM Operator enables Kubernetes cluster administrators to operate the software components and services necessary to deploy NVIDIA NIMs and NVIDIA NeMo microservices in Kubernetes as explained in [documentation](https://docs.nvidia.com/nim-operator/latest/).

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp nim | check the nim operator state | [Link](./get.md)
iserver set ocp nim | install nim operator | [Link](./create_operator.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp nim | uninstall nim operator | [Link](./delete_operator.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)