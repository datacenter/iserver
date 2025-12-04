# Grafana Operator

[Grafana Operator](https://github.com/grafana/grafana-operator) is an open-source based Kubernetes operator that manages Grafana instances and its resources. Check [here](./overview.md) for details.

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp grafana | check the grafana operator state | [Link](./get.md)
iserver set ocp grafana --mode operator | install grafana operator | [Link](./create_operator.md)
iserver set ocp grafana --mode mon | enable user-workload monitoring | [Link](./enable_monitoring.md)
iserver set ocp grafana --mode instance | create and configure instance | [Link](./create_instance.md)
iserver set ocp grafana --mode all | install grafana operator, enable user-workload monitoring and create instance | [Link](./create_all.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp grafana --mode operator | delete nvidia grafana operator | [Link](./delete_operator.md)
iserver delete ocp grafana --mode mon | disable user-workload monitoring | [Link](./disable_monitoring.md)
iserver delete ocp grafana --mode instance | delete instance | [Link](./delete_instance.md)
iserver delete ocp grafana --mode wipe | delete grafana crds | [Link](./delete_wipe.md)
iserver delete ocp grafana --mode all | delete grafana crds, disable monitoring and delete operator | [Link](./delete_all.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

## Extras

- [grafana instance](./grafana_instance.md)
- [empty dashboard](./add_empty_dashboard.md)
- [dashboard with panels](./add_panels_dashboard.md)
- [integration with Intersight OpenTelemtry](https://github.com/akaliwod/imonitor/blob/master/README.md)

[[Back]](../Operations.md)
