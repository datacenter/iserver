# Fabric checks with interface mismatch

## Case: interface mismatch

```
Apic [myapic] domain [management] configuration
------------------------------------------------
- Tenant [my_tenant] found
- VLAN pool [my_vlan_pool] found
        Vlans [666] match
- AAEP [my_aaep] found
- Physical domain [my_phys_dom] found
        VLAN pool [my_vlan_pool] match
        AAEP [my_aaep] match
- PolicyGroup [my_pg]
        CDP policy [my_cdp] match
        LLDP policy [my_lldp] match
        Link level policy [my_link_level] match
        Port channel policy [my_lacp] match
        L2 policy [my_l2] match
        Deployed on pod-1:node-100:eth1/1/1
[ERROR] No server found
        Deployed on pod-1:node-200:eth1/1/1
[ERROR] No server found
- Application profile [my_anp] found
        Tenant [my_tenant] match
- EPG [my_epg]
        Tenant [my_tenant] match
        Application profile [my_anp] match
        Bridge Domain [my_bd] match
        Static port [my_pg] match
- Bridge Domain [my_bd] found
        Tenant [my_tenant] match
        Gateway [10.4.4.15/28] match
        L3out [my_l3out] match

Server [bm1] interfaces in domain [management]
---------------------------------------------------

Interface pod-1:node-100:1/4/1
- Interface found
        Operational State up
        Switching State enabled
        Usage epg
        Operational Mode trunk
        Operational Speed 10G
        IP endpoint [10.4.4.1] found
        - my_tenant/my_anp/my_epg
                pod-1:node-100:eth1/1/1 (my_pg)
                pod-1:node-200:eth1/1/1 (my_pg)
        IP endpoint with EPG match
[ERROR] IP endpoint found on different interfaces
        MAC endpoint [aa:aa:aa:aa:aa:aa] found
        - my_tenant/my_anp/my_epg
                pod-1:node-100:eth1/1/1 (my_pg)
                pod-1:node-200:eth1/1/1 (my_pg)
        MAC endpoint with EPG match
[ERROR] MAC endpoint found on different interfaces
[ERROR] EPG [my_tenant/my_anp/my_epg] may not be enabled on interface
- Trunk mode match
[ERROR] VLAN [666] may not be enabled
[ERROR] PC/VPC policy expected
- PolicyGroup mismatch [some_pg] vs. [my_pg]
[ERROR] Interface channel unknown

Interface pod-1:node-200:1/4/1
- Interface found
        Operational State up
        Switching State enabled
        Usage epg
        Operational Mode trunk
        Operational Speed 10G
        IP endpoint [10.4.4.1] found
        - my_tenant/my_anp/my_epg
                pod-1:node-100:eth1/1/1 (my_pg)
                pod-1:node-200:eth1/1/1 (my_pg)
        IP endpoint with EPG match
[ERROR] IP endpoint found on different interfaces
        MAC endpoint [bb:bb:bb:bb:bb:bb] not found
[ERROR] EPG [my_tenant/my_anp/my_epg] may not be enabled on interface
- Trunk mode match
[ERROR] VLAN [666] may not be enabled
[ERROR] PC/VPC policy expected
- PolicyGroup mismatch [my_tenant_sriov_200_bm_PolGrp] vs. [my_pg]
[ERROR] Interface channel unknown
```

## Case: parent breakout interface

```
Apic [myapic] domain [management] configuration
------------------------------------------------
- Tenant [my_tenant] found
- VLAN pool [my_vlan_pool] found
        Vlans [666] match
- AAEP [my_aaep] found
- Physical domain [my_phys_dom] found
        VLAN pool [my_vlan_pool] match
        AAEP [my_aaep] match
- PolicyGroup [my_pg]
        CDP policy [my_cdp] match
        LLDP policy [my_lldp] match
        Link level policy [my_link_level] match
        Port channel policy [my_lacp] match
        L2 policy [my_l2] match
        Deployed on pod-1:node-100:eth1/1/1
[ERROR] No server found
        Deployed on pod-1:node-200:eth1/1/1
[ERROR] No server found
- Application profile [my_anp] found
        Tenant [my_tenant] match
- EPG [my_epg]
        Tenant [my_tenant] match
        Application profile [my_anp] match
        Bridge Domain [my_bd] match
        Static port [my_pg] match
- Bridge Domain [my_bd] found
        Tenant [my_tenant] match
        Gateway [10.4.4.15/28] match
        L3out [my_l3out] match

Server [bm1] interfaces in domain [management]
---------------------------------------------------

Interface pod-1:node-100:1/3
- Interface found
[ERROR] Missing interface stats (breakout parent interface?)
        IP endpoint [10.4.4.1] found
        - my_tenant/my_anp/my_epg
                pod-1:node-100:eth1/1/1 (my_pg)
                pod-1:node-200:eth1/1/1 (my_pg)
        IP endpoint with EPG match
[ERROR] IP endpoint found on different interfaces
        MAC endpoint [aa:aa:aa:aa:aa:aa] found
        - my_tenant/my_anp/my_epg
                pod-1:node-100:eth1/1/1 (my_pg)
                pod-1:node-200:eth1/1/1 (my_pg)
        MAC endpoint with EPG match
[ERROR] MAC endpoint found on different interfaces
- Trunk mode match
[ERROR] Cannot confirm if VLAN [666] is configured on an interface
[ERROR] PC/VPC policy expected
- PolicyGroup mismatch [system-breakout-25g-4x] vs. [my_pg]
[ERROR] Interface channel unknown

Interface pod-1:node-200:1/3
- Interface found
[ERROR] Missing interface stats (breakout parent interface?)
        IP endpoint [10.4.4.1] found
        - my_tenant/my_anp/my_epg
                pod-1:node-100:eth1/1/1 (my_pg)
                pod-1:node-200:eth1/1/1 (my_pg)
        IP endpoint with EPG match
[ERROR] IP endpoint found on different interfaces
        MAC endpoint [bb:bb:bb:bb:bb:bb] not found
- Trunk mode match
[ERROR] Cannot confirm if VLAN [666] is configured on an interface
[ERROR] PC/VPC policy expected
- PolicyGroup mismatch [system-breakout-25g-4x] vs. [my_pg]
[ERROR] Interface channel unknown
```

[Back](./fabric_aci_check.md)
