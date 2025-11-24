# Prometheus Operator

OpenShift Container Platform ships with a pre-configured and self-updating monitoring stack that is based on the Prometheus open source project and its wider eco-system. It provides monitoring of cluster components and ships with a set of alerts to immediately notify the cluster administrator about any occurring problems and a set of Grafana dashboards. Check [here](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/monitoring/about-openshift-container-platform-monitoring) for details.

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp prometheus | check the prometheus state | [Link](./get.md)
iserver set ocp prometheus --mode user | enable user-workload monitoring | [Link](./enable_monitoring.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp prometheus --mode user | disable user-workload monitoring | [Link](./disable_monitoring.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

## Related Commands

Command | Intent | Details
--- | --- | ---
iserver get k8s ep | get endpoints | [Link](./endpoints.md)
iserver get k8s ep | get services | [Link](./services.md)
iserver get k8s promtarget | get prometheus targets | [Link](./prometheus_targets.md)
iserver get k8s smon | get service monitors | [Link](./service_monitors.md)

## Extras

- [enable user workload monitoring](./enable_user_workload_monitoring.md)
- [platform metrics targets via cli](./platform_metrics_targets_cli.md)
- [user metrics targets via cli](./user_metrics_targets_cli.md)
- [create basic service monitor via cli](./service_monitor_cli.md)
- [service monitor crd](./service_monitor_crd.md)

[[Back]](../Operations.md)
