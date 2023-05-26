# OpenShift Virtualization - Fedora Test Results

## Virtual Machine Launcher Pod

```
# oc get pod -n default virt-launcher-fedora06-wwtvw
NAME                           READY   STATUS    RESTARTS   AGE
virt-launcher-fedora06-wwtvw   1/1     Running   0          51s


# oc get pod -n default virt-launcher-fedora06-wwtvw -o yaml
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/network-status: |-
      [{
          "name": "openshift-sdn",
          "interface": "eth0",
          "ips": [
              "10.131.0.172"
          ],
          "default": true,
          "dns": {}
      }]
    k8s.v1.cni.cncf.io/networks-status: |-
      [{
          "name": "openshift-sdn",
          "interface": "eth0",
          "ips": [
              "10.131.0.172"
          ],
          "default": true,
          "dns": {}
      }]
    kubectl.kubernetes.io/default-container: compute
    kubevirt.io/domain: fedora06
    kubevirt.io/migrationTransportUnix: "true"
    post.hook.backup.velero.io/command: '["/usr/bin/virt-freezer", "--unfreeze", "--name",
      "fedora06", "--namespace", "default"]'
    post.hook.backup.velero.io/container: compute
    pre.hook.backup.velero.io/command: '["/usr/bin/virt-freezer", "--freeze", "--name",
      "fedora06", "--namespace", "default"]'
    pre.hook.backup.velero.io/container: compute
    traffic.sidecar.istio.io/kubevirtInterfaces: k6t-eth0
  creationTimestamp: "2023-03-16T17:11:43Z"
  generateName: virt-launcher-fedora06-
  labels:
    kubevirt.io: virt-launcher
    kubevirt.io/created-by: 2076f683-2d58-4f46-a2d9-4cb682060e36
    kubevirt.io/domain: fedora06
    special: fedora06
    vm.kubevirt.io/name: fedora06
  name: virt-launcher-fedora06-wwtvw
  namespace: default
  ownerReferences:
  - apiVersion: kubevirt.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: VirtualMachineInstance
    name: fedora06
    uid: 2076f683-2d58-4f46-a2d9-4cb682060e36
  resourceVersion: "23908393"
  uid: e566efd1-741e-4def-b164-403f2585fbba
spec:
  automountServiceAccountToken: false
  containers:
  - command:
    - /usr/bin/virt-launcher-monitor
    - --qemu-timeout
    - 242s
    - --name
    - fedora06
    - --uid
    - 2076f683-2d58-4f46-a2d9-4cb682060e36
    - --namespace
    - default
    - --kubevirt-share-dir
    - /var/run/kubevirt
    - --ephemeral-disk-dir
    - /var/run/kubevirt-ephemeral-disks
    - --container-disk-dir
    - /var/run/kubevirt/container-disks
    - --grace-period-seconds
    - "45"
    - --hook-sidecars
    - "0"
    - --ovmf-path
    - /usr/share/OVMF
    - --run-as-nonroot
    env:
    - name: XDG_CACHE_HOME
      value: /var/run/kubevirt-private
    - name: XDG_CONFIG_HOME
      value: /var/run/kubevirt-private
    - name: XDG_RUNTIME_DIR
      value: /var/run
    - name: POD_NAME
      valueFrom:
        fieldRef:
          apiVersion: v1
          fieldPath: metadata.name
    image: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:ae751656eccca94e1f2e55dc8fb1339565b3f83256b0dbc8be6720e8a8db2d7b
    imagePullPolicy: IfNotPresent
    name: compute
    resources:
      limits:
        devices.kubevirt.io/kvm: "1"
        devices.kubevirt.io/tun: "1"
        devices.kubevirt.io/vhost-net: "1"
      requests:
        cpu: 100m
        devices.kubevirt.io/kvm: "1"
        devices.kubevirt.io/tun: "1"
        devices.kubevirt.io/vhost-net: "1"
        ephemeral-storage: 50M
        memory: 1266Mi
    securityContext:
      capabilities:
        add:
        - NET_BIND_SERVICE
        - SYS_PTRACE
        drop:
        - NET_RAW
      privileged: false
      runAsGroup: 107
      runAsNonRoot: true
      runAsUser: 107
    terminationMessagePath: /dev/termination-log
    terminationMessagePolicy: File
    volumeMounts:
    - mountPath: /var/run/kubevirt-private
      name: private
    - mountPath: /var/run/kubevirt
      name: public
    - mountPath: /var/run/kubevirt-ephemeral-disks
      name: ephemeral-disks
    - mountPath: /var/run/kubevirt/container-disks
      mountPropagation: HostToContainer
      name: container-disks
    - mountPath: /var/run/kubevirt/hotplug-disks
      mountPropagation: HostToContainer
      name: hotplug-disks
    - mountPath: /var/run/libvirt
      name: libvirt-runtime
    - mountPath: /var/run/kubevirt/sockets
      name: sockets
    - mountPath: /var/run/kubevirt-private/vmi-disks/rootdisk
      name: rootdisk
  dnsPolicy: ClusterFirst
  enableServiceLinks: false
  hostname: fedora06
  imagePullSecrets:
  - name: default-dockercfg-9tgqh
  nodeName: kubevirt-nn4bm-worker-srxr9
  nodeSelector:
    kubevirt.io/schedulable: "true"
  preemptionPolicy: PreemptLowerPriority
  priority: 0
  readinessGates:
  - conditionType: kubevirt.io/virtual-machine-unpaused
  restartPolicy: Never
  schedulerName: default-scheduler
  securityContext:
    runAsGroup: 107
    runAsNonRoot: true
    runAsUser: 107
    seLinuxOptions:
      type: virt_launcher.process
  serviceAccount: default
  serviceAccountName: default
  terminationGracePeriodSeconds: 60
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
  - emptyDir: {}
    name: private
  - emptyDir: {}
    name: public
  - emptyDir: {}
    name: sockets
  - name: rootdisk
    persistentVolumeClaim:
      claimName: fedora06
  - emptyDir: {}
    name: virt-bin-share-dir
  - emptyDir: {}
    name: libvirt-runtime
  - emptyDir: {}
    name: ephemeral-disks
  - emptyDir: {}
    name: container-disks
  - emptyDir: {}
    name: hotplug-disks
status:
  conditions:
  - lastProbeTime: "2023-03-16T17:11:43Z"
    lastTransitionTime: "2023-03-16T17:11:43Z"
    message: the virtual machine is not paused
    reason: NotPaused
    status: "True"
    type: kubevirt.io/virtual-machine-unpaused
  - lastProbeTime: null
    lastTransitionTime: "2023-03-16T17:11:43Z"
    status: "True"
    type: Initialized
  - lastProbeTime: null
    lastTransitionTime: "2023-03-16T17:11:55Z"
    status: "True"
    type: Ready
  - lastProbeTime: null
    lastTransitionTime: "2023-03-16T17:11:55Z"
    status: "True"
    type: ContainersReady
  - lastProbeTime: null
    lastTransitionTime: "2023-03-16T17:11:43Z"
    status: "True"
    type: PodScheduled
  containerStatuses:
  - containerID: cri-o://52f8b978beb8301fbdb5d52ad19bc997522998b891c2e44ede61b2f9e5e396ff
    image: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:ae751656eccca94e1f2e55dc8fb1339565b3f83256b0dbc8be6720e8a8db2d7b
    imageID: registry.redhat.io/container-native-virtualization/virt-launcher@sha256:1a7996616acb7a7e0e5616be3fa2f591c663999d89f53c3cd1affda5b1ea3db1
    lastState: {}
    name: compute
    ready: true
    restartCount: 0
    started: true
    state:
      running:
        startedAt: "2023-03-16T17:11:55Z"
  hostIP: 10.58.24.217
  phase: Running
  podIP: 10.131.0.172
  podIPs:
  - ip: 10.131.0.172
  qosClass: Burstable
  startTime: "2023-03-16T17:11:43Z"
```
