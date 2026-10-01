# LVM Storage

[[Back]](../Operations.md) [[Linux: Disk and LVM]](../disk/README.md)

Logical volume manager storage (LVM Storage) uses an LVM CSI driver to dynamically provision local storage on OpenShift clusters. 

## Knowledge Base

- [create operator](./kb/operator.md)
- [create cluster](./kb/cluster.md)
- [LVM Operator in GitHub](https://github.com/openshift/lvm-operator)
- [OpenShift documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/configuring-persistent-storage#persistent-storage-using-lvms)

## Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp lvm | check the LVM operator state | [Link](./get.md)
iserver set ocp lvm --mode operator | install LVM operator | [Link](./create_operator.md)
iserver set ocp lvm --mode cluster | create LVM cluster instance | [Link](./create_cluster.md)
iserver set ocp lvm --mode all | install operator and add LVM cluster instance | [Link](./create_all.md)
iserver set ocp lvm --mode test | test LVM operator | [Link](./test.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp lvm --mode cluster | delete LVM Cluster object | [Link](./delete_cluster.md)
iserver delete ocp lvm --mode operator| uninstall LVM operator | [Link](./delete_operator.md)
iserver delete ocp lvm --mode all | install operator and add LVM cluster instance | [Link](./delete_all.md)
iserver delete ocp lvm --mode unused | delete unused LVM resources | [Link](./delete_unused.md)
iserver delete ocp lvm --mode orphan | delete orphan Linux LVM resources | [Link](./delete_orphan.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md) [[Linux: Disk and LVM]](../disk/README.md)