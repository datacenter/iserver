# ACI Fabric - Data model

## Connector

Connector is the name type:string reference to internal authentication definition of REST API access to APIC. It must refer to existing controller

### View connectors

```
# iserver get aci controller

+-------------+---------------------------+------+----------+----------+
| Name        | IP                        | Port | Username | Password |
+-------------+---------------------------+------+----------+----------+
| apic1       | apic1.domain.com          | 443  | admin    | ******   |
| apic2       | apic2.domain.com          | 443  | admin    | ******   |
+-------------+---------------------------+------+----------+----------+
```

### Add connector

```
# iserver set aci controller --name apic1 --ip apic1.domain.com --port 443 --username admin --password secret
```

### Delete connector

```
# iserver delete aci controller --name apic1
```