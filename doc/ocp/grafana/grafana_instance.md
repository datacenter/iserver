# Grafana Operator - Grafana Instance

Grafana instance is managed with Grafana CRD. Grafana operator triggers deployment and services based on Grafana definition. An extra route can expose the service for external access. As the final outcome, you get the empty Grafana instance that you can either further configure manually (via UI) or continue as-a-code approach by applying other CRDs for dashboards, folders, data sources, alerts etc. These definitions are applied to Grafana instance based on the labels.

Explore iserver-way to [create](./create_instance.md), [delete](./delete_instance.md) and [get](./get.md) operations.

## YAML-way

Create yaml file following example below. Keep namespace the same as Grafana operator's namespace.

```
apiVersion: grafana.integreatly.org/v1beta1
kind: Grafana
metadata:
  labels:
    dashboards: test
  name: test
  namespace: grafana-operator
spec:
  config:
    auth:
      disable_login_form: "false"
    log:
      mode: console
    security:
      admin_user: user
      admin_password: pass
  route:
    spec: {}
```

```
$ oc apply -f grafana.yaml
```

Wait until deployment ready. Route is created automatically for Grafana instance UI access from outside.

```
$ oc get all -n grafana-operator
pod/grafana-operator-controller-manager-v5-589d6b5747-hc77x   1/1     Running   0          12d
pod/test-deployment-6d58f7886f-8ldfj                          1/1     Running   0          67s

NAME                                                TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)             AGE
service/grafana-operator-operator-metrics-service   ClusterIP   172.30.162.190   <none>        9090/TCP,8888/TCP   12d
service/test-alerting                               ClusterIP   None             <none>        9094/TCP            67s
service/test-service                                ClusterIP   172.30.130.186   <none>        3000/TCP            67s

NAME                                                     READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/grafana-operator-controller-manager-v5   1/1     1            1           12d
deployment.apps/test-deployment                          1/1     1            1           67s

NAME                                                                DESIRED   CURRENT   READY   AGE
replicaset.apps/grafana-operator-controller-manager-v5-589d6b5747   1         1         1       12d
replicaset.apps/test-deployment-6d58f7886f                          1         1         1       67s

NAME                                  HOST/PORT                                          PATH   SERVICES       PORT   TERMINATION   WILDCARD
route.route.openshift.io/test-route   test-route-grafana-operator.apps.bm1.domain.com           test-service   3000   edge          None
```

Login page redirection

```
$ curl -k https://test-route-grafana-operator.apps.bm1.domain.com
<a href="/login">Found</a>.
```

![Login](../images/grafana/instance_login.png)

Deleting Grafana CRD will delete deployment, service and route.

[[Back]](./README.md)