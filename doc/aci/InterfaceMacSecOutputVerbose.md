# Node Interface - MACsec

## Verbose output

```
# iserver get aci intf macsec
    --apic apic11
    --node bl205-eu-spdc
    --id eth1/28
    --view verbose

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: bl205-eu-spdc

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
    --apic apic11
    --node bl205-eu-spdc
    --id eth1/28
    --view verbose

{
    "duration": 2851,
    "apic": {
        "read": true,
        "success": 9,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 8,
        "connect_time": 398,
        "disconnect_time": 0,
        "mo_time": 2315,
        "total_time": 2713
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

True	398	-	connect apic11o.emea-sp.cisco.com
True	309	13	apic11o.emea-sp.cisco.com class fabricNode
True	288	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/macsecIf
True	291	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l1PhysIf
True	298	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ethpmPhysIf
True	297	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28]/dbgIfMacsectx
True	275	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/phys-[eth1/28]/dbgIfMacsecrx
True	274	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/macsec/inst/if-[eth1/28] query query-target=children&target-subtree-class=macsecIfStats
True	283	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/macsec/inst/if-[eth1/28] query query-target=children&target-subtree-class=macsecCAStats
```

[[Back]](./InterfaceMacSec.md)