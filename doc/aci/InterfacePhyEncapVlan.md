# Node Interface - Physical

## Filter by encapsulation vlan

Example: single vlan

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc --vlan 908 -o vlan

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc
No interface
```

Example: multiple vlans

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --vlan 900,904-905 -o vlan

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc
No interface
```

[[Back]](./InterfacePhy.md)