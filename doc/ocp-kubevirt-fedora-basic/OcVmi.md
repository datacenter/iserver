# OpenShift Virtualization - Fedora Test Results

## Virtual Machine Instance

```
# oc get vmi -n default fedora02
NAME       AGE   PHASE     IP             NODENAME                      READY
fedora02   46s   Running   10.131.0.169   kubevirt-nn4bm-worker-srxr9   True


# oc get vmi -n default fedora02 -o yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachineInstance
metadata:
  annotations:
    kubevirt.io/latest-observed-api-version: v1
    kubevirt.io/storage-observed-api-version: v1alpha3
  creationTimestamp: "2023-03-16T17:09:27Z"
  finalizers:
  - kubevirt.io/virtualMachineControllerFinalize
  - foregroundDeleteVirtualMachine
  generation: 12
  labels:
    kubevirt.io/domain: fedora02
    kubevirt.io/nodeName: kubevirt-nn4bm-worker-srxr9
    special: fedora02
  name: fedora02
  namespace: default
  ownerReferences:
  - apiVersion: kubevirt.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: VirtualMachine
    name: fedora02
    uid: 4a95b3f6-bf78-4c4c-a361-415cfce605ca
  resourceVersion: "23904910"
  uid: 34f4ad5b-a7e8-4f2c-af31-9b680b46955c
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
      - disk:
          bus: virtio
        name: cloudinitdisk
      interfaces:
      - macAddress: 02:6c:cf:00:00:3f
        masquerade: {}
        name: default
      rng: {}
    features:
      acpi:
        enabled: true
    firmware:
      uuid: 06930e3f-7659-58fd-af67-64ee4e6d348e
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
  activePods:
    8d1f3b3d-d488-4963-8f0d-fc7115fe5123: kubevirt-nn4bm-worker-srxr9
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
  guestOSInfo:
    id: fedora
    kernelRelease: 6.0.7-301.fc37.x86_64
    kernelVersion: '#1 SMP PREEMPT_DYNAMIC Fri Nov 4 18:35:48 UTC 2022'
    name: Fedora Linux
    prettyName: Fedora Linux 37 (Cloud Edition)
    version: "37"
    versionId: "37"
  interfaces:
  - infoSource: domain, guest-agent
    interfaceName: eth0
    ipAddress: 10.131.0.169
    ipAddresses:
    - 10.131.0.169
    mac: 02:6c:cf:00:00:3f
    name: default
  launcherContainerImageVersion: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:ae751656eccca94e1f2e55dc8fb1339565b3f83256b0dbc8be6720e8a8db2d7b
  migrationMethod: BlockMigration
  migrationTransport: Unix
  nodeName: kubevirt-nn4bm-worker-srxr9
  phase: Running
  phaseTransitionTimestamps:
  - phase: Pending
    phaseTransitionTimestamp: "2023-03-16T17:09:27Z"
  - phase: Scheduling
    phaseTransitionTimestamp: "2023-03-16T17:09:27Z"
  - phase: Scheduled
    phaseTransitionTimestamp: "2023-03-16T17:09:33Z"
  - phase: Running
    phaseTransitionTimestamp: "2023-03-16T17:09:34Z"
  qosClass: Burstable
  runtimeUser: 107
  virtualMachineRevisionName: revision-start-vm-4a95b3f6-bf78-4c4c-a361-415cfce605ca-1
  volumeStatus:
  - name: cloudinitdisk
    size: 1048576
    target: vdb
  - name: rootdisk
    persistentVolumeClaimInfo:
      accessModes:
      - ReadWriteOnce
      capacity:
        storage: 30Gi
      filesystemOverhead: "0.055"
      requests:
        storage: 30Gi
      volumeMode: Filesystem
    target: vda
```
