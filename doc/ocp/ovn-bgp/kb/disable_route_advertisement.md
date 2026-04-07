# OVNKubernetes BGP - Disable Route Advertisement

[[Back]](../README.md) [[Enable]](./enable_route_advertisement.md)

Route advertisements allows to 
- advertise default and user-defined network routes, including EgressIPs
- import routes from the provider network that configure the default pod network and user-defined networks

> [!NOTE]
> Route advertisement requires frr bgp provider [enabled](./enable.md)

## CLI

```
# oc edit Network.operator.openshift.io/cluster
---remove---
  "spec": {
    "defaultNetwork": {
        "ovnKubernetesConfig": {
            "routeAdvertisements": "Enabled"
        }
    }
  }
```

## iserver

```
# iserver delete ocp ovn-bgp --cluster bm1 --mode ra
```

Check details [here](../ra_disable.md)

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
# iserver delete ocp task --cluster bm1 --file /tmp/task.json
```

Check details [here](../task_ra_disable.md)

[[Back]](../README.md) [[Enable]](./enable_route_advertisement.md)