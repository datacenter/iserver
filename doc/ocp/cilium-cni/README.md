# Cilium CNI

[Cilium](https://cilium.io/) CNI can be selected during OpenShift cluster installation. 

## State

Command | Intent | Details
--- | --- | ---
iserver get ocp cilium config | check cilium configuration | [Link](./get_config.md)
iserver get ocp cilium package | check cilium subscription and package | [Link](./get_package.md)
iserver get ocp cilium pod | check cilium pods | [Link](./get_pod.md)
iserver get ocp cilium state | check cilium state | [Link](./get_state.md)

## Image

Command | Intent | Details
--- | --- | ---
iserver set ocp cilium image | set cilium target image | [Link](./set_image.md)
iserver set ocp task | in task way | [Link](./set_image_task.md)

## Version control

Command | Intent | Details
--- | --- | ---
iserver set ocp cilium plan | approve cilium install plan | [Link](./set_plan.md)

## Features

- [cluster mesh](../cilium-mesh/README.md)
- [timescape](../cilium-timescape/README.md)

[[Back]](../Operations.md)