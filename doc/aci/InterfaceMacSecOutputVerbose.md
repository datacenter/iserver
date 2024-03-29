# Node Interface - MACsec

## Verbose view

```
# iserver get aci intf macsec
    --apic apic21
    --node bl2205-eu-spdc
    --id eth1/28
    --view verbose

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Interface Macsec
----------------
- Interface       : eth1/28
- Admin State     : disabled
- Oper State      : down
- Reason          : admin-down
- Session State   : not-initialized
- Peers           : 0
- Cepher Suite    : 0
- Confid Offset   : 0
- Key Chain       : 
- Ker Server Prio : 16
- Replay Window   : 64


MKA Stats
---------

SecY Stats
----------
- OK Packets           : 0
- Rx Decrypted Octets  : 0
- Rx Decrypted Packets : 0
- Delayed Packets      : 0
- Invalidated Octets   : 0
- Invalidated Packets  : 0
- Invalid Packets      : 0
- Late Packets         : 0
- Not Using SA Packets : 0
- Not Valid Packets    : 0
- Unchecked Packets    : 0
- Unused SA Packets    : 0
- Tx Encrypted Octets  : 0
- Tx Encrypted Packets : 0
- Tx Protected Octets  : 0
- Tx Protected Packets : 0
```

Developer

```
# iserver get aci intf macsec
    --apic apic21
    --node bl2205-eu-spdc
    --id eth1/28
    --view verbose

{
    "duration": 5164,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 686,
        "disconnect_time": 0,
        "mo_time": 4137,
        "total_time": 4823
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

True	686	-	connect apic21o.emea-sp.cisco.com:443
True	404	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	404	28	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/macsecIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	1175	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	385	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	451	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/28]/dbgIfMacsectx
True	387	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/phys-[eth1/28]/dbgIfMacsecrx
True	519	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/macsec/inst/if-[eth1/28] query query-target=children&target-subtree-class=macsecIfStats
True	412	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/macsec/inst/if-[eth1/28] query query-target=children&target-subtree-class=macsecCAStats
```

[[Back]](./InterfaceMacSec.md)