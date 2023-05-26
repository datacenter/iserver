# Application Endpoint Group (EPG)

## Filter by associated bridge domain IP address

EPGs associated with bridge domain with IP subnet that contains provided IP address will be shown.

```
# iserver get aci epg --apic apic21 --ip 10.58.24.209

Apic: apic21

+----+--------------------+---------------+-----------------+-----------+----------+
| Up | EPG                | Bridge Domain | Subnets         | Endpoints | Contract |
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_4 | k8s/vk8s_4_BD | 10.58.24.222/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
```

[[Back]](./ApplicationEpg.md)