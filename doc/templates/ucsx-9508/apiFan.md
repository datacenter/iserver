# UCSX-9508 fan monitoring with Intersight API

![API](image/api-fan.png)

## equipment.Chassis

Intersight API object relationships:
- reference to fan control via FanControl/Moid
- reference to fan modules via Fanmodules[]

```
API_DEBUG:get_ucsx_fan.overview:equipment chassis:0
```

## equipment.FanControl

Intersight API object relationships:
- reference to equipment.Chassis via Parent/Moid

```
API_DEBUG:get_ucsx_fan.overview:equipment fancontrol:0
```

## equipment.Fanmodule

Intersight API object relationships:
- reference to equipment.Chassis via Parent/Moid
- reference to fan objects via Fans[]

```
API_DEBUG:get_ucsx_fan.overview:equipment fanmodule:1
```

## equipment.Fan

Intersight API object relationships:
- reference to equipment.Fanmodule via Parent/Moid

```
API_DEBUG:get_ucsx_fan.overview:equipment fan:1
```