# OpenShift Virtualization - Fedora Test Results

## Virtual Machine Instance

```
# oc get vmi -n default fedora06
NAME       AGE   PHASE     IP             NODENAME                      READY
fedora06   53s   Running   10.131.0.172   kubevirt-nn4bm-worker-srxr9   True


# oc get vmi -n default fedora06 -o yaml
apiVersion: kubevirt.io/v1
kind: VirtualMachineInstance
metadata:
  annotations:
    kubevirt.io/latest-observed-api-version: v1
    kubevirt.io/storage-observed-api-version: v1alpha3
  creationTimestamp: "2023-03-16T17:11:43Z"
  finalizers:
  - kubevirt.io/virtualMachineControllerFinalize
  - foregroundDeleteVirtualMachine
  generation: 11
  labels:
    kubevirt.io/domain: fedora06
    kubevirt.io/nodeName: kubevirt-nn4bm-worker-srxr9
    special: fedora06
  name: fedora06
  namespace: default
  ownerReferences:
  - apiVersion: kubevirt.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: VirtualMachine
    name: fedora06
    uid: 94e0304d-26d6-4868-942a-7e1043cc9c8d
  resourceVersion: "23909049"
  uid: 2076f683-2d58-4f46-a2d9-4cb682060e36
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
    features:
      acpi:
        enabled: true
    firmware:
      uuid: 367213e8-efae-52f1-8591-fc30b4cd2e7b
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
  activePods:
    e566efd1-741e-4def-b164-403f2585fbba: kubevirt-nn4bm-worker-srxr9
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
    ipAddress: 10.131.0.172
    ipAddresses:
    - 10.131.0.172
    mac: 02:6c:cf:00:00:40
    name: default
  launcherContainerImageVersion: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:ae751656eccca94e1f2e55dc8fb1339565b3f83256b0dbc8be6720e8a8db2d7b
  migrationMethod: BlockMigration
  migrationTransport: Unix
  nodeName: kubevirt-nn4bm-worker-srxr9
  phase: Running
  phaseTransitionTimestamps:
  - phase: Pending
    phaseTransitionTimestamp: "2023-03-16T17:11:43Z"
  - phase: Scheduling
    phaseTransitionTimestamp: "2023-03-16T17:11:43Z"
  - phase: Scheduled
    phaseTransitionTimestamp: "2023-03-16T17:11:58Z"
  - phase: Running
    phaseTransitionTimestamp: "2023-03-16T17:12:01Z"
  qosClass: Burstable
  runtimeUser: 107
  virtualMachineRevisionName: revision-start-vm-94e0304d-26d6-4868-942a-7e1043cc9c8d-1
  volumeStatus:
  - name: cloudinitdisk
    size: 1048576
    target: vdb
  - name: extra1
    target: vdc
  - name: extra2
    target: vdd
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
