# Physical Volume

[[Back]](./README.md)

## Workflow

- `sudo pvs --reportformat json`

## Example

```
# iserver get linux pv --server ocp:bm1:bm1-1

Physical Volume (LVM) [ocp:bm1:bm1-1]
-------------------------------------

+----------+-----+------+------+---------+---------+
| PV       | VG  | Fmt  | Attr | PSize   | PFree   |
+----------+-----+------+------+---------+---------+
| /dev/sda | vg1 | lvm2 | a--  | 894.25g | 0       | 
| /dev/sdb | vg1 | lvm2 | a--  | 894.25g | 894.25g | 
| /dev/sdc | vg1 | lvm2 | a--  | 894.25g | 0       | 
| /dev/sdd | vg1 | lvm2 | a--  | 894.25g | <89.43g | 
| /dev/sde | vg1 | lvm2 | a--  | 1.09t   | 0       | 
| /dev/sdf | vg1 | lvm2 | a--  | 1.09t   | 0       | 
| /dev/sdh | vg1 | lvm2 | a--  | 894.25g | 0       | 
| /dev/sdi | vg1 | lvm2 | a--  | 1.09t   | 0       | 
| /dev/sdj | vg1 | lvm2 | a--  | 894.25g | 0       | 
| /dev/sdk | vg1 | lvm2 | a--  | 1.09t   | 0       | 
+----------+-----+------+------+---------+---------+
```

[[Back]](./README.md)