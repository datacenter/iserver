# Application Endpoint Group (EPG)

## Get EPGs' member properties

```
# iserver get aci epg --apic apic21 --tenant k8s* --view member

Apic: apic21 (mode:online, cache:off)

EPG Members
-----------

+------------------------+-------------+----------------+--------------+---------------------+-----------+
| EPG                    | Member Type | Node           | Type         | ID                  | VLAN      |
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/backbone1  | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1301 | 
|                        | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1301 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1301 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1301 | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/bmk8s_1    | static      | cl2207-eu-spdc | Policy Group | k8s_ocp_bm_1_PolGrp | vlan-801  | 
|                        | static      | cl2208-eu-spdc | Policy Group | k8s_ocp_bm_1_PolGrp | vlan-801  | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/bmk8s_2    | static      | cl2207-eu-spdc | Policy Group | k8s_ocp_bm_2_PolGrp | vlan-802  | 
|                        | static      | cl2208-eu-spdc | Policy Group | k8s_ocp_bm_2_PolGrp | vlan-802  | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/bmk8s_prov | static      | cl2207-eu-spdc | Policy Group | k8s_ocp_bm_1_PolGrp | vlan-809  | 
|                        | static      | cl2207-eu-spdc | Policy Group | k8s_ocp_bm_2_PolGrp | vlan-809  | 
|                        | static      | cl2207-eu-spdc | Policy Group | k8s_ocp_bm_3_PolGrp | vlan-809  | 
|                        | static      | cl2207-eu-spdc | Policy Group | k8s_ocp_bm_4_PolGrp | vlan-809  | 
|                        | static      | cl2207-eu-spdc | Policy Group | k8s_ocp_bm_5_PolGrp | vlan-809  | 
|                        | static      | cl2208-eu-spdc | Policy Group | k8s_ocp_bm_1_PolGrp | vlan-809  | 
|                        | static      | cl2208-eu-spdc | Policy Group | k8s_ocp_bm_2_PolGrp | vlan-809  | 
|                        | static      | cl2208-eu-spdc | Policy Group | k8s_ocp_bm_3_PolGrp | vlan-809  | 
|                        | static      | cl2208-eu-spdc | Policy Group | k8s_ocp_bm_4_PolGrp | vlan-809  | 
|                        | static      | cl2208-eu-spdc | Policy Group | k8s_ocp_bm_5_PolGrp | vlan-809  | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/csr1_lan   | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1303 | 
|                        | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1303 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1303 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1303 | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/csr2_lan   | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1435 | 
|                        | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1435 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1435 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1435 | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/csr_b2b    | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1305 | 
|                        | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1305 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1305 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1305 | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/MGMT       | static      | cl2207-eu-spdc | Policy Group | k8s_ocp_bm_1_PolGrp | vlan-800  | 
|                        | static      | cl2208-eu-spdc | Policy Group | k8s_ocp_bm_1_PolGrp | vlan-800  | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/site1_lan  | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1306 | 
|                        | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1306 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1306 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1306 | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/site1_pe   | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1304 | 
|                        | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1304 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1304 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1304 | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/site2_lan  | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1437 | 
|                        | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1437 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1437 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1437 | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/site2_pe   | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1302 | 
|                        | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1302 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1302 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1302 | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/SRIoV_A    | static      | cl2207-eu-spdc | Intf         | eth1/3/1            | vlan-808  | 
|                        | static      | cl2207-eu-spdc | Intf         | eth1/3/2            | vlan-808  | 
|                        | static      | cl2207-eu-spdc | Intf         | eth1/3/3            | vlan-808  | 
|                        | static      | cl2207-eu-spdc | Intf         | eth1/3/4            | vlan-808  | 
|                        | static      | cl2207-eu-spdc | Intf         | eth1/4/1            | vlan-808  | 
|                        | static      | cl2207-eu-spdc | Intf         | eth1/4/2            | vlan-808  | 
|                        | static      | cl2207-eu-spdc | Intf         | eth1/4/3            | vlan-808  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/3/1            | vlan-808  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/3/2            | vlan-808  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/3/3            | vlan-808  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/3/4            | vlan-808  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/4/1            | vlan-808  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/4/2            | vlan-808  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/4/3            | vlan-808  | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/SRIoV_B    | static      | cl2207-eu-spdc | Intf         | eth1/5/1            | vlan-807  | 
|                        | static      | cl2207-eu-spdc | Intf         | eth1/5/2            | vlan-807  | 
|                        | static      | cl2207-eu-spdc | Intf         | eth1/5/3            | vlan-807  | 
|                        | static      | cl2207-eu-spdc | Intf         | eth1/5/4            | vlan-807  | 
|                        | static      | cl2207-eu-spdc | Intf         | eth1/6/1            | vlan-807  | 
|                        | static      | cl2207-eu-spdc | Intf         | eth1/6/2            | vlan-807  | 
|                        | static      | cl2207-eu-spdc | Intf         | eth1/6/3            | vlan-807  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/5/1            | vlan-807  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/5/2            | vlan-807  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/5/3            | vlan-807  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/5/4            | vlan-807  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/6/1            | vlan-807  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/6/2            | vlan-807  | 
|                        | static      | cl2208-eu-spdc | Intf         | eth1/6/3            | vlan-807  | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/Test       |             |                |              |                     |           | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/vk8s_1     | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1367 | 
|                        | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1367 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1367 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1367 | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/vk8s_2     | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1300 | 
|                        | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1300 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1300 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1300 | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/vk8s_3     | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1369 | 
|                        | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1369 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1369 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1369 | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
| k8s/k8s_ANP/vk8s_4     | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1368 | 
|                        | dynamic     | cl2207-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1368 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx71_PolGrp    | vlan-1368 | 
|                        | dynamic     | cl2208-eu-spdc | Policy Group | k8s_esx72_PolGrp    | vlan-1368 | 
+------------------------+-------------+----------------+--------------+---------------------+-----------+
```

Developer

```
# iserver get aci epg --apic apic21 --tenant k8s* --view member

{
    "duration": 2940,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 470,
        "disconnect_time": 0,
        "mo_time": 1371,
        "total_time": 1841
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

True	470	-	connect apic21o.emea-sp.cisco.com:443
True	597	37	apic21o.emea-sp.cisco.com:443 class fvAEPg query rsp-subtree=children&rsp-subtree-class=fvRsBd,fvRsCons,fvRsProv,fvRsProtBy,fvRtMatchEPg,fvRsPathAtt,fvRsDomAtt
True	362	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	412	280	apic21o.emea-sp.cisco.com:443 class fvIfConn
```

[[Back]](./ApplicationEpg.md)