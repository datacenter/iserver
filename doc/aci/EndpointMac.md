# Endpoint

## Filter by mac

```
# iserver get aci ep --apic apic11 --tenant smi5Gc --mac e6

Apic: apic11 (mode:online, cache:off)

+----+-------------------+---------------+--------------------------------------------------+-------+------------------------------------+-------------------------------+
| SF | MAC Address       | IP Address    | EPG                                              | Encap | BD                                 | VRF                           |
+----+-------------------+---------------+--------------------------------------------------+-------+------------------------------------+-------------------------------+
| L  | FA:16:3E:63:7D:AA | 15.100.5.101  | smi5Gc/smi5Gc-cvim1_ANP/smi5Gc-cvim1-Control-N2  | 1105  | smi5Gc/smi5Gc-cvim1-Control-N2_BD  | common/smi5Gc-cvim1_VRF       | 
|    |                   | 15.100.5.103  |                                                  |       |                                    |                               | 
|    |                   | 15.100.5.102  |                                                  |       |                                    |                               | 
|    |                   | 15.100.5.104  |                                                  |       |                                    |                               | 
+----+-------------------+---------------+--------------------------------------------------+-------+------------------------------------+-------------------------------+
| L  | FA:16:3E:69:DE:1D | 15.100.100.80 | smi5Gc/smi5Gc-cvim4_ANP/smi5Gc-cvim4-Control-SBI | 2704  | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | common/smi5Gc-cvim4_VRF       | 
+----+-------------------+---------------+--------------------------------------------------+-------+------------------------------------+-------------------------------+
| L  | FA:16:3E:6B:5B:AB | 15.100.6.1    | smi5Gc/smi5Gc-cvim1_ANP/smi5Gc-cvim1-Control-N4  | 1106  | smi5Gc/smi5Gc-cvim1-Control-N4_BD  | common/smi5Gc-cvim1-N3-N4_VRF | 
+----+-------------------+---------------+--------------------------------------------------+-------+------------------------------------+-------------------------------+
| L  | FA:16:3E:6F:C6:B7 | 15.100.6.2    | smi5Gc/smi5Gc-cvim1_ANP/smi5Gc-cvim1-Control-N4  | 1106  | smi5Gc/smi5Gc-cvim1-Control-N4_BD  | common/smi5Gc-cvim1-N3-N4_VRF | 
+----+-------------------+---------------+--------------------------------------------------+-------+------------------------------------+-------------------------------+
| L  | FA:16:3E:E0:A2:E6 | 15.100.6.221  | smi5Gc/smi5Gc-cvim1_ANP/smi5Gc-cvim1-Control-N4  | 1106  | smi5Gc/smi5Gc-cvim1-Control-N4_BD  | common/smi5Gc-cvim1-N3-N4_VRF | 
+----+-------------------+---------------+--------------------------------------------------+-------+------------------------------------+-------------------------------+
```

Developer

```
# iserver get aci ep --apic apic11 --tenant smi5Gc --mac e6

{
    "duration": 1378,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 389,
        "disconnect_time": 0,
        "mo_time": 758,
        "total_time": 1147
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

True	389	-	connect apic11o.emea-sp.cisco.com:443
True	758	357	apic11o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health,fault-count&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
```

[[Back]](./Endpoint.md)