# UCSX-9508 node monitoring with Intersight API

![API](image/api-node.png)

## equipment.Chassis

Intersight API object relationships:
- reference to nodes via Blades[]

```
API_DEBUG:get_ucsx_node.overview:equipment chassis:0
```

## compute.Blade

Intersight API object relationships:
- reference to equipment.Chassis via Parent/Moid

```
API_DEBUG:get_ucsx_node.overview:compute blade:1
```