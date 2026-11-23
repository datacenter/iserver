# Node Feature Discovery Operator

[[Back]](../Operations.md)

Node Feature Discovery (NFD) Operator
- detects hardware features and configuration
- labels the nodes with hardware-specific information e.g., PCI cards, kernel, operating system version

```
apiVersion: v1
kind: Node
metadata:
  labels:
    cpu-feature.node.kubevirt.io/3dnowprefetch: "true"
    cpu-feature.node.kubevirt.io/abm: "true"
    ...
```

## Knowledge Base

- [install operator](./kb/operator.md)
- [create nfd instance](./kb/instance.md)
- [RedHat OpenShift documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/specialized_hardware_and_driver_enablement/psap-node-feature-discovery-operator)

## Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp nfd | check the NFD operator state | [Link](./get.md)
iserver set ocp nfd --mode operator | install and configure NFD operator | [Link](./create_operator.md)
iserver set ocp nfd --mode instance | configure NFD instance | [Link](./create_instance.md)
iserver set ocp nfd --mode all | runs operator and instance workflows | [Link](./create_all.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp nfd --mode operator | uninstall NFD operator | [Link](./delete_operator.md)
iserver delete ocp nfd --mode instance | delete NFD instance | [Link](./delete_instance.md)
iserver delete ocp nfd --mode all | runs instance and operator workflows | [Link](./delete_all.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

[[Back]](../Operations.md)