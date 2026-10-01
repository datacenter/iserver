# Container Virtualization Operator

Container virtualization (cnv) operator adds Openshift Virtualization feature that supports virtual machine deployment

## Knowledge Base

- [install operator](./kb/operator.md)
- [create instance](./kb/instance.md)
- [RedHat OpenShift documentation](https://developers.redhat.com/products/openshift/virtualization)

## Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp cnv -v state | check the cnv operator and hyperconverged instance state | [Link](./get_state.md)
iserver get ocp cnv -v import | check data import details | [Link](./get_import.md)
iserver get ocp cnv -v crd | get cnv related crds | [Link](./get_crd.md)
iserver set ocp cnv --mode operator | install cnv operator | [Link](./create_operator.md)
iserver set ocp cnv --mode instance | create cnv instance | [Link](./create_instance.md)
iserver set ocp cnv --mode import | enable data import | [Link](./enable_import.md)
iserver set ocp cnv --mode all | install cnv operator and create instance | [Link](./create_all.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp cnv --mode operator | delete cnv operator | [Link](./delete_operator.md)
iserver delete ocp cnv --mode instance | delete cnv instance | [Link](./delete_instance.md)
iserver delete ocp cnv --mode import | disable data import | [Link](./disable_import.md)
iserver delete ocp cnv --mode all | delete cnv instance and operator | [Link](./delete_all.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)