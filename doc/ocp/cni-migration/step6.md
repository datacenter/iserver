# Cilium EE migration workflow

[[Back]](./step5.md) [[Next]](./step7.md)

## Step 6: Restart cluster

- unpause Machine Config Operator
- wait for kubernetes API to be not available <=> master nodes restarted
- wait for kubernetes API to be again available <=> cluster at least responding
- resolve any potential roadblocks manually

## Possible manual intervention

Unpausing the machineconfigpool performed in step number 6 should trigger the restart of all the nodes. However, it may not always be the case.

You may see in the output of migration workflow the following

```
Node [ocp-bm7-3] Status ['Ready', 'NoSchedule', 'PreferNoSchedule', 'unschedulable', 'UpdateInProgress']
[ERROR] Timed out
Waiting for automatic node restart timed out
- check what blocks that
- consider reboot
- press Y once all nodes restarted or N to break the workflow
Continue [Y/N]?
```

One node went into schedulingDisabled status, but no further.

```
$ oc get node
NAME        STATUS                     ROLES                         AGE    VERSION
ocp-bm7-1   Ready                      control-plane,master,worker   138d   v1.31.7
ocp-bm7-2   Ready                      control-plane,master,worker   138d   v1.31.7
ocp-bm7-3   Ready,SchedulingDisabled   control-plane,master,worker   138d   v1.31.7
```

[Graceful reboot of the node](https://docs.openshift.com/container-platform/4.14/nodes/nodes/nodes-nodes-rebooting.html#nodes-nodes-rebooting-gracefully_nodes-nodes-rebooting) procedure example:

```
$ oc adm cordon ocp-bm7-3
node/ocp-bm7-3 already cordoned
$ oc adm drain ocp-bm7-3 --ignore-daemonsets --delete-emptydir-data --force --disable-eviction
node/ocp-bm7-3 already cordoned
node/ocp-bm7-3 drained
```

Followed with reboot of the node. Once it is done, hit 'Y' on the workflow prompt so it can continue.

### Output

```
Step 6: Restart cluster
=======================


Set Machine Config Pool Pause
-----------------------------
- name: worker
- pause: False

~~~
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: worker
spec:
  paused: false

~~~
Patch successful

Set Machine Config Pool Pause
-----------------------------
- name: master
- pause: False

~~~
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: master
spec:
  paused: false

~~~
Patch successful

Wait for no kubernetes api [1hr]...

Wait for kubernetes api [30min]...
```

[[Back]](./step5.md) [[Next]](./step7.md)