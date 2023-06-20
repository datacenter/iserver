# Application Endpoint Group (EPG)

## Filter by EPG name

Example: name

```
# iserver get aci epg --apic apic21 --name *vk8s*

Apic: apic21 (mode:online, cache:off)

EPG Summary
-----------

+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| Up | EPG                | BD            | BD Subnet       | Endpoint | Node | Domain               | Contract | StPort | StMember | DynMember |
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_1 | k8s/vk8s_1_BD | 10.58.24.174/28 | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                    |               |                 |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_2 | k8s/vk8s_2_BD | 10.58.24.190/28 | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                    |               |                 |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_3 | k8s/vk8s_3_BD | 10.58.24.206/28 | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                    |               |                 |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_4 | k8s/vk8s_4_BD | 10.58.24.222/28 | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                    |               |                 |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
```

Example: profile and name

```
# iserver get aci epg --apic apic21 --name k8*/vk8s*

Apic: apic21 (mode:online, cache:off)

EPG Summary
-----------

+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| Up | EPG                | BD            | BD Subnet       | Endpoint | Node | Domain               | Contract | StPort | StMember | DynMember |
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_1 | k8s/vk8s_1_BD | 10.58.24.174/28 | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                    |               |                 |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_2 | k8s/vk8s_2_BD | 10.58.24.190/28 | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                    |               |                 |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_3 | k8s/vk8s_3_BD | 10.58.24.206/28 | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                    |               |                 |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_4 | k8s/vk8s_4_BD | 10.58.24.222/28 | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                    |               |                 |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
```

Example: tenant, profile and name

```
# iserver get aci epg --apic apic21 --name k8*/k8*/vk8s*

Apic: apic21 (mode:online, cache:off)

EPG Summary
-----------

+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| Up | EPG                | BD            | BD Subnet       | Endpoint | Node | Domain               | Contract | StPort | StMember | DynMember |
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_1 | k8s/vk8s_1_BD | 10.58.24.174/28 | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                    |               |                 |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_2 | k8s/vk8s_2_BD | 10.58.24.190/28 | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                    |               |                 |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_3 | k8s/vk8s_3_BD | 10.58.24.206/28 | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                    |               |                 |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
| V  | k8s/k8s_ANP/vk8s_4 | k8s/vk8s_4_BD | 10.58.24.222/28 | 8        |      | VMware/EU-SPDC-POD2B | 1        | 0      | 0        | 0         | 
|    |                    |               |                 |          |      | k8s_esx_PhysDom      |          |        |          |           | 
+----+--------------------+---------------+-----------------+----------+------+----------------------+----------+--------+----------+-----------+
```

Developer

```
# iserver get aci epg --apic apic21 --name *vk8s*

{
    "duration": 4655,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 447,
        "disconnect_time": 0,
        "mo_time": 3406,
        "total_time": 3853
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

True	447	-	connect apic21o.emea-sp.cisco.com:443
True	393	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	321	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	362	280	apic21o.emea-sp.cisco.com:443 class fvIfConn
True	351	152	apic21o.emea-sp.cisco.com:443 class fvLocale
True	420	36	apic21o.emea-sp.cisco.com:443 class fvBD query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvRsCtx&rsp-subtree-class=fvRsBdToEpRet&rsp-subtree-class=fvRsIgmpsn&rsp-subtree-class=fvRsMldsn&rsp-subtree-class=fvRsBDToOut&rsp-subtree-class=fvSubnet
True	406	91	apic21o.emea-sp.cisco.com:443 class fvCEp query rsp-subtree-include=health&rsp-subtree=children&rsp-subtree-class=fvIp&rsp-subtree-class=fvRsCEpToPathEp&rsp-subtree-class=fvRsToVm&rsp-subtree-class=fvRsHyper&rsp-subtree-class=fvRsToNic
True	448	22	apic21o.emea-sp.cisco.com:443 class vzBrCP query rsp-subtree=children&rsp-subtree-class=vzSubj,vzRtCons,vzRtProv
True	337	24	apic21o.emea-sp.cisco.com:443 class vzSubj query rsp-subtree=children&rsp-subtree-class=vzRsSubjFiltAtt
True	368	30	apic21o.emea-sp.cisco.com:443 class vzFilter query rsp-subtree=children&rsp-subtree-class=vzEntry
```

[[Back]](./ApplicationEpg.md)