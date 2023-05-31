# Node Protocol - LLDP

## Filter by server's ip address

- Server must be found by IP address in intersight account
- MAC address of every network adapter is added to endpoint search criteria

```
# iserver get aci proto lldp
    --apic apic11
    --role leaf
    --xd server:10.58.29.58
    --view nei

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
Resolve xd server...

+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| Name                          | Model              | Serial      | IP          | CPU        | Memory    |
+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| comp2-p4a-eu-spdc-WZP22520B04 | (R) UCSC-C220-M5SX | WZP22520B04 | 10.58.29.58 | 2S 48C 96T | 256 [GiB] | 
+-------------------------------+--------------------+-------------+-------------+------------+-----------+

+-------------------+-----------+--------------------------------------------------+----------+
| MAC Address       | Interface | Adapter                                          | Pci Slot |
+-------------------+-----------+--------------------------------------------------+----------+
| 3c:fd:fe:cb:f5:18 | eth-1     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | 
| 3c:fd:fe:cb:f5:19 | eth-2     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | 
| 3c:fd:fe:cb:f5:1a | eth-3     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | 
| 3c:fd:fe:cb:f5:1b | eth-4     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | 
| 40:a6:b7:08:fb:b0 | eth-1     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | 
| 40:a6:b7:08:fb:b1 | eth-2     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | 
| 40:a6:b7:08:fb:b2 | eth-3     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | 
| 40:a6:b7:08:fb:b3 | eth-4     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | 
| 70:ea:1a:fc:34:72 | eth-1     | Cisco(R) LOM X550-T2                             | L        | 
| 70:ea:1a:fc:34:73 | eth-2     | Cisco(R) LOM X550-T2                             | L        | 
+-------------------+-----------+--------------------------------------------------+----------+

+---------------------+--------------+-----------+-------------------+
| Node                | Interface ID | Hold Time | MAC               |
+---------------------+--------------+-----------+-------------------+
| pod-1/cl201-eu-spdc | eth1/61      | 121       | 3c:fd:fe:cb:f5:18 | 
| pod-1/cl201-eu-spdc | eth1/62      | 121       | 3c:fd:fe:cb:f5:19 | 
| pod-1/cl201-eu-spdc | eth1/63      | 121       | 3c:fd:fe:cb:f5:1a | 
| pod-1/cl202-eu-spdc | eth1/61      | 121       | 40:a6:b7:08:fb:b0 | 
| pod-1/cl202-eu-spdc | eth1/62      | 121       | 40:a6:b7:08:fb:b1 | 
| pod-1/cl202-eu-spdc | eth1/63      | 121       | 40:a6:b7:08:fb:b2 | 
+---------------------+--------------+-----------+-------------------+
Interface context: lldp
```

- Use context to get interface details

```
# iserver get aci intf phy --apic apic11 --role leaf --ctx lldp

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: cl201-eu-spdc
- node: cl202-eu-spdc

+---------------------+-----------+-------+-----------+------+-----------+------+----------+------+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason    | Type | Layer    | PC   | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-----------+------+----------+------+-------------------+-------+-------+--------+------+-------------+
| pod-1/cl201-eu-spdc | 1/61      | up    | enabled   | up   | connected | leaf | switched | po14 | 4C:71:0D:23:FA:75 | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 1/62      | up    | enabled   | up   | connected | leaf | switched | po11 | 4C:71:0D:23:FA:76 | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 1/63      | up    | enabled   | up   | connected | leaf | switched |      | 4C:71:0D:23:FA:77 | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/61      | up    | enabled   | up   | connected | leaf | switched | po5  | 10:B3:D5:B5:62:59 | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/62      | up    | enabled   | up   | connected | leaf | switched | po6  | 10:B3:D5:B5:62:5A | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/63      | up    | enabled   | up   | connected | leaf | switched |      | 10:B3:D5:B5:62:5B | trunk | 10G   | full   | 9000 | disable-fec | 
+---------------------+-----------+-------+-----------+------+-----------+------+----------+------+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

Developer

```
# iserver get aci proto lldp
    --apic apic11
    --role leaf
    --xd server:10.58.29.58
    --view nei

{
    "duration": 14488,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 7017
    },
    "apic": {
        "read": true,
        "success": 20,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 19,
        "connect_time": 410,
        "disconnect_time": 0,
        "mo_time": 6268,
        "total_time": 6678
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
        "lines": 71
    }
}

Log: isctl
-----------

2023-05-30 22:08:21.131744	True	3144	100	isctl get compute rackunit   -o json --top 100
2023-05-30 22:08:23.573956	True	2440	4	isctl get compute rackunit   -o json --top 100 --skip 100
2023-05-30 22:08:25.137910	True	1433	2	isctl get compute blade   -o json --top 100


Log: apic
----------

True	410	-	connect apic11o.emea-sp.cisco.com
True	324	11	apic11o.emea-sp.cisco.com class fabricNode
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lldp/inst
True	282	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/lldpInstStats
True	298	13	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	317	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lldp/inst
True	328	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/lldpInstStats
True	315	10	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lldp/inst
True	346	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/lldpInstStats
True	338	42	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	320	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lldp/inst
True	324	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/lldpInstStats
True	423	42	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	353	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lldp/inst
True	338	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/lldpInstStats
True	360	21	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
True	340	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lldp/inst
True	317	1	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/lldpInstStats
True	321	21	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp
```

[[Back Protocol]](./ProtocolLldp.md) [[Back Cross Domain]](./XdServer.md)