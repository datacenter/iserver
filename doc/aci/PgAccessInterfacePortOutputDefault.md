# Policy Group - Access Interface - Leaf Access Port

## Default output

```
# iserver get aci pg access intf port --apic apic21

Apic: apic21 (mode:online, cache:off)

Policy Group - Access Interface Port [#8]
-----------------------------------------

+---------+---------------------------+-----------------+-------------+-----------+----------------+---------+-----------------+---------+---------------+
| Faults  | Name                      | AAEP            | Link Level  | Link Flap | CDP            | MCP     | LLDP            | STP     | Storm Control |
+---------+---------------------------+-----------------+-------------+-----------+----------------+---------+-----------------+---------+---------------+
| 0 0 0 0 | ESX-CDC-22_PolGrp         | ESX-CDC-22_AAEP | Inherit     | default   | CDP-enable     | default | LLDP-enable     | default | default       | 
| 0 0 0 0 | ESX-R7DC_PolGrp           | ESX-R7DC_AAEP   | Inherit     | default   | default        | default | LLDP-enable     | default | default       | 
| 0 0 0 0 | Infra-L3_PolGrp           | Infra_AAEP      | Inherit     | default   | CDP-enable     | default | LLDP-enable     | default | default       | 
| 0 0 0 0 | k8s_sriov_2207_bm_PolGrp  | k8s_phys_AAEP   | k8s_default | default   | k8s_cdp_enable | default | k8s_lldp_enable | default | default       | 
| 0 0 0 0 | k8s_sriov_2207_esx_PolGrp | k8s_phys_AAEP   | k8s_default | default   | k8s_cdp_enable | default | k8s_lldp_enable | default | default       | 
| 0 0 0 0 | k8s_sriov_2208_bm_PolGrp  | k8s_phys_AAEP   | k8s_default | default   | k8s_cdp_enable | default | k8s_lldp_enable | default | default       | 
| 0 0 0 0 | k8s_sriov_2208_esx_PolGrp | k8s_phys_AAEP   | k8s_default | default   | k8s_cdp_enable | default | k8s_lldp_enable | default | default       | 
| 0 0 0 0 | nidemo-bare-metal         | nidemo          | 10G-auto    | default   | default        | default | LLDP-enable     | default | default       | 
+---------+---------------------------+-----------------+-------------+-----------+----------------+---------+-----------------+---------+---------------+
```

Developer

```
# iserver get aci pg access intf port --apic apic21

{
    "duration": 1074,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 465,
        "disconnect_time": 0,
        "mo_time": 387,
        "total_time": 852
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

True	465	-	connect apic21o.emea-sp.cisco.com:443
True	387	8	apic21o.emea-sp.cisco.com:443 mo uni/infra/funcprof query query-target=subtree&target-subtree-class=infraAccPortGrp&rsp-subtree=children&rsp-subtree-include=fault-count&rsp-subtree-class=infraRsAttEntP,infraRsCdpIfPol,infraRsHIfPol,infraRsLinkFlapPol,infraRsLldpIfPol,infraRsMonIfInfraPol,infraRsStpIfPol,infraRsMcpIfPol,infraRsStormctrlIfPol
```

[[Back]](./PgAccessInterfacePort.md)