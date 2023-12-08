# Device

## Show devices

Use '--show-password' option to get the passwords.

```
# iserver get nx device

+-------+-------------------------+----------+----------+--------+
| Name  | IP                      | Username | Password | Domain |
+-------+-------------------------+----------+----------+--------+
| ipn11 | ipn11.emea-sp.cisco.com | akaliwod | ******   | milan  |
| ipn12 | ipn12.emea-sp.cisco.com | akaliwod | ******   | milan  |
| ipn13 | ipn13.emea-sp.cisco.com | akaliwod | ******   | milan  |
| ipn14 | ipn14.emea-sp.cisco.com | akaliwod | ******   | milan  |
| ipn21 | ipn21.emea-sp.cisco.com | akaliwod | ******   | milan  |
| ipn22 | ipn22.emea-sp.cisco.com | akaliwod | ******   | milan  |
| ipn25 | ipn25.emea-sp.cisco.com | akaliwod | ******   | milan  |
| ipn26 | ipn26.emea-sp.cisco.com | akaliwod | ******   | milan  |
+-------+-------------------------+----------+----------+--------+
```

Devices can be tagged with domain. You can run nx commands for group of devices by using --device dom:domain-name parameter.

## Add device

Domain (--domain) is optional.

```
# iserver set nx device --name test --ip 10.1.1.1 --username admin --password secret --domain lab
[ERROR] Failed to connect to Nexus device. Continue?
Continue [Y/N]? y
Nexus device entry created: test
```

## Delete device

```
# iserver delete nx device --name test
Nexus device deleted: test
```

[[Back]](./README.md)