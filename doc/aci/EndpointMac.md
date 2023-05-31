# Endpoint

## Filter by mac

```
# iserver get aci ep --apic apic11 --tenant smi5Gc --mac e6

Apic: apic11

+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------------+
| SF | MAC Address       | IP Address    | Tenant | BD                                 | EPG                      | Ap               | VRF                           |
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------------+
| L  | FA:16:3E:69:DE:1D | 15.100.100.80 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF       | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------------+
| L  | FA:16:3E:6B:5B:AB | 15.100.6.1    | smi5Gc | smi5Gc/smi5Gc-cvim1-Control-N4_BD  | smi5Gc-cvim1-Control-N4  | smi5Gc-cvim1_ANP | common/smi5Gc-cvim1-N3-N4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------------+
| L  | FA:16:3E:6F:C6:B7 | 15.100.6.2    | smi5Gc | smi5Gc/smi5Gc-cvim1-Control-N4_BD  | smi5Gc-cvim1-Control-N4  | smi5Gc-cvim1_ANP | common/smi5Gc-cvim1-N3-N4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------------+
| L  | FA:16:3E:E0:A2:E6 | 15.100.6.221  | smi5Gc | smi5Gc/smi5Gc-cvim1-Control-N4_BD  | smi5Gc-cvim1-Control-N4  | smi5Gc-cvim1_ANP | common/smi5Gc-cvim1-N3-N4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------------+
```

Developer

```
# iserver get aci ep --apic apic11 --tenant smi5Gc --mac e6

{
    "duration": 1065,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 386,
        "disconnect_time": 0,
        "mo_time": 568,
        "total_time": 954
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
    }
}

Log: apic
----------

True	386	-	connect apic11o.emea-sp.cisco.com
True	568	322	apic11o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
```

[[Back]](./Endpoint.md)