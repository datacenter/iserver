# Application Endpoint Group (EPG)

## Filter by EPG's subnet

EPGs associated with bridge domain with IP subnet that contains provided IP subnet will be shown.

```
# iserver get aci epg --apic apic21 --subnet 10.58.24.206/28

Apic: apic21

+----+--------------------+---------------+-----------------+-----------+----------+
| Up | EPG                | Bridge Domain | Subnets         | Endpoints | Contract |
+----+--------------------+---------------+-----------------+-----------+----------+
| V  | k8s/k8s_ANP/vk8s_3 | k8s/vk8s_3_BD | 10.58.24.206/28 | 8         | V        | 
+----+--------------------+---------------+-----------------+-----------+----------+
```

[[Back]](./ApplicationEpg.md)