# VAST Operator

The VAST Operator provides CSI driver for the VAST Data storage system.

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp vast | check the vast operator state | [Link](./get.md)
iserver set ocp vast --mode operator | install vast operator | [Link](./create_operator.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp vast --mode operator | delete vast operator | [Link](./delete_operator.md)
iserver delete ocp vast --mode wipe | wipe vast crds | [Link](./delete_wipe.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

## Related Commands

Command | Intent | Details
--- | --- | ---
iserver get k8s vastd | get vast csi drivers | [Link](./driver.md)
iserver get k8s vastc | get vast cluster | [Link](./cluster.md)
iserver get k8s vasts | get vast storage | [Link](./storage.md)

## Extras

- Deploying VAST CSI Driver on OpenShift with VAST CSI Operator [knowledge base article](https://kb.vastdata.com/documentation/docs/deploying-vast-csi-driver-on-openshift-with-vast-csi-operator)
- VAST CSI operator configuration [example](./example.md)

[[Back]](../Operations.md)