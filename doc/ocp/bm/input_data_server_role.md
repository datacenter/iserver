# Server Role

[[Back]](../BareMetalCluster.md)

In case of single node OpenShift cluster or 3 node clusters, every node in the cluster has dual-role: master and worker, that is auto-assigned.

In case of 3+ clusters, you may want to explictly define the master and worker role. You can do that as per example below in server section.

Note: server section can be either part of cluster.json file in case of [all-in-one definition](./input_data_cluster_aio.md) or be in dedicated [server.json](./input_data_server.md) file as per example below.

```json
[
  {
    "hostname": "cp1",
    "role": "master",
    ...
  },
  {
    "hostname": "cp2",
    "role": "master",
    ...
  },
  {
    "hostname": "cp3",
    "role": "master",
    ...
  },
  {
    "hostname": "wk1",
    "role": "worker",
    ...
  },
  {
    "hostname": "wk2",
    "role": "worker",
    ...
  },
  {
    "hostname": "wk3",
    "role": "worker",
    ...
  }
]
```

[[Back]](../BareMetalCluster.md)