# Application Endpoint Group (EPG)

## Filter by tenant name

```
# iserver get aci epg --apic apic21 --tenant k8s

Apic: apic21

+----+------------------------+-------------------+--------------------+-----------+----------+
| Up | EPG                    | Bridge Domain     | Subnets            | Endpoints | Contract |
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/backbone1  | k8s/VM2VM_BD      |                    | 2         |          | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/bmk8s_1    | k8s/bmk8s_1_BD    | 10.58.24.78/28     | 0         | V        | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/bmk8s_2    | k8s/bmk8s_2_BD    | 10.58.24.94/28     | 0         | V        | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/bmk8s_prov | k8s/bmk8s_prov_BD | 10.58.29.94/28     | 4         | V        | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/csr1_lan   | k8s/VM2VM_BD      |                    | 1         |          | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/csr2_lan   | k8s/VM2VM_BD      |                    | 1         |          | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/csr_b2b    | k8s/VM2VM_BD      |                    | 0         |          | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/MGMT       | k8s/MGMT_BD       | 10.58.25.174/28    | 0         | V        | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/site1_lan  | k8s/VM2VM_BD      |                    | 1         |          | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/site1_pe   | k8s/VM2VM_BD      |                    | 2         |          | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/site2_lan  | k8s/VM2VM_BD      |                    | 1         |          | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/site2_pe   | k8s/VM2VM_BD      |                    | 2         |          | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/SRIoV_A    | k8s/SRIoV_A_BD    | 15.20.16.254/24    | 1         | V        | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/SRIoV_B    | k8s/SRIoV_B_BD    | 15.20.17.254/24    | 2         |          | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/Test       | k8s/Test          | 169.169.170.254/24 | 0         |          | 
|    |                        |                   | 169.169.169.254/24 |           |          | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_1     | k8s/vk8s_1_BD     | 10.58.24.174/28    | 8         | V        | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_2     | k8s/vk8s_2_BD     | 10.58.24.190/28    | 8         | V        | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_3     | k8s/vk8s_3_BD     | 10.58.24.206/28    | 8         | V        | 
+----+------------------------+-------------------+--------------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_4     | k8s/vk8s_4_BD     | 10.58.24.222/28    | 8         | V        | 
+----+------------------------+-------------------+--------------------+-----------+----------+
```

Developer

```
# iserver get aci epg --apic apic21 --tenant k8s

{
    "duration": 2580,
    "apic": {
        "read": true,
        "success": 6,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 5,
        "connect_time": 400,
        "disconnect_time": 0,
        "mo_time": 1848,
        "total_time": 2248
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

True	400	-	connect apic21o.emea-sp.cisco.com
True	360	37	apic21o.emea-sp.cisco.com class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRtMatchEPg
True	394	53	apic21o.emea-sp.cisco.com class fvAREpP query rsp-subtree=children&rsp-subtree-class=fvLocale
True	332	13	apic21o.emea-sp.cisco.com class fabricNode
True	397	36	apic21o.emea-sp.cisco.com class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	365	71	apic21o.emea-sp.cisco.com class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper
```

[[Back]](./ApplicationEpg.md)