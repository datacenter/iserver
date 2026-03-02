# OpenShift Data Foundation (ODF) Operator

OpenShift Data Foundation (ODF) is a software-defined storage solution for Red Hat's container platform, OpenShift, that provides unified, persistent storage for containerized applications across various environments as explained on [RedHat documentation](https://docs.redhat.com/en/documentation/red_hat_openshift_data_foundation/4.19).

ODF can be installed on bare metal infrastructure where OpenShift is already installed. In such case ODF depends on [Local Storage Operator](../lso/README.md). iserver supports such deployment model only.

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp odf | check the odf operator and cluster state | [Link](./get.md)
iserver set ocp odf --mode operator | install odf operator | [Link](./create_operator.md)
iserver set ocp odf --mode cluster | create odf cluster | [Link](./create_cluster.md)
iserver set ocp odf --mode all | install odf operator and create cluster | [Link](./create_all.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp odf --mode operator | delete odf operator | [Link](./delete_operator.md)
iserver delete ocp odf --mode cluster | delete odf cluster | [Link](./delete_cluster.md)
iserver delete ocp odf --mode all | delete odf cluster and operator | [Link](./delete_all.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)