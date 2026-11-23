# Volume Group

[[Back]](./README.md)

## Workflow

- `sudo vgs --reportformat json -o all`

## Example

```
# iserver get linux vg --server ocp:bm1:bm1-1

Volume Groups (LVM) [ocp:bm1:bm1-1]
-----------------------------------

+-----+-----+-----+--------+--------+----------+
| VG  | #PV | #LV | Attr   | VSize  | VFree    |
+-----+-----+-----+--------+--------+----------+
| vg1 | 10  | 3   | wz--n- | <9.61t | <983.68g | 
+-----+-----+-----+--------+--------+----------+
```

[[Back]](./README.md)