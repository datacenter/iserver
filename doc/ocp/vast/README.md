# VAST CSI

[[Back]](../Operations.md)

![Logo](../images/vast/logo.png) 

The VAST Operator provides CSI driver for the VAST Data storage system configuration via custom resources

## Knowledge Base

- [VAST operator](./kb/operator.md)
- [VastCSIDriver](./kb/driver.md)
- [VastCluster](./kb/cluster.md)
- [VastStorage](./kb/storage.md)
- [CSI configuration example](./example.md)
- Deploying VAST CSI Driver on OpenShift with VAST CSI Operator - [external kb](https://kb.vastdata.com/documentation/docs/deploying-vast-csi-driver-on-openshift-with-vast-csi-operator)

## Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp vast | check the vast operator state | [Link](./get.md)
iserver set ocp vast --mode operator | install vast operator | [Link](./create_operator.md)
iserver set ocp vast --mode driver | add vast driver | [Link](./create_driver.md)
iserver set ocp vast --mode cluster | add vast cluster | [Link](./create_cluster.md)
iserver set ocp vast --mode storage | add vast storage | [Link](./create_storage.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp vast --mode operator | delete vast operator | [Link](./delete_operator.md)
iserver delete ocp vast --mode driver | delete vast driver | [Link](./delete_driver.md)
iserver delete ocp vast --mode cluster | delete vast cluster | [Link](./delete_cluster.md)
iserver delete ocp vast --mode storage | delete vast storage | [Link](./delete_storage.md)
iserver delete ocp vast --mode wipe | wipe vast crds | [Link](./delete_wipe.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

## Related

Command | Intent | Details
--- | --- | ---
iserver get k8s vastd | get vast csi drivers | [Link](./driver.md)
iserver get k8s vastc | get vast cluster | [Link](./cluster.md)
iserver get k8s vasts | get vast storage | [Link](./storage.md)

[[Back]](../Operations.md)