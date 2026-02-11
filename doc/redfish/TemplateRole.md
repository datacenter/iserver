# Role Template

[[Next]](./TemplateStorage.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v role

+----+---------------+---------------+---------------------+---------------------+-----------------------+----------+
| ID | Role          | RID           | Description         | Role Privileges     | Role Oem Privileges   | Members  |
+----+---------------+---------------+---------------------+---------------------+-----------------------+----------+
| 1  | admin         | admin         | Admin User Role     | Login               | OemClearLog           | admin    | 
|    |               |               |                     | ConfigureManager    | OemPowerControl       |          | 
|    |               |               |                     | ConfigureUsers      | OemAccessVirtualMedia |          | 
|    |               |               |                     | ConfigureSelf       | SNMPAccess            |          | 
|    |               |               |                     | ConfigureComponents |                       |          | 
+----+---------------+---------------+---------------------+---------------------+-----------------------+----------+
| 2  | readonly      | readonly      | ReadOnly User Role  | Login               | SNMPAccess            | ---      | 
+----+---------------+---------------+---------------------+---------------------+-----------------------+----------+
| 3  | user          | user          | User Role           | Login               | OemClearLog           | monitor  |
|    |               |               |                     |                     | OemPowerControl       |          |
|    |               |               |                     |                     | OemAccessVirtualMedia |          |
|    |               |               |                     |                     | SNMPAccess            |          |
+----+---------------+---------------+---------------------+---------------------+-----------------------+----------+
| 4  | SNMPOnly      | SNMPOnly      | Only access to SNMP | ---                 | SNMPAccess            | ---      |
+----+---------------+---------------+---------------------+---------------------+-----------------------+----------+
| 5  | Administrator | Administrator | Administrator role  | Login               | ---                   | ---      |
|    |               |               |                     | ConfigureManager    |                       |          |
|    |               |               |                     | ConfigureUsers      |                       |          |
|    |               |               |                     | ConfigureSelf       |                       |          |
|    |               |               |                     | ConfigureComponents |                       |          | 
+----+---------------+---------------+---------------------+---------------------+-----------------------+----------+
| 6  | Operator      | Operator      | Operator role       | Login               | ---                   | ---      |
|    |               |               |                     | ConfigureSelf       |                       |          |
|    |               |               |                     | ConfigureComponents |                       |          |
+----+---------------+---------------+---------------------+---------------------+-----------------------+----------+
| 7  | ReadOnly      | ReadOnly      | ReadOnly role       | Login               | ---                   | ---      |
|    |               |               |                     | ConfigureSelf       |                       |          |
+----+---------------+---------------+---------------------+---------------------+-----------------------+----------+

View: access, account, bios, cpu, fan, gpu, hw, identity (def), mem, net, pci, power, psu, role, storage, thermal, all
```

[[Back]](./README.md)