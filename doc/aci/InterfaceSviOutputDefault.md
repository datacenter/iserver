# Node Interface - SVI

## Default output type

```
# iserver get aci intf svi --apic apic21 --node any --type ext

Apic: apic21 (mode:online, cache:off)
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: cl2209-eu-spdc
- node: cl2210-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

Interface SVI - State [#22]
---------------------------

+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| Node                 | Health | Faults  | Interface | Admin | Oper | Type | Medium | Mcast | MTU  | VLAN | Access Encap | Fabric Encap   | MAC               | IPv4                  |
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | vlan1     | up    | up   | Ext  | bcast  | no    | 9000 | 1    | vlan-2501    | vxlan-15269817 | 00:22:BD:F8:25:01 | 192.168.23.205/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/bl2205-eu-spdc | 100    | 0 0 0 0 | vlan20    | up    | up   | Ext  | bcast  | no    | 9000 | 20   | vlan-2502    | vxlan-15105996 | 00:22:BD:F8:25:02 | 192.168.24.205/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | vlan1     | up    | up   | Ext  | bcast  | no    | 9000 | 1    | vlan-2501    | vxlan-15269817 | 00:22:BD:F8:25:01 | 192.168.23.206/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/bl2206-eu-spdc | 100    | 0 0 0 0 | vlan2     | up    | up   | Ext  | bcast  | no    | 9000 | 2    | vlan-2502    | vxlan-15105996 | 00:22:BD:F8:25:02 | 192.168.24.206/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | vlan1     | up    | up   | Ext  | bcast  | no    | 9000 | 1    | vlan-601     | vxlan-15040469 | 00:22:BD:F8:19:FF | 15.16.131.253/24      | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | vlan2     | up    | up   | Ext  | bcast  | no    | 9000 | 2    | vlan-2503    | vxlan-15662985 | 00:22:BD:F8:25:03 | 192.168.20.201/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2201-eu-spdc | 100    | 0 0 0 0 | vlan20    | up    | up   | Ext  | bcast  | no    | 9000 | 20   | vlan-804     | vxlan-15269820 | 00:22:BD:B8:99:AA | 10.58.24.125/28 (pri) | 
|                      |        |         |           |       |      |      |        |       |      |      |              |                |                   | 10.58.24.126/28       | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | vlan1     | up    | up   | Ext  | bcast  | no    | 9000 | 1    | vlan-601     | vxlan-15040469 | 00:22:BD:F8:19:FF | 15.16.131.252/24      | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | vlan2     | up    | up   | Ext  | bcast  | no    | 9000 | 2    | vlan-2503    | vxlan-15662985 | 00:22:BD:F8:25:03 | 192.168.20.202/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2202-eu-spdc | 100    | 0 0 0 0 | vlan20    | up    | up   | Ext  | bcast  | no    | 9000 | 20   | vlan-804     | vxlan-15269820 | 00:22:BD:B8:99:AA | 10.58.24.124/28 (pri) | 
|                      |        |         |           |       |      |      |        |       |      |      |              |                |                   | 10.58.24.126/28       | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | vlan26    | up    | up   | Ext  | bcast  | no    | 1500 | 26   | vlan-810     | vxlan-15040476 | 00:22:BD:F8:19:FF | 169.254.0.1/24 (pri)  | 
|                      |        |         |           |       |      |      |        |       |      |      |              |                |                   | 169.254.0.254/24      | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | vlan27    | up    | up   | Ext  | bcast  | no    | 1500 | 27   | vlan-812     | vxlan-15237056 | 00:22:BD:F8:19:FF | 169.254.2.254/24      | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | vlan28    | up    | up   | Ext  | bcast  | no    | 1500 | 28   | vlan-811     | vxlan-14942183 | 00:22:BD:F8:19:FF | 169.254.1.1/24 (pri)  | 
|                      |        |         |           |       |      |      |        |       |      |      |              |                |                   | 169.254.1.254/24      | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | vlan29    | up    | up   | Ext  | bcast  | no    | 1500 | 29   | vlan-813     | vxlan-15269821 | 00:22:BD:F8:19:FF | 169.254.3.254/24      | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | vlan30    | up    | up   | Ext  | bcast  | no    | 9000 | 30   | vlan-2501    | vxlan-15269817 | 00:22:BD:F8:25:01 | 192.168.23.207/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2207-eu-spdc | 100    | 0 0 0 0 | vlan31    | up    | up   | Ext  | bcast  | no    | 9000 | 31   | vlan-2502    | vxlan-15105996 | 00:22:BD:F8:25:02 | 192.168.24.207/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan25    | up    | up   | Ext  | bcast  | no    | 9000 | 25   | vlan-2502    | vxlan-15105996 | 00:22:BD:F8:25:02 | 192.168.24.208/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan26    | up    | up   | Ext  | bcast  | no    | 9000 | 26   | vlan-2501    | vxlan-15269817 | 00:22:BD:F8:25:01 | 192.168.23.208/24     | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan27    | up    | up   | Ext  | bcast  | no    | 1500 | 27   | vlan-813     | vxlan-15269821 | 00:22:BD:F8:19:FF | 169.254.3.1/24 (pri)  | 
|                      |        |         |           |       |      |      |        |       |      |      |              |                |                   | 169.254.3.254/24      | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan28    | up    | up   | Ext  | bcast  | no    | 1500 | 28   | vlan-811     | vxlan-14942183 | 00:22:BD:F8:19:FF | 169.254.1.254/24      | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan29    | up    | up   | Ext  | bcast  | no    | 1500 | 29   | vlan-810     | vxlan-15040476 | 00:22:BD:F8:19:FF | 169.254.0.254/24      | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
| pod-1/cl2208-eu-spdc | 100    | 0 0 0 0 | vlan30    | up    | up   | Ext  | bcast  | no    | 1500 | 30   | vlan-812     | vxlan-15237056 | 00:22:BD:F8:19:FF | 169.254.2.1/24 (pri)  | 
|                      |        |         |           |       |      |      |        |       |      |      |              |                |                   | 169.254.2.254/24      | 
+----------------------+--------+---------+-----------+-------+------+------+--------+-------+------+------+--------------+----------------+-------------------+-----------------------+
```

Developer

```
# iserver get aci intf svi --apic apic21 --node any --type ext

{
    "duration": 8718,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 373,
        "disconnect_time": 0,
        "mo_time": 7572,
        "total_time": 7945
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
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	373	-	connect apic21o.emea-sp.cisco.com:443
True	270	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	325	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	260	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ipv4Addr
True	315	10	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	276	24	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ipv4Addr
True	365	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	277	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ipv4Addr
True	371	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	277	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ipv4Addr
True	435	20	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	273	30	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ipv4Addr
True	402	19	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	274	29	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ipv4Addr
True	280	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	318	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/ipv4Addr
True	273	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	262	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/ipv4Addr
True	304	5	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	317	13	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ipv4Addr
True	294	6	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	284	14	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ipv4Addr
True	272	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	295	21	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/ipv4Addr
True	271	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=health,fault-count,required
True	282	21	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/ipv4Addr
```

[[Back]](./InterfaceSvi.md)