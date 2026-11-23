# Account Template

[[Next]](./TemplateBios.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v account

+----+----------+-----+--------------+---------+---------+------------+---------------------+-----------------------+
| ID | Username | UID | Description  | Role Id | Enabled | Change Req | Role Privileges     | Role Oem Privileges   |
+----+----------+-----+--------------+---------+---------+------------+---------------------+-----------------------+
| 1  | admin    | 1   | User Account | admin   | V       | X          | Login               | OemClearLog           | 
|    |          |     |              |         |         |            | ConfigureManager    | OemPowerControl       | 
|    |          |     |              |         |         |            | ConfigureUsers      | OemAccessVirtualMedia | 
|    |          |     |              |         |         |            | ConfigureSelf       | SNMPAccess            | 
|    |          |     |              |         |         |            | ConfigureComponents |                       | 
+----+----------+-----+--------------+---------+---------+------------+---------------------+-----------------------+
| 2  | monitor  | 2   | User Account | user    | V       | X          | Login               | OemClearLog           | 
|    |          |     |              |         |         |            |                     | OemPowerControl       | 
|    |          |     |              |         |         |            |                     | OemAccessVirtualMedia | 
|    |          |     |              |         |         |            |                     | SNMPAccess            | 
+----+----------+-----+--------------+---------+---------+------------+---------------------+-----------------------+

View: access, account, bios, cpu, fan, gpu, hw, identity (def), mem, net, pci, power, psu, role, storage, thermal, all
```

[[Back]](./README.md)