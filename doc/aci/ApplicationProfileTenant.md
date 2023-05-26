# Application Profile (AP)

## Filter by application profile's tenant name

```
# iserver get aci ap --apic apic21 --tenant common

Apic: apic21

+---------------------+--------------------+-------------+
| Application Profile | Application EPGs   | Priority    |
+---------------------+--------------------+-------------+
| common/default      |                    | unspecified | 
+---------------------+--------------------+-------------+
| common/privIP_TEST  | common/privIP_TEST | unspecified | 
+---------------------+--------------------+-------------+
| common/Test_ANP     | common/Test_EPG    | unspecified | 
+---------------------+--------------------+-------------+
```

[[Back]](./ApplicationProfile.md)