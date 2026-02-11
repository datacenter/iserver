# Network Interface Template

[[Next]](./TemplatePci.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v net

+----+--------+--------------------+-------------------+-------------------+
| ID | Net Id | Name               | BIA               | MAC               |
+----+--------+--------------------+-------------------+-------------------+
| 1  | 3.1    | Ethernet Interface | aa:bb:cc:ee:2c:30 | aa:bb:cc:ee:2c:30 |
| 2  | 3.2    | Ethernet Interface | aa:bb:cc:ee:2c:31 | aa:bb:cc:ee:2c:31 |
| 3  | 6.1    | Ethernet Interface | aa:bb:cc:ee:2d:60 | aa:bb:cc:ee:2d:60 |
| 4  | 6.2    | Ethernet Interface | aa:bb:cc:ee:2d:61 | aa:bb:cc:ee:2d:61 |
| 5  | L.1    | Ethernet Interface | aa:bb:cc:26:37:b2 | aa:bb:cc:26:37:b2 |
| 6  | L.2    | Ethernet Interface | aa:bb:cc:26:37:b3 | aa:bb:cc:26:37:b3 |
| 7  | MLOM.0 | Ethernet Interface | aa:bb:cc:CC:0E:3E | aa:bb:cc:CC:0E:3E |
| 8  | MLOM.1 | Ethernet Interface | aa:bb:cc:CC:0E:40 | aa:bb:cc:CC:0E:40 |
| 9  | MLOM.2 | Ethernet Interface | aa:bb:cc:CC:0E:3F | aa:bb:cc:CC:0E:3F |
| 10 | MLOM.3 | Ethernet Interface | aa:bb:cc:CC:0E:41 | aa:bb:cc:CC:0E:41 |
+----+--------+--------------------+-------------------+-------------------+
```

[[Back]](./README.md)