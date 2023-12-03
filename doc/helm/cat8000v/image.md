# Cat8000v image

Follow this steps to prepare cat8000v image on your OpenShift cluster. The name of the image (dv/pvc) will be further used in the values.yaml in the helm chart.

Requirements:
- cat8000v qcow image downloaded to the machine
- oc and virtctl commands

Step 1: image

```
$ ls -lta c8000v-universalk9_8G_vga.17.06.05.qcow2
-rw-r--r--. 1 core core 1777860608 Oct  6 06:56 c8000v-universalk9_8G_vga.17.06.05.qcow2

$ md5sum c8000v-universalk9_8G_vga.17.06.05.qcow2
e18b32ca2a5f3795045d270df9f66594  c8000v-universalk9_8G_vga.17.06.05.qcow2
```

Step 2: data volume

```
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: cat8000v-image
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
        storage: 10Gi
```

```
$ oc apply -f image.yaml
datavolume.cdi.kubevirt.io/cat8000v-image created
```

It is expected that both data volume (dv) and persistent volume claim (pvc) are created. Make sure pvc is in Bound state.

```
$ oc get dv
NAME             PHASE         PROGRESS   RESTARTS   AGE
cat8000v-image   UploadReady   N/A                   12s
```

```
$ oc get pvc
NAME                     STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
cat8000v-image           Bound     pvc-7d506ab1-660f-4b01-893b-db4e395fb1df   10Gi       RWO            lvms-vg1       77s
cat8000v-image-scratch   Bound     pvc-8f286bf6-4ad6-4d6a-a7f8-91b9c7af4274   10Gi       RWO            lvms-vg1       76s
```

Step 3: upload image to data volume

```
$ virtctl image-upload dv cat8000v-image --no-create --image-path=./c8000v-universalk9_8G_vga.17.06.05.qcow2 --insecure
Using existing PVC default/cat8000v-image
Uploading data to https://cdi-uploadproxy-openshift-cnv.apps.ocp-bm1.ocp.lan

 1.66 GiB / 1.66 GiB [========================================================================================================================================] 100.00% 4s

Uploading data completed successfully, waiting for processing to complete, you can hit ctrl-c without interrupting the progress
Processing completed successfully
Uploading ./c8000v-universalk9_8G_vga.17.06.05.qcow2 completed successfully
```

Notes:
- data volume object is gone once the upload completes
- pvc -scratch is gone too
- only pvc that inherited the name from dv should remain

```
$ oc get pvc
NAME                    STATUS    VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
cat8000v-image          Bound     pvc-7d506ab1-660f-4b01-893b-db4e395fb1df   10Gi       RWO            lvms-vg1       5m6s
```

That's all. The cat8000v image is uploaded and ready to be used.