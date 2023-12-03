# Hypervisor

## All view

```
# iserver get osp hv --cluster pod1 -v all

Cluster: pod1

Hypervisor [#5]
---------------

+----+------------------+----------------+---------+-------+-----+-------+----------------------------+--------------------+
| Id | Hypervisor       | IP             | Status  | State | VMs | CPU   | Memory                     | Disk               |
+----+------------------+----------------+---------+-------+-----+-------+----------------------------+--------------------+
| 13 | AIO-server-1     | 192.168.100.13 | enabled | up    | 5   | 22/80 | 111,616/257,397 [MB] (43%) | 100/825 [GB] (12%) | 
| 7  | AIO-server-2     | 192.168.100.12 | enabled | up    | 2   | 14/48 | 89,088/257,405 [MB] (34%)  | 62/825 [GB] (7%)   | 
| 10 | AIO-server-3     | 192.168.100.14 | enabled | up    | 2   | 30/80 | 115,712/257,398 [MB] (44%) | 44/825 [GB] (5%)   | 
| 1  | compute-server-1 | 192.168.100.11 | enabled | up    | 3   | 22/92 | 66,560/257,396 [MB] (25%)  | 102/852 [GB] (11%) | 
| 4  | compute-server-2 | 192.168.100.10 | enabled | up    | 5   | 35/92 | 101,376/385,412 [MB] (26%) | 142/852 [GB] (16%) | 
+----+------------------+----------------+---------+-------+-----+-------+----------------------------+--------------------+

Hypervisor - Virtual Machine [#5]
---------------------------------

+----+------------------+---------+---------------+---------+-----+-------------+-----------+
| Id | Hypervisor       | Tenant  | Name          | Status  | CPU | Memory [MB] | Disk [GB] |
+----+------------------+---------+---------------+---------+-----+-------------+-----------+
| 13 | AIO-server-1     | ialonso | ORANGE-C8KV-1 | ACTIVE  | 4   | 4096        | 0         | 
|    |                  | ialonso | ORANGE-C8KV-2 | ACTIVE  | 4   | 4096        | 0         | 
|    |                  | ialonso | SDWAN-C8KV01B | ACTIVE  | 4   | 4096        | 0         | 
|    |                  | smi5gc  | portal        | ACTIVE  | 8   | 32768       | 80        | 
|    |                  | smi5gc  | VPC-SI-mme    | ACTIVE  | 2   | 16384       | 4         | 
+----+------------------+---------+---------------+---------+-----+-------------+-----------+
| 7  | AIO-server-2     | smi5gc  | esc           | ACTIVE  | 2   | 6144        | 40        | 
|    |                  | smi5gc  | VPC-SI-saegw2 | ACTIVE  | 12  | 32768       | 6         | 
+----+------------------+---------+---------------+---------+-----+-------------+-----------+
| 10 | AIO-server-3     | smi5gc  | VPC-SI-saegw1 | ACTIVE  | 12  | 32768       | 6         | 
|    |                  | smi5gc  | VPC-SI-upf8   | ACTIVE  | 18  | 32768       | 6         | 
+----+------------------+---------+---------------+---------+-----+-------------+-----------+
| 1  | compute-server-1 | admin   | test-sriov    | ACTIVE  | 2   | 4096        | 40        | 
|    |                  | smi5gc  | server        | ACTIVE  | 2   | 4096        | 40        | 
|    |                  | smi5gc  | VPC-SI-upf1   | ACTIVE  | 18  | 32768       | 6         | 
+----+------------------+---------+---------------+---------+-----+-------------+-----------+
| 4  | compute-server-2 | admin   | c8koncinder   | SHUTOFF | 4   | 4096        | 0         | 
|    |                  | admin   | my-c8kv       | SHUTOFF | 4   | 4096        | 0         | 
|    |                  | admin   | my-cirros-img | ACTIVE  | 1   | 2048        | 20        | 
|    |                  | smi5gc  | lattice       | ACTIVE  | 8   | 32768       | 100       | 
|    |                  | smi5gc  | VPC-SI-upf2   | ACTIVE  | 18  | 32768       | 6         | 
+----+------------------+---------+---------------+---------+-----+-------------+-----------+

Filter: name, address, vm
View:   state (def), vm, all
```

Developer

```
# iserver get osp hv --cluster pod1 -v all

{
    "duration": 8958,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 7958,
        "total_time": 7958
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": true,
        "lines": 3
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-19 09:54:28.534410	True	3014	get	hypervisors
2023-11-19 09:54:31.656339	True	3105	get	virtual_machines
2023-11-19 09:54:33.339495	True	1640	get	tenants
2023-11-19 09:54:33.554232	True	199	get	flavors
```

[[Back]](./HypervisorGet.md)