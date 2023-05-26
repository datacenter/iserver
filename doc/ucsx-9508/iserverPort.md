# UCSX-9508 IFM port monitoring with iserver

Use '-p|--port' option with '.|*|all' value to select all ports on all IFMs.

```
# iserver get chassis --serial FOX2611PPHP -p .

+------------------+-------+------------+---------+--------+--------+---------------+---------------+--------------------------------------------+
| I/O Module       | Path  | Host Port  | Mode    | Speed  | State  | State Qual    | Port Channel  | Peer Info                                  |
+------------------+-------+------------+---------+--------+--------+---------------+---------------+--------------------------------------------+
| IFM #1 (top)     | B     | 1/1/1      | vntag   | auto   | down   | link-failure  | 1283          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)     | B     | 1/1/2      | vntag   | auto   | down   | link-failure  | 1283          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)     | B     | 1/1/3      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/4      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/5      | vntag   | auto   | down   | link-failure  | 1280          | Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)     | B     | 1/1/6      | vntag   | auto   | down   | link-failure  | 1280          | Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)     | B     | 1/1/7      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/8      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/9      | vntag   | auto   | down   | link-failure  | 1281          | Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)     | B     | 1/1/10     | vntag   | auto   | down   | link-failure  | 1281          | Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)     | B     | 1/1/11     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/12     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/13     | vntag   | auto   | down   | link-failure  | 1282          | Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)     | B     | 1/1/14     | vntag   | auto   | down   | link-failure  | 1282          | Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)     | B     | 1/1/15     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/16     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/17     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/18     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/19     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/20     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/21     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/22     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/23     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/24     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/25     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/26     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/27     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/28     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/29     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/30     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/31     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/32     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)     | B     | 1/1/33     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/1      | vntag   | auto   | down   | link-failure  | 1287          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #2 (bottom)  | A     | 1/1/2      | vntag   | auto   | down   | link-failure  | 1287          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #2 (bottom)  | A     | 1/1/3      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/4      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/5      | vntag   | auto   | down   | link-failure  | 1284          | Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #2 (bottom)  | A     | 1/1/6      | vntag   | auto   | down   | link-failure  | 1284          | Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #2 (bottom)  | A     | 1/1/7      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/8      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/9      | vntag   | auto   | down   | link-failure  | 1285          | Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #2 (bottom)  | A     | 1/1/10     | vntag   | auto   | down   | link-failure  | 1285          | Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #2 (bottom)  | A     | 1/1/11     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/12     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/13     | vntag   | auto   | down   | link-failure  | 1286          | Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #2 (bottom)  | A     | 1/1/14     | vntag   | auto   | down   | link-failure  | 1286          | Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #2 (bottom)  | A     | 1/1/15     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/16     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/17     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/18     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/19     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/20     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/21     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/22     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/23     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/24     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/25     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/26     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/27     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/28     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/29     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/30     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/31     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/32     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #2 (bottom)  | A     | 1/1/33     | access  | auto   | down   | admin-down    | 0             |                                            | 
+------------------+-------+------------+---------+--------+--------+---------------+---------------+--------------------------------------------+

+------------------+---------------+--------+------------+--------------+----------------------+---------------------+--------------------+
| I/O Module       | Network Port  | Speed  | Switch ID  | Switch Port  | Switch Port Channel  | Switch Transceiver  | Switch Port Speed  |
+------------------+---------------+--------+------------+--------------+----------------------+---------------------+--------------------+
| IFM #1 (top)     | 1/1           | 10G    | B          | 1/17         | 1153                 | SFP-25G-AOC2M       | 25G                | 
| IFM #1 (top)     | 1/2           | 10G    | B          | 1/19         | 1153                 | SFP-25G-AOC2M       | 25G                | 
| IFM #1 (top)     | 1/3           | 10G    | B          | 1/21         | 1153                 | SFP-25G-AOC2M       | 25G                | 
| IFM #1 (top)     | 1/4           | 10G    | B          | 1/23         | 1153                 | SFP-25G-AOC2M       | 25G                | 
| IFM #2 (bottom)  | 2/1           | 10G    | A          | 1/17         | 1025                 | SFP-25G-AOC2M       | 25G                | 
| IFM #2 (bottom)  | 2/2           | 10G    | A          | 1/19         | 1025                 | SFP-25G-AOC2M       | 25G                | 
| IFM #2 (bottom)  | 2/3           | 10G    | A          | 1/21         | 1025                 | SFP-25G-AOC2M       | 25G                | 
| IFM #2 (bottom)  | 2/4           | 10G    | A          | 1/23         | 1025                 | SFP-25G-AOC2M       | 25G                | 
+------------------+---------------+--------+------------+--------------+----------------------+---------------------+--------------------+
```

## Show host ports only

Use '-p t:host' option to select only host (backplane) ports. Use '-m' option to further select single IFM.

```
# iserver get chassis --serial FOX2611PPHP -p m:b -p t:host

+---------------+-------+------------+---------+--------+--------+---------------+---------------+--------------------------------------------+
| I/O Module    | Path  | Host Port  | Mode    | Speed  | State  | State Qual    | Port Channel  | Peer Info                                  |
+---------------+-------+------------+---------+--------+--------+---------------+---------------+--------------------------------------------+
| IFM #1 (top)  | B     | 1/1/1      | vntag   | auto   | down   | link-failure  | 1283          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/2      | vntag   | auto   | down   | link-failure  | 1283          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/3      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/4      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/5      | vntag   | auto   | down   | link-failure  | 1280          | Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/6      | vntag   | auto   | down   | link-failure  | 1280          | Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/7      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/8      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/9      | vntag   | auto   | down   | link-failure  | 1281          | Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/10     | vntag   | auto   | down   | link-failure  | 1281          | Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/11     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/12     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/13     | vntag   | auto   | down   | link-failure  | 1282          | Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/14     | vntag   | auto   | down   | link-failure  | 1282          | Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/15     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/16     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/17     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/18     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/19     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/20     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/21     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/22     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/23     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/24     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/25     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/26     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/27     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/28     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/29     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/30     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/31     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/32     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/33     | access  | auto   | down   | admin-down    | 0             |                                            | 
+---------------+-------+------------+---------+--------+--------+---------------+---------------+--------------------------------------------+
```

## Show network ports only

Use '-p t:net' option to select only network (fabric) ports. Use '-m' option to further select single IFM.

```
# iserver get chassis --serial FOX2611PPHP -p m:a -p t:net

+------------------+---------------+--------+------------+--------------+----------------------+---------------------+--------------------+
| I/O Module       | Network Port  | Speed  | Switch ID  | Switch Port  | Switch Port Channel  | Switch Transceiver  | Switch Port Speed  |
+------------------+---------------+--------+------------+--------------+----------------------+---------------------+--------------------+
| IFM #1 (top)     | 1/1           | 10G    | B          | 1/17         | 1153                 | SFP-25G-AOC2M       | 25G                | 
| IFM #1 (top)     | 1/2           | 10G    | B          | 1/19         | 1153                 | SFP-25G-AOC2M       | 25G                | 
| IFM #1 (top)     | 1/3           | 10G    | B          | 1/21         | 1153                 | SFP-25G-AOC2M       | 25G                | 
| IFM #1 (top)     | 1/4           | 10G    | B          | 1/23         | 1153                 | SFP-25G-AOC2M       | 25G                | 
| IFM #2 (bottom)  | 2/1           | 10G    | A          | 1/17         | 1025                 | SFP-25G-AOC2M       | 25G                | 
| IFM #2 (bottom)  | 2/2           | 10G    | A          | 1/19         | 1025                 | SFP-25G-AOC2M       | 25G                | 
| IFM #2 (bottom)  | 2/3           | 10G    | A          | 1/21         | 1025                 | SFP-25G-AOC2M       | 25G                | 
| IFM #2 (bottom)  | 2/4           | 10G    | A          | 1/23         | 1025                 | SFP-25G-AOC2M       | 25G                | 
+------------------+---------------+--------+------------+--------------+----------------------+---------------------+--------------------+
```

## Select ports by module

Use '-p m:1|2|a|b' option to select ports by module.

```
# iserver get chassis --serial FOX2611PPHP -p m:1

+---------------+-------+------------+---------+--------+--------+---------------+---------------+--------------------------------------------+
| I/O Module    | Path  | Host Port  | Mode    | Speed  | State  | State Qual    | Port Channel  | Peer Info                                  |
+---------------+-------+------------+---------+--------+--------+---------------+---------------+--------------------------------------------+
| IFM #1 (top)  | B     | 1/1/1      | vntag   | auto   | down   | link-failure  | 1283          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/2      | vntag   | auto   | down   | link-failure  | 1283          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/3      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/4      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/5      | vntag   | auto   | down   | link-failure  | 1280          | Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/6      | vntag   | auto   | down   | link-failure  | 1280          | Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/7      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/8      | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/9      | vntag   | auto   | down   | link-failure  | 1281          | Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/10     | vntag   | auto   | down   | link-failure  | 1281          | Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/11     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/12     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/13     | vntag   | auto   | down   | link-failure  | 1282          | Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/14     | vntag   | auto   | down   | link-failure  | 1282          | Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)  | B     | 1/1/15     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/16     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/17     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/18     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/19     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/20     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/21     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/22     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/23     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/24     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/25     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/26     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/27     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/28     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/29     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/30     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/31     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/32     | access  | auto   | down   | admin-down    | 0             |                                            | 
| IFM #1 (top)  | B     | 1/1/33     | access  | auto   | down   | admin-down    | 0             |                                            | 
+---------------+-------+------------+---------+--------+--------+---------------+---------------+--------------------------------------------+

+------------------+---------------+--------+------------+--------------+----------------------+---------------------+--------------------+
| I/O Module       | Network Port  | Speed  | Switch ID  | Switch Port  | Switch Port Channel  | Switch Transceiver  | Switch Port Speed  |
+------------------+---------------+--------+------------+--------------+----------------------+---------------------+--------------------+
| IFM #1 (top)     | 1/1           | 10G    | B          | 1/17         | 1153                 | SFP-25G-AOC2M       | 25G                | 
| IFM #1 (top)     | 1/2           | 10G    | B          | 1/19         | 1153                 | SFP-25G-AOC2M       | 25G                | 
| IFM #1 (top)     | 1/3           | 10G    | B          | 1/21         | 1153                 | SFP-25G-AOC2M       | 25G                | 
| IFM #1 (top)     | 1/4           | 10G    | B          | 1/23         | 1153                 | SFP-25G-AOC2M       | 25G                | 
| IFM #2 (bottom)  | 2/1           | 10G    | A          | 1/17         | 1025                 | SFP-25G-AOC2M       | 25G                | 
| IFM #2 (bottom)  | 2/2           | 10G    | A          | 1/19         | 1025                 | SFP-25G-AOC2M       | 25G                | 
| IFM #2 (bottom)  | 2/3           | 10G    | A          | 1/21         | 1025                 | SFP-25G-AOC2M       | 25G                | 
| IFM #2 (bottom)  | 2/4           | 10G    | A          | 1/23         | 1025                 | SFP-25G-AOC2M       | 25G                | 
+------------------+---------------+--------+------------+--------------+----------------------+---------------------+--------------------+
```

## Select ports by node

Use '-p n:<id>' option to select host (fabric) ports connected to node <id>

```
# iserver get chassis --serial FOX2611PPHP -p n:1

+------------------+-------+------------+--------+--------+--------+---------------+---------------+--------------------------------------------+
| I/O Module       | Path  | Host Port  | Mode   | Speed  | State  | State Qual    | Port Channel  | Peer Info                                  |
+------------------+-------+------------+--------+--------+--------+---------------+---------------+--------------------------------------------+
| IFM #1 (top)     | B     | 1/1/1      | vntag  | auto   | down   | link-failure  | 1283          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)     | B     | 1/1/2      | vntag  | auto   | down   | link-failure  | 1283          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #2 (bottom)  | A     | 1/1/1      | vntag  | auto   | down   | link-failure  | 1287          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #2 (bottom)  | A     | 1/1/2      | vntag  | auto   | down   | link-failure  | 1287          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
+------------------+-------+------------+--------+--------+--------+---------------+---------------+--------------------------------------------+
```

## Select ports by state (up or down)

Use '-p s:up|down' option to select ports by state

```
# iserver get chassis --serial FOX2611PPHP -p n:1 -p s:down

+------------------+-------+------------+--------+--------+--------+---------------+---------------+--------------------------------------------+
| I/O Module       | Path  | Host Port  | Mode   | Speed  | State  | State Qual    | Port Channel  | Peer Info                                  |
+------------------+-------+------------+--------+--------+--------+---------------+---------------+--------------------------------------------+
| IFM #1 (top)     | B     | 1/1/1      | vntag  | auto   | down   | link-failure  | 1283          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #1 (top)     | B     | 1/1/2      | vntag  | auto   | down   | link-failure  | 1283          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #2 (bottom)  | A     | 1/1/1      | vntag  | auto   | down   | link-failure  | 1287          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
| IFM #2 (bottom)  | A     | 1/1/2      | vntag  | auto   | down   | link-failure  | 1287          | Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML  | 
+------------------+-------+------------+--------+--------+--------+---------------+---------------+--------------------------------------------+
```

## JSON output

```
# iserver get chassis --serial FOX2611PPHP -p . -o json

{
    "Chassis": {
        "ConnectionPath": "A,B",
        "ConnectionStatus": "A,B",
        "Description": "Cisco Blade Server Chassis, 7U with Eight Vertical Blade Server Slots",
        "Dn": "chassis-1",
        "DeviceMoId": "632999466f72612d39b26942",
        "Moid": "632b13c876752d32362fc175",
        "Model": "UCSX-9508",
        "Name": "ucsX-1",
        "OperState": "OK",
        "PartNumber": "68-6847-03",
        "Pid": "UCSX-9508",
        "ProductName": "Cisco UCSX 9508 Chassis",
        "Serial": "FOX2611PPHP",
        "Sku": "UCSX-9508",
        "Vendor": "Cisco Systems Inc",
        "Health": "Warnings",
        "HealthSummary": "Warnings (2)",
        "AlarmWarning": 2,
        "AlarmCritical": 0,
        "ConnectionSummary": "A,B / A,B",
        "NodeMax": 8,
        "IfmMax": 2,
        "FanModuleMax": 4,
        "FanMax": 8,
        "PsuMax": 6,
        "IfmOn": 2,
        "IfmCount": 2,
        "IfmSummary": "2/2/2",
        "HostPortCount": 66,
        "HostPortUp": 0,
        "HostPortSummary": "0/66",
        "NodePowerOn": 0,
        "NodeCount": 4,
        "NodeSummary": "0/4/8",
        "NetworkPortUp": 8,
        "NetworkPortCount": 8,
        "NetworkPortMax": 16,
        "NetworkPortSummary": "8/8/16"
    },
    "IfmInfo": [
        {
            "Moid": "632b13c976752d32362fc244",
            "Dn": "chassis-1-ioc-1",
            "Model": "UCSX-I-9108-25G",
            "ConnectionPath": "B",
            "ConnectionStatus": "B",
            "Description": "Cisco UCS 9108-25G 8 Port IFM",
            "ManagementIp": "10.90.90.49",
            "ManagementSubnet": "255.255.255.0",
            "ManagementPrefix": 24,
            "ManagementCidr": "10.90.90.49/24",
            "ManagementGateway": "10.90.89.1",
            "ManagementVlan": 89,
            "FanMoids": [
                "632b178c76752d323630ceca",
                "632b178c76752d323630ced9",
                "632b178c76752d323630cee8"
            ],
            "HostPorts": [
                "632b175c6373582d42a02271",
                "632b175c6373582d42a02275",
                "632b175c6373582d42a0227a",
                "632b175c6373582d42a0227d",
                "632b175c6373582d42a02280",
                "632b175c6373582d42a02277",
                "632b175c6373582d42a02272",
                "632b175c6373582d42a0227b",
                "632b175c6373582d42a02286",
                "632b175c6373582d42a02289",
                "632b175c6373582d42a02270",
                "632b175c6373582d42a02274",
                "632b175c6373582d42a02278",
                "632b175c6373582d42a0228b",
                "632b175c6373582d42a0226d",
                "632b175c6373582d42a0226e",
                "632b175c6373582d42a02276",
                "632b175c6373582d42a0227c",
                "632b175c6373582d42a02284",
                "632b175c6373582d42a0226f",
                "632b175c6373582d42a0227f",
                "632b175c6373582d42a02281",
                "632b175c6373582d42a02288",
                "632b175c6373582d42a02273",
                "632b175c6373582d42a02279",
                "632b175c6373582d42a0227e",
                "632b175c6373582d42a02282",
                "632b175c6373582d42a02287",
                "632b175c6373582d42a0228a",
                "632b175c6373582d42a0226c",
                "632b175c6373582d42a02283",
                "632b175c6373582d42a02285",
                "632b1fcc6373582d42a023ab"
            ],
            "NetworkPorts": [
                "632b13c976752d32362fc25a",
                "632c81ec76752d32369daa08",
                "632c81f276752d32369dac8d",
                "632c820576752d32369db290"
            ],
            "NetworkPortMax": 8,
            "Name": "IFM #1 (top)",
            "ModuleId": 1,
            "On": true,
            "OperState": "OK",
            "PartNumber": "73-20533-03",
            "Pid": "UCSX-I-9108-25G",
            "Presence": "equipped",
            "ProductName": "Cisco UCS 9108-25G",
            "Serial": "FCH261770KU",
            "Side": "top",
            "Version": "4.2(2c)",
            "NetworkPortCount": 4,
            "NetworkPortUp": 4,
            "NetworkPortSummary": "4/4/8"
        },
        {
            "Moid": "632b13c876752d32362fc17c",
            "Dn": "chassis-1-ioc-2",
            "Model": "UCSX-I-9108-25G",
            "ConnectionPath": "A",
            "ConnectionStatus": "A",
            "Description": "Cisco UCS 9108-25G 8 Port IFM",
            "ManagementIp": "10.90.90.48",
            "ManagementSubnet": "255.255.255.0",
            "ManagementPrefix": 24,
            "ManagementCidr": "10.90.90.48/24",
            "ManagementGateway": "10.90.89.1",
            "ManagementVlan": 89,
            "FanMoids": [
                "632b15b576752d3236304d3d",
                "632b15b576752d3236304d58",
                "632b15b576752d3236304d6f"
            ],
            "HostPorts": [
                "632b158c6373582d415a5ad6",
                "632b158c6373582d415a5ac0",
                "632b158c6373582d415a5acc",
                "632b158c6373582d415a5abf",
                "632b158c6373582d415a5ac6",
                "632b158c6373582d415a5ac7",
                "632b158c6373582d415a5ad4",
                "632b158c6373582d415a5ad8",
                "632b158c6373582d415a5ac1",
                "632b158c6373582d415a5ac4",
                "632b158c6373582d415a5acf",
                "632b158c6373582d415a5ad2",
                "632b158c6373582d415a5ad3",
                "632b158c6373582d415a5ac9",
                "632b158c6373582d415a5ad5",
                "632b158c6373582d415a5adb",
                "632b158c6373582d415a5ac2",
                "632b158c6373582d415a5ac8",
                "632b158c6373582d415a5add",
                "632b158c6373582d415a5aca",
                "632b158c6373582d415a5acb",
                "632b158c6373582d415a5acd",
                "632b158c6373582d415a5ace",
                "632b158c6373582d415a5ac5",
                "632b158c6373582d415a5ac3",
                "632b158c6373582d415a5ad0",
                "632b158c6373582d415a5adc",
                "632b158c6373582d415a5ad7",
                "632b158c6373582d415a5abe",
                "632b158c6373582d415a5ad1",
                "632b158c6373582d415a5ad9",
                "632b158c6373582d415a5ada",
                "632c6acd6373582d415a8b96"
            ],
            "NetworkPorts": [
                "632b13c876752d32362fc189",
                "632c81e776752d32369da82f",
                "632c81ed76752d32369daa9c",
                "632c81fe76752d32369db10a"
            ],
            "NetworkPortMax": 8,
            "Name": "IFM #2 (bottom)",
            "ModuleId": 2,
            "On": true,
            "OperState": "OK",
            "PartNumber": "73-20533-03",
            "Pid": "UCSX-I-9108-25G",
            "Presence": "equipped",
            "ProductName": "Cisco UCS 9108-25G",
            "Serial": "FCH261770RN",
            "Side": "bottom",
            "Version": "4.2(2c)",
            "NetworkPortCount": 4,
            "NetworkPortUp": 4,
            "NetworkPortSummary": "4/4/8"
        }
    ],
    "HostPortInfo": [
        {
            "Moid": "632b175c6373582d42a02282",
            "Dn": "chassis-1-ioc-1-muxhostport-port-1",
            "Name": "1/1/1",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:83",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316eab",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1283,
            "PortId": 1,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 1
        },
        {
            "Moid": "632b175c6373582d42a02283",
            "Dn": "chassis-1-ioc-1-muxhostport-port-2",
            "Name": "1/1/2",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:84",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316eac",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1283,
            "PortId": 2,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 1
        },
        {
            "Moid": "632b175c6373582d42a02284",
            "Dn": "chassis-1-ioc-1-muxhostport-port-3",
            "Name": "1/1/3",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:85",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 3,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02285",
            "Dn": "chassis-1-ioc-1-muxhostport-port-4",
            "Name": "1/1/4",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:86",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 4,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02286",
            "Dn": "chassis-1-ioc-1-muxhostport-port-5",
            "Name": "1/1/5",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:87",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bc0",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1280,
            "PortId": 5,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 2
        },
        {
            "Moid": "632b175c6373582d42a02287",
            "Dn": "chassis-1-ioc-1-muxhostport-port-6",
            "Name": "1/1/6",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:88",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bc5",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1280,
            "PortId": 6,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 2
        },
        {
            "Moid": "632b175c6373582d42a02288",
            "Dn": "chassis-1-ioc-1-muxhostport-port-7",
            "Name": "1/1/7",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:89",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 7,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02289",
            "Dn": "chassis-1-ioc-1-muxhostport-port-8",
            "Name": "1/1/8",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8A",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 8,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0228a",
            "Dn": "chassis-1-ioc-1-muxhostport-port-9",
            "Name": "1/1/9",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8B",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc5",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1281,
            "PortId": 9,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 3
        },
        {
            "Moid": "632b175c6373582d42a0228b",
            "Dn": "chassis-1-ioc-1-muxhostport-port-10",
            "Name": "1/1/10",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8C",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc6",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1281,
            "PortId": 10,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 3
        },
        {
            "Moid": "632b175c6373582d42a0226c",
            "Dn": "chassis-1-ioc-1-muxhostport-port-11",
            "Name": "1/1/11",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8D",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 11,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0226d",
            "Dn": "chassis-1-ioc-1-muxhostport-port-12",
            "Name": "1/1/12",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8E",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 12,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0226e",
            "Dn": "chassis-1-ioc-1-muxhostport-port-13",
            "Name": "1/1/13",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8F",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee3",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1282,
            "PortId": 13,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 4
        },
        {
            "Moid": "632b175c6373582d42a0226f",
            "Dn": "chassis-1-ioc-1-muxhostport-port-14",
            "Name": "1/1/14",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:90",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee4",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1282,
            "PortId": 14,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 4
        },
        {
            "Moid": "632b175c6373582d42a02270",
            "Dn": "chassis-1-ioc-1-muxhostport-port-15",
            "Name": "1/1/15",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:91",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 15,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02271",
            "Dn": "chassis-1-ioc-1-muxhostport-port-16",
            "Name": "1/1/16",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:92",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 16,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02272",
            "Dn": "chassis-1-ioc-1-muxhostport-port-17",
            "Name": "1/1/17",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:93",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 17,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02273",
            "Dn": "chassis-1-ioc-1-muxhostport-port-18",
            "Name": "1/1/18",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:94",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 18,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02274",
            "Dn": "chassis-1-ioc-1-muxhostport-port-19",
            "Name": "1/1/19",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:95",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 19,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02275",
            "Dn": "chassis-1-ioc-1-muxhostport-port-20",
            "Name": "1/1/20",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:96",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 20,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02276",
            "Dn": "chassis-1-ioc-1-muxhostport-port-21",
            "Name": "1/1/21",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:97",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 21,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02277",
            "Dn": "chassis-1-ioc-1-muxhostport-port-22",
            "Name": "1/1/22",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:98",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 22,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02278",
            "Dn": "chassis-1-ioc-1-muxhostport-port-23",
            "Name": "1/1/23",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:99",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 23,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02279",
            "Dn": "chassis-1-ioc-1-muxhostport-port-24",
            "Name": "1/1/24",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9A",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 24,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0227a",
            "Dn": "chassis-1-ioc-1-muxhostport-port-25",
            "Name": "1/1/25",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9B",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 25,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0227b",
            "Dn": "chassis-1-ioc-1-muxhostport-port-26",
            "Name": "1/1/26",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9C",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 26,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0227c",
            "Dn": "chassis-1-ioc-1-muxhostport-port-27",
            "Name": "1/1/27",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9D",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 27,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0227d",
            "Dn": "chassis-1-ioc-1-muxhostport-port-28",
            "Name": "1/1/28",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9E",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 28,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0227e",
            "Dn": "chassis-1-ioc-1-muxhostport-port-29",
            "Name": "1/1/29",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9F",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 29,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0227f",
            "Dn": "chassis-1-ioc-1-muxhostport-port-30",
            "Name": "1/1/30",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:A0",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 30,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02280",
            "Dn": "chassis-1-ioc-1-muxhostport-port-31",
            "Name": "1/1/31",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:A1",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 31,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02281",
            "Dn": "chassis-1-ioc-1-muxhostport-port-32",
            "Name": "1/1/32",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:A2",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 32,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b1fcc6373582d42a023ab",
            "Dn": "chassis-1-ioc-1-muxhostport-port-33",
            "Name": "1/1/33",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "00:00:00:00:00:00",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 33,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5abe",
            "Dn": "chassis-1-ioc-2-muxhostport-port-1",
            "Name": "1/1/1",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C3",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316ea9",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1287,
            "PortId": 1,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 1
        },
        {
            "Moid": "632b158c6373582d415a5abf",
            "Dn": "chassis-1-ioc-2-muxhostport-port-2",
            "Name": "1/1/2",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C4",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316eaa",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1287,
            "PortId": 2,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 1
        },
        {
            "Moid": "632b158c6373582d415a5ac0",
            "Dn": "chassis-1-ioc-2-muxhostport-port-3",
            "Name": "1/1/3",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C5",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 3,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ac1",
            "Dn": "chassis-1-ioc-2-muxhostport-port-4",
            "Name": "1/1/4",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C6",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 4,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ac2",
            "Dn": "chassis-1-ioc-2-muxhostport-port-5",
            "Name": "1/1/5",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C7",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bb7",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1284,
            "PortId": 5,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac3",
            "Dn": "chassis-1-ioc-2-muxhostport-port-6",
            "Name": "1/1/6",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C8",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bbe",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1284,
            "PortId": 6,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac4",
            "Dn": "chassis-1-ioc-2-muxhostport-port-7",
            "Name": "1/1/7",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C9",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 7,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ac5",
            "Dn": "chassis-1-ioc-2-muxhostport-port-8",
            "Name": "1/1/8",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CA",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 8,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ac6",
            "Dn": "chassis-1-ioc-2-muxhostport-port-9",
            "Name": "1/1/9",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CB",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc3",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1285,
            "PortId": 9,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 3
        },
        {
            "Moid": "632b158c6373582d415a5ac7",
            "Dn": "chassis-1-ioc-2-muxhostport-port-10",
            "Name": "1/1/10",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CC",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc4",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1285,
            "PortId": 10,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 3
        },
        {
            "Moid": "632b158c6373582d415a5ac8",
            "Dn": "chassis-1-ioc-2-muxhostport-port-11",
            "Name": "1/1/11",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CD",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 11,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ac9",
            "Dn": "chassis-1-ioc-2-muxhostport-port-12",
            "Name": "1/1/12",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CE",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 12,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5aca",
            "Dn": "chassis-1-ioc-2-muxhostport-port-13",
            "Name": "1/1/13",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CF",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee1",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1286,
            "PortId": 13,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 4
        },
        {
            "Moid": "632b158c6373582d415a5acb",
            "Dn": "chassis-1-ioc-2-muxhostport-port-14",
            "Name": "1/1/14",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D0",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee2",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1286,
            "PortId": 14,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 4
        },
        {
            "Moid": "632b158c6373582d415a5acc",
            "Dn": "chassis-1-ioc-2-muxhostport-port-15",
            "Name": "1/1/15",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D1",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 15,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5acd",
            "Dn": "chassis-1-ioc-2-muxhostport-port-16",
            "Name": "1/1/16",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D2",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 16,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ace",
            "Dn": "chassis-1-ioc-2-muxhostport-port-17",
            "Name": "1/1/17",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D3",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 17,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5acf",
            "Dn": "chassis-1-ioc-2-muxhostport-port-18",
            "Name": "1/1/18",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D4",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 18,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad0",
            "Dn": "chassis-1-ioc-2-muxhostport-port-19",
            "Name": "1/1/19",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D5",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 19,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad1",
            "Dn": "chassis-1-ioc-2-muxhostport-port-20",
            "Name": "1/1/20",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D6",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 20,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad2",
            "Dn": "chassis-1-ioc-2-muxhostport-port-21",
            "Name": "1/1/21",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D7",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 21,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad3",
            "Dn": "chassis-1-ioc-2-muxhostport-port-22",
            "Name": "1/1/22",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D8",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 22,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad4",
            "Dn": "chassis-1-ioc-2-muxhostport-port-23",
            "Name": "1/1/23",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D9",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 23,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad5",
            "Dn": "chassis-1-ioc-2-muxhostport-port-24",
            "Name": "1/1/24",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DA",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 24,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad6",
            "Dn": "chassis-1-ioc-2-muxhostport-port-25",
            "Name": "1/1/25",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DB",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 25,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad7",
            "Dn": "chassis-1-ioc-2-muxhostport-port-26",
            "Name": "1/1/26",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DC",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 26,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad8",
            "Dn": "chassis-1-ioc-2-muxhostport-port-27",
            "Name": "1/1/27",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DD",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 27,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad9",
            "Dn": "chassis-1-ioc-2-muxhostport-port-28",
            "Name": "1/1/28",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DE",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 28,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ada",
            "Dn": "chassis-1-ioc-2-muxhostport-port-29",
            "Name": "1/1/29",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DF",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 29,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5adb",
            "Dn": "chassis-1-ioc-2-muxhostport-port-30",
            "Name": "1/1/30",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:E0",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 30,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5adc",
            "Dn": "chassis-1-ioc-2-muxhostport-port-31",
            "Name": "1/1/31",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:E1",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 31,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5add",
            "Dn": "chassis-1-ioc-2-muxhostport-port-32",
            "Name": "1/1/32",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:E2",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 32,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632c6acd6373582d415a8b96",
            "Dn": "chassis-1-ioc-2-muxhostport-port-33",
            "Name": "1/1/33",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "00:00:00:00:00:00",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 33,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        }
    ],
    "NodeInfo": [
        {
            "Moid": "632b174e76752d323630bb47",
            "Dn": "/redfish/v1/Systems/FCH26167MMZ",
            "Name": "ucsX-1-1",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167MMZ",
            "HardwareUuid": "8A552335-ED7E-4A28-924D-BE8748DA5BF8",
            "ServiceProfile": "",
            "SlotId": 1,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        },
        {
            "Moid": "632b163d76752d323630734f",
            "Dn": "/redfish/v1/Systems/FCH26167L94",
            "Name": "ucsX-1-2",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167L94",
            "HardwareUuid": "D576BED6-EF35-439C-B088-0735FED04410",
            "ServiceProfile": "",
            "SlotId": 2,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        },
        {
            "Moid": "632b163e76752d32363073aa",
            "Dn": "/redfish/v1/Systems/FCH26167MQK",
            "Name": "ucsX-1-3",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167MQK",
            "HardwareUuid": "0607F131-46C2-4CDC-B237-1F872D01E441",
            "ServiceProfile": "",
            "SlotId": 3,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        },
        {
            "Moid": "632b163f76752d32363073f7",
            "Dn": "/redfish/v1/Systems/FCH26167MHB",
            "Name": "ucsX-1-4",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167MHB",
            "HardwareUuid": "6918688F-1B00-4DDB-A6E3-D316F6D07F64",
            "ServiceProfile": "",
            "SlotId": 4,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        }
    ],
    "AdapterUnitInfo": [
        {
            "Moid": "632b188376752d3236311708",
            "Dn": "/redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0",
            "AdapterId": "UCSX-V4-Q25GML_FCH26217EZ0",
            "BaseMacAddress": "48:2E:72:E4:50:28",
            "ComputeNodeMoid": "632b163d76752d323630734f",
            "ExtEthIfsIds": [
                "632b188b76752d3236311bb7",
                "632b188b76752d3236311bbe",
                "632b188b76752d3236311bc0",
                "632b188b76752d3236311bc5"
            ],
            "Model": "UCSX-V4-Q25GML",
            "OperState": "OK",
            "Presence": "equipped",
            "Healthy": true,
            "Serial": "FCH26217EZ0",
            "PciSlot": "SlotID:0-MLOM",
            "ComputeNodeId": 2,
            "ComputeNodePowerOn": false
        },
        {
            "Moid": "632b188476752d3236311879",
            "Dn": "/redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77",
            "AdapterId": "UCSX-V4-Q25GML_FCH26217F77",
            "BaseMacAddress": "48:2E:72:E4:52:60",
            "ComputeNodeMoid": "632b163e76752d32363073aa",
            "ExtEthIfsIds": [
                "632b188d76752d3236311cc3",
                "632b188d76752d3236311cc4",
                "632b188d76752d3236311cc5",
                "632b188d76752d3236311cc6"
            ],
            "Model": "UCSX-V4-Q25GML",
            "OperState": "OK",
            "Presence": "equipped",
            "Healthy": true,
            "Serial": "FCH26217F77",
            "PciSlot": "SlotID:0-MLOM",
            "ComputeNodeId": 3,
            "ComputeNodePowerOn": false
        },
        {
            "Moid": "632b188576752d32363119ed",
            "Dn": "/redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72",
            "AdapterId": "UCSX-V4-Q25GML_FCH26217F72",
            "BaseMacAddress": "48:2E:72:E4:52:68",
            "ComputeNodeMoid": "632b163f76752d32363073f7",
            "ExtEthIfsIds": [
                "632b189176752d3236311ee1",
                "632b189176752d3236311ee2",
                "632b189176752d3236311ee3",
                "632b189176752d3236311ee4"
            ],
            "Model": "UCSX-V4-Q25GML",
            "OperState": "OK",
            "Presence": "equipped",
            "Healthy": true,
            "Serial": "FCH26217F72",
            "PciSlot": "SlotID:0-MLOM",
            "ComputeNodeId": 4,
            "ComputeNodePowerOn": false
        },
        {
            "Moid": "632b19a776752d3236316cb1",
            "Dn": "/redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU",
            "AdapterId": "UCSX-V4-Q25GML_FCH26217FVU",
            "BaseMacAddress": "48:2E:72:E4:50:40",
            "ComputeNodeMoid": "632b174e76752d323630bb47",
            "ExtEthIfsIds": [
                "632b19af76752d3236316ea9",
                "632b19af76752d3236316eaa",
                "632b19af76752d3236316eab",
                "632b19af76752d3236316eac"
            ],
            "Model": "UCSX-V4-Q25GML",
            "OperState": "OK",
            "Presence": "equipped",
            "Healthy": true,
            "Serial": "FCH26217FVU",
            "PciSlot": "SlotID:0-MLOM",
            "ComputeNodeId": 1,
            "ComputeNodePowerOn": false
        }
    ],
    "AdapterExtEthInterfaceInfo": [
        {
            "Moid": "632b188b76752d3236311bb7",
            "Dn": "/redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0/iom-id-2/ext-eth-1",
            "AdapterUnitId": "632b188376752d3236311708",
            "AdminState": "Enabled",
            "InterfaceId": "1",
            "MacAddress": "48:2E:72:E4:50:29",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5ac2",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-5",
            "PeerPortId": 5,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163d76752d323630734f",
            "ComputeNodeId": 2,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217EZ0",
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188b76752d3236311bbe",
            "Dn": "/redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0/iom-id-2/ext-eth-2",
            "AdapterUnitId": "632b188376752d3236311708",
            "AdminState": "Enabled",
            "InterfaceId": "2",
            "MacAddress": "48:2E:72:E4:50:2A",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5ac3",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-6",
            "PeerPortId": 6,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163d76752d323630734f",
            "ComputeNodeId": 2,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217EZ0",
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188b76752d3236311bc0",
            "Dn": "/redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0/iom-id-1/ext-eth-3",
            "AdapterUnitId": "632b188376752d3236311708",
            "AdminState": "Enabled",
            "InterfaceId": "3",
            "MacAddress": "48:2E:72:E4:50:2B",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a02286",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-5",
            "PeerPortId": 5,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163d76752d323630734f",
            "ComputeNodeId": 2,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217EZ0",
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188b76752d3236311bc5",
            "Dn": "/redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0/iom-id-1/ext-eth-4",
            "AdapterUnitId": "632b188376752d3236311708",
            "AdminState": "Enabled",
            "InterfaceId": "4",
            "MacAddress": "48:2E:72:E4:50:2C",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a02287",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-6",
            "PeerPortId": 6,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163d76752d323630734f",
            "ComputeNodeId": 2,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217EZ0",
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188d76752d3236311cc3",
            "Dn": "/redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77/iom-id-2/ext-eth-1",
            "AdapterUnitId": "632b188476752d3236311879",
            "AdminState": "Enabled",
            "InterfaceId": "1",
            "MacAddress": "48:2E:72:E4:52:61",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5ac6",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-9",
            "PeerPortId": 9,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163e76752d32363073aa",
            "ComputeNodeId": 3,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F77",
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188d76752d3236311cc4",
            "Dn": "/redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77/iom-id-2/ext-eth-2",
            "AdapterUnitId": "632b188476752d3236311879",
            "AdminState": "Enabled",
            "InterfaceId": "2",
            "MacAddress": "48:2E:72:E4:52:62",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5ac7",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-10",
            "PeerPortId": 10,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163e76752d32363073aa",
            "ComputeNodeId": 3,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F77",
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188d76752d3236311cc5",
            "Dn": "/redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77/iom-id-1/ext-eth-3",
            "AdapterUnitId": "632b188476752d3236311879",
            "AdminState": "Enabled",
            "InterfaceId": "3",
            "MacAddress": "48:2E:72:E4:52:63",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a0228a",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-9",
            "PeerPortId": 9,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163e76752d32363073aa",
            "ComputeNodeId": 3,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F77",
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188d76752d3236311cc6",
            "Dn": "/redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77/iom-id-1/ext-eth-4",
            "AdapterUnitId": "632b188476752d3236311879",
            "AdminState": "Enabled",
            "InterfaceId": "4",
            "MacAddress": "48:2E:72:E4:52:64",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a0228b",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-10",
            "PeerPortId": 10,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163e76752d32363073aa",
            "ComputeNodeId": 3,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F77",
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b189176752d3236311ee1",
            "Dn": "/redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72/iom-id-2/ext-eth-1",
            "AdapterUnitId": "632b188576752d32363119ed",
            "AdminState": "Enabled",
            "InterfaceId": "1",
            "MacAddress": "48:2E:72:E4:52:69",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5aca",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-13",
            "PeerPortId": 13,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163f76752d32363073f7",
            "ComputeNodeId": 4,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F72",
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b189176752d3236311ee2",
            "Dn": "/redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72/iom-id-2/ext-eth-2",
            "AdapterUnitId": "632b188576752d32363119ed",
            "AdminState": "Enabled",
            "InterfaceId": "2",
            "MacAddress": "48:2E:72:E4:52:6A",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5acb",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-14",
            "PeerPortId": 14,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163f76752d32363073f7",
            "ComputeNodeId": 4,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F72",
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b189176752d3236311ee3",
            "Dn": "/redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72/iom-id-1/ext-eth-3",
            "AdapterUnitId": "632b188576752d32363119ed",
            "AdminState": "Enabled",
            "InterfaceId": "3",
            "MacAddress": "48:2E:72:E4:52:6B",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a0226e",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-13",
            "PeerPortId": 13,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163f76752d32363073f7",
            "ComputeNodeId": 4,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F72",
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b189176752d3236311ee4",
            "Dn": "/redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72/iom-id-1/ext-eth-4",
            "AdapterUnitId": "632b188576752d32363119ed",
            "AdminState": "Enabled",
            "InterfaceId": "4",
            "MacAddress": "48:2E:72:E4:52:6C",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a0226f",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-14",
            "PeerPortId": 14,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163f76752d32363073f7",
            "ComputeNodeId": 4,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F72",
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b19af76752d3236316ea9",
            "Dn": "/redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU/iom-id-2/ext-eth-1",
            "AdapterUnitId": "632b19a776752d3236316cb1",
            "AdminState": "Enabled",
            "InterfaceId": "1",
            "MacAddress": "48:2E:72:E4:50:41",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5abe",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-1",
            "PeerPortId": 1,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b174e76752d323630bb47",
            "ComputeNodeId": 1,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217FVU",
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b19af76752d3236316eaa",
            "Dn": "/redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU/iom-id-2/ext-eth-2",
            "AdapterUnitId": "632b19a776752d3236316cb1",
            "AdminState": "Enabled",
            "InterfaceId": "2",
            "MacAddress": "48:2E:72:E4:50:42",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5abf",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-2",
            "PeerPortId": 2,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b174e76752d323630bb47",
            "ComputeNodeId": 1,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217FVU",
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b19af76752d3236316eab",
            "Dn": "/redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU/iom-id-1/ext-eth-3",
            "AdapterUnitId": "632b19a776752d3236316cb1",
            "AdminState": "Enabled",
            "InterfaceId": "3",
            "MacAddress": "48:2E:72:E4:50:43",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a02282",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-1",
            "PeerPortId": 1,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b174e76752d323630bb47",
            "ComputeNodeId": 1,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217FVU",
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b19af76752d3236316eac",
            "Dn": "/redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU/iom-id-1/ext-eth-4",
            "AdapterUnitId": "632b19a776752d3236316cb1",
            "AdminState": "Enabled",
            "InterfaceId": "4",
            "MacAddress": "48:2E:72:E4:50:44",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a02283",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-2",
            "PeerPortId": 2,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b174e76752d323630bb47",
            "ComputeNodeId": 1,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217FVU",
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        }
    ],
    "NetworkPortInfo": [
        {
            "Moid": "632b13c976752d32362fc25a",
            "Dn": "chassis-1-ioc-1-slot-1-port-1",
            "Name": "1/1",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a64",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 1,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerSwitchId": "B",
            "PeerPortName": "1/17",
            "PeerPortChannelId": 1153,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632c81ec76752d32369daa08",
            "Dn": "chassis-1-ioc-1-slot-1-port-2",
            "Name": "1/2",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a6a",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 2,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerSwitchId": "B",
            "PeerPortName": "1/19",
            "PeerPortChannelId": 1153,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632c81f276752d32369dac8d",
            "Dn": "chassis-1-ioc-1-slot-1-port-3",
            "Name": "1/3",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a14",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 3,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerSwitchId": "B",
            "PeerPortName": "1/21",
            "PeerPortChannelId": 1153,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632c820576752d32369db290",
            "Dn": "chassis-1-ioc-1-slot-1-port-4",
            "Name": "1/4",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a6c",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 4,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerSwitchId": "B",
            "PeerPortName": "1/23",
            "PeerPortChannelId": 1153,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632b13c876752d32362fc189",
            "Dn": "chassis-1-ioc-2-slot-2-port-1",
            "Name": "2/1",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd9923",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 1,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerSwitchId": "A",
            "PeerPortName": "1/17",
            "PeerPortChannelId": 1025,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632c81e776752d32369da82f",
            "Dn": "chassis-1-ioc-2-slot-2-port-2",
            "Name": "2/2",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd98da",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 2,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerSwitchId": "A",
            "PeerPortName": "1/19",
            "PeerPortChannelId": 1025,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632c81ed76752d32369daa9c",
            "Dn": "chassis-1-ioc-2-slot-2-port-3",
            "Name": "2/3",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd98dd",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 3,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerSwitchId": "A",
            "PeerPortName": "1/21",
            "PeerPortChannelId": 1025,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632c81fe76752d32369db10a",
            "Dn": "chassis-1-ioc-2-slot-2-port-4",
            "Name": "2/4",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd98d0",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 4,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerSwitchId": "A",
            "PeerPortName": "1/23",
            "PeerPortChannelId": 1025,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        }
    ],
    "PhysicalPortInfo": [
        {
            "Moid": "6329994b76752d3236cd98d0",
            "Dn": "switch-FDO26340DE3/slot-1/switch-ether/port-23",
            "Name": "1/23",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:5E",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 23,
            "PortChannelId": 1025,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "A",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994b76752d3236cd98da",
            "Dn": "switch-FDO26340DE3/slot-1/switch-ether/port-19",
            "Name": "1/19",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:5A",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 19,
            "PortChannelId": 1025,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "A",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994b76752d3236cd98dd",
            "Dn": "switch-FDO26340DE3/slot-1/switch-ether/port-21",
            "Name": "1/21",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:5C",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 21,
            "PortChannelId": 1025,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "A",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994b76752d3236cd9923",
            "Dn": "switch-FDO26340DE3/slot-1/switch-ether/port-17",
            "Name": "1/17",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:58",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 17,
            "PortChannelId": 1025,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "A",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994c76752d3236cd9a14",
            "Dn": "switch-FDO26340CVC/slot-1/switch-ether/port-21",
            "Name": "1/21",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:BC",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 21,
            "PortChannelId": 1153,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "B",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994c76752d3236cd9a64",
            "Dn": "switch-FDO26340CVC/slot-1/switch-ether/port-17",
            "Name": "1/17",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:B8",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 17,
            "PortChannelId": 1153,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "B",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994c76752d3236cd9a6a",
            "Dn": "switch-FDO26340CVC/slot-1/switch-ether/port-19",
            "Name": "1/19",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:BA",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 19,
            "PortChannelId": 1153,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "B",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994c76752d3236cd9a6c",
            "Dn": "switch-FDO26340CVC/slot-1/switch-ether/port-23",
            "Name": "1/23",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:BE",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 23,
            "PortChannelId": 1153,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "B",
            "TransceiverType": "SFP-25G-AOC2M"
        }
    ]
}
```

## YAML output

```
# iserver get chassis --serial FOX2611PPHP -p . -o yaml

AdapterExtEthInterfaceInfo:
- AdapterUnitId: 632b188376752d3236311708
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217EZ0
  AdminState: Enabled
  ComputeNodeId: 2
  ComputeNodeMoid: 632b163d76752d323630734f
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0/iom-id-2/ext-eth-1
  InterfaceId: '1'
  MacAddress: 48:2E:72:E4:50:29
  Moid: 632b188b76752d3236311bb7
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-2-muxhostport-port-5
  PeerHostPortId: 632b158c6373582d415a5ac2
  PeerInfo: 'Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 5
  PeerSlotId: 1
  SwitchId: A
- AdapterUnitId: 632b188376752d3236311708
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217EZ0
  AdminState: Enabled
  ComputeNodeId: 2
  ComputeNodeMoid: 632b163d76752d323630734f
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0/iom-id-2/ext-eth-2
  InterfaceId: '2'
  MacAddress: 48:2E:72:E4:50:2A
  Moid: 632b188b76752d3236311bbe
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-2-muxhostport-port-6
  PeerHostPortId: 632b158c6373582d415a5ac3
  PeerInfo: 'Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 6
  PeerSlotId: 1
  SwitchId: A
- AdapterUnitId: 632b188376752d3236311708
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217EZ0
  AdminState: Enabled
  ComputeNodeId: 2
  ComputeNodeMoid: 632b163d76752d323630734f
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0/iom-id-1/ext-eth-3
  InterfaceId: '3'
  MacAddress: 48:2E:72:E4:50:2B
  Moid: 632b188b76752d3236311bc0
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-1-muxhostport-port-5
  PeerHostPortId: 632b175c6373582d42a02286
  PeerInfo: 'Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 5
  PeerSlotId: 1
  SwitchId: B
- AdapterUnitId: 632b188376752d3236311708
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217EZ0
  AdminState: Enabled
  ComputeNodeId: 2
  ComputeNodeMoid: 632b163d76752d323630734f
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0/iom-id-1/ext-eth-4
  InterfaceId: '4'
  MacAddress: 48:2E:72:E4:50:2C
  Moid: 632b188b76752d3236311bc5
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-1-muxhostport-port-6
  PeerHostPortId: 632b175c6373582d42a02287
  PeerInfo: 'Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 6
  PeerSlotId: 1
  SwitchId: B
- AdapterUnitId: 632b188476752d3236311879
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217F77
  AdminState: Enabled
  ComputeNodeId: 3
  ComputeNodeMoid: 632b163e76752d32363073aa
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77/iom-id-2/ext-eth-1
  InterfaceId: '1'
  MacAddress: 48:2E:72:E4:52:61
  Moid: 632b188d76752d3236311cc3
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-2-muxhostport-port-9
  PeerHostPortId: 632b158c6373582d415a5ac6
  PeerInfo: 'Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 9
  PeerSlotId: 1
  SwitchId: A
- AdapterUnitId: 632b188476752d3236311879
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217F77
  AdminState: Enabled
  ComputeNodeId: 3
  ComputeNodeMoid: 632b163e76752d32363073aa
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77/iom-id-2/ext-eth-2
  InterfaceId: '2'
  MacAddress: 48:2E:72:E4:52:62
  Moid: 632b188d76752d3236311cc4
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-2-muxhostport-port-10
  PeerHostPortId: 632b158c6373582d415a5ac7
  PeerInfo: 'Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 10
  PeerSlotId: 1
  SwitchId: A
- AdapterUnitId: 632b188476752d3236311879
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217F77
  AdminState: Enabled
  ComputeNodeId: 3
  ComputeNodeMoid: 632b163e76752d32363073aa
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77/iom-id-1/ext-eth-3
  InterfaceId: '3'
  MacAddress: 48:2E:72:E4:52:63
  Moid: 632b188d76752d3236311cc5
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-1-muxhostport-port-9
  PeerHostPortId: 632b175c6373582d42a0228a
  PeerInfo: 'Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 9
  PeerSlotId: 1
  SwitchId: B
- AdapterUnitId: 632b188476752d3236311879
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217F77
  AdminState: Enabled
  ComputeNodeId: 3
  ComputeNodeMoid: 632b163e76752d32363073aa
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77/iom-id-1/ext-eth-4
  InterfaceId: '4'
  MacAddress: 48:2E:72:E4:52:64
  Moid: 632b188d76752d3236311cc6
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-1-muxhostport-port-10
  PeerHostPortId: 632b175c6373582d42a0228b
  PeerInfo: 'Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 10
  PeerSlotId: 1
  SwitchId: B
- AdapterUnitId: 632b188576752d32363119ed
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217F72
  AdminState: Enabled
  ComputeNodeId: 4
  ComputeNodeMoid: 632b163f76752d32363073f7
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72/iom-id-2/ext-eth-1
  InterfaceId: '1'
  MacAddress: 48:2E:72:E4:52:69
  Moid: 632b189176752d3236311ee1
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-2-muxhostport-port-13
  PeerHostPortId: 632b158c6373582d415a5aca
  PeerInfo: 'Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 13
  PeerSlotId: 1
  SwitchId: A
- AdapterUnitId: 632b188576752d32363119ed
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217F72
  AdminState: Enabled
  ComputeNodeId: 4
  ComputeNodeMoid: 632b163f76752d32363073f7
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72/iom-id-2/ext-eth-2
  InterfaceId: '2'
  MacAddress: 48:2E:72:E4:52:6A
  Moid: 632b189176752d3236311ee2
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-2-muxhostport-port-14
  PeerHostPortId: 632b158c6373582d415a5acb
  PeerInfo: 'Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 14
  PeerSlotId: 1
  SwitchId: A
- AdapterUnitId: 632b188576752d32363119ed
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217F72
  AdminState: Enabled
  ComputeNodeId: 4
  ComputeNodeMoid: 632b163f76752d32363073f7
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72/iom-id-1/ext-eth-3
  InterfaceId: '3'
  MacAddress: 48:2E:72:E4:52:6B
  Moid: 632b189176752d3236311ee3
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-1-muxhostport-port-13
  PeerHostPortId: 632b175c6373582d42a0226e
  PeerInfo: 'Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 13
  PeerSlotId: 1
  SwitchId: B
- AdapterUnitId: 632b188576752d32363119ed
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217F72
  AdminState: Enabled
  ComputeNodeId: 4
  ComputeNodeMoid: 632b163f76752d32363073f7
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72/iom-id-1/ext-eth-4
  InterfaceId: '4'
  MacAddress: 48:2E:72:E4:52:6C
  Moid: 632b189176752d3236311ee4
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-1-muxhostport-port-14
  PeerHostPortId: 632b175c6373582d42a0226f
  PeerInfo: 'Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 14
  PeerSlotId: 1
  SwitchId: B
- AdapterUnitId: 632b19a776752d3236316cb1
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217FVU
  AdminState: Enabled
  ComputeNodeId: 1
  ComputeNodeMoid: 632b174e76752d323630bb47
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU/iom-id-2/ext-eth-1
  InterfaceId: '1'
  MacAddress: 48:2E:72:E4:50:41
  Moid: 632b19af76752d3236316ea9
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-2-muxhostport-port-1
  PeerHostPortId: 632b158c6373582d415a5abe
  PeerInfo: 'Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 1
  PeerSlotId: 1
  SwitchId: A
- AdapterUnitId: 632b19a776752d3236316cb1
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217FVU
  AdminState: Enabled
  ComputeNodeId: 1
  ComputeNodeMoid: 632b174e76752d323630bb47
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU/iom-id-2/ext-eth-2
  InterfaceId: '2'
  MacAddress: 48:2E:72:E4:50:42
  Moid: 632b19af76752d3236316eaa
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-2-muxhostport-port-2
  PeerHostPortId: 632b158c6373582d415a5abf
  PeerInfo: 'Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 2
  PeerSlotId: 1
  SwitchId: A
- AdapterUnitId: 632b19a776752d3236316cb1
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217FVU
  AdminState: Enabled
  ComputeNodeId: 1
  ComputeNodeMoid: 632b174e76752d323630bb47
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU/iom-id-1/ext-eth-3
  InterfaceId: '3'
  MacAddress: 48:2E:72:E4:50:43
  Moid: 632b19af76752d3236316eab
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-1-muxhostport-port-1
  PeerHostPortId: 632b175c6373582d42a02282
  PeerInfo: 'Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 1
  PeerSlotId: 1
  SwitchId: B
- AdapterUnitId: 632b19a776752d3236316cb1
  AdepterModel: UCSX-V4-Q25GML
  AdepterOperState: OK
  AdepterPresence: equipped
  AdepterSerial: FCH26217FVU
  AdminState: Enabled
  ComputeNodeId: 1
  ComputeNodeMoid: 632b174e76752d323630bb47
  ComputeNodePowerOn: false
  ComputeNodeSlot: SlotID:0-MLOM
  Dn: /redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU/iom-id-1/ext-eth-4
  InterfaceId: '4'
  MacAddress: 48:2E:72:E4:50:44
  Moid: 632b19af76752d3236316eac
  PeerAggrPortId: 0
  PeerDn: chassis-1-ioc-1-muxhostport-port-2
  PeerHostPortId: 632b175c6373582d42a02283
  PeerInfo: 'Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerPortId: 2
  PeerSlotId: 1
  SwitchId: B
AdapterUnitInfo:
- AdapterId: UCSX-V4-Q25GML_FCH26217EZ0
  BaseMacAddress: 48:2E:72:E4:50:28
  ComputeNodeId: 2
  ComputeNodeMoid: 632b163d76752d323630734f
  ComputeNodePowerOn: false
  Dn: /redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0
  ExtEthIfsIds:
  - 632b188b76752d3236311bb7
  - 632b188b76752d3236311bbe
  - 632b188b76752d3236311bc0
  - 632b188b76752d3236311bc5
  Healthy: true
  Model: UCSX-V4-Q25GML
  Moid: 632b188376752d3236311708
  OperState: OK
  PciSlot: SlotID:0-MLOM
  Presence: equipped
  Serial: FCH26217EZ0
- AdapterId: UCSX-V4-Q25GML_FCH26217F77
  BaseMacAddress: 48:2E:72:E4:52:60
  ComputeNodeId: 3
  ComputeNodeMoid: 632b163e76752d32363073aa
  ComputeNodePowerOn: false
  Dn: /redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77
  ExtEthIfsIds:
  - 632b188d76752d3236311cc3
  - 632b188d76752d3236311cc4
  - 632b188d76752d3236311cc5
  - 632b188d76752d3236311cc6
  Healthy: true
  Model: UCSX-V4-Q25GML
  Moid: 632b188476752d3236311879
  OperState: OK
  PciSlot: SlotID:0-MLOM
  Presence: equipped
  Serial: FCH26217F77
- AdapterId: UCSX-V4-Q25GML_FCH26217F72
  BaseMacAddress: 48:2E:72:E4:52:68
  ComputeNodeId: 4
  ComputeNodeMoid: 632b163f76752d32363073f7
  ComputeNodePowerOn: false
  Dn: /redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72
  ExtEthIfsIds:
  - 632b189176752d3236311ee1
  - 632b189176752d3236311ee2
  - 632b189176752d3236311ee3
  - 632b189176752d3236311ee4
  Healthy: true
  Model: UCSX-V4-Q25GML
  Moid: 632b188576752d32363119ed
  OperState: OK
  PciSlot: SlotID:0-MLOM
  Presence: equipped
  Serial: FCH26217F72
- AdapterId: UCSX-V4-Q25GML_FCH26217FVU
  BaseMacAddress: 48:2E:72:E4:50:40
  ComputeNodeId: 1
  ComputeNodeMoid: 632b174e76752d323630bb47
  ComputeNodePowerOn: false
  Dn: /redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU
  ExtEthIfsIds:
  - 632b19af76752d3236316ea9
  - 632b19af76752d3236316eaa
  - 632b19af76752d3236316eab
  - 632b19af76752d3236316eac
  Healthy: true
  Model: UCSX-V4-Q25GML
  Moid: 632b19a776752d3236316cb1
  OperState: OK
  PciSlot: SlotID:0-MLOM
  Presence: equipped
  Serial: FCH26217FVU
Chassis:
  AlarmCritical: 0
  AlarmWarning: 2
  ConnectionPath: A,B
  ConnectionStatus: A,B
  ConnectionSummary: A,B / A,B
  Description: Cisco Blade Server Chassis, 7U with Eight Vertical Blade Server Slots
  DeviceMoId: 632999466f72612d39b26942
  Dn: chassis-1
  FanMax: 8
  FanModuleMax: 4
  Health: Warnings
  HealthSummary: Warnings (2)
  HostPortCount: 66
  HostPortSummary: 0/66
  HostPortUp: 0
  IfmCount: 2
  IfmMax: 2
  IfmOn: 2
  IfmSummary: 2/2/2
  Model: UCSX-9508
  Moid: 632b13c876752d32362fc175
  Name: ucsX-1
  NetworkPortCount: 8
  NetworkPortMax: 16
  NetworkPortSummary: 8/8/16
  NetworkPortUp: 8
  NodeCount: 4
  NodeMax: 8
  NodePowerOn: 0
  NodeSummary: 0/4/8
  OperState: OK
  PartNumber: 68-6847-03
  Pid: UCSX-9508
  ProductName: Cisco UCSX 9508 Chassis
  PsuMax: 6
  Serial: FOX2611PPHP
  Sku: UCSX-9508
  Vendor: Cisco Systems Inc
HostPortInfo:
- Dn: chassis-1-ioc-1-muxhostport-port-1
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:83
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a02282
  Name: 1/1/1
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b19af76752d3236316eab
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 1
  PortChannelId: 1283
  PortId: 1
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-2
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:84
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a02283
  Name: 1/1/2
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b19af76752d3236316eac
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 1
  PortChannelId: 1283
  PortId: 2
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-3
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:85
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02284
  Name: 1/1/3
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 3
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-4
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:86
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02285
  Name: 1/1/4
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 4
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-5
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:87
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a02286
  Name: 1/1/5
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b188b76752d3236311bc0
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 2
  PortChannelId: 1280
  PortId: 5
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-6
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:88
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a02287
  Name: 1/1/6
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b188b76752d3236311bc5
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 2
  PortChannelId: 1280
  PortId: 6
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-7
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:89
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02288
  Name: 1/1/7
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 7
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-8
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:8A
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02289
  Name: 1/1/8
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 8
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-9
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:8B
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a0228a
  Name: 1/1/9
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b188d76752d3236311cc5
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 3
  PortChannelId: 1281
  PortId: 9
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-10
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:8C
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a0228b
  Name: 1/1/10
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b188d76752d3236311cc6
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 3
  PortChannelId: 1281
  PortId: 10
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-11
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:8D
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0226c
  Name: 1/1/11
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 11
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-12
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:8E
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0226d
  Name: 1/1/12
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 12
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-13
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:8F
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a0226e
  Name: 1/1/13
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b189176752d3236311ee3
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 4
  PortChannelId: 1282
  PortId: 13
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-14
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:90
  Mode: vntag
  ModuleId: 1
  Moid: 632b175c6373582d42a0226f
  Name: 1/1/14
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b189176752d3236311ee4
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 4
  PortChannelId: 1282
  PortId: 14
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-15
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:91
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02270
  Name: 1/1/15
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 15
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-16
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:92
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02271
  Name: 1/1/16
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 16
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-17
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:93
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02272
  Name: 1/1/17
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 17
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-18
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:94
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02273
  Name: 1/1/18
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 18
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-19
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:95
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02274
  Name: 1/1/19
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 19
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-20
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:96
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02275
  Name: 1/1/20
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 20
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-21
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:97
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02276
  Name: 1/1/21
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 21
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-22
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:98
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02277
  Name: 1/1/22
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 22
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-23
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:99
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02278
  Name: 1/1/23
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 23
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-24
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:9A
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02279
  Name: 1/1/24
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 24
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-25
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:9B
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0227a
  Name: 1/1/25
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 25
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-26
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:9C
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0227b
  Name: 1/1/26
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 26
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-27
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:9D
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0227c
  Name: 1/1/27
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 27
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-28
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:9E
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0227d
  Name: 1/1/28
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 28
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-29
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:9F
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0227e
  Name: 1/1/29
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 29
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-30
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:A0
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a0227f
  Name: 1/1/30
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 30
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-31
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:A1
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02280
  Name: 1/1/31
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 31
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-32
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: A8:4F:B1:55:4D:A2
  Mode: access
  ModuleId: 1
  Moid: 632b175c6373582d42a02281
  Name: 1/1/32
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 32
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-1-muxhostport-port-33
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  MacAddress: 00:00:00:00:00:00
  Mode: access
  ModuleId: 1
  Moid: 632b1fcc6373582d42a023ab
  Name: 1/1/33
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 33
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: B
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-1
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C3
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5abe
  Name: 1/1/1
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b19af76752d3236316ea9
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 1
  PortChannelId: 1287
  PortId: 1
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-2
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C4
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5abf
  Name: 1/1/2
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b19af76752d3236316eaa
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 1
  PortChannelId: 1287
  PortId: 2
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-3
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C5
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac0
  Name: 1/1/3
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 3
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-4
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C6
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac1
  Name: 1/1/4
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 4
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-5
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C7
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac2
  Name: 1/1/5
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b188b76752d3236311bb7
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 2
  PortChannelId: 1284
  PortId: 5
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-6
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C8
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac3
  Name: 1/1/6
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b188b76752d3236311bbe
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 2
  PortChannelId: 1284
  PortId: 6
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-7
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:C9
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac4
  Name: 1/1/7
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 7
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-8
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:CA
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac5
  Name: 1/1/8
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 8
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-9
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:CB
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac6
  Name: 1/1/9
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b188d76752d3236311cc3
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 3
  PortChannelId: 1285
  PortId: 9
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-10
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:CC
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac7
  Name: 1/1/10
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b188d76752d3236311cc4
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 3
  PortChannelId: 1285
  PortId: 10
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-11
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:CD
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac8
  Name: 1/1/11
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 11
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-12
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:CE
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ac9
  Name: 1/1/12
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 12
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-13
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:CF
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5aca
  Name: 1/1/13
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b189176752d3236311ee1
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 4
  PortChannelId: 1286
  PortId: 13
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-14
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D0
  Mode: vntag
  ModuleId: 1
  Moid: 632b158c6373582d415a5acb
  Name: 1/1/14
  OperSpeed: auto
  OperState: down
  OperStateQual: link-failure
  PeerDn: ''
  PeerInfo: 'Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML'
  PeerInterfaceId: 632b189176752d3236311ee2
  PeerInterfaceType: adapter.ExtEthInterface
  PeerNodeId: 4
  PortChannelId: 1286
  PortId: 14
  PortType: Ethernet
  Role: BladeServer
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-15
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D1
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5acc
  Name: 1/1/15
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 15
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-16
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D2
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5acd
  Name: 1/1/16
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 16
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-17
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D3
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ace
  Name: 1/1/17
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 17
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-18
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D4
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5acf
  Name: 1/1/18
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 18
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-19
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D5
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad0
  Name: 1/1/19
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 19
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-20
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D6
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad1
  Name: 1/1/20
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 20
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-21
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D7
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad2
  Name: 1/1/21
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 21
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-22
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D8
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad3
  Name: 1/1/22
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 22
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-23
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:D9
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad4
  Name: 1/1/23
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 23
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-24
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:DA
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad5
  Name: 1/1/24
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 24
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-25
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:DB
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad6
  Name: 1/1/25
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 25
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-26
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:DC
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad7
  Name: 1/1/26
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 26
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-27
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:DD
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad8
  Name: 1/1/27
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 27
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-28
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:DE
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ad9
  Name: 1/1/28
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 28
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-29
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:DF
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5ada
  Name: 1/1/29
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 29
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-30
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:E0
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5adb
  Name: 1/1/30
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 30
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-31
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:E1
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5adc
  Name: 1/1/31
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 31
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-32
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: A8:4F:B1:55:4A:E2
  Mode: access
  ModuleId: 1
  Moid: 632b158c6373582d415a5add
  Name: 1/1/32
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 32
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
- Dn: chassis-1-ioc-2-muxhostport-port-33
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  MacAddress: 00:00:00:00:00:00
  Mode: access
  ModuleId: 1
  Moid: 632c6acd6373582d415a8b96
  Name: 1/1/33
  OperSpeed: auto
  OperState: down
  OperStateQual: admin-down
  PeerDn: ''
  PeerInfo: ''
  PeerInterfaceId: null
  PeerInterfaceType: null
  PeerNodeId: null
  PortChannelId: 0
  PortId: 33
  PortType: Ethernet
  Role: unknown
  SlotId: 1
  Speed: auto
  SwitchId: A
  TransceiverType: unknown
  Up: false
IfmInfo:
- ConnectionPath: B
  ConnectionStatus: B
  Description: Cisco UCS 9108-25G 8 Port IFM
  Dn: chassis-1-ioc-1
  FanMoids:
  - 632b178c76752d323630ceca
  - 632b178c76752d323630ced9
  - 632b178c76752d323630cee8
  HostPorts:
  - 632b175c6373582d42a02271
  - 632b175c6373582d42a02275
  - 632b175c6373582d42a0227a
  - 632b175c6373582d42a0227d
  - 632b175c6373582d42a02280
  - 632b175c6373582d42a02277
  - 632b175c6373582d42a02272
  - 632b175c6373582d42a0227b
  - 632b175c6373582d42a02286
  - 632b175c6373582d42a02289
  - 632b175c6373582d42a02270
  - 632b175c6373582d42a02274
  - 632b175c6373582d42a02278
  - 632b175c6373582d42a0228b
  - 632b175c6373582d42a0226d
  - 632b175c6373582d42a0226e
  - 632b175c6373582d42a02276
  - 632b175c6373582d42a0227c
  - 632b175c6373582d42a02284
  - 632b175c6373582d42a0226f
  - 632b175c6373582d42a0227f
  - 632b175c6373582d42a02281
  - 632b175c6373582d42a02288
  - 632b175c6373582d42a02273
  - 632b175c6373582d42a02279
  - 632b175c6373582d42a0227e
  - 632b175c6373582d42a02282
  - 632b175c6373582d42a02287
  - 632b175c6373582d42a0228a
  - 632b175c6373582d42a0226c
  - 632b175c6373582d42a02283
  - 632b175c6373582d42a02285
  - 632b1fcc6373582d42a023ab
  ManagementCidr: 10.90.90.49/24
  ManagementGateway: 10.90.89.1
  ManagementIp: 10.90.90.49
  ManagementPrefix: 24
  ManagementSubnet: 255.255.255.0
  ManagementVlan: 89
  Model: UCSX-I-9108-25G
  ModuleId: 1
  Moid: 632b13c976752d32362fc244
  Name: 'IFM #1 (top)'
  NetworkPortCount: 4
  NetworkPortMax: 8
  NetworkPortSummary: 4/4/8
  NetworkPortUp: 4
  NetworkPorts:
  - 632b13c976752d32362fc25a
  - 632c81ec76752d32369daa08
  - 632c81f276752d32369dac8d
  - 632c820576752d32369db290
  'On': true
  OperState: OK
  PartNumber: 73-20533-03
  Pid: UCSX-I-9108-25G
  Presence: equipped
  ProductName: Cisco UCS 9108-25G
  Serial: FCH261770KU
  Side: top
  Version: 4.2(2c)
- ConnectionPath: A
  ConnectionStatus: A
  Description: Cisco UCS 9108-25G 8 Port IFM
  Dn: chassis-1-ioc-2
  FanMoids:
  - 632b15b576752d3236304d3d
  - 632b15b576752d3236304d58
  - 632b15b576752d3236304d6f
  HostPorts:
  - 632b158c6373582d415a5ad6
  - 632b158c6373582d415a5ac0
  - 632b158c6373582d415a5acc
  - 632b158c6373582d415a5abf
  - 632b158c6373582d415a5ac6
  - 632b158c6373582d415a5ac7
  - 632b158c6373582d415a5ad4
  - 632b158c6373582d415a5ad8
  - 632b158c6373582d415a5ac1
  - 632b158c6373582d415a5ac4
  - 632b158c6373582d415a5acf
  - 632b158c6373582d415a5ad2
  - 632b158c6373582d415a5ad3
  - 632b158c6373582d415a5ac9
  - 632b158c6373582d415a5ad5
  - 632b158c6373582d415a5adb
  - 632b158c6373582d415a5ac2
  - 632b158c6373582d415a5ac8
  - 632b158c6373582d415a5add
  - 632b158c6373582d415a5aca
  - 632b158c6373582d415a5acb
  - 632b158c6373582d415a5acd
  - 632b158c6373582d415a5ace
  - 632b158c6373582d415a5ac5
  - 632b158c6373582d415a5ac3
  - 632b158c6373582d415a5ad0
  - 632b158c6373582d415a5adc
  - 632b158c6373582d415a5ad7
  - 632b158c6373582d415a5abe
  - 632b158c6373582d415a5ad1
  - 632b158c6373582d415a5ad9
  - 632b158c6373582d415a5ada
  - 632c6acd6373582d415a8b96
  ManagementCidr: 10.90.90.48/24
  ManagementGateway: 10.90.89.1
  ManagementIp: 10.90.90.48
  ManagementPrefix: 24
  ManagementSubnet: 255.255.255.0
  ManagementVlan: 89
  Model: UCSX-I-9108-25G
  ModuleId: 2
  Moid: 632b13c876752d32362fc17c
  Name: 'IFM #2 (bottom)'
  NetworkPortCount: 4
  NetworkPortMax: 8
  NetworkPortSummary: 4/4/8
  NetworkPortUp: 4
  NetworkPorts:
  - 632b13c876752d32362fc189
  - 632c81e776752d32369da82f
  - 632c81ed76752d32369daa9c
  - 632c81fe76752d32369db10a
  'On': true
  OperState: OK
  PartNumber: 73-20533-03
  Pid: UCSX-I-9108-25G
  Presence: equipped
  ProductName: Cisco UCS 9108-25G
  Serial: FCH261770RN
  Side: bottom
  Version: 4.2(2c)
NetworkPortInfo:
- Dn: chassis-1-ioc-1-slot-1-port-1
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  ModuleId: 0
  Moid: 632b13c976752d32362fc25a
  Name: 1/1
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994c76752d3236cd9a64
  PeerInterfaceType: ether.PhysicalPort
  PeerOperSpeed: 25G
  PeerPortChannelId: 1153
  PeerPortName: 1/17
  PeerPortTransceiverType: SFP-25G-AOC2M
  PeerSwitchId: B
  PortId: 1
  SlotId: 1
  Speed: 10G
  SwitchId: B
  Up: true
- Dn: chassis-1-ioc-1-slot-1-port-2
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  ModuleId: 0
  Moid: 632c81ec76752d32369daa08
  Name: 1/2
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994c76752d3236cd9a6a
  PeerInterfaceType: ether.PhysicalPort
  PeerOperSpeed: 25G
  PeerPortChannelId: 1153
  PeerPortName: 1/19
  PeerPortTransceiverType: SFP-25G-AOC2M
  PeerSwitchId: B
  PortId: 2
  SlotId: 1
  Speed: 10G
  SwitchId: B
  Up: true
- Dn: chassis-1-ioc-1-slot-1-port-3
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  ModuleId: 0
  Moid: 632c81f276752d32369dac8d
  Name: 1/3
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994c76752d3236cd9a14
  PeerInterfaceType: ether.PhysicalPort
  PeerOperSpeed: 25G
  PeerPortChannelId: 1153
  PeerPortName: 1/21
  PeerPortTransceiverType: SFP-25G-AOC2M
  PeerSwitchId: B
  PortId: 3
  SlotId: 1
  Speed: 10G
  SwitchId: B
  Up: true
- Dn: chassis-1-ioc-1-slot-1-port-4
  IfmDn: chassis-1-ioc-1
  IfmId: 1
  IfmName: 'IFM #1 (top)'
  IoModuleId: 632b13c976752d32362fc244
  ModuleId: 0
  Moid: 632c820576752d32369db290
  Name: 1/4
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994c76752d3236cd9a6c
  PeerInterfaceType: ether.PhysicalPort
  PeerOperSpeed: 25G
  PeerPortChannelId: 1153
  PeerPortName: 1/23
  PeerPortTransceiverType: SFP-25G-AOC2M
  PeerSwitchId: B
  PortId: 4
  SlotId: 1
  Speed: 10G
  SwitchId: B
  Up: true
- Dn: chassis-1-ioc-2-slot-2-port-1
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  ModuleId: 0
  Moid: 632b13c876752d32362fc189
  Name: 2/1
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994b76752d3236cd9923
  PeerInterfaceType: ether.PhysicalPort
  PeerOperSpeed: 25G
  PeerPortChannelId: 1025
  PeerPortName: 1/17
  PeerPortTransceiverType: SFP-25G-AOC2M
  PeerSwitchId: A
  PortId: 1
  SlotId: 2
  Speed: 10G
  SwitchId: A
  Up: true
- Dn: chassis-1-ioc-2-slot-2-port-2
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  ModuleId: 0
  Moid: 632c81e776752d32369da82f
  Name: 2/2
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994b76752d3236cd98da
  PeerInterfaceType: ether.PhysicalPort
  PeerOperSpeed: 25G
  PeerPortChannelId: 1025
  PeerPortName: 1/19
  PeerPortTransceiverType: SFP-25G-AOC2M
  PeerSwitchId: A
  PortId: 2
  SlotId: 2
  Speed: 10G
  SwitchId: A
  Up: true
- Dn: chassis-1-ioc-2-slot-2-port-3
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  ModuleId: 0
  Moid: 632c81ed76752d32369daa9c
  Name: 2/3
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994b76752d3236cd98dd
  PeerInterfaceType: ether.PhysicalPort
  PeerOperSpeed: 25G
  PeerPortChannelId: 1025
  PeerPortName: 1/21
  PeerPortTransceiverType: SFP-25G-AOC2M
  PeerSwitchId: A
  PortId: 3
  SlotId: 2
  Speed: 10G
  SwitchId: A
  Up: true
- Dn: chassis-1-ioc-2-slot-2-port-4
  IfmDn: chassis-1-ioc-2
  IfmId: 2
  IfmName: 'IFM #2 (bottom)'
  IoModuleId: 632b13c876752d32362fc17c
  ModuleId: 0
  Moid: 632c81fe76752d32369db10a
  Name: 2/4
  OperState: up
  PeerDn: ''
  PeerInterfaceId: 6329994b76752d3236cd98d0
  PeerInterfaceType: ether.PhysicalPort
  PeerOperSpeed: 25G
  PeerPortChannelId: 1025
  PeerPortName: 1/23
  PeerPortTransceiverType: SFP-25G-AOC2M
  PeerSwitchId: A
  PortId: 4
  SlotId: 2
  Speed: 10G
  SwitchId: A
  Up: true
NodeInfo:
- AlarmCritical: 0
  AlarmWarning: 0
  CpuSummary: 2S 64C 128T
  Dn: /redfish/v1/Systems/FCH26167MMZ
  HardwareUuid: 8A552335-ED7E-4A28-924D-BE8748DA5BF8
  Health: Healthy
  HealthSummary: Healthy
  Model: UCSX-210C-M6
  Moid: 632b174e76752d323630bb47
  Name: ucsX-1-1
  NumAdaptors: 1
  NumCpuCores: 64
  NumCpuCoresEnabled: 64
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 128
  OperPowerState: 'off'
  PowerOn: false
  Serial: FCH26167MMZ
  ServiceProfile: ''
  SlotId: 1
  TotalMemory: 1048576
  TotalMemoryUnit: 1.0 [TiB]
- AlarmCritical: 0
  AlarmWarning: 0
  CpuSummary: 2S 64C 128T
  Dn: /redfish/v1/Systems/FCH26167L94
  HardwareUuid: D576BED6-EF35-439C-B088-0735FED04410
  Health: Healthy
  HealthSummary: Healthy
  Model: UCSX-210C-M6
  Moid: 632b163d76752d323630734f
  Name: ucsX-1-2
  NumAdaptors: 1
  NumCpuCores: 64
  NumCpuCoresEnabled: 64
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 128
  OperPowerState: 'off'
  PowerOn: false
  Serial: FCH26167L94
  ServiceProfile: ''
  SlotId: 2
  TotalMemory: 1048576
  TotalMemoryUnit: 1.0 [TiB]
- AlarmCritical: 0
  AlarmWarning: 0
  CpuSummary: 2S 64C 128T
  Dn: /redfish/v1/Systems/FCH26167MQK
  HardwareUuid: 0607F131-46C2-4CDC-B237-1F872D01E441
  Health: Healthy
  HealthSummary: Healthy
  Model: UCSX-210C-M6
  Moid: 632b163e76752d32363073aa
  Name: ucsX-1-3
  NumAdaptors: 1
  NumCpuCores: 64
  NumCpuCoresEnabled: 64
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 128
  OperPowerState: 'off'
  PowerOn: false
  Serial: FCH26167MQK
  ServiceProfile: ''
  SlotId: 3
  TotalMemory: 1048576
  TotalMemoryUnit: 1.0 [TiB]
- AlarmCritical: 0
  AlarmWarning: 0
  CpuSummary: 2S 64C 128T
  Dn: /redfish/v1/Systems/FCH26167MHB
  HardwareUuid: 6918688F-1B00-4DDB-A6E3-D316F6D07F64
  Health: Healthy
  HealthSummary: Healthy
  Model: UCSX-210C-M6
  Moid: 632b163f76752d32363073f7
  Name: ucsX-1-4
  NumAdaptors: 1
  NumCpuCores: 64
  NumCpuCoresEnabled: 64
  NumCpus: 2
  NumEthHostInterfaces: 0
  NumFcHostInterfaces: 0
  NumThreads: 128
  OperPowerState: 'off'
  PowerOn: false
  Serial: FCH26167MHB
  ServiceProfile: ''
  SlotId: 4
  TotalMemory: 1048576
  TotalMemoryUnit: 1.0 [TiB]
PhysicalPortInfo:
- AdminState: Enabled
  AggregatePortId: 0
  Dn: switch-FDO26340DE3/slot-1/switch-ether/port-23
  MacAddress: 00:08:31:1B:AA:5E
  Mode: fex-fabric
  Moid: 6329994b76752d3236cd98d0
  Name: 1/23
  OperSpeed: 25G
  OperState: up
  PortChannelId: 1025
  PortId: 23
  Role: Server
  SlotId: 1
  SwitchId: A
  TransceiverType: SFP-25G-AOC2M
- AdminState: Enabled
  AggregatePortId: 0
  Dn: switch-FDO26340DE3/slot-1/switch-ether/port-19
  MacAddress: 00:08:31:1B:AA:5A
  Mode: fex-fabric
  Moid: 6329994b76752d3236cd98da
  Name: 1/19
  OperSpeed: 25G
  OperState: up
  PortChannelId: 1025
  PortId: 19
  Role: Server
  SlotId: 1
  SwitchId: A
  TransceiverType: SFP-25G-AOC2M
- AdminState: Enabled
  AggregatePortId: 0
  Dn: switch-FDO26340DE3/slot-1/switch-ether/port-21
  MacAddress: 00:08:31:1B:AA:5C
  Mode: fex-fabric
  Moid: 6329994b76752d3236cd98dd
  Name: 1/21
  OperSpeed: 25G
  OperState: up
  PortChannelId: 1025
  PortId: 21
  Role: Server
  SlotId: 1
  SwitchId: A
  TransceiverType: SFP-25G-AOC2M
- AdminState: Enabled
  AggregatePortId: 0
  Dn: switch-FDO26340DE3/slot-1/switch-ether/port-17
  MacAddress: 00:08:31:1B:AA:58
  Mode: fex-fabric
  Moid: 6329994b76752d3236cd9923
  Name: 1/17
  OperSpeed: 25G
  OperState: up
  PortChannelId: 1025
  PortId: 17
  Role: Server
  SlotId: 1
  SwitchId: A
  TransceiverType: SFP-25G-AOC2M
- AdminState: Enabled
  AggregatePortId: 0
  Dn: switch-FDO26340CVC/slot-1/switch-ether/port-21
  MacAddress: 00:08:31:1B:AA:BC
  Mode: fex-fabric
  Moid: 6329994c76752d3236cd9a14
  Name: 1/21
  OperSpeed: 25G
  OperState: up
  PortChannelId: 1153
  PortId: 21
  Role: Server
  SlotId: 1
  SwitchId: B
  TransceiverType: SFP-25G-AOC2M
- AdminState: Enabled
  AggregatePortId: 0
  Dn: switch-FDO26340CVC/slot-1/switch-ether/port-17
  MacAddress: 00:08:31:1B:AA:B8
  Mode: fex-fabric
  Moid: 6329994c76752d3236cd9a64
  Name: 1/17
  OperSpeed: 25G
  OperState: up
  PortChannelId: 1153
  PortId: 17
  Role: Server
  SlotId: 1
  SwitchId: B
  TransceiverType: SFP-25G-AOC2M
- AdminState: Enabled
  AggregatePortId: 0
  Dn: switch-FDO26340CVC/slot-1/switch-ether/port-19
  MacAddress: 00:08:31:1B:AA:BA
  Mode: fex-fabric
  Moid: 6329994c76752d3236cd9a6a
  Name: 1/19
  OperSpeed: 25G
  OperState: up
  PortChannelId: 1153
  PortId: 19
  Role: Server
  SlotId: 1
  SwitchId: B
  TransceiverType: SFP-25G-AOC2M
- AdminState: Enabled
  AggregatePortId: 0
  Dn: switch-FDO26340CVC/slot-1/switch-ether/port-23
  MacAddress: 00:08:31:1B:AA:BE
  Mode: fex-fabric
  Moid: 6329994c76752d3236cd9a6c
  Name: 1/23
  OperSpeed: 25G
  OperState: up
  PortChannelId: 1153
  PortId: 23
  Role: Server
  SlotId: 1
  SwitchId: B
  TransceiverType: SFP-25G-AOC2M
```

## Developer output

```
# iserver get chassis --serial FOX2611PPHP -p .

Developer output

{
    "duration": 13303,
    "isctl": {
        "read": true,
        "calls": 8,
        "success": 8,
        "failed": 0,
        "total_time": 12367
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": true,
        "lines": 3012
    }
}

Log: debug
-----------

[2022-11-17 10:16:26.066245]	[chassis_info.get]	{
    "Chassis": {
        "ConnectionPath": "A,B",
        "ConnectionStatus": "A,B",
        "Description": "Cisco Blade Server Chassis, 7U with Eight Vertical Blade Server Slots",
        "Dn": "chassis-1",
        "DeviceMoId": "632999466f72612d39b26942",
        "Moid": "632b13c876752d32362fc175",
        "Model": "UCSX-9508",
        "Name": "ucsX-1",
        "OperState": "OK",
        "PartNumber": "68-6847-03",
        "Pid": "UCSX-9508",
        "ProductName": "Cisco UCSX 9508 Chassis",
        "Serial": "FOX2611PPHP",
        "Sku": "UCSX-9508",
        "Vendor": "Cisco Systems Inc",
        "Health": "Warnings",
        "HealthSummary": "Warnings (2)",
        "AlarmWarning": 2,
        "AlarmCritical": 0,
        "ConnectionSummary": "A,B / A,B",
        "NodeMax": 8,
        "IfmMax": 2,
        "FanModuleMax": 4,
        "FanMax": 8,
        "PsuMax": 6,
        "IfmOn": 2,
        "IfmCount": 2,
        "IfmSummary": "2/2/2",
        "HostPortCount": 66,
        "HostPortUp": 0,
        "HostPortSummary": "0/66",
        "NodePowerOn": 0,
        "NodeCount": 4,
        "NodeSummary": "0/4/8",
        "NetworkPortUp": 8,
        "NetworkPortCount": 8,
        "NetworkPortMax": 16,
        "NetworkPortSummary": "8/8/16"
    },
    "IfmInfo": [
        {
            "Moid": "632b13c976752d32362fc244",
            "Dn": "chassis-1-ioc-1",
            "Model": "UCSX-I-9108-25G",
            "ConnectionPath": "B",
            "ConnectionStatus": "B",
            "Description": "Cisco UCS 9108-25G 8 Port IFM",
            "ManagementIp": "10.90.90.49",
            "ManagementSubnet": "255.255.255.0",
            "ManagementPrefix": 24,
            "ManagementCidr": "10.90.90.49/24",
            "ManagementGateway": "10.90.89.1",
            "ManagementVlan": 89,
            "FanMoids": [
                "632b178c76752d323630ceca",
                "632b178c76752d323630ced9",
                "632b178c76752d323630cee8"
            ],
            "HostPorts": [
                "632b175c6373582d42a02271",
                "632b175c6373582d42a02275",
                "632b175c6373582d42a0227a",
                "632b175c6373582d42a0227d",
                "632b175c6373582d42a02280",
                "632b175c6373582d42a02277",
                "632b175c6373582d42a02272",
                "632b175c6373582d42a0227b",
                "632b175c6373582d42a02286",
                "632b175c6373582d42a02289",
                "632b175c6373582d42a02270",
                "632b175c6373582d42a02274",
                "632b175c6373582d42a02278",
                "632b175c6373582d42a0228b",
                "632b175c6373582d42a0226d",
                "632b175c6373582d42a0226e",
                "632b175c6373582d42a02276",
                "632b175c6373582d42a0227c",
                "632b175c6373582d42a02284",
                "632b175c6373582d42a0226f",
                "632b175c6373582d42a0227f",
                "632b175c6373582d42a02281",
                "632b175c6373582d42a02288",
                "632b175c6373582d42a02273",
                "632b175c6373582d42a02279",
                "632b175c6373582d42a0227e",
                "632b175c6373582d42a02282",
                "632b175c6373582d42a02287",
                "632b175c6373582d42a0228a",
                "632b175c6373582d42a0226c",
                "632b175c6373582d42a02283",
                "632b175c6373582d42a02285",
                "632b1fcc6373582d42a023ab"
            ],
            "NetworkPorts": [
                "632b13c976752d32362fc25a",
                "632c81ec76752d32369daa08",
                "632c81f276752d32369dac8d",
                "632c820576752d32369db290"
            ],
            "NetworkPortMax": 8,
            "Name": "IFM #1 (top)",
            "ModuleId": 1,
            "On": true,
            "OperState": "OK",
            "PartNumber": "73-20533-03",
            "Pid": "UCSX-I-9108-25G",
            "Presence": "equipped",
            "ProductName": "Cisco UCS 9108-25G",
            "Serial": "FCH261770KU",
            "Side": "top",
            "Version": "4.2(2c)",
            "NetworkPortCount": 4,
            "NetworkPortUp": 4,
            "NetworkPortSummary": "4/4/8"
        },
        {
            "Moid": "632b13c876752d32362fc17c",
            "Dn": "chassis-1-ioc-2",
            "Model": "UCSX-I-9108-25G",
            "ConnectionPath": "A",
            "ConnectionStatus": "A",
            "Description": "Cisco UCS 9108-25G 8 Port IFM",
            "ManagementIp": "10.90.90.48",
            "ManagementSubnet": "255.255.255.0",
            "ManagementPrefix": 24,
            "ManagementCidr": "10.90.90.48/24",
            "ManagementGateway": "10.90.89.1",
            "ManagementVlan": 89,
            "FanMoids": [
                "632b15b576752d3236304d3d",
                "632b15b576752d3236304d58",
                "632b15b576752d3236304d6f"
            ],
            "HostPorts": [
                "632b158c6373582d415a5ad6",
                "632b158c6373582d415a5ac0",
                "632b158c6373582d415a5acc",
                "632b158c6373582d415a5abf",
                "632b158c6373582d415a5ac6",
                "632b158c6373582d415a5ac7",
                "632b158c6373582d415a5ad4",
                "632b158c6373582d415a5ad8",
                "632b158c6373582d415a5ac1",
                "632b158c6373582d415a5ac4",
                "632b158c6373582d415a5acf",
                "632b158c6373582d415a5ad2",
                "632b158c6373582d415a5ad3",
                "632b158c6373582d415a5ac9",
                "632b158c6373582d415a5ad5",
                "632b158c6373582d415a5adb",
                "632b158c6373582d415a5ac2",
                "632b158c6373582d415a5ac8",
                "632b158c6373582d415a5add",
                "632b158c6373582d415a5aca",
                "632b158c6373582d415a5acb",
                "632b158c6373582d415a5acd",
                "632b158c6373582d415a5ace",
                "632b158c6373582d415a5ac5",
                "632b158c6373582d415a5ac3",
                "632b158c6373582d415a5ad0",
                "632b158c6373582d415a5adc",
                "632b158c6373582d415a5ad7",
                "632b158c6373582d415a5abe",
                "632b158c6373582d415a5ad1",
                "632b158c6373582d415a5ad9",
                "632b158c6373582d415a5ada",
                "632c6acd6373582d415a8b96"
            ],
            "NetworkPorts": [
                "632b13c876752d32362fc189",
                "632c81e776752d32369da82f",
                "632c81ed76752d32369daa9c",
                "632c81fe76752d32369db10a"
            ],
            "NetworkPortMax": 8,
            "Name": "IFM #2 (bottom)",
            "ModuleId": 2,
            "On": true,
            "OperState": "OK",
            "PartNumber": "73-20533-03",
            "Pid": "UCSX-I-9108-25G",
            "Presence": "equipped",
            "ProductName": "Cisco UCS 9108-25G",
            "Serial": "FCH261770RN",
            "Side": "bottom",
            "Version": "4.2(2c)",
            "NetworkPortCount": 4,
            "NetworkPortUp": 4,
            "NetworkPortSummary": "4/4/8"
        }
    ],
    "HostPortInfo": [
        {
            "Moid": "632b175c6373582d42a02282",
            "Dn": "chassis-1-ioc-1-muxhostport-port-1",
            "Name": "1/1/1",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:83",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316eab",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1283,
            "PortId": 1,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 1
        },
        {
            "Moid": "632b175c6373582d42a02283",
            "Dn": "chassis-1-ioc-1-muxhostport-port-2",
            "Name": "1/1/2",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:84",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316eac",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1283,
            "PortId": 2,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 1
        },
        {
            "Moid": "632b175c6373582d42a02284",
            "Dn": "chassis-1-ioc-1-muxhostport-port-3",
            "Name": "1/1/3",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:85",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 3,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02285",
            "Dn": "chassis-1-ioc-1-muxhostport-port-4",
            "Name": "1/1/4",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:86",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 4,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02286",
            "Dn": "chassis-1-ioc-1-muxhostport-port-5",
            "Name": "1/1/5",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:87",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bc0",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1280,
            "PortId": 5,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 2
        },
        {
            "Moid": "632b175c6373582d42a02287",
            "Dn": "chassis-1-ioc-1-muxhostport-port-6",
            "Name": "1/1/6",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:88",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bc5",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1280,
            "PortId": 6,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 2
        },
        {
            "Moid": "632b175c6373582d42a02288",
            "Dn": "chassis-1-ioc-1-muxhostport-port-7",
            "Name": "1/1/7",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:89",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 7,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02289",
            "Dn": "chassis-1-ioc-1-muxhostport-port-8",
            "Name": "1/1/8",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8A",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 8,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0228a",
            "Dn": "chassis-1-ioc-1-muxhostport-port-9",
            "Name": "1/1/9",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8B",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc5",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1281,
            "PortId": 9,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 3
        },
        {
            "Moid": "632b175c6373582d42a0228b",
            "Dn": "chassis-1-ioc-1-muxhostport-port-10",
            "Name": "1/1/10",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8C",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc6",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1281,
            "PortId": 10,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 3
        },
        {
            "Moid": "632b175c6373582d42a0226c",
            "Dn": "chassis-1-ioc-1-muxhostport-port-11",
            "Name": "1/1/11",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8D",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 11,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0226d",
            "Dn": "chassis-1-ioc-1-muxhostport-port-12",
            "Name": "1/1/12",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8E",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 12,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0226e",
            "Dn": "chassis-1-ioc-1-muxhostport-port-13",
            "Name": "1/1/13",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:8F",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee3",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1282,
            "PortId": 13,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 4
        },
        {
            "Moid": "632b175c6373582d42a0226f",
            "Dn": "chassis-1-ioc-1-muxhostport-port-14",
            "Name": "1/1/14",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:90",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee4",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1282,
            "PortId": 14,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 4
        },
        {
            "Moid": "632b175c6373582d42a02270",
            "Dn": "chassis-1-ioc-1-muxhostport-port-15",
            "Name": "1/1/15",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:91",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 15,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02271",
            "Dn": "chassis-1-ioc-1-muxhostport-port-16",
            "Name": "1/1/16",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:92",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 16,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02272",
            "Dn": "chassis-1-ioc-1-muxhostport-port-17",
            "Name": "1/1/17",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:93",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 17,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02273",
            "Dn": "chassis-1-ioc-1-muxhostport-port-18",
            "Name": "1/1/18",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:94",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 18,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02274",
            "Dn": "chassis-1-ioc-1-muxhostport-port-19",
            "Name": "1/1/19",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:95",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 19,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02275",
            "Dn": "chassis-1-ioc-1-muxhostport-port-20",
            "Name": "1/1/20",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:96",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 20,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02276",
            "Dn": "chassis-1-ioc-1-muxhostport-port-21",
            "Name": "1/1/21",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:97",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 21,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02277",
            "Dn": "chassis-1-ioc-1-muxhostport-port-22",
            "Name": "1/1/22",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:98",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 22,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02278",
            "Dn": "chassis-1-ioc-1-muxhostport-port-23",
            "Name": "1/1/23",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:99",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 23,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02279",
            "Dn": "chassis-1-ioc-1-muxhostport-port-24",
            "Name": "1/1/24",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9A",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 24,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0227a",
            "Dn": "chassis-1-ioc-1-muxhostport-port-25",
            "Name": "1/1/25",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9B",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 25,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0227b",
            "Dn": "chassis-1-ioc-1-muxhostport-port-26",
            "Name": "1/1/26",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9C",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 26,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0227c",
            "Dn": "chassis-1-ioc-1-muxhostport-port-27",
            "Name": "1/1/27",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9D",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 27,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0227d",
            "Dn": "chassis-1-ioc-1-muxhostport-port-28",
            "Name": "1/1/28",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9E",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 28,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0227e",
            "Dn": "chassis-1-ioc-1-muxhostport-port-29",
            "Name": "1/1/29",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:9F",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 29,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a0227f",
            "Dn": "chassis-1-ioc-1-muxhostport-port-30",
            "Name": "1/1/30",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:A0",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 30,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02280",
            "Dn": "chassis-1-ioc-1-muxhostport-port-31",
            "Name": "1/1/31",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:A1",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 31,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b175c6373582d42a02281",
            "Dn": "chassis-1-ioc-1-muxhostport-port-32",
            "Name": "1/1/32",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "A8:4F:B1:55:4D:A2",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 32,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b1fcc6373582d42a023ab",
            "Dn": "chassis-1-ioc-1-muxhostport-port-33",
            "Name": "1/1/33",
            "IoModuleId": "632b13c976752d32362fc244",
            "MacAddress": "00:00:00:00:00:00",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 33,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "B",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5abe",
            "Dn": "chassis-1-ioc-2-muxhostport-port-1",
            "Name": "1/1/1",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C3",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316ea9",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1287,
            "PortId": 1,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 1
        },
        {
            "Moid": "632b158c6373582d415a5abf",
            "Dn": "chassis-1-ioc-2-muxhostport-port-2",
            "Name": "1/1/2",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C4",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b19af76752d3236316eaa",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1287,
            "PortId": 2,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 1
        },
        {
            "Moid": "632b158c6373582d415a5ac0",
            "Dn": "chassis-1-ioc-2-muxhostport-port-3",
            "Name": "1/1/3",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C5",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 3,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ac1",
            "Dn": "chassis-1-ioc-2-muxhostport-port-4",
            "Name": "1/1/4",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C6",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 4,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ac2",
            "Dn": "chassis-1-ioc-2-muxhostport-port-5",
            "Name": "1/1/5",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C7",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bb7",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1284,
            "PortId": 5,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac3",
            "Dn": "chassis-1-ioc-2-muxhostport-port-6",
            "Name": "1/1/6",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C8",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188b76752d3236311bbe",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1284,
            "PortId": 6,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 2
        },
        {
            "Moid": "632b158c6373582d415a5ac4",
            "Dn": "chassis-1-ioc-2-muxhostport-port-7",
            "Name": "1/1/7",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:C9",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 7,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ac5",
            "Dn": "chassis-1-ioc-2-muxhostport-port-8",
            "Name": "1/1/8",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CA",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 8,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ac6",
            "Dn": "chassis-1-ioc-2-muxhostport-port-9",
            "Name": "1/1/9",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CB",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc3",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1285,
            "PortId": 9,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 3
        },
        {
            "Moid": "632b158c6373582d415a5ac7",
            "Dn": "chassis-1-ioc-2-muxhostport-port-10",
            "Name": "1/1/10",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CC",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b188d76752d3236311cc4",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1285,
            "PortId": 10,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 3
        },
        {
            "Moid": "632b158c6373582d415a5ac8",
            "Dn": "chassis-1-ioc-2-muxhostport-port-11",
            "Name": "1/1/11",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CD",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 11,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ac9",
            "Dn": "chassis-1-ioc-2-muxhostport-port-12",
            "Name": "1/1/12",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CE",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 12,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5aca",
            "Dn": "chassis-1-ioc-2-muxhostport-port-13",
            "Name": "1/1/13",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:CF",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee1",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1286,
            "PortId": 13,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 4
        },
        {
            "Moid": "632b158c6373582d415a5acb",
            "Dn": "chassis-1-ioc-2-muxhostport-port-14",
            "Name": "1/1/14",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D0",
            "Mode": "vntag",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "link-failure",
            "PeerDn": "",
            "PeerInterfaceId": "632b189176752d3236311ee2",
            "PeerInterfaceType": "adapter.ExtEthInterface",
            "PortChannelId": 1286,
            "PortId": 14,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "BladeServer",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML",
            "PeerNodeId": 4
        },
        {
            "Moid": "632b158c6373582d415a5acc",
            "Dn": "chassis-1-ioc-2-muxhostport-port-15",
            "Name": "1/1/15",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D1",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 15,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5acd",
            "Dn": "chassis-1-ioc-2-muxhostport-port-16",
            "Name": "1/1/16",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D2",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 16,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ace",
            "Dn": "chassis-1-ioc-2-muxhostport-port-17",
            "Name": "1/1/17",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D3",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 17,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5acf",
            "Dn": "chassis-1-ioc-2-muxhostport-port-18",
            "Name": "1/1/18",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D4",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 18,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad0",
            "Dn": "chassis-1-ioc-2-muxhostport-port-19",
            "Name": "1/1/19",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D5",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 19,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad1",
            "Dn": "chassis-1-ioc-2-muxhostport-port-20",
            "Name": "1/1/20",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D6",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 20,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad2",
            "Dn": "chassis-1-ioc-2-muxhostport-port-21",
            "Name": "1/1/21",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D7",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 21,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad3",
            "Dn": "chassis-1-ioc-2-muxhostport-port-22",
            "Name": "1/1/22",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D8",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 22,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad4",
            "Dn": "chassis-1-ioc-2-muxhostport-port-23",
            "Name": "1/1/23",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:D9",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 23,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad5",
            "Dn": "chassis-1-ioc-2-muxhostport-port-24",
            "Name": "1/1/24",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DA",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 24,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad6",
            "Dn": "chassis-1-ioc-2-muxhostport-port-25",
            "Name": "1/1/25",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DB",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 25,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad7",
            "Dn": "chassis-1-ioc-2-muxhostport-port-26",
            "Name": "1/1/26",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DC",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 26,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad8",
            "Dn": "chassis-1-ioc-2-muxhostport-port-27",
            "Name": "1/1/27",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DD",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 27,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ad9",
            "Dn": "chassis-1-ioc-2-muxhostport-port-28",
            "Name": "1/1/28",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DE",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 28,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5ada",
            "Dn": "chassis-1-ioc-2-muxhostport-port-29",
            "Name": "1/1/29",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:DF",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 29,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5adb",
            "Dn": "chassis-1-ioc-2-muxhostport-port-30",
            "Name": "1/1/30",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:E0",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 30,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5adc",
            "Dn": "chassis-1-ioc-2-muxhostport-port-31",
            "Name": "1/1/31",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:E1",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 31,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632b158c6373582d415a5add",
            "Dn": "chassis-1-ioc-2-muxhostport-port-32",
            "Name": "1/1/32",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "A8:4F:B1:55:4A:E2",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 32,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        },
        {
            "Moid": "632c6acd6373582d415a8b96",
            "Dn": "chassis-1-ioc-2-muxhostport-port-33",
            "Name": "1/1/33",
            "IoModuleId": "632b13c876752d32362fc17c",
            "MacAddress": "00:00:00:00:00:00",
            "Mode": "access",
            "ModuleId": 1,
            "OperSpeed": "auto",
            "OperState": "down",
            "Up": false,
            "OperStateQual": "admin-down",
            "PeerDn": "",
            "PeerInterfaceId": null,
            "PeerInterfaceType": null,
            "PortChannelId": 0,
            "PortId": 33,
            "PortType": "Ethernet",
            "SlotId": 1,
            "Speed": "auto",
            "SwitchId": "A",
            "Role": "unknown",
            "TransceiverType": "unknown",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerInfo": "",
            "PeerNodeId": null
        }
    ],
    "NodeInfo": [
        {
            "Moid": "632b174e76752d323630bb47",
            "Dn": "/redfish/v1/Systems/FCH26167MMZ",
            "Name": "ucsX-1-1",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167MMZ",
            "HardwareUuid": "8A552335-ED7E-4A28-924D-BE8748DA5BF8",
            "ServiceProfile": "",
            "SlotId": 1,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        },
        {
            "Moid": "632b163d76752d323630734f",
            "Dn": "/redfish/v1/Systems/FCH26167L94",
            "Name": "ucsX-1-2",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167L94",
            "HardwareUuid": "D576BED6-EF35-439C-B088-0735FED04410",
            "ServiceProfile": "",
            "SlotId": 2,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        },
        {
            "Moid": "632b163e76752d32363073aa",
            "Dn": "/redfish/v1/Systems/FCH26167MQK",
            "Name": "ucsX-1-3",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167MQK",
            "HardwareUuid": "0607F131-46C2-4CDC-B237-1F872D01E441",
            "ServiceProfile": "",
            "SlotId": 3,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        },
        {
            "Moid": "632b163f76752d32363073f7",
            "Dn": "/redfish/v1/Systems/FCH26167MHB",
            "Name": "ucsX-1-4",
            "Model": "UCSX-210C-M6",
            "Serial": "FCH26167MHB",
            "HardwareUuid": "6918688F-1B00-4DDB-A6E3-D316F6D07F64",
            "ServiceProfile": "",
            "SlotId": 4,
            "AlarmCritical": 0,
            "AlarmWarning": 0,
            "Health": "Healthy",
            "HealthSummary": "Healthy",
            "OperPowerState": "off",
            "PowerOn": false,
            "NumAdaptors": 1,
            "NumCpuCores": 64,
            "NumCpuCoresEnabled": 64,
            "NumCpus": 2,
            "NumThreads": 128,
            "CpuSummary": "2S 64C 128T",
            "TotalMemory": 1048576,
            "TotalMemoryUnit": "1.0 [TiB]",
            "NumEthHostInterfaces": 0,
            "NumFcHostInterfaces": 0
        }
    ],
    "AdapterUnitInfo": [
        {
            "Moid": "632b188376752d3236311708",
            "Dn": "/redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0",
            "AdapterId": "UCSX-V4-Q25GML_FCH26217EZ0",
            "BaseMacAddress": "48:2E:72:E4:50:28",
            "ComputeNodeMoid": "632b163d76752d323630734f",
            "ExtEthIfsIds": [
                "632b188b76752d3236311bb7",
                "632b188b76752d3236311bbe",
                "632b188b76752d3236311bc0",
                "632b188b76752d3236311bc5"
            ],
            "Model": "UCSX-V4-Q25GML",
            "OperState": "OK",
            "Presence": "equipped",
            "Healthy": true,
            "Serial": "FCH26217EZ0",
            "PciSlot": "SlotID:0-MLOM",
            "ComputeNodeId": 2,
            "ComputeNodePowerOn": false
        },
        {
            "Moid": "632b188476752d3236311879",
            "Dn": "/redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77",
            "AdapterId": "UCSX-V4-Q25GML_FCH26217F77",
            "BaseMacAddress": "48:2E:72:E4:52:60",
            "ComputeNodeMoid": "632b163e76752d32363073aa",
            "ExtEthIfsIds": [
                "632b188d76752d3236311cc3",
                "632b188d76752d3236311cc4",
                "632b188d76752d3236311cc5",
                "632b188d76752d3236311cc6"
            ],
            "Model": "UCSX-V4-Q25GML",
            "OperState": "OK",
            "Presence": "equipped",
            "Healthy": true,
            "Serial": "FCH26217F77",
            "PciSlot": "SlotID:0-MLOM",
            "ComputeNodeId": 3,
            "ComputeNodePowerOn": false
        },
        {
            "Moid": "632b188576752d32363119ed",
            "Dn": "/redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72",
            "AdapterId": "UCSX-V4-Q25GML_FCH26217F72",
            "BaseMacAddress": "48:2E:72:E4:52:68",
            "ComputeNodeMoid": "632b163f76752d32363073f7",
            "ExtEthIfsIds": [
                "632b189176752d3236311ee1",
                "632b189176752d3236311ee2",
                "632b189176752d3236311ee3",
                "632b189176752d3236311ee4"
            ],
            "Model": "UCSX-V4-Q25GML",
            "OperState": "OK",
            "Presence": "equipped",
            "Healthy": true,
            "Serial": "FCH26217F72",
            "PciSlot": "SlotID:0-MLOM",
            "ComputeNodeId": 4,
            "ComputeNodePowerOn": false
        },
        {
            "Moid": "632b19a776752d3236316cb1",
            "Dn": "/redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU",
            "AdapterId": "UCSX-V4-Q25GML_FCH26217FVU",
            "BaseMacAddress": "48:2E:72:E4:50:40",
            "ComputeNodeMoid": "632b174e76752d323630bb47",
            "ExtEthIfsIds": [
                "632b19af76752d3236316ea9",
                "632b19af76752d3236316eaa",
                "632b19af76752d3236316eab",
                "632b19af76752d3236316eac"
            ],
            "Model": "UCSX-V4-Q25GML",
            "OperState": "OK",
            "Presence": "equipped",
            "Healthy": true,
            "Serial": "FCH26217FVU",
            "PciSlot": "SlotID:0-MLOM",
            "ComputeNodeId": 1,
            "ComputeNodePowerOn": false
        }
    ],
    "AdapterExtEthInterfaceInfo": [
        {
            "Moid": "632b188b76752d3236311bb7",
            "Dn": "/redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0/iom-id-2/ext-eth-1",
            "AdapterUnitId": "632b188376752d3236311708",
            "AdminState": "Enabled",
            "InterfaceId": "1",
            "MacAddress": "48:2E:72:E4:50:29",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5ac2",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-5",
            "PeerPortId": 5,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163d76752d323630734f",
            "ComputeNodeId": 2,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217EZ0",
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188b76752d3236311bbe",
            "Dn": "/redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0/iom-id-2/ext-eth-2",
            "AdapterUnitId": "632b188376752d3236311708",
            "AdminState": "Enabled",
            "InterfaceId": "2",
            "MacAddress": "48:2E:72:E4:50:2A",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5ac3",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-6",
            "PeerPortId": 6,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163d76752d323630734f",
            "ComputeNodeId": 2,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217EZ0",
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188b76752d3236311bc0",
            "Dn": "/redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0/iom-id-1/ext-eth-3",
            "AdapterUnitId": "632b188376752d3236311708",
            "AdminState": "Enabled",
            "InterfaceId": "3",
            "MacAddress": "48:2E:72:E4:50:2B",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a02286",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-5",
            "PeerPortId": 5,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163d76752d323630734f",
            "ComputeNodeId": 2,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217EZ0",
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188b76752d3236311bc5",
            "Dn": "/redfish/v1/Chassis/FCH26167L94/NetworkAdapters/UCSX-V4-Q25GML_FCH26217EZ0/iom-id-1/ext-eth-4",
            "AdapterUnitId": "632b188376752d3236311708",
            "AdminState": "Enabled",
            "InterfaceId": "4",
            "MacAddress": "48:2E:72:E4:50:2C",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a02287",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-6",
            "PeerPortId": 6,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163d76752d323630734f",
            "ComputeNodeId": 2,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217EZ0",
            "PeerInfo": "Node #2 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188d76752d3236311cc3",
            "Dn": "/redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77/iom-id-2/ext-eth-1",
            "AdapterUnitId": "632b188476752d3236311879",
            "AdminState": "Enabled",
            "InterfaceId": "1",
            "MacAddress": "48:2E:72:E4:52:61",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5ac6",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-9",
            "PeerPortId": 9,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163e76752d32363073aa",
            "ComputeNodeId": 3,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F77",
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188d76752d3236311cc4",
            "Dn": "/redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77/iom-id-2/ext-eth-2",
            "AdapterUnitId": "632b188476752d3236311879",
            "AdminState": "Enabled",
            "InterfaceId": "2",
            "MacAddress": "48:2E:72:E4:52:62",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5ac7",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-10",
            "PeerPortId": 10,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163e76752d32363073aa",
            "ComputeNodeId": 3,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F77",
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188d76752d3236311cc5",
            "Dn": "/redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77/iom-id-1/ext-eth-3",
            "AdapterUnitId": "632b188476752d3236311879",
            "AdminState": "Enabled",
            "InterfaceId": "3",
            "MacAddress": "48:2E:72:E4:52:63",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a0228a",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-9",
            "PeerPortId": 9,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163e76752d32363073aa",
            "ComputeNodeId": 3,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F77",
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b188d76752d3236311cc6",
            "Dn": "/redfish/v1/Chassis/FCH26167MQK/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F77/iom-id-1/ext-eth-4",
            "AdapterUnitId": "632b188476752d3236311879",
            "AdminState": "Enabled",
            "InterfaceId": "4",
            "MacAddress": "48:2E:72:E4:52:64",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a0228b",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-10",
            "PeerPortId": 10,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163e76752d32363073aa",
            "ComputeNodeId": 3,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F77",
            "PeerInfo": "Node #3 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b189176752d3236311ee1",
            "Dn": "/redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72/iom-id-2/ext-eth-1",
            "AdapterUnitId": "632b188576752d32363119ed",
            "AdminState": "Enabled",
            "InterfaceId": "1",
            "MacAddress": "48:2E:72:E4:52:69",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5aca",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-13",
            "PeerPortId": 13,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163f76752d32363073f7",
            "ComputeNodeId": 4,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F72",
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b189176752d3236311ee2",
            "Dn": "/redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72/iom-id-2/ext-eth-2",
            "AdapterUnitId": "632b188576752d32363119ed",
            "AdminState": "Enabled",
            "InterfaceId": "2",
            "MacAddress": "48:2E:72:E4:52:6A",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5acb",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-14",
            "PeerPortId": 14,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163f76752d32363073f7",
            "ComputeNodeId": 4,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F72",
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b189176752d3236311ee3",
            "Dn": "/redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72/iom-id-1/ext-eth-3",
            "AdapterUnitId": "632b188576752d32363119ed",
            "AdminState": "Enabled",
            "InterfaceId": "3",
            "MacAddress": "48:2E:72:E4:52:6B",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a0226e",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-13",
            "PeerPortId": 13,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163f76752d32363073f7",
            "ComputeNodeId": 4,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F72",
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b189176752d3236311ee4",
            "Dn": "/redfish/v1/Chassis/FCH26167MHB/NetworkAdapters/UCSX-V4-Q25GML_FCH26217F72/iom-id-1/ext-eth-4",
            "AdapterUnitId": "632b188576752d32363119ed",
            "AdminState": "Enabled",
            "InterfaceId": "4",
            "MacAddress": "48:2E:72:E4:52:6C",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a0226f",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-14",
            "PeerPortId": 14,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b163f76752d32363073f7",
            "ComputeNodeId": 4,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217F72",
            "PeerInfo": "Node #4 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b19af76752d3236316ea9",
            "Dn": "/redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU/iom-id-2/ext-eth-1",
            "AdapterUnitId": "632b19a776752d3236316cb1",
            "AdminState": "Enabled",
            "InterfaceId": "1",
            "MacAddress": "48:2E:72:E4:50:41",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5abe",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-1",
            "PeerPortId": 1,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b174e76752d323630bb47",
            "ComputeNodeId": 1,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217FVU",
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b19af76752d3236316eaa",
            "Dn": "/redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU/iom-id-2/ext-eth-2",
            "AdapterUnitId": "632b19a776752d3236316cb1",
            "AdminState": "Enabled",
            "InterfaceId": "2",
            "MacAddress": "48:2E:72:E4:50:42",
            "SwitchId": "A",
            "PeerHostPortId": "632b158c6373582d415a5abf",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-2-muxhostport-port-2",
            "PeerPortId": 2,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b174e76752d323630bb47",
            "ComputeNodeId": 1,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217FVU",
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b19af76752d3236316eab",
            "Dn": "/redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU/iom-id-1/ext-eth-3",
            "AdapterUnitId": "632b19a776752d3236316cb1",
            "AdminState": "Enabled",
            "InterfaceId": "3",
            "MacAddress": "48:2E:72:E4:50:43",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a02282",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-1",
            "PeerPortId": 1,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b174e76752d323630bb47",
            "ComputeNodeId": 1,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217FVU",
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        },
        {
            "Moid": "632b19af76752d3236316eac",
            "Dn": "/redfish/v1/Chassis/FCH26167MMZ/NetworkAdapters/UCSX-V4-Q25GML_FCH26217FVU/iom-id-1/ext-eth-4",
            "AdapterUnitId": "632b19a776752d3236316cb1",
            "AdminState": "Enabled",
            "InterfaceId": "4",
            "MacAddress": "48:2E:72:E4:50:44",
            "SwitchId": "B",
            "PeerHostPortId": "632b175c6373582d42a02283",
            "PeerAggrPortId": 0,
            "PeerDn": "chassis-1-ioc-1-muxhostport-port-2",
            "PeerPortId": 2,
            "PeerSlotId": 1,
            "ComputeNodeMoid": "632b174e76752d323630bb47",
            "ComputeNodeId": 1,
            "ComputeNodePowerOn": false,
            "ComputeNodeSlot": "SlotID:0-MLOM",
            "AdepterModel": "UCSX-V4-Q25GML",
            "AdepterOperState": "OK",
            "AdepterPresence": "equipped",
            "AdepterSerial": "FCH26217FVU",
            "PeerInfo": "Node #1 (P-) SlotID:0-MLOM UCSX-V4-Q25GML"
        }
    ],
    "NetworkPortInfo": [
        {
            "Moid": "632b13c976752d32362fc25a",
            "Dn": "chassis-1-ioc-1-slot-1-port-1",
            "Name": "1/1",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a64",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 1,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerSwitchId": "B",
            "PeerPortName": "1/17",
            "PeerPortChannelId": 1153,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632c81ec76752d32369daa08",
            "Dn": "chassis-1-ioc-1-slot-1-port-2",
            "Name": "1/2",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a6a",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 2,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerSwitchId": "B",
            "PeerPortName": "1/19",
            "PeerPortChannelId": 1153,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632c81f276752d32369dac8d",
            "Dn": "chassis-1-ioc-1-slot-1-port-3",
            "Name": "1/3",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a14",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 3,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerSwitchId": "B",
            "PeerPortName": "1/21",
            "PeerPortChannelId": 1153,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632c820576752d32369db290",
            "Dn": "chassis-1-ioc-1-slot-1-port-4",
            "Name": "1/4",
            "IoModuleId": "632b13c976752d32362fc244",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994c76752d3236cd9a6c",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 4,
            "SlotId": 1,
            "Speed": "10G",
            "SwitchId": "B",
            "IfmDn": "chassis-1-ioc-1",
            "IfmName": "IFM #1 (top)",
            "IfmId": 1,
            "PeerSwitchId": "B",
            "PeerPortName": "1/23",
            "PeerPortChannelId": 1153,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632b13c876752d32362fc189",
            "Dn": "chassis-1-ioc-2-slot-2-port-1",
            "Name": "2/1",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd9923",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 1,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerSwitchId": "A",
            "PeerPortName": "1/17",
            "PeerPortChannelId": 1025,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632c81e776752d32369da82f",
            "Dn": "chassis-1-ioc-2-slot-2-port-2",
            "Name": "2/2",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd98da",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 2,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerSwitchId": "A",
            "PeerPortName": "1/19",
            "PeerPortChannelId": 1025,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632c81ed76752d32369daa9c",
            "Dn": "chassis-1-ioc-2-slot-2-port-3",
            "Name": "2/3",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd98dd",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 3,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerSwitchId": "A",
            "PeerPortName": "1/21",
            "PeerPortChannelId": 1025,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        },
        {
            "Moid": "632c81fe76752d32369db10a",
            "Dn": "chassis-1-ioc-2-slot-2-port-4",
            "Name": "2/4",
            "IoModuleId": "632b13c876752d32362fc17c",
            "ModuleId": 0,
            "OperState": "up",
            "Up": true,
            "PeerDn": "",
            "PeerInterfaceId": "6329994b76752d3236cd98d0",
            "PeerInterfaceType": "ether.PhysicalPort",
            "PortId": 4,
            "SlotId": 2,
            "Speed": "10G",
            "SwitchId": "A",
            "IfmDn": "chassis-1-ioc-2",
            "IfmName": "IFM #2 (bottom)",
            "IfmId": 2,
            "PeerSwitchId": "A",
            "PeerPortName": "1/23",
            "PeerPortChannelId": 1025,
            "PeerPortTransceiverType": "SFP-25G-AOC2M",
            "PeerOperSpeed": "25G"
        }
    ],
    "PhysicalPortInfo": [
        {
            "Moid": "6329994b76752d3236cd98d0",
            "Dn": "switch-FDO26340DE3/slot-1/switch-ether/port-23",
            "Name": "1/23",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:5E",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 23,
            "PortChannelId": 1025,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "A",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994b76752d3236cd98da",
            "Dn": "switch-FDO26340DE3/slot-1/switch-ether/port-19",
            "Name": "1/19",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:5A",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 19,
            "PortChannelId": 1025,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "A",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994b76752d3236cd98dd",
            "Dn": "switch-FDO26340DE3/slot-1/switch-ether/port-21",
            "Name": "1/21",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:5C",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 21,
            "PortChannelId": 1025,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "A",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994b76752d3236cd9923",
            "Dn": "switch-FDO26340DE3/slot-1/switch-ether/port-17",
            "Name": "1/17",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:58",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 17,
            "PortChannelId": 1025,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "A",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994c76752d3236cd9a14",
            "Dn": "switch-FDO26340CVC/slot-1/switch-ether/port-21",
            "Name": "1/21",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:BC",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 21,
            "PortChannelId": 1153,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "B",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994c76752d3236cd9a64",
            "Dn": "switch-FDO26340CVC/slot-1/switch-ether/port-17",
            "Name": "1/17",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:B8",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 17,
            "PortChannelId": 1153,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "B",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994c76752d3236cd9a6a",
            "Dn": "switch-FDO26340CVC/slot-1/switch-ether/port-19",
            "Name": "1/19",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:BA",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 19,
            "PortChannelId": 1153,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "B",
            "TransceiverType": "SFP-25G-AOC2M"
        },
        {
            "Moid": "6329994c76752d3236cd9a6c",
            "Dn": "switch-FDO26340CVC/slot-1/switch-ether/port-23",
            "Name": "1/23",
            "AdminState": "Enabled",
            "AggregatePortId": 0,
            "MacAddress": "00:08:31:1B:AA:BE",
            "Mode": "fex-fabric",
            "OperSpeed": "25G",
            "OperState": "up",
            "PortId": 23,
            "PortChannelId": 1153,
            "Role": "Server",
            "SlotId": 1,
            "SwitchId": "B",
            "TransceiverType": "SFP-25G-AOC2M"
        }
    ]
}
[2022-11-17 10:16:26.577386]	[chassis_info.print_ports]	{
    "enabled": true,
    "type": null,
    "state": null,
    "module": null,
    "node": null
}


Log: isctl
-----------

2022-11-17 10:16:15.113028	True	1564	2	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2022-11-17 10:16:17.184269	True	2064	2	isctl get equipment iocard --filter "Parent/Moid eq '632b13c876752d32362fc175'"  -o json --top 100
2022-11-17 10:16:18.694504	True	1505	66	isctl get ether hostport --filter "EquipmentIoCardBase/Moid in ('632b13c876752d32362fc17c', '632b13c976752d32362fc244')"  -o json --top 100
2022-11-17 10:16:19.941413	True	1234	4	isctl get compute blade --filter "EquipmentChassis/Moid eq '632b13c876752d32362fc175'"  -o json --top 100
2022-11-17 10:16:21.518923	True	1556	4	isctl get adapter unit --filter "Parent/Moid in ('632b163d76752d323630734f', '632b163e76752d32363073aa', '632b163f76752d32363073f7', '632b174e76752d323630bb47')"  -o json --top 100
2022-11-17 10:16:23.102786	True	1549	16	isctl get adapter extethinterface --filter "Parent/Moid in ('632b188376752d3236311708', '632b188476752d3236311879', '632b188576752d32363119ed', '632b19a776752d3236316cb1')"  -o json --top 100
2022-11-17 10:16:24.402865	True	1280	8	isctl get ether networkport --filter "EquipmentIoCardBase/Moid in ('632b13c876752d32362fc17c', '632b13c976752d32362fc244')"  -o json --top 100
2022-11-17 10:16:26.037136	True	1615	8	isctl get ether physicalport --filter "Moid in ('6329994b76752d3236cd9923', '6329994c76752d3236cd9a64', '6329994b76752d3236cd98da', '6329994c76752d3236cd9a6a', '6329994b76752d3236cd98dd', '6329994c76752d3236cd9a14', '6329994b76752d3236cd98d0', '6329994c76752d3236cd9a6c')"  -o json --top 100
```