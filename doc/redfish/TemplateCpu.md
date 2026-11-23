# CPU Template

[[Next]](./TemplateFan.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v cpu

+----+--------+--------+---------+------------------------------------------+-------+---------+------+-------------+----------------------+-------------+------+
| Id | Socket | Health | State   | Model                                    | Cores | Threads | Arch | Instruction | Manufacturer         | Speed [MHz] | Step |
+----+--------+--------+---------+------------------------------------------+-------+---------+------+-------------+----------------------+-------------+------+
| 1  | CPU1   | OK     | Enabled | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | 20    | 40      | x86  | x86-64      | Intel(R) Corporation | 4000        | 7    |
| 2  | CPU2   | OK     | Enabled | Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz | 20    | 40      | x86  | x86-64      | Intel(R) Corporation | 4000        | 7    |
+----+--------+--------+---------+------------------------------------------+-------+---------+------+-------------+----------------------+-------------+------+
```

[[Back]](./README.md)