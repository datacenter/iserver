# Intersight Server

## power view

```
# iserver get server
    --group test-env -v power
    --iaccount demo
    --ttl 0
    --anonymize

iaccount demo (cache: any)
Select servers...
Selected servers: 2
Collect server api objects...


Power Consumption [#2]
----------------------

+-----------+---------+-----+---------+-----+--------------+
| Server    | Current | Min | Average | Max | Limit action |
+-----------+---------+-----+---------+-----+--------------+
| Server259 | 324     | 182 | 323     | 563 | NoAction     |
| Server943 | 216     | 175 | 214     | 374 | NoAction     |
+-----------+---------+-----+---------+-----+--------------+

Power Sensor [#8]
-----------------

+-----------+----------------+---------+--------+--------+-----------------+
| Server    | Sensor Name    | State   | Health | Volts  | Upper Threshold |
+-----------+----------------+---------+--------+--------+-----------------+
| Server259 | PSU1_VOUT      | Enabled | OK     | 12.2   | 14              |
| Server259 | PSU2_VOUT      | Enabled | OK     | 12.2   | 14              |
| Server259 | P12V           | Enabled | OK     | 11.774 | 13.166          |
| Server259 | P3V_BAT_SCALED | Enabled | OK     | 3.026  | 3.588           |
| Server943 | PSU1_VOUT      | Enabled | OK     | 12.1   | 14              |
| Server943 | PSU2_VOUT      | Enabled | OK     | 12.2   | 14              |
| Server943 | P12V           | Enabled | OK     | 11.832 | 13.166          |
| Server943 | P3V_BAT_SCALED | Enabled | OK     | 3.042  | 3.588           |
+-----------+----------------+---------+--------+--------+-----------------+

Power Supply [#4]
-----------------

+-----------+----------+---------+--------+-------------+------------+---------------+--------------+---------+---------+----------+----------+
| Server    | PSU Name | State   | Health | Serial      | Firmware   | Output (Watt) | Input (Watt) | Max (V) | Min (V) | Max (Hz) | Min (Hz) |
+-----------+----------+---------+--------+-------------+------------+---------------+--------------+---------+---------+----------+----------+
| Server259 | PSU1     | Enabled | OK     | Serial259   | Version-24 | 159           | 175          | 264     | 180     | 63       | 47       |
| Server259 | PSU2     | Enabled | OK     | Serial259   | Version-43 | 144           | 170          | 264     | 180     | 63       | 47       |
| Server943 | PSU1     | Enabled | OK     | Serial943   | Version-94 | 102           | 115          | 264     | 180     | 63       | 47       |
| Server943 | PSU2     | Enabled | OK     | Serial943   | Version-13 | 94            | 111          | 264     | 180     | 63       | 47       |
+-----------+----------+---------+--------+-------------+------------+---------------+--------------+---------+---------+----------+----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)