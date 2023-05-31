# Endpoint

## Filter by subnet

```
# iserver get aci ep --apic apic11 --subnet 15.100.100.0/24

Apic: apic11

+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| SF | MAC Address       | IP Address    | Tenant | BD                                 | EPG                      | Ap               | VRF                     |
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:3E | 15.100.100.62 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:3F | 15.100.100.63 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:40 | 15.100.100.64 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:41 | 15.100.100.65 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:42 | 15.100.100.66 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:43 | 15.100.100.67 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:44 | 15.100.100.68 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:47 | 15.100.100.71 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:52 | 15.100.100.82 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:53 | 15.100.100.83 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:54 | 15.100.100.84 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:55 | 15.100.100.85 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:56 | 15.100.100.86 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:57 | 15.100.100.87 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:58 | 15.100.100.88 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:5B | 15.100.100.91 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | 02:42:0F:64:64:5C | 15.100.100.92 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | FA:16:3E:69:DE:1D | 15.100.100.80 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | FA:16:3E:A2:04:47 | 15.100.100.2  | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | FA:16:3E:A6:8C:AC | 15.100.100.1  | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
| L  | FA:16:3E:BA:5C:58 | 15.100.100.70 | smi5Gc | smi5Gc/smi5Gc-cvim4-Control-SBI_BD | smi5Gc-cvim4-Control-SBI | smi5Gc-cvim4_ANP | common/smi5Gc-cvim4_VRF | 
+----+-------------------+---------------+--------+------------------------------------+--------------------------+------------------+-------------------------+
```

Developer

```
# iserver get aci ep --apic apic11 --subnet 15.100.100.0/24

{
    "duration": 1086,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 397,
        "disconnect_time": 0,
        "mo_time": 558,
        "total_time": 955
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

True	397	-	connect apic11o.emea-sp.cisco.com
True	558	322	apic11o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
```

[[Back]](./Endpoint.md)