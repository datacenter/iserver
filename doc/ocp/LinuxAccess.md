# Linux Access

Day2 operations that run on Linux level use CLI commands executed via SSH. The connection to Linux server is abstracted with `connector`.

## Get connectors

```
# iserver get linux connector

+----+------------+--------------+----------+----------+-------------------------------+
| ID | Name       | Address      | Username | Password | Key                           |
+----+------------+--------------+----------+----------+-------------------------------+
| 1  | ocp-bm1    | 10.10.10.10  | core     | --       | C:\Users\user\.ssh\id_ed25519 | 
+----+------------+--------------+----------+----------+-------------------------------+
```

## Set connector

```
# iserver set linux connector --name test --ip 10.10.10.11 --username user --password pass
```

```
# iserver set linux connector
Connector name: test
IP: 10.10.10.11
Username: user
Password: pass

+----+------------+--------------+----------+----------+-------------------------------+
| ID | Name       | Address      | Username | Password | Key                           |
+----+------------+--------------+----------+----------+-------------------------------+
| 1  | ocp-bm1    | 10.10.10.10  | core     | --       | C:\Users\user\.ssh\id_ed25519 | 
| 2  | test       | 10.10.10.11  | user     | ******   | --                            | 
+----+------------+--------------+----------+----------+-------------------------------+
```

## Delete connector

```
# iserver delete linux connector --name test
```

```
# iserver delete linux connector

+----+------------+--------------+----------+----------+-------------------------------+
| ID | Name       | Address      | Username | Password | Key                           |
+----+------------+--------------+----------+----------+-------------------------------+
| 1  | ocp-bm1    | 10.10.10.10  | core     | --       | C:\Users\user\.ssh\id_ed25519 | 
| 2  | test       | 10.10.10.11  | user     | ******   | --                            | 
+----+------------+--------------+----------+----------+-------------------------------+
Connector name: test
Server test deleted

+----+------------+--------------+----------+----------+-------------------------------+
| ID | Name       | Address      | Username | Password | Key                           |
+----+------------+--------------+----------+----------+-------------------------------+
| 1  | ocp-bm1    | 10.10.10.10  | core     | --       | C:\Users\user\.ssh\id_ed25519 | 
+----+------------+--------------+----------+----------+-------------------------------+
```

[[Back]](./Operations.md)