# Grafana Operator - Add empty dashboard (as-a-code)

Grafana dashboard can be created in as-a-code way using GrafanaDashboard CRD. This example is for the simplest empty dashboard. Keep in mind that any changes made to the dashboard via UI or not synchronized with CRD content.

Explore iserver-way to [create](./create_dashboard.md) and [delete](./delete_dashboard.md) operations.

## YAML-way

```
apiVersion: grafana.integreatly.org/v1beta1
kind: GrafanaDashboard
metadata:
  name: dashboard1
  namespace: grafana-operator
spec:
  instanceSelector:
    matchLabels:
      dashboards: test
  folder: 'my-tests'
  json: |
    {
      "title": "my-first-dashboard",
      "uid" : "my-first-dashboard-id"
    }
```

Notes:
- keep namespace the same as operator and instance
- use labels to assign dashboard to desired Grafana instance
- check status of CRD

```
  status:
    conditions:
    - lastTransitionTime: "2025-11-28T15:43:54Z"
      message: Dashboard was successfully applied to 1 instances
      observedGeneration: 1
      reason: ApplySuccessful
      status: "True"
      type: DashboardSynchronized
    hash: ...
    lastResync: "2025-11-28T15:43:54Z"
    uid: my-first-dashboard-id
```

![Dashboards](../images/grafana/empty_dashboard_list.png)

![Content](../images/grafana/empty_dashboard_content.png)

[[Back]](./README.md)