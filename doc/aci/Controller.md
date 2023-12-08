# Controller

## Show controllers

Use '--show-password' option to get the passwords.

```
# iserver get aci controller

+----------+---------------------------+--------------------------+----------+--------+
| Name     | IP                        | Username                 | Password | Domain |
+----------+---------------------------+--------------------------+----------+--------+
| apic11   | apic11o.emea-sp.cisco.com | admin                    | ******   | milan  |
| apic21   | apic21o.emea-sp.cisco.com | admin                    | ******   | milan  |
+----------+---------------------------+--------------------------+----------+--------+
```

Controlles can be tagged with domain. You can run aci commands for group of controllers by using --apic dom:domain-name parameter.

## Add controller

Domain (--domain) is optional.

```
# iserver set aci controller --name test --ip 10.1.1.1 --username admin --password secret --domain lab
APIC entry created: test
```

## Delete controller

```
# iserver delete aci controller --name test
APIC entry deleted: test
```

[[Back]](./README.md)