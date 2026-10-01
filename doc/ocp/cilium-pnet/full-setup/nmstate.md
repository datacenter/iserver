```
iserver set ocp nmstate --mode all --fw --keep-nncp --skip-down --no-confirm
```

```
[
  {
    "nmstate": {
      "operator": {},
      "instance": {},
      "lldp": {
        "enable": true,
        "fw": true,
        "keep-nncp": false,
        "skip-down": true
      }
    }
  }
]
```

Expected 

```
python.exe .\iserver.py get k8s nns -v lldp --name bm3-1
Cluster: bm3 (type: ocp)
|
+----+-------+------------+-------------------+-------+------+-------------------+---------------+
| ID | Node  | Ethernet   | MAC               | State | LLDP | Nei System        | Nei Interface |
+----+-------+------------+-------------------+-------+------+-------------------+---------------+
| 1  | bm3-1 | eno1       | D4:AD:BD:93:82:D2 | ✗     | ✗    |                  |               | 
| 2  | bm3-1 | eno2       | D4:AD:BD:93:82:D3 | ✗     | ✗    |                  |               | 
| 3  | bm3-1 | eno5       | 3C:57:31:CC:0D:B6 | ✓     | ✓    | leaf1.domain.com | Ethernet1/15  | 
| 4  | bm3-1 | eno6       | 3C:57:31:CC:0D:B7 | ✓     | ✓    | leaf2.domain.com | Ethernet1/15  | 
| 5  | bm3-1 | eno7       | 3C:57:31:CC:0D:B8 | ✓     | ✓    | leaf3.domain.com | Eth1/2/1      | 
| 6  | bm3-1 | eno8       | 3C:57:31:CC:0D:B8 | ✓     | ✓    | leaf4.domain.com | Eth1/2/1      | 
| 7  | bm3-1 | enp216s0f0 | 3C:FD:FE:EE:2E:4C | ✓     | ✓    | leaf3.domain.com | Eth1/4/1      | 
| 8  | bm3-1 | enp216s0f1 | 3C:FD:FE:EE:2E:4D | ✓     | ✓    | leaf3.domain.com | Eth1/6/1      | 
| 9  | bm3-1 | ens1f0     | 3C:FD:FE:EE:2D:08 | ✓     | ✓    | leaf4.domain.com | Eth1/4/1      | 
| 10 | bm3-1 | ens1f1     | 3C:FD:FE:EE:2D:09 | ✓     | ✓    | leaf4.domain.com | Eth1/6/1      | 
+----+-------+------------+-------------------+-------+------+-------------------+---------------+
```