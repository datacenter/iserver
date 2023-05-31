# Data Volume

DataVolume automates importing virtual machine disks onto PVCs during the virtual machine's launch flow. PVC creation and import is automated on behalf of the user.

Target PVC content's source can be
- another pvc defined with namespace/name
- http defined with url and optional authentication related secret or certificate
- registry
Other source options not covered here: s3, imageio, registry.

When the VM is deleted, the storage provisioned by the DataVolume will automatically be deleted as well.

https://kubevirt.io/user-guide/virtual_machines/disks_and_volumes/

## CDI

Data Volume feature is implemented by Containerized Data Importer (CDI)

```
# oc get pod -A | grep cdi
openshift-cnv                                      cdi-apiserver-595c7b99cc-pnjhq                                    1/1     Running     0                 6d22h
openshift-cnv                                      cdi-deployment-59d7bb998-h8rc6                                    1/1     Running     659 (63m ago)     6d22h
openshift-cnv                                      cdi-operator-fb8f96655-8v62g                                      1/1     Running     560 (64m ago)     6d2h
openshift-cnv                                      cdi-uploadproxy-5f745d88dc-dvfzg                                  1/1     Running     0                 6d22h
```

API Server - manages the authorization to upload VM disks into PVCs by issuing secure upload tokens.
Upload Proxy - directs external disk upload traffic to the appropriate upload server pod so that it can be written to the correct PVC. Requires a valid upload token.
CDI Importer - (ephemeral) helper pod that imports a virtual machine image into a PVC when creating a data volume.

## Data Volume

Data Volume can be predefined

```
# oc get dvs -A
NAMESPACE                            NAME                          PHASE       PROGRESS   RESTARTS   AGE
default                              cirros-dv                     Succeeded   N/A                   7d17h
default                              cirros-registry               Succeeded   100.0%                3m47s
openshift-virtualization-os-images   centos-stream8-2f16c067b974                                     7d21h
openshift-virtualization-os-images   centos-stream9-0623716483a4                                     7d21h
openshift-virtualization-os-images   centos7-680e9b4e0fba                                            7d21h
openshift-virtualization-os-images   fedora-56ccabc01cbe                                             7d21h
openshift-virtualization-os-images   rhel8-b0bacbb4e426                                              7d21h
openshift-virtualization-os-images   rhel9-9d0d9575e03e                                              7d21h
```

Data Volumes in openshift-virtualization-os-images are pre-populated by OCP installer.

### Add data volume

```
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  name: cirros-registry
spec:
  pvc:
    accessModes:
      - ReadWriteOnce
    resources:
      requests:
        storage: 500Mi
    volumeMode: Filesystem
  source:
    registry:
      url: "docker://quay.io/kubevirt/cirros-container-disk-demo"
```

```
# oc get dvs
NAME              PHASE              PROGRESS   RESTARTS   AGE
cirros-registry   ImportInProgress   N/A                   9s

# oc get pod
NAME                       READY   STATUS      RESTARTS   AGE
importer-cirros-registry   0/1     Completed   0          13s

# oc get dvs
NAME              PHASE       PROGRESS   RESTARTS   AGE
cirros-registry   Succeeded   100.0%                21s

# oc get pvc
NAME              STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
cirros-registry   Bound    pvc-a672f8f3-64b4-401d-8208-9d53061183a8   500Mi      RWO            thin           25s
```

In this case, data volume creation triggers image import into PVC. Refer to 'source pvc' example how it can be used for virtual machine boot.

## Data Volume Template - Source pvc (cirros01.yaml)

Definition: Virtual machine disk => volume => Data Volume

```
spec:
  dataVolumeTemplates:
    - apiVersion: cdi.kubevirt.io/v1beta1
      kind: DataVolume
      metadata:
        name: cirros01
        namespace: default
      spec:
        pvc:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 500Mi
          volumeMode: Filesystem
        source:
          pvc:
            name: cirros-dv
            namespace: default
  template:
    spec:
      volumes:
        - dataVolume:
            name: cirros01
```

DataVolume definition refers to PVC as the source i.e. pvc must pre-exist.

```
# oc get pvc cirros-dv
NAME        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
cirros-dv   Bound    pvc-695af997-704a-4c04-866d-74e6b61cad2e   500Mi      RWO            thin           6d16h
```

This PVC was created indirectly, by creating DataVolume object followed with 'virtctl image-upload dv' command.

```
# oc get pvc cirros-dv -o yaml
  name: cirros-dv
  namespace: default
  ownerReferences:
  - apiVersion: cdi.kubevirt.io/v1beta1
    blockOwnerDeletion: true
    controller: true
    kind: DataVolume
    name: cirros-dv
    uid: 610ed029-873c-4045-a10f-a508d99d486c
```

The requested storage cannot be smaller than the size of the reference pvc

```
    lastTransitionTime: "2023-03-14T08:26:11Z"
    message: 'Error encountered while creating DataVolumes: Failed to create DataVolume:
      admission webhook "datavolume-validate.cdi.kubevirt.io" denied the request:  target
      resources requests storage size is smaller than the source'
    reason: FailedCreate
    status: "True"
    type: Failure
```

When cirros01.yaml is created, DataVolume is created for cirros virtual machine instance which triggers creation of PVC based on another PVC i.e. clone operation.
Clone is performed by cdi importer.

```
# oc get dv
NAME        PHASE       PROGRESS   RESTARTS   AGE
cirros01    Pending     N/A                   10s

# oc get dv
NAME        PHASE            PROGRESS   RESTARTS   AGE
cirros01    CloneScheduled   N/A                   20s

# oc get dv
NAME        PHASE             PROGRESS   RESTARTS   AGE
cirros01    CloneInProgress   N/A                   34s

# oc get pod
default                                            cdi-upload-cirros01                                               1/1     Running             0                 12s

# oc get dv
NAME        PHASE       PROGRESS   RESTARTS   AGE
cirros01    Succeeded   100.0%                3m35s
```

It all results in PVC and PV created specifically for virtual machine instance

```
# oc get pvc
NAME        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
cirros01    Bound    pvc-f21640d1-5003-4f9a-a53a-7f5f5013632a   500Mi      RWO            thin           4m3s

# oc get pv
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM               STORAGECLASS   REASON   AGE
pvc-f21640d1-5003-4f9a-a53a-7f5f5013632a   500Mi      RWO            Delete           Bound    default/cirros01    thin                    5m12s
```

PVC size is reflected in mounted filesystem size

```
$ df -k
Filesystem           1K-blocks      Used Available Use% Mounted on
/dev                    495064         0    495064   0% /dev
/dev/vda1               455526     33200    402533   8% /
tmpfs                   502332         0    502332   0% /dev/shm
tmpfs                   502332        32    502300   0% /run
```

## Data Volume Template - Source http (cirros02.yaml)

Definition: Virtual machine disk => volume => Data Volume

```
spec:
  dataVolumeTemplates:
    - apiVersion: cdi.kubevirt.io/v1beta1
      kind: DataVolume
      metadata:
        name: cirros02
        namespace: default
      spec:
        pvc:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 500Mi
          volumeMode: Filesystem
        source:
          http:
            url: "https://download.cirros-cloud.net/0.6.1/cirros-0.6.1-x86_64-disk.img"
  template:
    spec:
      volumes:
        - dataVolume:
            name: cirros02
```

When virtual machine is created, data volume creation is handled by cdi operator

```
# oc get dv
NAME        PHASE             PROGRESS   RESTARTS   AGE
cirros02    ImportScheduled   N/A                   5s

# oc get dv
NAME        PHASE              PROGRESS   RESTARTS   AGE
cirros02    ImportInProgress   N/A                   7s

# oc get dv
NAME        PHASE              PROGRESS   RESTARTS   AGE
cirros02    ImportInProgress   98.56%                92s

# oc get dv
NAME        PHASE       PROGRESS   RESTARTS   AGE
cirros02    Succeeded   100.0%                7m8s
```

CDI imported pod uses the cluster-wide http proxy settings.

```
# oc describe pod importer-cirros02
Name:         importer-cirros02
Namespace:    default
Priority:     0
Node:         kubevirt-nn4bm-worker-rrsl6/10.58.24.216
Start Time:   Tue, 14 Mar 2023 09:39:39 +0100
Labels:       app=containerized-data-importer
              app.kubernetes.io/component=storage
              app.kubernetes.io/managed-by=cdi-controller
              app.kubernetes.io/part-of=hyperconverged-cluster
              app.kubernetes.io/version=4.11.3
              cdi.kubevirt.io=importer
              prometheus.cdi.kubevirt.io=true
Annotations:  cdi.kubevirt.io/storage.createdByController: yes
              k8s.v1.cni.cncf.io/network-status:
                [{
                    "name": "openshift-sdn",
                    "interface": "eth0",
                    "ips": [
                        "10.129.3.124"
                    ],
                    "default": true,
                    "dns": {}
                }]
              k8s.v1.cni.cncf.io/networks-status:
                [{
                    "name": "openshift-sdn",
                    "interface": "eth0",
                    "ips": [
                        "10.129.3.124"
                    ],
                    "default": true,
                    "dns": {}
                }]
              sidecar.istio.io/inject: false
Status:       Running
IP:           10.129.3.124
IPs:
  IP:           10.129.3.124
Controlled By:  PersistentVolumeClaim/cirros02
Containers:
  importer:
    Container ID:  cri-o://3a82b8fb0e93e2dcd305ef887439bcf62bda09265532476ce36d83edaf7b79e9
    Image:         registry.redhat.io/container-native-virtualization/virt-cdi-importer@sha256:9dd7fbd18b44ade434da66500340d92283d20e23431312ecd2df93aeead84c39
    Image ID:      registry.redhat.io/container-native-virtualization/virt-cdi-importer@sha256:9dd7fbd18b44ade434da66500340d92283d20e23431312ecd2df93aeead84c39
    Port:          8443/TCP
    Host Port:     0/TCP
    Args:
      -v=1
    State:          Running
      Started:      Tue, 14 Mar 2023 09:39:44 +0100
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     750m
      memory:  600M
    Requests:
      cpu:     100m
      memory:  60M
    Environment:
      IMPORTER_SOURCE:               http
      IMPORTER_ENDPOINT:             https://download.cirros-cloud.net/0.6.1/cirros-0.6.1-x86_64-disk.img
      IMPORTER_CONTENTTYPE:          kubevirt
      IMPORTER_IMAGE_SIZE:           500Mi
      OWNER_UID:                     0bcfdc10-2abb-4117-aa88-f7997979a95b
      FILESYSTEM_OVERHEAD:           0.055
      INSECURE_TLS:                  false
      IMPORTER_DISK_ID:
      IMPORTER_UUID:
      IMPORTER_READY_FILE:
      IMPORTER_DONE_FILE:
      IMPORTER_BACKING_FILE:
      IMPORTER_THUMBPRINT:
      http_proxy:                    http://proxy.esl.cisco.com:80
      https_proxy:                   http://proxy.esl.cisco.com:80
      no_proxy:                      .cluster.local,.ocp.lan,.svc,10.128.0.0/14,10.58.24.208/28,10.58.24.209,10.58.24.210,10.58.24.211,10.58.24.212,10.58.24.213,10.58.24.214,10.58.24.215,10.58.24.216,10.58.24.217,10.58.24.218,10.58.29.66,127.0.0.1,172.30.0.0/16,api-int.kube
virt.ocp.lan,esx71.emea-sp.cisco.com,esx72.emea-sp.cisco.com,localhost,vc-iks-kali-eu-spdc.cisco.com
      IMPORTER_CURRENT_CHECKPOINT:
      IMPORTER_PREVIOUS_CHECKPOINT:
      IMPORTER_FINAL_CHECKPOINT:
      PREALLOCATION:                 false
    Mounts:
      /data from cdi-data-vol (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-gjjqk (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             True
  ContainersReady   True
  PodScheduled      True
Volumes:
  cdi-data-vol:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  cirros02
    ReadOnly:   false
  kube-api-access-gjjqk:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
    ConfigMapName:           openshift-service-ca.crt
    ConfigMapOptional:       <nil>
QoS Class:                   Burstable
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/memory-pressure:NoSchedule op=Exists
                             node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason                  Age   From                     Message
  ----    ------                  ----  ----                     -------
  Normal  Scheduled               18s   default-scheduler        Successfully assigned default/importer-cirros02 to kubevirt-nn4bm-worker-rrsl6 by kubevirt-nn4bm-master-2
  Normal  SuccessfulAttachVolume  18s   attachdetach-controller  AttachVolume.Attach succeeded for volume "pvc-4af281bb-f36e-48d8-bf88-363f093d73ea"
  Normal  AddedInterface          13s   multus                   Add eth0 [10.129.3.124/23] from openshift-sdn
  Normal  Pulled                  13s   kubelet                  Container image "registry.redhat.io/container-native-virtualization/virt-cdi-importer@sha256:9dd7fbd18b44ade434da66500340d92283d20e23431312ecd2df93aeead84c39" already present on machine
  Normal  Created                 13s   kubelet                  Created container importer
  Normal  Started                 13s   kubelet                  Started container importer
```

PVC and PV are created

```
# oc get pvc
NAME        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
cirros02    Bound    pvc-4af281bb-f36e-48d8-bf88-363f093d73ea   500Mi      RWO            thin           3m53s

# oc get pv
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM               STORAGECLASS   REASON   AGE
pvc-4af281bb-f36e-48d8-bf88-363f093d73ea   500Mi      RWO            Delete           Bound    default/cirros02    thin                    3m55s
```

## Data Volume Template - Source registry (cirros03.yaml)

```
spec:
  dataVolumeTemplates:
    - apiVersion: cdi.kubevirt.io/v1beta1
      kind: DataVolume
      metadata:
        name: cirros03
        namespace: default
      spec:
        pvc:
          accessModes:
            - ReadWriteOnce
          resources:
            requests:
              storage: 500Mi
          volumeMode: Filesystem
        source:
          registry:
            url: "docker://quay.io/kubevirt/cirros-container-disk-demo"
  template:
    spec:
      volumes:
        - dataVolume:
            name: cirros03
```

Data Volume state changes when virtual machine is deployed

```
# oc get dvs
NAME        PHASE       PROGRESS   RESTARTS   AGE
cirros03    Pending     N/A                   0s

# oc get dvs
NAME        PHASE             PROGRESS   RESTARTS   AGE
cirros03    ImportScheduled   N/A                   1s

# oc get dvs
NAME        PHASE       PROGRESS   RESTARTS   AGE
cirros03    Succeeded   100.0%                54s
```

Data Volume and related PVC were prepared via cdi importer pod

```
# oc get pod importer-cirros03 -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    cdi.kubevirt.io/storage.createdByController: "yes"
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "openshift-sdn",
          "interface": "eth0",
          "ips": [
              "10.128.2.24"
          ],
          "default": true,
          "dns": {}
      }]
    k8s.v1.cni.cncf.io/networks-status: |-
      [{
          "name": "openshift-sdn",
          "interface": "eth0",
          "ips": [
              "10.128.2.24"
          ],
          "default": true,
          "dns": {}
      }]
    sidecar.istio.io/inject: "false"
  creationTimestamp: "2023-03-14T17:10:00Z"
  labels:
    app: containerized-data-importer
    app.kubernetes.io/component: storage
    app.kubernetes.io/managed-by: cdi-controller
    app.kubernetes.io/part-of: hyperconverged-cluster
    app.kubernetes.io/version: 4.11.3
    cdi.kubevirt.io: importer
    prometheus.cdi.kubevirt.io: "true"
  name: importer-cirros03
  namespace: default
  ownerReferences:
  - apiVersion: v1
    blockOwnerDeletion: true
    controller: true
    kind: PersistentVolumeClaim
    name: cirros03
    uid: 0ab75e26-fca4-49a8-a15b-d06eba0ff922
  resourceVersion: "19142812"
  uid: 808ded6d-b6a1-4b45-b266-fbca4a3e20a1
spec:
  containers:
  - args:
    - -v=1
    env:
    - name: IMPORTER_SOURCE
      value: registry
    - name: IMPORTER_ENDPOINT
      value: docker://quay.io/kubevirt/cirros-container-disk-demo
    - name: IMPORTER_CONTENTTYPE
      value: kubevirt
    - name: IMPORTER_IMAGE_SIZE
      value: 500Mi
    - name: OWNER_UID
      value: 1ba57e49-2fad-4cdd-8528-d0850606c338
    - name: FILESYSTEM_OVERHEAD
      value: "0.055"
    - name: INSECURE_TLS
      value: "false"
    - name: IMPORTER_DISK_ID
    - name: IMPORTER_UUID
    - name: IMPORTER_READY_FILE
    - name: IMPORTER_DONE_FILE
    - name: IMPORTER_BACKING_FILE
    - name: IMPORTER_THUMBPRINT
    - name: http_proxy
      value: http://proxy.esl.cisco.com:80
    - name: https_proxy
      value: http://proxy.esl.cisco.com:80
    - name: no_proxy
      value: .cluster.local,.ocp.lan,.svc,10.128.0.0/14,10.58.24.208/28,10.58.24.209,10.58.24.210,10.58.24.211,10.58.24.212,10.58.24.213,10.58.24.214,10.58.24.215,10.58.24.216,10.58.24.217,10.58.24.218,10.58.29.66,127.0.0.1,172.30.0.0/16,api-int.kubevirt.ocp.lan,esx71.emea-
sp.cisco.com,esx72.emea-sp.cisco.com,localhost,vc-iks-kali-eu-spdc.cisco.com
    - name: IMPORTER_CURRENT_CHECKPOINT
    - name: IMPORTER_PREVIOUS_CHECKPOINT
    - name: IMPORTER_FINAL_CHECKPOINT
    - name: PREALLOCATION
      value: "false"
    image: registry.redhat.io/container-native-virtualization/virt-cdi-importer@sha256:9dd7fbd18b44ade434da66500340d92283d20e23431312ecd2df93aeead84c39
    imagePullPolicy: IfNotPresent
    name: importer
    ports:
    - containerPort: 8443
      name: metrics
      protocol: TCP
    resources:
      limits:
        cpu: 750m
        memory: 600M
      requests:
        cpu: 100m
        memory: 60M
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /data
      name: cdi-data-vol
    - mountPath: /scratch
      name: cdi-scratch-vol
    - mountPath: /var/run/secrets/kubernetes.io/serviceaccount
      name: kube-api-access-9g2vd
      readOnly: true
  dnsPolicy: ClusterFirst
  enableServiceLinks: true
  imagePullSecrets:
  - name: default-dockercfg-9tgqh
  nodeName: kubevirt-nn4bm-worker-9fxdj
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  restartPolicy: OnFailure
  schedulerName: default-scheduler
  securityContext:
    fsGroup: 107
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 30
  tolerations:
  - effect: NoExecute
    key: node.kubernetes.io/not-ready
    operator: Exists
    tolerationSeconds: 300
  - effect: NoExecute
    key: node.kubernetes.io/unreachable
    operator: Exists
    tolerationSeconds: 300
  - effect: NoSchedule
    key: node.kubernetes.io/memory-pressure
    operator: Exists
  volumes:
  - name: cdi-data-vol
    persistentVolumeClaim:
      claimName: cirros03
  - name: cdi-scratch-vol
    persistentVolumeClaim:
      claimName: cirros03-scratch
  - name: kube-api-access-9g2vd
    projected:
      defaultMode: 420
      sources:
      - serviceAccountToken:
          expirationSeconds: 3607
          path: token
      - configMap:
          items:
          - key: ca.crt
            path: ca.crt
          name: kube-root-ca.crt
      - downwardAPI:
          items:
          - fieldRef:
              apiVersion: v1
              fieldPath: metadata.namespace
            path: namespace
      - configMap:
          items:
          - key: service-ca.crt
            path: service-ca.crt
          name: openshift-service-ca.crt
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2023-03-14T17:10:02Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2023-03-14T17:10:10Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2023-03-14T17:10:10Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2023-03-14T17:10:02Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: cri-o://5078d586d015243a25821e2bf586c1ef27078b1c7060648c0243103479ec70c6
    image: registry.redhat.io/container-native-virtualization/virt-cdi-importer@sha256:9dd7fbd18b44ade434da66500340d92283d20e23431312ecd2df93aeead84c39
    imageID: registry.redhat.io/container-native-virtualization/virt-cdi-importer@sha256:9dd7fbd18b44ade434da66500340d92283d20e23431312ecd2df93aeead84c39
    lastState: {}
    name: importer
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2023-03-14T17:10:10Z"
  hostIP: 10.58.24.218
  phase: Running
  podIP: 10.128.2.24
  podIPs:
  - ip: 10.128.2.24
  qosClass: Burstable
  startTime: "2023-03-14T17:10:02Z"
```

Persistent Volume associated with virtual machine

```
# oc get pvc
NAME        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
cirros03    Bound    pvc-0ab75e26-fca4-49a8-a15b-d06eba0ff922   500Mi      RWO            thin           4m44s

# oc get pv
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM               STORAGECLASS   REASON   AGE
pvc-0ab75e26-fca4-49a8-a15b-d06eba0ff922   500Mi      RWO            Delete           Bound    default/cirros03    thin                    4m48s
```
