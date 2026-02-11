# PSU Template

[[Next]](./TemplateRole.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v psu

+----+--------+------+---------+-------------------+---------------+-------------+---------------+-------------------+----------+
| ID | PSU Id | Name | State   | Vendor            | Model         | Part Number | Serial Number | Spare Part Number | Firmware |
+----+--------+------+---------+-------------------+---------------+-------------+---------------+-------------------+----------+
| 1  | 1      | PSU1 | Enabled | Cisco Systems Inc | PSU-111-22-33 | abc         | 1111          | def               | 2222     |
| 2  | 2      | PSU2 | Enabled | Cisco Systems Inc | PSU-111-22-33 | abc         | 2222          | def               | 3333     |
+----+--------+------+---------+-------------------+---------------+-------------+---------------+-------------------+----------+
```

[[Back]](./README.md)