# Notes

```
[core@ocp-bm2 ~]$ sudo lvcreate -V 100M -T vg1/thin-pool-1 -n lalala
  Logical volume "lalala" created.
[core@ocp-bm2 ~]$ sudo lvs
  LV          VG  Attr       LSize   Pool        Origin Data%  Meta%  Move Log Cpy%Sync Convert
  lalala      vg1 Vwi-a-tz-- 100.00m thin-pool-1        0.00
  thin-pool-1 vg1 twi-aotz--  <1.77t                    0.00   2.17
```