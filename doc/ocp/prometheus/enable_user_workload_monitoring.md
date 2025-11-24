# Prometheus Operator - User workload monitoring

You can use OpenShift Monitoring for your own services in addition to monitoring the cluster. By default user workload monitoring is disabled.

Use [iserver set ocp prometheus --mode user](./enable_monitoring.md) and refer to details below.

## Config Map

Create or edit config map to contain enableUserWorkload

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: name
  namespace: namespace
data:
  config.yaml: |-
    enableUserWorkload: true
```

## Resources

Wait until resources are ready in openshift-user-workload-monitoring namespace

```
$ oc get all -n openshift-user-workload-monitoring
NAME                                       READY   STATUS    RESTARTS   AGE
pod/prometheus-operator-744ff78877-cl4w8   2/2     Running   0          3m48s
pod/prometheus-user-workload-0             6/6     Running   0          3m45s
pod/prometheus-user-workload-1             6/6     Running   0          3m45s
pod/thanos-ruler-user-workload-0           4/4     Running   0          3m45s
pod/thanos-ruler-user-workload-1           4/4     Running   0          3m45s

NAME                                              TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                       AGE
service/prometheus-operated                       ClusterIP   None             <none>        9090/TCP,10901/TCP            3m45s
service/prometheus-operator                       ClusterIP   None             <none>        8443/TCP                      3m48s
service/prometheus-user-workload                  ClusterIP   172.30.223.14    <none>        9091/TCP,9092/TCP,10902/TCP   3m47s
service/prometheus-user-workload-thanos-sidecar   ClusterIP   None             <none>        10902/TCP                     3m47s
service/thanos-ruler                              ClusterIP   172.30.162.231   <none>        9091/TCP,9092/TCP,10901/TCP   3m48s
service/thanos-ruler-operated                     ClusterIP   None             <none>        10902/TCP,10901/TCP           3m45s

NAME                                  READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/prometheus-operator   1/1     1            1           3m48s

NAME                                             DESIRED   CURRENT   READY   AGE
replicaset.apps/prometheus-operator-744ff78877   1         1         1       3m48s

NAME                                          READY   AGE
statefulset.apps/prometheus-user-workload     2/2     3m45s
statefulset.apps/thanos-ruler-user-workload   2/2     3m45s

NAME                                    HOST/PORT                                                             PATH        SERVICES                   PORT       TERMINATION          WILDCARD
route.route.openshift.io/federate       federate-openshift-user-workload-monitoring.apps.bm1.domain.com       /federate   prometheus-user-workload   federate   reencrypt/Redirect   None
route.route.openshift.io/thanos-ruler   thanos-ruler-openshift-user-workload-monitoring.apps.bm1.domain.com   /api        thanos-ruler               web        reencrypt/Redirect   None
```

[[Back]](./README.md)
