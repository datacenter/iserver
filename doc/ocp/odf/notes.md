```
$ oc -n openshift-storage rsh $(oc get pods -n openshift-storage -l app=rook-ceph-tools -o name)
sh-5.1$ 

$ oc exec -it -n openshift-storage rook-ceph-tools-7d48d47ccb-wmkxp -- ceph -s
cluster:
    id:     c664ae86-d7f7-4b04-80d3-3675840d06c4
    health: HEALTH_OK

services:
    mon: 3 daemons, quorum a,b,c (age 10m)
    mgr: b(active, since 7m), standbys: a
    mds: 1/1 daemons up, 1 hot standby
    osd: 6 osds: 6 up (since 9m), 6 in (since 9m)
    rgw: 1 daemon active (1 hosts, 1 zones)

data:
    volumes: 1/1 healthy
    pools:   12 pools, 201 pgs
    objects: 376 objects, 166 MiB
    usage:   386 MiB used, 5.2 TiB / 5.2 TiB avail
    pgs:     201 active+clean

io:
    client:   1.4 KiB/s rd, 8.7 KiB/s wr, 2 op/s rd, 1 op/s wr
```