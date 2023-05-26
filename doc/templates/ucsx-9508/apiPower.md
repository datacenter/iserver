# UCSX-9508 power monitoring with Intersight API

![API](image/api-psu.png)

## equipment.Chassis

Intersight API object relationships:
- reference to power control vua PowerControlState/Moid
- reference to psu modules via Psus[]

```
API_DEBUG:get_ucsx_power.overview:equipment chassis:0
```

## power.ControlState

Intersight API object relationships:
- reference to equipment.Chassis via Parent/Moid

```
API_DEBUG:get_ucsx_power.overview:power controlstate:0
```

## equipment.PsuControl

Intersight API object relationships:
- reference to equipment.Chassis via Parent/Moid

```
API_DEBUG:get_ucsx_power.overview:equipment psucontrol:0
```

## equipment.Psu

Intersight API object relationships:
- reference to equipment.Chassis via Parent/Moid

```
API_DEBUG:get_ucsx_power.overview:equipment psu:1
```