# Link Layer Discovery Protocol (LLDP)

## Default output

```
# iserver get nx lldp --device ipn11

Device: ipn11

LLDP [#11]
----------

+--------+-----------------+---------------------------------+----------------+-----------+------------+
| Device | Local Interface | Device ID                       | Port ID        | Hold Time | Capability |
+--------+-----------------+---------------------------------+----------------+-----------+------------+
| ipn11  | mgmt0           | r12-eu-spdc.emea-sp.cisco.com   | Ethernet1/41   | 120       | BR         | 
| ipn11  | Eth1/5          | 14a2.a0ec.7468                  | 14a2.a0ec.746c | 120       | --         | 
| ipn11  | Eth1/6          | 04a7.4110.15f0                  | 04a7.4110.15f4 | 120       | --         | 
| ipn11  | Eth1/7          | 04a7.410f.eb54                  | 04a7.410f.eb58 | 120       | --         | 
| ipn11  | Eth1/32/1       | r11-eu-spdc.emea-sp.cisco.com   | Ethernet1/51   | 120       | BR         | 
| ipn11  | Eth1/32/2       | r12-eu-spdc.emea-sp.cisco.com   | Ethernet1/51   | 120       | BR         | 
| ipn11  | Eth1/32/3       | r13-eu-spdc.emea-sp.cisco.com   | Ethernet1/51   | 120       | BR         | 
| ipn11  | Eth1/32/4       | r14-eu-spdc.emea-sp.cisco.com   | Ethernet1/51   | 120       | BR         | 
| ipn11  | Eth1/33         | ipn-eu-spdc.emea-sp.cisco.com   | Ethernet3/5    | 120       | BR         | 
| ipn11  | Eth1/34         | ipn-eu-spdc.emea-sp.cisco.com   | Ethernet3/6    | 120       | BR         | 
| ipn11  | Eth1/35         | ipn12-eu-spdc.emea-sp.cisco.com | Ethernet1/35   | 120       | BR         | 
+--------+-----------------+---------------------------------+----------------+-----------+------------+

Filter: id, mac
View:   state (def)
```

[[Back]](./Lldp.md)