# OVNKubernetes BGP - Enable Route Advertisement

[[Back]](../README.md) [[Disable]](./disable_route_advertisement.md)

Route advertisements allows to 
- advertise default and user-defined network routes, including EgressIPs
- import routes from the provider network that configure the default pod network and user-defined networks

> [!NOTE]
> Route advertisement requires frr bgp provider [enabled](./enable.md)

## CLI

```
# oc patch Network.operator.openshift.io/cluster --type=merge -p '{
  "spec": {
    "defaultNetwork": {
        "ovnKubernetesConfig": {
            "routeAdvertisements": "Enabled"
        }
    }
  }
}'
```

## iserver

```
# iserver set ocp ovn-bgp --cluster bm1 --mode ra
```

Check details [here](../ra_enable.md)

## task-way

```
[
    {
        "ovn-bgp": {
            "ra": {}
        }
    }
]
```

```
# iserver set ocp task --cluster bm1 --file /tmp/task.json
```

Check details [here](../task_ra_enable.md)

## Expected state

All resources should restart and come up in `openshift-ovn-kubernetes` namespace

```
$ oc get all -n openshift-ovn-kubernetes 
NAME                                         READY   STATUS    RESTARTS   AGE
pod/ovnkube-control-plane-8688458b77-q4hmv   2/2     Running   0          81s
pod/ovnkube-control-plane-8688458b77-t2qsg   2/2     Running   0          82s
pod/ovnkube-node-2t8hr                       8/8     Running   0          61s
pod/ovnkube-node-dcrqz                       8/8     Running   0          42s
pod/ovnkube-node-j7wks                       8/8     Running   0          80s

NAME                                   TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)             AGE
service/ovn-kubernetes-control-plane   ClusterIP   None         <none>        9108/TCP            13d
service/ovn-kubernetes-node            ClusterIP   None         <none>        9103/TCP,9105/TCP   13d

NAME                          DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
daemonset.apps/ovnkube-node   3         3         3       3            3           kubernetes.io/os=linux   13d

NAME                                    READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/ovnkube-control-plane   2/2     2            2           13d

NAME                                               DESIRED   CURRENT   READY   AGE
replicaset.apps/ovnkube-control-plane-5dd74876d6   0         0         0       13d
replicaset.apps/ovnkube-control-plane-8688458b77   2         2         2       82s
```

Containers in ovnkube-node 
- kube-rbac-proxy-node
- kube-rbac-proxy-ovn-metrics
- nbdb
- northd
- ovn-acl-logging
- ovn-controller
- ovnkube-controller
- sbdb

New api resources
- [RouteAdvertisements](./route_advertisement.md)

[[Back]](../README.md) [[Disable]](./disable_route_advertisement.md)