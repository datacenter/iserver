# OpenShift Virtualization - Cat8000v Test Results

## Virtual Machine Instance

```
# oc get vmi -n default cat8kv-01
NAME        AGE     PHASE     IP             NODENAME                      READY
cat8kv-01   5m44s   Running   10.128.2.217   kubevirt-nn4bm-worker-9fxdj   True


# oc get vmi -n default cat8kv-01 -o yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachineInstance
metadata:
  annotations:
    kubevirt.io/latest-observed-api-version: v1
    kubevirt.io/storage-observed-api-version: v1alpha3
  creationTimestamp: "2023-03-28T08:38:30Z"
  finalizers:
  - kubevirt.io/virtualMachineControllerFinalize
  - foregroundDeleteVirtualMachine
  generation: 8
  labels:
    kubevirt.io/domain: cat8kv-01
    kubevirt.io/nodeName: kubevirt-nn4bm-worker-9fxdj
    special: cat8kv-01
  name: cat8kv-01
  namespace: default
  ownerReferences:
  - apiVersion: kubevirt.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: VirtualMachine
    name: cat8kv-01
    uid: 13cc4023-acd7-4696-9f6a-662703655788
  resourceVersion: "50308729"
  uid: 60533689-c1b1-4b76-bbea-b42ec2a73ca6
spec:
  domain:
    cpu:
      cores: 1
      model: host-model
      sockets: 1
      threads: 1
    devices:
      disks:
      - disk:
          bus: virtio
        name: rootdisk
      - cdrom:
          bus: sata
          readonly: true
          tray: closed
        name: cdromdisk
      interfaces:
      - macAddress: 02:6c:cf:00:00:6a
        masquerade: {}
        name: default
      rng: {}
    features:
      acpi:
        enabled: true
    firmware:
      uuid: 30592aed-01ef-5ef9-8a5a-512013936f65
    machine:
      type: pc-q35-rhel8.6.0
    resources:
      requests:
        memory: 4Gi
  evictionStrategy: LiveMigrate
  hostname: cat8kv-01
  networks:
  - name: default
    pod: {}
  volumes:
  - dataVolume:
      name: cat8kv-01
    name: rootdisk
  - name: cdromdisk
    persistentVolumeClaim:
      claimName: cat8kv-01-day0
status:
  activePods:
    d83061b6-51e2-42a2-bf9c-468e273ea5fc: kubevirt-nn4bm-worker-9fxdj
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2023-03-28T08:38:38Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: null
    message: 'cannot migrate VMI: PVC cat8kv-01 is not shared, live migration requires
      that all PVCs must be shared (using ReadWriteMany access mode)'
    reason: DisksNotLiveMigratable
    status: "False"
    type: LiveMigratable
  guestOSInfo: {}
  interfaces:
  - infoSource: domain
    ipAddress: 10.128.2.217
    ipAddresses:
    - 10.128.2.217
    mac: 02:6c:cf:00:00:6a
    name: default
  launcherContainerImageVersion: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:ae751656eccca94e1f2e55dc8fb1339565b3f83256b0dbc8be6720e8a8db2d7b
  migrationMethod: BlockMigration
  migrationTransport: Unix
  nodeName: kubevirt-nn4bm-worker-9fxdj
  phase: Running
  phaseTransitionTimestamps:
  - phase: Pending
    phaseTransitionTimestamp: "2023-03-28T08:38:30Z"
  - phase: Scheduling
    phaseTransitionTimestamp: "2023-03-28T08:38:30Z"
  - phase: Scheduled
    phaseTransitionTimestamp: "2023-03-28T08:38:38Z"
  - phase: Running
    phaseTransitionTimestamp: "2023-03-28T08:38:39Z"
  qosClass: Burstable
  runtimeUser: 107
  virtualMachineRevisionName: revision-start-vm-13cc4023-acd7-4696-9f6a-662703655788-1
  volumeStatus:
  - name: cdromdisk
    persistentVolumeClaimInfo:
      accessModes:
      - ReadWriteOnce
      capacity:
        storage: 1Gi
      filesystemOverhead: "0.055"
      requests:
        storage: 1Gi
      volumeMode: Block
    target: sda
  - name: rootdisk
    persistentVolumeClaimInfo:
      accessModes:
      - ReadWriteOnce
      capacity:
        storage: 16Gi
      filesystemOverhead: "0.055"
      requests:
        storage: 16Gi
      volumeMode: Block
    target: vda
```
