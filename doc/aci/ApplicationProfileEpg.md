# Application Profile (AP)

## Filter by application profiles's epg name

```
# iserver get aci ap --apic apic21 --epg *epg*

Apic: apic21

+----------------------+-----------------------+-------------+
| Application Profile  | Application EPGs      | Priority    |
+----------------------+-----------------------+-------------+
| common/Test_ANP      | common/Test_EPG       | unspecified | 
+----------------------+-----------------------+-------------+
| hefernan_ni-demo/APP | hefernan_ni-demo/EPG1 | unspecified | 
|                      | hefernan_ni-demo/EPG2 |             | 
+----------------------+-----------------------+-------------+
| vEPC_demo/vEPG_ANP   | vEPC_demo/vEPG_ACC    | unspecified | 
|                      | vEPC_demo/vEPG_CTRL   |             | 
|                      | vEPC_demo/vEPG_INT    |             | 
|                      | vEPC_demo/vEPG_MGMT   |             | 
+----------------------+-----------------------+-------------+
```

[[Back]](./ApplicationProfile.md)