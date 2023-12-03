# OpenStack Cluster

## Show Clusters

```
# iserver get osp cluster

+--------------+---------+----------+---------------------------------------------------+
| Cluster Name | Default | Type     | Openrc                                            |
+--------------+---------+----------+---------------------------------------------------+
| pod1         | ✓       | standard | C:\Users\akaliwod\.itool\osp-clusters\pod1\openrc |
+--------------+---------+----------+---------------------------------------------------+
```

## Add Cluster

OpenStack cluster can be added to iserver using openrc file.

In case OS_CACERT is defined, make sure to certificate file is defined too.

```
# iserver set osp openrc \
    --cluster test \
    --file C:\Users\akaliwod\Downloads\osp-pod4.openrc \
    --cert C:\Users\akaliwod\Downloads\osp-pod4.crt

Openstack cluster set: test
```

## Delete Cluster

```
# iserver delete osp cluster --cluster test
Openstack cluster deleted
```

[[Back]](./README.md)