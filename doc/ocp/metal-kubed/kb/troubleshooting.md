## Troubleshooting

[[Back]](../README.md)

```
$ oc get events -n openshift-machine-api
```

```
$ oc logs -n openshift-machine-api deploy/metal3 -c metal3-ironic
```

If provisioning is successful however OS is not ip reachable or ssh access fails, you may want to run [rhel rescue](../../../linux/rhel-rescue.md) procedure to check what is the deployed state or filesystem state of the host.

[[Back]](../README.md)