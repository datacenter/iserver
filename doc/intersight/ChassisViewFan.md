# Intersight Chassis

## fan view

```
# iserver get chassis --name ucsx -v fan

iaccount demo (cache: any)
Select chassis...
Selected chassis: 1
Collect chassis api objects...

Fan [#8]
--------

+------------+----------------------+----------+----------+-------+---------------+--------+-------------+
| Chassis    | Fan                  | Control  | Presence | State | Model         | Serial | Part Number |
+------------+----------------------+----------+----------+-------+---------------+--------+-------------+
| Chassis610 | Fan Module 1 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-66  | PN-31       |
| Chassis610 | Fan Module 1 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-23  | PN-72       |
| Chassis610 | Fan Module 2 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-16  | PN-79       |
| Chassis610 | Fan Module 2 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-10  | PN-66       |
| Chassis610 | Fan Module 3 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-95  | PN-64       |
| Chassis610 | Fan Module 3 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-74  | PN-66       |
| Chassis610 | Fan Module 4 - Fan 1 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-26  | PN-45       |
| Chassis610 | Fan Module 4 - Fan 2 | Acoustic | equipped | OK    | UCSX-9508-FAN | SN-58  | PN-28       |
+------------+----------------------+----------+----------+-------+---------------+--------+-------------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

[[Back]](./ChassisInventory.md)