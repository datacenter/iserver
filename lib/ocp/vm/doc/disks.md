# Disk

Like all other vmi devices a spec.domain.devices.disks element has a mandatory name, and furthermore, the disk's name must reference the name of a volume inside spec.volumes.

A disk can be made accessible via four different types:
- lun
- disk
- cdrom

# Volumes

Supported volume sources are
- cloudInitNoCloud
- cloudInitConfigDrive
- persistentVolumeClaim
- dataVolume
- ephemeral
- containerDisk
- emptyDisk
- hostDisk
- configMap
- secret
- serviceAccount
- downwardMetrics

# ToDo

## CDROM device

```
metadata:
  name: testvmi-cdrom
apiVersion: kubevirt.io/v1
kind: VirtualMachineInstance
spec:
  domain:
    resources:
      requests:
        memory: 64M
    devices:
      disks:
      - name: mypvcdisk
        # This makes it a cdrom
        cdrom:
          # This makes the cdrom writeable
          readOnly: false
          # This makes the cdrom be exposed as SATA device
          bus: sata
  volumes:
    - name: mypvcdisk
      persistentVolumeClaim:
        claimName: mypvc
```
