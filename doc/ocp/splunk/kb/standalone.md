# Splunk - Standalone instance

[[Back]](../README.md) [[iserver-way]](../create_instance.md)

```yaml
apiVersion: enterprise.splunk.com/v4
kind: Standalone
metadata:
  finalizers:
  - enterprise.splunk.com/delete-pvc
  name: inst1
  namespace: splunk-operator
spec: {}
```

Expected resources

```
$ oc get pod -n splunk-operator
NAME                                                  READY   STATUS    RESTARTS   AGE
splunk-inst1-standalone-0                             1/1     Running   0          3m15s
```

```
$ oc get pvc -n splunk-operator
NAME                                STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   VOLUMEATTRIBUTESCLASS   AGE
pvc-etc-splunk-inst1-standalone-0   Bound    pvc-4b712b1c-9dc4-4bcc-ac66-a74b12fc6682   10Gi       RWO            lvms-vg1       <unset>                 3m33s
pvc-var-splunk-inst1-standalone-0   Bound    pvc-880accc7-1961-4b60-94e2-dcbdc77c570b   100Gi      RWO            lvms-vg1       <unset>                 3m33s
```

[[Back]](../README.md) [[iserver-way]](../create_instance.md)