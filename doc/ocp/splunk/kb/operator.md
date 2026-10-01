# Splunk - Operator

[[Back]](../README.md) [[iserver-way]](../create_operator.md)

## Namespace

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: splunk-operator
```

## Operator Group

```yaml
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: splunk-operator-group
  namespace: splunk-operator
spec:
  targetNamespaces:
  - splunk-operator
  upgradeStrategy: Default
```

## Subscription

```yaml
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: splunk-operator
  namespace: splunk-operator
spec:
  channel: stable
  installPlanApproval: Automatic
  name: splunk-operator
  source: certified-operators
  sourceNamespace: openshift-marketplace
```

## Patch CSV

>[!NOTE]
>set env SPLUNK_GENERAL_TERMS value to --accept-sgt-current-at-splunk-com

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: ClusterServiceVersion
metadata:
  name: splunk-operator.v3.1.0
  namespace: splunk-operator
spec:
  install:
    spec:
      deployments:
      - name: splunk-operator-controller-manager
        spec:
          template:
            spec:
              containers:
              - args:
                env:
                - name: SPLUNK_GENERAL_TERMS
                  value: --accept-sgt-current-at-splunk-com
~~~

## Role binding

>[!NOTE]
>Reference: https://github.com/splunk/splunk-operator/blob/main/docs/OpenShift.md

```
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: system:openshift:scc:nonroot-v2
  namespace: splunk-operator
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:openshift:scc:nonroot-v2
subjects:
- kind: ServiceAccount
  name: default
  namespace: splunk-operator
```

[[Back]](../README.md) [[iserver-way]](../create_operator.md)