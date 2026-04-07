# OVNKubernetes BGP - Enable

[[Back]](../README.md) [[Disable]](./disable.md)

## CLI

```
# oc patch Network.operator.openshift.io/cluster --type=merge -p '{
  "spec": {
    "additionalRoutingCapabilities": {
      "providers": ["FRR"]
    }
  }
}'
```

## iserver

```
# iserver set ocp ovn-bgp --cluster bm1 --mode feature
```

Check details [here](../feature_enable.md)

## task-way

```
[
    {
        "ovn-bgp": {
            "feature": {}
        }
    }
]
```

```
# iserver set ocp task --cluster bm1 --file /tmp/task.json
```

Check details [here](../task_feature_enable.md)

## Expected state

All resources should come up in `openshift-frr-k8s` namespace

```
$ oc get all -n openshift-frr-k8s
NAME                                         READY   STATUS    RESTARTS   AGE
pod/frr-k8s-9ckzb                            7/7     Running   0          2m50s
pod/frr-k8s-c4jk4                            7/7     Running   0          2m50s
pod/frr-k8s-statuscleaner-6c46867584-2f6n4   1/1     Running   0          2m49s
pod/frr-k8s-zpxj6                            7/7     Running   0          2m50s

NAME                              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)             AGE
service/frr-k8s-monitor-service   ClusterIP   None            <none>        9140/TCP,9141/TCP   2m50s
service/frr-k8s-webhook-service   ClusterIP   172.30.144.15   <none>        443/TCP             2m49s

NAME                     DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
daemonset.apps/frr-k8s   3         3         3       3            3           kubernetes.io/os=linux   2m50s

NAME                                    READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/frr-k8s-statuscleaner   1/1     1            1           2m49s

NAME                                               DESIRED   CURRENT   READY   AGE
replicaset.apps/frr-k8s-statuscleaner-6c46867584   1         1         1       2m49s
```

containers inside the frr pod
- controller
- frr
- frr-metrics
- frr-status
- kube-rbac-proxy
- kube-rbac-proxy-frr
- reloader

Refer [frr cli access](./frr_cli.md)

New api resources
- [BGPSessionState](./session_state.md)
- [FRRNodeState](./node_state.md)
- [FRRConfiguration](./configuration.md)

## iserver (get)

TBD

[[Back]](../README.md) [[Disable]](./disable.md)