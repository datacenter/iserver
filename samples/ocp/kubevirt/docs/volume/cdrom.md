# Cdrom Disk

Example (fedora09.yaml)

```
spec:
  template:
    spec:
      domain:
        devices:
          disks:
            - name: cdromdisk
            cdrom:
              readOnly: false
              bus: sata
      volumes:
        - name: cdromdisk
          persistentVolumeClaim:
            claimName: fedora-dv-cdrom
```

The cdrom content is in the pre-configured pvc. One way to create is the following

```
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: fedora-dv-cdrom
spec:
  source:
      upload: {}
  pvc:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 10Mi
```

followed with

```
# virtctl image-upload dv fedora-dv-cdrom --image-path=./csr1000v.iso --insecure
Using existing PVC default/fedora-dv-cdrom
Uploading data to https://cdi-uploadproxy-openshift-cnv.apps.kubevirt.ocp.lan

 350.00 KiB / 350.00 KiB [=================] 100.00% 0s

Uploading data completed successfully, waiting for processing to complete, you can hit ctrl-c without interrupting the progress
Processing completed successfully
Uploading ./csr1000v.iso completed successfully
```

When virtual machine boots, /dev/cdrom is there but still needs to be mounted to be seen

```
[root@fedora09 ~]# mkdir /cdrom
[root@fedora09 ~]# mount -t iso9660 /dev/cdrom /cdrom/
mount: /cdrom: WARNING: source write-protected, mounted read-only.
[root@fedora09 ~]# ls /cdrom/
iosxe_config.txt
```

An alternative approach is to add boot commands to make this step automated (cirros09a.yaml)

```
cloudInitNoCloud:
  userData: |-
    #cloud-config
    password: fedora
    chpasswd: { expire: False }
    bootcmd:
    - "mkdir /cdrom"
    - "mount -t iso9660 /dev/cdrom /cdrom/"
```
