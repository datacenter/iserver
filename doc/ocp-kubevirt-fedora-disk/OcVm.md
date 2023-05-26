# OpenShift Virtualization - Fedora Test Results

## Virtual Machine

```
# oc get vm -n default fedora06
NAME       AGE    STATUS    READY
fedora06   2m6s   Running   True


# oc get vm -n default fedora06 -o yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  annotations:
    kubemacpool.io/transaction-timestamp: "2023-03-16T17:10:29.708693834Z"
    kubevirt.io/latest-observed-api-version: v1
    kubevirt.io/storage-observed-api-version: v1alpha3
  creationTimestamp: "2023-03-16T17:10:29Z"
  generation: 1
  labels:
    app: fedora06
  name: fedora06
  namespace: default
  resourceVersion: "23909040"
  uid: 94e0304d-26d6-4868-942a-7e1043cc9c8d
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      creationTimestamp: null
      name: fedora06
      namespace: default
    spec:
      pvc:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 30Gi
        volumeMode: Filesystem
      source:
        pvc:
          name: fedora-registry
          namespace: default
  running: true
  template:
    metadata:
      creationTimestamp: null
      labels:
        kubevirt.io/domain: fedora06
        special: fedora06
    spec:
      domain:
        cpu:
          cores: 1
          sockets: 1
          threads: 1
        devices:
          disks:
          - disk:
              bus: virtio
            name: rootdisk
          - disk:
              bus: virtio
            name: cloudinitdisk
          - disk:
              bus: virtio
            name: extra1
          - disk:
              bus: virtio
            name: extra2
          interfaces:
          - macAddress: 02:6c:cf:00:00:40
            masquerade: {}
            name: default
          rng: {}
        machine:
          type: pc-q35-rhel8.6.0
        resources:
          requests:
            memory: 1Gi
      evictionStrategy: LiveMigrate
      hostname: fedora06
      networks:
      - name: default
        pod: {}
      volumes:
      - dataVolume:
          name: fedora06
        name: rootdisk
      - cloudInitNoCloud:
          userData: |-
            #cloud-config
            password: fedora
            chpasswd: { expire: False }
            ssh_pwauth: True
        name: cloudinitdisk
      - emptyDisk:
          capacity: 1Gi
        name: extra1
      - emptyDisk:
          capacity: 2Gi
        name: extra2
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2023-03-16T17:11:55Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: null
    message: 'cannot migrate VMI: PVC fedora06 is not shared, live migration requires
      that all PVCs must be shared (using ReadWriteMany access mode)'
    reason: DisksNotLiveMigratable
    status: "False"
    type: LiveMigratable
  - lastProbeTime: "2023-03-16T17:12:19Z"
    lastTransitionTime: null
    status: "True"
    type: AgentConnected
  created: true
  printableStatus: Running
  ready: true
  volumeSnapshotStatuses:
  - enabled: false
    name: rootdisk
    reason: 'No VolumeSnapshotClass: Volume snapshots are not configured for this
      StorageClass [thin] [rootdisk]'
  - enabled: false
    name: cloudinitdisk
    reason: Snapshot is not supported for this volumeSource type [cloudinitdisk]
  - enabled: false
    name: extra1
    reason: Snapshot is not supported for this volumeSource type [extra1]
  - enabled: false
    name: extra2
    reason: Snapshot is not supported for this volumeSource type [extra2]
```
