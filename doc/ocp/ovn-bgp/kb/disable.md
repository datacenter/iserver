# OVNKubernetes BGP - Disable

[[Back]](../README.md) [[Enable]](./enable.md)

## CLI

```
# oc edit Network.operator.openshift.io/cluster
---remove---
  "spec": {
    "additionalRoutingCapabilities": {
      "providers": ["FRR"]
    }
  }
```

## iserver

```
# iserver delete ocp ovn-bgp --cluster bm1 --mode feature
```

Check details [here](../feature_disable.md)

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
# iserver delete ocp task --cluster bm1 --file /tmp/task.json
```

Check details [here](../task_feature_disable.md)


[[Back]](../README.md) [[Enable]](./enable.md)