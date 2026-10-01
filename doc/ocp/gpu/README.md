# NVIDIA GPU Operator

The NVIDIA GPU Operator uses the operator framework within Kubernetes to automate the management of all NVIDIA software components needed to provision GPU e.g.,
- the NVIDIA drivers (to enable CUDA), 
- Kubernetes device plugin for GPUs, 
- the NVIDIA Container Toolkit, 
- automatic node labelling using GFD, 
- DCGM based monitoring.

Refer to [NVIDIA documentation](https://docs.nvidia.com/datacenter/cloud-native/openshift/24.3.0/introduction.html) for details.

## Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp gpu | check the GPU operator state | [Link](./get.md)
iserver set ocp gpu --mode operator | install nvidia gpu operator | [Link](./create_operator.md)
iserver set ocp gpu --mode policy | add cluster policy | [Link](./create_policy.md)
iserver set ocp gpu --mode dashboard | enable monitoring dashboard | [Link](./create_dashboard.md)
iserver set ocp gpu --mode all | do it all | [Link](./create_all.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp gpu --mode operator | delete nvidia gpu operator | [Link](./delete_operator.md)
iserver delete ocp gpu --mode policy | delete cluster policy | [Link](./delete_policy.md)
iserver delete ocp gpu --mode dashboard | disable monitoring dashboard | [Link](./delete_dashboard.md)
iserver delete ocp gpu --mode all | delete all | [Link](./delete_all.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)