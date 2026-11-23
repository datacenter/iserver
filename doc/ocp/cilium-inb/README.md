# Isovalent Network Bridge

The Isovalent Network Bride allows you to bridge Isovalent Private Network into existing external networks, enabling seamless, secure communication between different hypervisors, making it easier to migrate workloads with downtime or the requirement to change IP addresses.

![InbOverview](../images/inb/overview.png)

## Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp cilium inb | get inb configuration and state | [Link](./get.md)
iserver set ocp cilium inb --mode feature | install and configure inb | [Link](./enable.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp cilium inb --mode feature | unconfigure inb | [Link](./disable.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

## Note on dependencies

Isovalent Network Bridge is relatively complex feature that has multiple dependencies as summarized on the block diagram below

![Dependencies](../images/inb/dependencies.png)

- [certificate manager](../cert-manager/README.md)
- [timescape](../cilium-timescape/README.md)
- [cluster mesh](../cilium-mesh/README.md)
- [private network](../cilium-pnet/README.md)

You can enable inb with all dependencies with single [task](./create_e2e_task.md). 

[[Back]](../Operations.md)