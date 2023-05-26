# Tenant

Get the list of tenants with related policies count. Use specific policy commands with '--tenant' filtering rule to get the per-tenant policy details.

```
# iserver get aci tenant --apic apic21

Apic: apic21

+------------------+-------------+-----+---------------+-----+-------+-------+---------------+----------+----------+
| Name             | App Profile | EPG | Bridge Domain | VRF | L2Out | L3Out | MPLS-SR L3Out | Contract | Endpoint |
+------------------+-------------+-----+---------------+-----+-------+-------+---------------+----------+----------+
| common           | 3           | 2   | 4             | 5   | 1     | 0     | 0             | 7        | 2        | 
| hefernan_ni-demo | 1           | 2   | 2             | 1   | 0     | 0     | 0             | 2        | 0        | 
| infra            | 2           | 2   | 2             | 2   | 0     | 0     | 0             | 0        | 0        | 
| k8s              | 1           | 19  | 14            | 2   | 1     | 0     | 0             | 3        | 50       | 
| mgmt             | 1           | 2   | 3             | 4   | 0     | 0     | 0             | 1        | 2        | 
| nidemo           | 1           | 4   | 4             | 1   | 0     | 0     | 0             | 4        | 7        | 
| SPN_IntraLab     | 1           | 1   | 1             | 1   | 0     | 0     | 0             | 0        | 0        | 
| TESTING_BRUNO    | 2           | 2   | 2             | 1   | 0     | 0     | 0             | 1        | 0        | 
| Testing_MSO      | 0           | 0   | 0             | 0   | 0     | 0     | 0             | 0        | 0        | 
| ttrabatt-test    | 0           | 0   | 0             | 0   | 0     | 0     | 0             | 0        | 0        | 
| vEPC             | 1           | 1   | 2             | 2   | 0     | 0     | 0             | 1        | 1        | 
| vEPC_demo        | 1           | 4   | 4             | 3   | 0     | 0     | 0             | 3        | 8        | 
+------------------+-------------+-----+---------------+-----+-------+-------+---------------+----------+----------+
```

[[Back]](./README.md)