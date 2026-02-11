# Power Template

[[Next]](./TemplatePsu.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v power

Power Consumption (Watt)
------------------------
- Current      : 324
- Min          : 320
- Average      : 346
- Max          : 520
- Limit action : NoAction


+----+----------------+---------+--------+-------+-----------------+
| ID | Sensor Name    | State   | Health | Volts | Upper Threshold |
+----+----------------+---------+--------+-------+-----------------+
| 1  | PSU1_VOUT      | Enabled | OK     | 12.1  | 14              | 
| 2  | PSU2_VOUT      | Enabled | OK     | 12.2  | 14              |
| 3  | P12V           | Enabled | OK     | 11.89 | 13.166          |
| 4  | P3V_BAT_SCALED | Enabled | OK     | 3.026 | 3.588           |
+----+----------------+---------+--------+-------+-----------------+

+----+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| ID | PSU Name | State   | Health | Serial      | Firmware | Output (Watt) | Input (Watt) | Max (V) | Min (V) | Max (Hz) | Min (Hz) |
+----+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+
| 1  | PSU1     | Enabled | OK     | Serial1234  | 1111     | 150           | 173          | 264     | 180     | 63       | 47       |
| 2  | PSU2     | Enabled | OK     | Serial1234  | 1111     | 155           | 170          | 264     | 180     | 63       | 47       |
+----+----------+---------+--------+-------------+----------+---------------+--------------+---------+---------+----------+----------+

View: access, account, bios, cpu, fan, gpu, hw, identity (def), mem, net, pci, power, psu, role, storage, thermal, all
```

[[Back]](./README.md)