# Local Storage Operator

Operator for local storage as explained on [RedHat documentation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/configuring-persistent-storage#persistent-storage-using-local-storage) and [GitHub](https://github.com/openshift/local-storage-operator)

## HowTo by Example

- local storage on 3-node OpenShift Cluster with explicitly defined block devices ([detail](./example.md))

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp lso | check the LVM operator state | [Link](./get.md)
iserver set ocp lso --mode operator | install local storage operator | [Link](./create_operator.md)
iserver set ocp lso --mode volume | add local volumes | [Link](./create_volume.md)
iserver set ocp lso --mode all | install operator and add local volumes | [Link](./create_all.md)
iserver set ocp task | in task way | [Link](./create_task.md)
iserver delete ocp lso --mode operator | delete local storage operator | [Link](./delete_operator.md)
iserver delete ocp lso --mode volume | delete local storage volumes | [Link](./delete_volume.md)
iserver delete ocp lso --mode all | delete local storage operator and volumes | [Link](./delete_all.md)
iserver delete ocp task | in task way | [Link](./delete_task.md)

## Related Commands

Command | Intent | Details
--- | --- | ---
iserver get k8s locvd | get local volume discovery | [Link](./locvd.md)
iserver get k8s locvdr | get local volume discovery results | [Link](./locvd.md)
iserver get k8s locvs | get local volume set | [Link](./locvs.md)
iserver get k8s locv | get local volume | [Link](./locv.md)
iserver get k8s pv | get persistent volume | [Link](./pv.md)
iserver get k8s sc | get storage class | [Link](./sc.md)
iserver delete k8s locv | delete local volume | [Link](./locv.md)
iserver delete k8s locvd | delete local volume discovery | [Link](./locvd.md)
iserver delete k8s locvs | delete local volume set | [Link](./locvs.md)

[[Back]](../Operations.md)