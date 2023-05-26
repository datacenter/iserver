
# Controller

## Show Defined Controllers

Use '--show-password' option to get the passwords.

```
# iserver get aci controller

+----------+---------------------------+--------------------------+----------+--------+
| Name     | IP                        | Username                 | Password | Domain |
+----------+---------------------------+--------------------------+----------+--------+
| apic11   | apic11o.emea-sp.cisco.com | admin                    | ******   | milan  |
| apic21   | apic21o.emea-sp.cisco.com | admin                    | ******   | milan  |
| krk-mpod | 10.62.188.10              | apic#Local\\fwardzic-acc | ******   |        |
+----------+---------------------------+--------------------------+----------+--------+
```

## Add Controller

```
# iserver set aci controller --name test --ip 10.1.1.1 --username admin --password secret
APIC entry created: test
```

## Delete Controller

```
# iserver delete aci controller --name test
APIC entry deleted: test
```

[[Back]](./README.md)