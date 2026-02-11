# Bios Template

[[Next]](./TemplateCpu.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v bios

+-----+------------------------------+----------------------+
| ID  | Key                          | Value                |
+-----+------------------------------+----------------------+
| 1   | AdjacentCacheLinePrefetch    | Enabled              | 
| 2   | AdvancedMemTest              | Auto                 | 
| 3   | AllLomPortControl            | Enabled              | 
| 4   | ATS                          | Enabled              | 
| 5   | AutoCCState                  | Disabled             | 
| 6   | BaudRate                     | 115.2k               |
| ... | ...                          | ...                  |
| 131 | XPTPrefetch                  | Auto                 |
+-----+------------------------------+----------------------+

View: access, account, bios, cpu, fan, gpu, hw, identity (def), mem, net, pci, power, psu, role, storage, thermal, all

```

[[Back]](./README.md)