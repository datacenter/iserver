# OpenShift Virtualization - Fedora Test Results

## Virtual Machine

```
# oc get vm -n default fedora02
NAME       AGE     STATUS    READY
fedora02   3m44s   Running   True


# oc get vm -n default fedora02 -o yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  annotations:
    kubemacpool.io/transaction-timestamp: "2023-03-16T17:06:29.335595434Z"
    kubevirt.io/latest-observed-api-version: v1
    kubevirt.io/storage-observed-api-version: v1alpha3
  creationTimestamp: "2023-03-16T17:06:28Z"
  generation: 1
  labels:
    app: fedora02
  name: fedora02
  namespace: default
  resourceVersion: "23904909"
  uid: 4a95b3f6-bf78-4c4c-a361-415cfce605ca
spec:
  dataVolumeTemplates:
  - apiVersion: cdi.kubevirt.io/v1beta1
    kind: DataVolume
    metadata:
      creationTimestamp: null
      name: fedora02
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
        kubevirt.io/domain: fedora02
        special: fedora02
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
          interfaces:
          - macAddress: 02:6c:cf:00:00:3f
            masquerade: {}
            name: default
          rng: {}
        machine:
          type: pc-q35-rhel8.6.0
        resources:
          requests:
            memory: 1Gi
      evictionStrategy: LiveMigrate
      hostname: fedora02
      networks:
      - name: default
        pod: {}
      volumes:
      - dataVolume:
          name: fedora02
        name: rootdisk
      - cloudInitNoCloud:
          userData: |-
            #cloud-config
            password: fedora
            chpasswd: { expire: False }
            ssh_pwauth: True
        name: cloudinitdisk
status:
  conditions:
  - lastProbeTime: null
    lastTransitionTime: "2023-03-16T17:09:33Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: null
    message: 'cannot migrate VMI: PVC fedora02 is not shared, live migration requires
      that all PVCs must be shared (using ReadWriteMany access mode)'
    reason: DisksNotLiveMigratable
    status: "False"
    type: LiveMigratable
  - lastProbeTime: "2023-03-16T17:09:52Z"
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
```
