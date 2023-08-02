# Node Protocol - BGP

## Filter BGP neighbors by session type (ebgp|ibgp)

Example: iBGP

```
# iserver get aci proto bgp --apic apic11 --node rl301 --type ibgp --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

Protocol BGP - Neighbor [#7]
----------------------------

+---------------------+--------------------------+---------------+-----------------+---------+-------------+-------+------+-----+----------+---------------+---------------+-----------------+
| Node                | VRF                      | Nbr Address   | Router Id       | Admin   | BGP         | ASN   | Type | TTL | Src Intf | Local IP      | Conns (A/D/E) | Paths           |
+---------------------+--------------------------+---------------+-----------------+---------+-------------+-------+------+-----+----------+---------------+---------------+-----------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1    | 172.24.3.1      | enabled | established | 64371 | ebgp | 4   | lo17     | 172.24.3.15   | 3/0/1         | IPv4-ucast:3    | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2    | 172.24.3.2      | enabled | established | 64371 | ebgp | 4   | lo17     | 172.24.3.15   | 3/0/1         | IPv4-ucast:3    | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3    | 172.24.3.3      | enabled | established | 64371 | ebgp | 4   | lo17     | 172.24.3.15   | 3/0/1         | IPv4-ucast:3    | 
| pod-1/rl301-eu-spdc | overlay-1                | 15.16.3.1     | 35.35.35.35     | enabled | established | 64001 | ebgp | 1   | eth1/29  | 15.16.3.2     | 1/0/1         |                 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.1   | 102.102.102.102 | enabled | established | 50000 | ibgp | 1   | lo0      | 172.16.30.160 | 1/0/1         | VPNv4-ucast:393 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.228 | 101.101.101.101 | enabled | established | 50000 | ibgp | 1   | lo0      | 172.16.30.160 | 1/0/1         | VPNv4-ucast:393 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.31.3.35   | 35.35.35.35     | enabled | established | 64001 | ebgp | 2   | lo3      | 172.31.3.31   | 3/0/1         |                 | 
+---------------------+--------------------------+---------------+-----------------+---------+-------------+-------+------+-----+----------+---------------+---------------+-----------------+
```

Example: eBGP

```
# iserver get aci proto bgp --apic apic11 --node rl301 --type ebgp --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: rl301-eu-spdc

Protocol BGP - Neighbor [#7]
----------------------------

+---------------------+--------------------------+---------------+-----------------+---------+-------------+-------+------+-----+----------+---------------+---------------+-----------------+
| Node                | VRF                      | Nbr Address   | Router Id       | Admin   | BGP         | ASN   | Type | TTL | Src Intf | Local IP      | Conns (A/D/E) | Paths           |
+---------------------+--------------------------+---------------+-----------------+---------+-------------+-------+------+-----+----------+---------------+---------------+-----------------+
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.1    | 172.24.3.1      | enabled | established | 64371 | ebgp | 4   | lo17     | 172.24.3.15   | 3/0/1         | IPv4-ucast:3    | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.2    | 172.24.3.2      | enabled | established | 64371 | ebgp | 4   | lo17     | 172.24.3.15   | 3/0/1         | IPv4-ucast:3    | 
| pod-1/rl301-eu-spdc | MPC-E:MPC-E-sPBR-OUT_VRF | 172.24.3.3    | 172.24.3.3      | enabled | established | 64371 | ebgp | 4   | lo17     | 172.24.3.15   | 3/0/1         | IPv4-ucast:3    | 
| pod-1/rl301-eu-spdc | overlay-1                | 15.16.3.1     | 35.35.35.35     | enabled | established | 64001 | ebgp | 1   | eth1/29  | 15.16.3.2     | 1/0/1         |                 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.1   | 102.102.102.102 | enabled | established | 50000 | ibgp | 1   | lo0      | 172.16.30.160 | 1/0/1         | VPNv4-ucast:393 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.16.11.228 | 101.101.101.101 | enabled | established | 50000 | ibgp | 1   | lo0      | 172.16.30.160 | 1/0/1         | VPNv4-ucast:393 | 
| pod-1/rl301-eu-spdc | overlay-1                | 172.31.3.35   | 35.35.35.35     | enabled | established | 64001 | ebgp | 2   | lo3      | 172.31.3.31   | 3/0/1         |                 | 
+---------------------+--------------------------+---------------+-----------------+---------+-------------+-------+------+-----+----------+---------------+---------------+-----------------+
```

Developer

```
# iserver get aci proto bgp --apic apic11 --node rl301 --type ibgp --view nei

{
    "duration": 3796,
    "apic": {
        "read": true,
        "success": 12,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 11,
        "connect_time": 399,
        "disconnect_time": 0,
        "mo_time": 3146,
        "total_time": 3545
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

True	399	-	connect apic11o.emea-sp.cisco.com:443
True	298	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	288	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp query query-target=children&rsp-subtree-include=health,fault-count
True	327	18	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	283	27	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-301/bgpDom query query-target=subtree&target-subtree-class=bgpPeer&target-subtree-class=bgpPeerEntry&target-subtree-class=bgpPeerAfEntry
True	276	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[15.16.3.1/32]/ent-[15.16.3.1]/peerstats
True	277	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[172.31.3.35/32]/ent-[172.31.3.35]/peerstats
True	292	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[172.16.11.228/32]/ent-[172.16.11.228]/peerstats
True	275	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-overlay-1/peer-[172.16.11.1/32]/ent-[172.16.11.1]/peerstats
True	269	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.1/32]/ent-[172.24.3.1]/peerstats
True	284	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.2/32]/ent-[172.24.3.2]/peerstats
True	277	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/bgp/inst/dom-MPC-E:MPC-E-sPBR-OUT_VRF/peer-[172.24.3.3/32]/ent-[172.24.3.3]/peerstats
```

[[Back]](./ProtocolBgp.md)