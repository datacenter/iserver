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

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
Resolve xd server...

+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| Name                          | Model              | Serial      | IP          | CPU        | Memory    |
+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| comp2-p4a-eu-spdc-WZP22520B04 | (R) UCSC-C220-M5SX | WZP22520B04 | 10.58.29.58 | 2S 48C 96T | 384 [GiB] | 
+-------------------------------+--------------------+-------------+-------------+------------+-----------+

LLDP Adjacency [#6]
-------------------

+---------------------+--------+---------+--------------+-----------+-----------------+-------------------+------+------+------------------+--------------+
| Node                | Health | Faults  | Interface ID | Hold Time | Neighbor Device | MAC               | Port | VLAN | Port Description | Capabilities |
+---------------------+--------+---------+--------------+-----------+-----------------+-------------------+------+------+------------------+--------------+
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/61      | 121       |                 | 3c:fd:fe:cb:f5:18 |      |      |                  |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/62      | 121       |                 | 3c:fd:fe:cb:f5:19 |      |      |                  |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/63      | 121       |                 | 3c:fd:fe:cb:f5:1a |      |      |                  |              | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | eth1/61      | 121       |                 | 40:a6:b7:08:fb:b0 |      |      |                  |              | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | eth1/62      | 121       |                 | 40:a6:b7:08:fb:b1 |      |      |                  |              | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | eth1/63      | 121       |                 | 40:a6:b7:08:fb:b2 |      |      |                  |              | 
+---------------------+--------+---------+--------------+-----------+-----------------+-------------------+------+------+------------------+--------------+

LLDP Adjacency - Endpoints [#10]
--------------------------------

+-------------+-------------------+-----+-----------+--------------------------------------------------+---------------------+-------------------+
| Server      | MAC               | PCI | Interface | Model                                            | LLDP Node           | LLDP Interface ID |
+-------------+-------------------+-----+-----------+--------------------------------------------------+---------------------+-------------------+
| 10.58.29.58 | 3c:fd:fe:cb:f5:18 | 1   | eth-1     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | pod-1/cl201-eu-spdc | eth1/61           | 
| 10.58.29.58 | 3c:fd:fe:cb:f5:19 | 1   | eth-2     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | pod-1/cl201-eu-spdc | eth1/62           | 
| 10.58.29.58 | 3c:fd:fe:cb:f5:1a | 1   | eth-3     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | pod-1/cl201-eu-spdc | eth1/63           | 
| 10.58.29.58 | 3c:fd:fe:cb:f5:1b | 1   | eth-4     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC |                     |                   | 
| 10.58.29.58 | 40:a6:b7:08:fb:b0 | 2   | eth-1     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | pod-1/cl202-eu-spdc | eth1/61           | 
| 10.58.29.58 | 40:a6:b7:08:fb:b1 | 2   | eth-2     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | pod-1/cl202-eu-spdc | eth1/62           | 
| 10.58.29.58 | 40:a6:b7:08:fb:b2 | 2   | eth-3     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | pod-1/cl202-eu-spdc | eth1/63           | 
| 10.58.29.58 | 40:a6:b7:08:fb:b3 | 2   | eth-4     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC |                     |                   | 
| 10.58.29.58 | 70:ea:1a:fc:34:72 | L   | eth-1     | Cisco(R) LOM X550-T2                             |                     |                   | 
| 10.58.29.58 | 70:ea:1a:fc:34:73 | L   | eth-2     | Cisco(R) LOM X550-T2                             |                     |                   | 
+-------------+-------------------+-----+-----------+--------------------------------------------------+---------------------+-------------------+
Interface context: lldp
```

- Use context to get interface details

```
# iserver get aci intf phy --apic apic11 --role leaf --ctx lldp

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: cl201-eu-spdc
- node: cl202-eu-spdc

Interface Phy - State [#6]
--------------------------

+---------------------+--------+---------+-----------+-------+-----------+------+-----------+------+----------+------+-------------------+-------+-------+--------+------+-------------+
| Node                | Health | Faults  | Interface | Admin | Switching | Oper | Reason    | Type | Layer    | PC   | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+--------+---------+-----------+-------+-----------+------+-----------+------+----------+------+-------------------+-------+-------+--------+------+-------------+
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | 1/61      | up    | enabled   | up   | connected | leaf | switched | po16 | 4C:71:0D:23:FA:75 | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | 1/62      | up    | enabled   | up   | connected | leaf | switched | po27 | 4C:71:0D:23:FA:76 | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | 1/63      | up    | enabled   | up   | connected | leaf | switched |      | 4C:71:0D:23:FA:77 | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | 1/61      | up    | enabled   | up   | connected | leaf | switched | po19 | 10:B3:D5:B5:62:59 | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | 1/62      | up    | enabled   | up   | connected | leaf | switched | po22 | 10:B3:D5:B5:62:5A | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | 1/63      | up    | enabled   | up   | connected | leaf | switched |      | 10:B3:D5:B5:62:5B | trunk | 10G   | full   | 9000 | disable-fec | 
+---------------------+--------+---------+-----------+-------+-----------+------+-----------+------+----------+------+-------------------+-------+-------+--------+------+-------------+
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
    "duration": 12090,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 8109
    },
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 439,
        "disconnect_time": 0,
        "mo_time": 2848,
        "total_time": 3287
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
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-08-02 15:00:05.444250	True	3720	100	isctl get compute rackunit   -o json --top 100
2023-08-02 15:00:07.751817	True	2304	14	isctl get compute rackunit   -o json --top 100 --skip 100
2023-08-02 15:00:09.978996	True	2085	5	isctl get compute blade   -o json --top 100


Log: apic
----------

True	439	-	connect apic11o.emea-sp.cisco.com:443
True	293	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	418	13	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	336	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	332	44	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	316	44	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	288	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	279	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	281	21	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	305	21	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
```

[[Back Protocol]](./ProtocolLldp.md) [[Back Cross Domain]](./XdServer.md)