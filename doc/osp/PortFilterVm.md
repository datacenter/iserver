# Port

## Filter by virtual machine

```
# iserver get osp port --cluster pod1 --vm smi5gc/VPC-SI-upf1 -v hv

Cluster: pod1

Port - Hypervisor [#4]
----------------------

+-------------------+-------+--------+---------+----------------+--------------------+--------+-------------------------------------+------------------+--------+------------------------------+
| MAC               | Admin | Status | Type    | IP             | VM                 | VNIC   | Profile                             | Host             | Type   | Details                      |
+-------------------+-------+--------+---------+----------------+--------------------+--------+-------------------------------------+------------------+--------+------------------------------+
| fa:16:3e:22:9c:e2 | V     | ACTIVE | Compute | 15.100.1.191   | smi5gc/VPC-SI-upf1 | normal | --                                  | compute-server-1 | ovs    | {                            | 
|                   |       |        |         |                |                    |        |                                     |                  |        |   "connectivity": "l2",      | 
|                   |       |        |         |                |                    |        |                                     |                  |        |   "port_filter": true,       | 
|                   |       |        |         |                |                    |        |                                     |                  |        |   "ovs_hybrid_plug": false,  | 
|                   |       |        |         |                |                    |        |                                     |                  |        |   "datapath_type": "system", | 
|                   |       |        |         |                |                    |        |                                     |                  |        |   "bridge_name": "br-int"    | 
|                   |       |        |         |                |                    |        |                                     |                  |        | }                            | 
+-------------------+-------+--------+---------+----------------+--------------------+--------+-------------------------------------+------------------+--------+------------------------------+
| fa:16:3e:e8:f1:d5 | V     | ACTIVE | Compute | 15.100.105.191 | smi5gc/VPC-SI-upf1 | direct | {                                   | compute-server-1 | hw_veb | {                            | 
|                   |       |        |         |                |                    |        |   "pci_vendor_info": "8086:154c",   |                  |        |   "port_filter": false,      | 
|                   |       |        |         |                |                    |        |   "pci_slot": "0000:5e:0b.7",       |                  |        |   "connectivity": "l2",      | 
|                   |       |        |         |                |                    |        |   "physical_network": "phys_sriov0" |                  |        |   "vlan": "0"                | 
|                   |       |        |         |                |                    |        | }                                   |                  |        | }                            | 
+-------------------+-------+--------+---------+----------------+--------------------+--------+-------------------------------------+------------------+--------+------------------------------+
| fa:16:3e:e7:65:c7 | V     | ACTIVE | Compute | 15.100.105.91  | smi5gc/VPC-SI-upf1 | direct | {                                   | compute-server-1 | hw_veb | {                            | 
|                   |       |        |         |                |                    |        |   "pci_vendor_info": "8086:154c",   |                  |        |   "port_filter": false,      | 
|                   |       |        |         |                |                    |        |   "pci_slot": "0000:5e:0b.2",       |                  |        |   "connectivity": "l2",      | 
|                   |       |        |         |                |                    |        |   "physical_network": "phys_sriov0" |                  |        |   "vlan": "0"                | 
|                   |       |        |         |                |                    |        | }                                   |                  |        | }                            | 
+-------------------+-------+--------+---------+----------------+--------------------+--------+-------------------------------------+------------------+--------+------------------------------+
| fa:16:3e:cf:4b:b5 | V     | ACTIVE | Compute | 15.100.2.191   | smi5gc/VPC-SI-upf1 | normal | --                                  | compute-server-1 | ovs    | {                            | 
|                   |       |        |         |                |                    |        |                                     |                  |        |   "connectivity": "l2",      | 
|                   |       |        |         |                |                    |        |                                     |                  |        |   "port_filter": true,       | 
|                   |       |        |         |                |                    |        |                                     |                  |        |   "ovs_hybrid_plug": false,  | 
|                   |       |        |         |                |                    |        |                                     |                  |        |   "datapath_type": "system", | 
|                   |       |        |         |                |                    |        |                                     |                  |        |   "bridge_name": "br-int"    | 
|                   |       |        |         |                |                    |        |                                     |                  |        | }                            | 
+-------------------+-------+--------+---------+----------------+--------------------+--------+-------------------------------------+------------------+--------+------------------------------+

Filter: name, state, type, tenant, net, subnet, address, mac, hv, vm, sg
View:   state (def), id, sec, hv, all
```

Developer

```
# iserver get osp port --cluster pod1 --vm smi5gc/VPC-SI-upf1 -v hv

{
    "duration": 7459,
    "osp": {
        "read": true,
        "success": 3,
        "failed": 0,
        "mo": 3,
        "mo_time": 7119,
        "total_time": 7119
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
        "lines": 4
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-19 14:44:27.270864	True	2957	get	ports
2023-11-19 14:44:31.046807	True	3571	get	virtual_machines
2023-11-19 14:44:31.661778	True	591	get	tenants
```

[[Back]](./PortGet.md)