# Trident

[[Back]](../Operations.md)

![Logo](../images/trident/logo.png) 

NetApp Trident is an open source storage provisioner and orchestrator maintained by NetApp. It enables you to create storage volumes for containerized applications managed by Docker and Kubernetes. 

## Knowledge Base

- [install operator](./kb/operator.md)
- [create instance](./kb/instance.md)
- Install Trident on a Red Hat OpenShift cluster and create storage objects [link](https://docs.netapp.com/us-en/netapp-solutions-virtualization/openshift/osv-trident-install.html)
- [official documentation](https://docs.netapp.com/us-en/trident/trident-rn.html)

## Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp trident | check the trident operator | [Link](./get.md)
iserver set ocp trident --mode operator | install trident operator | [Link](./create_operator.md)
iserver set ocp trident --mode instance | creates trident orchestrator instance | [Link](./create_instance.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp trident --mode operator | delete trident operator | [Link](./delete_operator.md)
iserver delete ocp trident --mode instance | delete trident orchestrator instance | [Link](./delete_instance.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)