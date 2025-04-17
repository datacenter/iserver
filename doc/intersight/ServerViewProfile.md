# Intersight Server

## profile view

```
# iserver get server --group test -v profile

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Profile [#1]
------------

+-----------+---------+------------+--------------------------+-----------------+-------------+----------------------------+--------------------------+--------+---------+
| Server    | Profile | State      | Last Modified            | Target Platform | Policy Name | Class Id                   | Modification Time        | Shared | In Sync |
+-----------+---------+------------+--------------------------+-----------------+-------------+----------------------------+--------------------------+--------+---------+
| Server909 | profile | Associated | 2025-01-01T00:00:00.000Z | Standalone      | Name-57     | bios.Policy                | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-68     | storage.StoragePolicy      | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-85     | vnic.LanConnectivityPolicy | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-28     | adapter.ConfigPolicy       | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-69     | boot.PrecisionPolicy       | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-82     | networkconfig.Policy       | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-57     | smtp.Policy                | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-90     | deviceconnector.Policy     | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-45     | ssh.Policy                 | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-56     | syslog.Policy              | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-92     | iam.EndPointUserPolicy     | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-67     | ipmioverlan.Policy         | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-68     | ntp.Policy                 | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-90     | iam.LdapPolicy             | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-84     | thermal.Policy             | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-16     | kvm.Policy                 | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-61     | firmware.Policy            | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-96     | sol.Policy                 | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-68     | snmp.Policy                | 2025-01-01T00:00:00.000Z | True   | True    |
+-----------+---------+------------+--------------------------+-----------------+-------------+----------------------------+--------------------------+--------+---------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)