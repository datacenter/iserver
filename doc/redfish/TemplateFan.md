# Fan Template

[[Next]](./TemplateGpu.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v fan

+----+----+-----------------+---------+--------+---------+-------+
| ID | Id | Name            | State   | Health | Reading | Units |
+----+----+-----------------+---------+--------+---------+-------+
| 1  | 1  | MOD1_FAN1_SPEED | Enabled | OK     | 7070    | RPM   | 
| 2  | 2  | MOD1_FAN2_SPEED | Enabled | OK     | 7056    | RPM   | 
| 3  | 3  | MOD2_FAN1_SPEED | Enabled | OK     | 6868    | RPM   | 
| 4  | 4  | MOD2_FAN2_SPEED | Enabled | OK     | 7056    | RPM   | 
| 5  | 5  | MOD3_FAN1_SPEED | Enabled | OK     | 6868    | RPM   | 
| 6  | 6  | MOD3_FAN2_SPEED | Enabled | OK     | 7056    | RPM   | 
| 7  | 7  | MOD4_FAN1_SPEED | Enabled | OK     | 6868    | RPM   | 
| 8  | 8  | MOD4_FAN2_SPEED | Enabled | OK     | 7056    | RPM   | 
| 9  | 9  | MOD5_FAN1_SPEED | Enabled | OK     | 7070    | RPM   | 
| 10 | 10 | MOD5_FAN2_SPEED | Enabled | OK     | 7056    | RPM   | 
| 11 | 11 | MOD6_FAN1_SPEED | Enabled | OK     | 6868    | RPM   | 
| 12 | 12 | MOD6_FAN2_SPEED | Enabled | OK     | 7350    | RPM   | 
| 13 | 13 | MOD7_FAN1_SPEED | Absent  | ---    | ---     | ---   | 
+----+----+-----------------+---------+--------+---------+-------+

View: access, account, bios, cpu, fan, gpu, hw, identity (def), mem, net, pci, power, psu, role, storage, thermal, all
```

[[Back]](./README.md)