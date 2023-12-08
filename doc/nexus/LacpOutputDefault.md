# Link Aggregation Control Protocol (LACP)

## Default output

```
# iserver get nx lacp --device ipn11

Device: ipn11

LACP [#7]
---------

+--------+-----------------+----------------+-------------------+--------------+---------------+
| Device | Interface       | Port           | Partner MAC       | Partner Port | Partner State |
+--------+-----------------+----------------+-------------------+--------------+---------------+
| ipn11  | port-channel5   | Ethernet1/33   | 00:a3:8e:eb:b3:3f | 0x311        | 0x3d          | 
|        |                 | Ethernet1/34   | 00:a3:8e:eb:b3:3f | 0x315        | 0x3d          | 
| ipn11  | port-channel11  | Ethernet1/32/1 | d0:09:c8:50:dd:ff | 0x1c9        | 0x3d          | 
| ipn11  | port-channel12  | Ethernet1/32/2 | d0:09:c8:50:b3:3f | 0x1c9        | 0x2065723d    | 
| ipn11  | port-channel13  | Ethernet1/32/3 | d0:09:c8:50:e0:87 | 0x1c9        | 0x3d          | 
| ipn11  | port-channel14  | Ethernet1/32/4 | d0:09:c8:50:ad:0f | 0x1c9        | 0x3d          | 
| ipn11  | port-channel100 | Ethernet1/35   | a0:b4:39:71:f6:d3 | 0x189        | 0x3d          | 
| ipn11  | port-channel800 | Ethernet1/3    | 14:a2:a0:ec:75:04 | 0x1          | 0x2e37003d    | 
+--------+-----------------+----------------+-------------------+--------------+---------------+

Filter: mac
View:   state (def)
```

[[Back]](./Lldp.md)