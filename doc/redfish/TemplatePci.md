# PCI Template

[[Next]](./TemplatePower.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v pci

+----+--------+------------------------------------------------------------------+---------+--------+--------+--------+-----------+-----+-----+---------+--------+
| ID | PCI Id | Name                                                             | Fw      | DevId  | Vendor | SubId  | SubVendor | Net | Eth | Storage | Drives |
+----+--------+------------------------------------------------------------------+---------+--------+--------+--------+-----------+-----+-----+---------+--------+
| 1  | MRAID  | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | N/A     | 0x0014 | 0x1000 | 0x020e | 0x1137    | 0   | 0   | 1       | 26     | 
| 2  | MLOM   | Cisco UCS VIC 1457 MLOM                                          | 1.1     | 0x0042 | 0x1137 | 0x0218 | 0x1137    | 7   | 4   | 0       | 0      | 
| 3  | L      | Intel X550 LOM                                                   | 2.2     | 0x1563 | 0x8086 | 0x01a4 | 0x1137    | 0   | 2   | 0       | 0      | 
| 4  | 3      | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 2.2     | 0x158b | 0x8086 | 0x0225 | 0x1137    | 0   | 2   | 0       | 0      | 
| 5  | 6      | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 2.2     | 0x158b | 0x8086 | 0x0225 | 0x1137    | 0   | 2   | 0       | 0      | 
+----+--------+------------------------------------------------------------------+---------+--------+--------+--------+-----------+-----+-----+---------+--------+

View: access, account, bios, cpu, fan, gpu, hw, identity (def), mem, net, pci, power, psu, role, storage, thermal, all
```

[[Back]](./README.md)