# Container Virtualization Operator

Container virtualization (cnv) operator adds Openshift Virtualization feature that supports virtual machine deployment as explained in [RedHat OpenShift documentation](https://developers.redhat.com/products/openshift/virtualization).

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp cnv | check the cnv operator and instance state | [Link](./get.md)
iserver set ocp cnv --mode operator | install cnv operator | [Link](./create_operator.md)
iserver set ocp cnv --mode instance | create cnv instance | [Link](./create_instance.md)
iserver set ocp cnv --mode all | install cnv operator and create instance | [Link](./create_all.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp cnv --mode operator | delete cnv operator | [Link](./delete_operator.md)
iserver delete ocp cnv --mode instance | delete cnv instance | [Link](./delete_instance.md)
iserver delete ocp cnv --mode all | delete cnv instance and operator | [Link](./delete_all.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)