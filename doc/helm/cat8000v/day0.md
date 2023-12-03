# Cat8000v day0

Follow this steps to prepare cat8000v day0 configuration file on your OpenShift cluster. The name of the dv/pvc will be further used in the values.yaml in the helm chart.

Requirements:
- genisoimage command
- oc and virtctl commands

Step 1: day0 configuration

```
hostname c8000v-generic-day0
!
aaa new-login
aaa authentication login default local
aaa authorization exec local
username admin privilege 15 secret Cisco_123
!
no ip http secure-server
crypto key generate rsa modulus 2048
ip ssh version 2
!
vrf definition Mgmt-intf
 address-family ipv4
 exit-address-family
!
interface GigabitEthernet1
    vrf forwarding Mgmt-intf
    ip address dhcp
    no shutdown
!
ip http secure-server
!
line con 0
    login authentication default
    length 0
line vty 0 4
    login authentication default
    length 0
```

Step 2: create iso

```
$ genisoimage -r -o ./c8000v_config.iso ./iosxe_config.txt
I: -input-charset not specified, using utf-8 (detected in locale settings)
Total translation table size: 0
Total rockridge attributes bytes: 257
Total directory bytes: 0
Path table size(bytes): 10
Max brk space used 0
176 extents written (0 MB)
```

```
$ file c8000v_config.iso
c8000v_config.iso: ISO 9660 CD-ROM filesystem data 'CDROM'
```

Step 3: data volume

```
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: cat8000v-generic-day0
  annotations:
    cdi.kubevirt.io/storage.bind.immediate.requested: "true"
spec:
  source:
      upload: {}
  pvc:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 1Gi
```

```
$ oc apply -f day0.yaml
datavolume.cdi.kubevirt.io/cat8000v-generic-day0 created
```

It is expected that both data volume (dv) and persistent volume claim (pvc) are created. Make sure pvc is in Bound state.

```
$ oc get dv
NAME                    PHASE         PROGRESS   RESTARTS   AGE
cat8000v-generic-day0   UploadReady   N/A                   16s
```

```
$ oc get pvc
NAME                            STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
cat8000v-generic-day0           Bound     pvc-d57c96fb-a6e2-4be0-8266-8cb5c9436b59   1Gi        RWO            lvms-vg1       20s
cat8000v-generic-day0-scratch   Bound     pvc-41f8ddc4-56c9-4a2d-b54d-9b529309d567   1Gi        RWO            lvms-vg1       20s
```

Step 4: upload day0 iso to data volume

```
$ virtctl image-upload dv cat8000v-generic-day0 --no-create --image-path=./c8000v_config.iso --insecure
Using existing PVC default/cat8000v-generic-day0
Uploading data to https://cdi-uploadproxy-openshift-cnv.apps.ocp-bm1.ocp.lan

 352.00 KiB / 352.00 KiB [====================================================================================================================================] 100.00% 0s

Uploading data completed successfully, waiting for processing to complete, you can hit ctrl-c without interrupting the progress
Processing completed successfully
Uploading ./c8000v_config.iso completed successfully
```

Notes:
- data volume object is gone once the upload completes
- pvc -scratch is gone too
- only pvc that inherited the name from dv should remain

```
$ oc get pvc
NAME                    STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
cat8000v-generic-day0   Bound     pvc-d57c96fb-a6e2-4be0-8266-8cb5c9436b59   1Gi        RWO            lvms-vg1       4m40s
```

That's all. The cat8000v generic day0 is uploaded and ready to be used.