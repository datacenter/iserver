# RunIt - DNS Check

[[Back]](../BareMetalCluster.md) [[Next]](./example_variables_check.md) [[Prev]](./example_openshift_api_check.md)

Workflow
- check DNS resolution of `api` and `apps` names in the OpenShift cluster domain as defined in [cluster.json](./input_data_cluster_base.md)

```json
{
    "name": "my-cluster",
    "base_dns_domain": "domain.com",
    "api": "10.10.10.20",
    "ingress": "10.10.10.21"
}
```

Expected DNS resolution:
- (api.my-cluster.domain.com, 10.10.10.20)
- (oauth-openshift.apps.my-cluster.domain.com, 10.10.10.21)
- (console-openshift-console.apps.my-cluster.domain.com, 10.10.10.21)
- (grafana-openshift-monitoring.apps.my-cluster.domain.com, 10.10.10.21)
- (thanos-querier-openshift-monitoring.apps.my-cluster.domain.com, 10.10.10.21)
- (prometheus-k8s-openshift-monitoring.apps.my-cluster.domain.com, 10.10.10.21)
- (alertmanager-main-openshift-monitoring.apps.my-cluster.domain.com, 10.10.10.21)
- (hyperconverged-cluster-cli-download-openshift-cnv.apps.my-cluster.domain.com, 10.10.10.21)

```
Checking cluster fqdn resolution
Cluster FQDNs resolved correctly
```

[[Back]](../BareMetalCluster.md) [[Next]](./example_variables_check.md) [[Prev]](./example_openshift_api_check.md)