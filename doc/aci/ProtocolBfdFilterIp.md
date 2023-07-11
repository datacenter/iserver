# Node Protocol - BFD

## Filter sessions by IP address

```
# iserver get aci proto bfd --apic apic11 --node any --address 15.254.104.192

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
- node: s101-eu-spdc
- node: s102-eu-spdc

BFD Sessions [#1]
-----------------

+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| Node                | Health | Faults  | VRF                           | Interface | Type      | Local Address  | Local MAC         | State | Session Id | Remote Address | Remote MAC        | State | Session Id |
+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | common:smi5Gc-cvim1-N3-N4_VRF | vlan488   | singlehop | 15.254.104.253 | 00:22:BD:F8:19:FF | up    | 1090519041 | 15.254.104.192 | FA:16:3E:CB:11:71 | up    | 4          | 
+---------------------+--------+---------+-------------------------------+-----------+-----------+----------------+-------------------+-------+------------+----------------+-------------------+-------+------------+
```

Developer

```
# iserver get aci proto bfd --apic apic11 --node any --address 15.254.104.192

{
    "duration": 9219,
    "apic": {
        "read": true,
        "success": 24,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 23,
        "connect_time": 453,
        "disconnect_time": 0,
        "mo_time": 7709,
        "total_time": 8162
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

True	453	-	connect apic11o.emea-sp.cisco.com:443
True	352	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	321	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	355	11	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	329	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	369	15	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	466	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	360	42	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	288	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	313	36	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	346	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	302	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	299	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	303	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	316	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	313	0	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/bfd/inst query query-target=children&target-subtree-class=bfdIf
True	310	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	363	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	359	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	351	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	326	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	317	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-101/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
True	336	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query rsp-subtree-include=health,fault-count
True	315	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-102/sys/bfd/inst query query-target=subtree&target-subtree-class=bfdSess,bfdSessStats,bfdPeerV,bfdIf&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolBfd.md)