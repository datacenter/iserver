# Application Endpoint Group (EPG)

## Get EPGs' static port properties

```
# iserver get aci epg --apic apic21 --name sriov* --view stport

Apic: apic21 (mode:online, cache:off)

EPG - Static Port [#2]
----------------------

+---------------------+-----------+------+----------+---------------+-------+----------------------+----------+
| EPG                 | Path      | Type | Ep       | Encapsulation | Mode  | Deployment Immediacy | State    |
+---------------------+-----------+------+----------+---------------+-------+----------------------+----------+
| k8s/k8s_ANP/SRIoV_A | node-2207 | Intf | eth1/3/1 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/3/2 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/3/3 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/3/4 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/4/1 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/4/2 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/4/3 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/3/1 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/3/2 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/3/3 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/3/4 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/4/1 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/4/2 | vlan-808      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/4/3 | vlan-808      | Trunk | immediate            | unformed | 
+---------------------+-----------+------+----------+---------------+-------+----------------------+----------+
| k8s/k8s_ANP/SRIoV_B | node-2207 | Intf | eth1/5/1 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/5/2 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/5/3 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/5/4 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/6/1 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/6/2 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2207 | Intf | eth1/6/3 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/5/1 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/5/2 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/5/3 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/5/4 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/6/1 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/6/2 | vlan-807      | Trunk | immediate            | unformed | 
|                     | node-2208 | Intf | eth1/6/3 | vlan-807      | Trunk | immediate            | unformed | 
+---------------------+-----------+------+----------+---------------+-------+----------------------+----------+
```

Developer

```
# iserver get aci epg --apic apic21 --name sriov* --view stport

{
    "duration": 2029,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 442,
        "disconnect_time": 0,
        "mo_time": 1185,
        "total_time": 1627
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

True	442	-	connect apic21o.emea-sp.cisco.com:443
True	470	36	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-include=health,fault-count&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	341	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	374	282	apic21o.emea-sp.cisco.com:443 class fvIfConn
```

[[Back]](./ApplicationEpg.md)