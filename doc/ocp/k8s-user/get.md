# User - Get

## Workflow

- get all `User`, `Identity` and `Group` objects
- prepare combined data for output

## Configurable options

```
# iserver get k8s user
  --cluster TEXT                  Cluster name
  --name TEXT                     Filter by name
  --group TEXT                    Filter by group
  --provider TEXT                 Filter by provider
```

## Example

```
# iserver get k8s group --cluster bm1 --provider ldap
Cluster: bm1 (type: ocp)

+----+---------------------+--------------------+-------+------------------+---------------+---------------+
| ID | User                | Full Name          | Group | Identity         | Provider Name | Provider User |
+----+---------------------+--------------------+-------+------------------+---------------+---------------+
| 1  | xxx@domain.com      | XXX                | EMEA  | ldap:YWthbGl3b2Q | ldap          | YWthbGl3b2Q   |
| 3  | test1@domain.com    | test 1             | ---   | ldap:dGVzdDE     | ldap          | dGVzdDE       | 
| 4  | test2@domain.com    | test 2             | ---   | ldap:dGVzdDI     | ldap          | dGVzdDI       |
+----+---------------------+--------------------+-------+------------------+---------------+---------------+
```

[[Back]](./README.md)