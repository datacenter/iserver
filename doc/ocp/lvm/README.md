# LVM Storage Operator

Logical volume manager storage (LVM Storage) uses an LVM CSI driver to dynamically provision local storage on OpenShift clusters. 

Check more details in [OpenShift](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/configuring-persistent-storage#persistent-storage-using-lvms) and [GitHub](https://github.com/openshift/lvm-operator) documentation.

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver set ocp lvm --mode operator | install LVM operator | [Link](./create_operator.md)
iserver set ocp lvm --mode cluster | add LVM cluster instance | [Link](./create_cluster.md)
iserver set ocp lvm --mode all | install operator and add LVM cluster instance | [Link](./create_all.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp lvm --mode cluster | delete LVM Cluster object | [Link](./delete_cluster.md)
iserver delete ocp lvm --mode operator| uninstall LVM operator | [Link](./delete_operator.md)
iserver delete ocp lvm --mode all | install operator and add LVM cluster instance | [Link](./delete_all.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

## Other Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp lvm | check the LVM operator state | [Link](./get.md)
iserver set ocp lvm --mode test | test LVM operator | [Link](./test.md)
iserver delete ocp lvm --mode unused | delete unused LVM resources | [Link](./delete_unused.md)
iserver delete ocp lvm --mode orphan | delete orphan Linux LVM resources | [Link](./delete_orphan.md)

## Related Commands

Command | Intent | Details
--- | --- | ---
iserver get linux lsblk | check block devices on Linux server | [Link](./lsblk.md)
iserver get linux lv | check logical volumes on Linux server | [Link](./lv.md)
iserver get linux vg | check volume groups on Linux server | [Link](./vg.md)
iserver get linux pv | check physical volumes on Linux server | [Link](./pv.md)
iserver get linux lvm | check logical volume manager on Linux server | [Link](./lvm.md)

[[Back]](../Operations.md)