# Delete LVM from block devices

If non-root disks are not formatted, they may have lvm filesystem from previous instance. This workflow will remove LVM entirely from the disks.

## Workflow 

- get lvs, vgs and pvs
- remove one-by-one

## Configurable options

```
# iserver delete linux lvm
  --server TEXT  Linux server name
  --no-confirm   Confirmation mode
```

## Example

```
# iserver delete linux lvm --server ocp:bm1:bm1-1 

LVM Cleanup [ocp:bm1:bm1-1]
---------------------------
- gettings lvs...
- gettings vgs...
- gettings pvs...
- deactivate vg: nvme-vg
  0 logical volume(s) in volume group "nvme-vg" now active

- delete vg: nvme-vg
  WARNING: Couldn't find device with uuid 58qUGn-51oz-K4wG-KQK4-1mGE-gxWh-hIeby1.
  WARNING: VG nvme-vg is missing PV 58qUGn-51oz-K4wG-KQK4-1mGE-gxWh-hIeby1 (last written to [unknown]).
  WARNING: Couldn't find device with uuid 58qUGn-51oz-K4wG-KQK4-1mGE-gxWh-hIeby1.
  Volume group "nvme-vg" not found, is inconsistent or has PVs missing.
  Consider vgreduce --removemissing if metadata is inconsistent.

[ERROR] Volume group delete failed
- reduce vg: nvme-vg
- delete (again) vg: nvme-vg
  Volume group "nvme-vg" successfully removed

- delete pv: /dev/nvme1n1
  Labels on physical volume "/dev/nvme1n1" successfully wiped.

- delete pv: /dev/nvme2n1
  Labels on physical volume "/dev/nvme2n1" successfully wiped.

- delete pv: /dev/nvme3n1
  Labels on physical volume "/dev/nvme3n1" successfully wiped.

- delete pv: /dev/nvme4n1
  Labels on physical volume "/dev/nvme4n1" successfully wiped.

- delete pv: /dev/nvme5n1
  Labels on physical volume "/dev/nvme5n1" successfully wiped.

- delete pv: /dev/nvme6n1
  Labels on physical volume "/dev/nvme6n1" successfully wiped.

- delete pv: /dev/nvme7n1
  Labels on physical volume "/dev/nvme7n1" successfully wiped.

- delete pv: /dev/nvme8n1
  Labels on physical volume "/dev/nvme8n1" successfully wiped.
```

[[Back]](./README.md)