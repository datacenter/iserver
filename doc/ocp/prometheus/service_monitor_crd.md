# Service Monitor CRD

Refer to [documentation](https://docs.okd.io/4.18/rest_api/monitoring_apis/servicemonitor-monitoring-coreos-com-v1.html) for details

## Spec

Field | Type | Required | Description
endpoints | list | yes | how to scrape metrics from Kubernetes Endpoints (path, interval, port)
selector | object | yes | how to select Endpoints (label)
namespaceSelector | object | false | where (namespace) to search for endpoints, default the namespace of service monitor
targetLabels | list | false | labels to be copied from Service into ingested metric
podTargetLabels | list | false | labels to be copied from Pod into ingested metric

## Example

```
    "spec": {
        "endpoints": [
            {
                "bearerTokenFile": "/var/run/secrets/kubernetes.io/serviceaccount/token",
                "interval": "30s",
                "path": "/metrics",
                "port": "metrics",
                "relabelings": [
                    {
                        "action": "replace",
                        "regex": ";(.*)",
                        "replacement": "$1",
                        "separator": ";",
                        "sourceLabels": [
                            "node",
                            "__meta_kubernetes_pod_node_name"
                        ],
                        "targetLabel": "node"
                    }
                ],
                "scheme": "https",
                "tlsConfig": {
                    "caFile": "/etc/prometheus/configmaps/serving-certs-ca-bundle/service-ca.crt",
                    "serverName": "machine-config-controller.openshift-machine-config-operator.svc"
                }
            }
        ],
        "namespaceSelector": {
            "matchNames": [
                "openshift-machine-config-operator"
            ]
        },
        "selector": {
            "matchLabels": {
                "k8s-app": "machine-config-controller"
            }
        }
    }
```

[[Back]](./README.md)