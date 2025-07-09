# OpenShift Operations

OpenShift cluster day2 operations are clearly defined in OpenShift documentation. At the same time, some operational tasks require multiple steps, multiple commands, yaml file edits etc.

## Requirement

On-time-task := load kubeconfig file of OpenShift cluster into iserver

```
# iserver set ocp kc --cluster my-cluster --file /tmp/kubeconfig
OCP cluster kubeconfig created: my-cluster
```

Workflow commands take --cluster [name] parameter that selects the target OpenShift cluster.

Last used cluster name is cashed and does not have to be defined each time command runs.

## Workflows

- [HTPasswd Identity Provider](./htpasswd/README.md)

[[Back]](../../README.md)