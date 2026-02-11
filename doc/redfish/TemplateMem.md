# Memory Template

[[Next]](./TemplateNet.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v mem

+----+-----------+--------+---------+---------+-------------+-------------+--------+---------+------+-------------+----------------------+---------------+
| ID | Memory Id | Health | State   | Locator | CapacityMiB | Speed [Mhz] | Socket | Channel | Type | Device Type | Part Number          | Serial Number |
+----+-----------+--------+---------+---------+-------------+-------------+--------+---------+------+-------------+----------------------+---------------+
| 1  | 1         | OK     | Enabled | DIMM_A1 | 32768       | 2933        | 0      | 0       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 2  | 3         | OK     | Enabled | DIMM_B1 | 32768       | 2933        | 0      | 1       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 3  | 5         | OK     | Enabled | DIMM_C1 | 32768       | 2933        | 0      | 2       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 4  | 7         | OK     | Enabled | DIMM_D1 | 32768       | 2933        | 0      | 3       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 5  | 9         | OK     | Enabled | DIMM_E1 | 32768       | 2933        | 0      | 4       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 6  | 11        | OK     | Enabled | DIMM_F1 | 32768       | 2933        | 0      | 5       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 7  | 13        | OK     | Enabled | DIMM_G1 | 32768       | 2933        | 1      | 0       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 8  | 15        | OK     | Enabled | DIMM_H1 | 32768       | 2933        | 1      | 1       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 9  | 17        | OK     | Enabled | DIMM_J1 | 32768       | 2933        | 1      | 2       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 10 | 19        | OK     | Enabled | DIMM_K1 | 32768       | 2933        | 1      | 3       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 11 | 21        | OK     | Enabled | DIMM_L1 | 32768       | 2933        | 1      | 4       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
| 12 | 23        | OK     | Enabled | DIMM_M1 | 32768       | 2933        | 1      | 5       | DRAM | DDR4        | 11111111111-22222    | Serial11      | 
+----+-----------+--------+---------+---------+-------------+-------------+--------+---------+------+-------------+----------------------+---------------+

View: access, account, bios, cpu, fan, gpu, hw, identity (def), mem, net, pci, power, psu, role, storage, thermal, all
```

[[Back]](./README.md)