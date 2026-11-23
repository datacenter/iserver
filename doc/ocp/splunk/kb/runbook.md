# Splunk Enterprise on OpenShift Installation Runbook

[[Back]](../README.md)

This document captures the full installation procedure used to deploy Splunk Enterprise on OpenShift, including the fixes applied during setup.

## Target Environment

- OpenShift namespace: `splunk-operator`
- Splunk Operator version: `3.1.0`
- Splunk Enterprise deployment type: `Standalone`
- StorageClass used: `vast-nfs`
- External FQDN: `splunk-enterprise.ai-pod.domain.com`

## Important Notes

- The Splunk Operator is **not available through OperatorHub**, so the installation is using Splunk's published manifest directly from GitHub.
- On newer OpenShift versions, the required SCC is `nonroot-v2`.
- Splunk Web on this deployment served plain HTTP on port `8000`, so the OpenShift route had to use `edge` TLS termination instead of `passthrough`.
- To make Splunk generate correct external `https://` URLs behind the OpenShift route, reverse-proxy settings were added and then made declarative through the `Standalone` spec.

## 1. Install the Splunk Operator

Apply the published cluster-scoped operator manifest:

```bash
curl -L https://github.com/splunk/splunk-operator/releases/download/3.1.0/splunk-operator-cluster.yaml | oc apply --server-side -f -
```

Verify that the operator resources exist:

```bash
oc get deploy -n splunk-operator
oc get crd | rg enterprise.splunk.com
```

## 2. Grant Required OpenShift SCCs

Grant `nonroot-v2` to the operator controller service account:

```bash
oc adm policy add-scc-to-user nonroot-v2 -z splunk-operator-controller-manager -n splunk-operator
```

Create the Splunk Enterprise service account and grant the same SCC:

```bash
oc -n splunk-operator create serviceaccount splunk-enterprise-sa --dry-run=client -o yaml | oc apply -f -
oc adm policy add-scc-to-user nonroot-v2 -z splunk-enterprise-sa -n splunk-operator
```

## 3. Accept Splunk Image Terms

Set the required environment variable on the operator deployment:

```bash
oc -n splunk-operator set env deploy/splunk-operator-controller-manager \
  SPLUNK_GENERAL_TERMS=--accept-sgt-current-at-splunk-com
```

Wait for the operator to become healthy:

```bash
oc -n splunk-operator rollout status deploy/splunk-operator-controller-manager --timeout=10m
oc get deploy/pod -n splunk-operator
```

## 4. Create the First Splunk Enterprise Instance

Create a standalone deployment using the `vast-nfs` StorageClass:

```bash
cat <<'EOF' | oc apply -f -
apiVersion: enterprise.splunk.com/v4
kind: Standalone
metadata:
  name: splunk
  namespace: splunk-operator
  finalizers:
  - enterprise.splunk.com/delete-pvc
spec:
  serviceAccount: splunk-enterprise-sa
  etcVolumeStorageConfig:
    storageClassName: vast-nfs
    storageCapacity: 10Gi
  varVolumeStorageConfig:
    storageClassName: vast-nfs
    storageCapacity: 100Gi
EOF
```

Check rollout status:

```bash
oc get standalone,statefulset,pods,pvc -n splunk-operator -o wide
oc wait --for=condition=Ready pod/splunk-splunk-standalone-0 -n splunk-operator --timeout=12m
```

Expected healthy state:

```bash
oc get standalone,pods,svc,pvc -n splunk-operator -o wide
```

## 5. Create the OpenShift Route

### Initial Attempt That Failed

The route was first created with `passthrough` TLS termination:

```yaml
tls:
  termination: passthrough
```

That caused TLS handshake failures because Splunk Web on port `8000` was serving plain HTTP, not HTTPS.

### Correct Route Configuration

Create the route with `edge` termination and redirect HTTP to HTTPS:

```bash
cat <<'EOF' | oc apply -f -
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: splunk-enterprise-web
  namespace: splunk-operator
spec:
  host: splunk-enterprise.ai-pod.domain.com
  to:
    kind: Service
    name: splunk-splunk-standalone-service
    weight: 100
  port:
    targetPort: http-splunkweb
  tls:
    termination: edge
    insecureEdgeTerminationPolicy: Redirect
EOF
```

Verify the route:

```bash
oc get route splunk-enterprise-web -n splunk-operator -o wide
oc get route splunk-enterprise-web -n splunk-operator \
  -o jsonpath='{range .status.ingress[*]}{.host}{"\t"}{.routerName}{"\t"}{.conditions[?(@.type=="Admitted")].status}{"\n"}{end}'
```

## 6. Fix Splunk Reverse-Proxy Behavior

### Problem

After the route was corrected, `curl` to the external HTTPS URL still returned a redirect to `http://.../en-US/`.

Example of the bad behavior:

```http
HTTP/1.1 303 See Other
location: http://splunk-enterprise.ai-pod.domain.com/en-US/
```

### Fix

The working Splunk settings are:

- `tools.proxy.on = true`
- `tools.proxy.base = https://splunk-enterprise.ai-pod.domain.com`

Instead of keeping this as a manual pod edit, the final fix was made **declarative** through a ConfigMap and the `Standalone` spec.

Create the ConfigMap and patch the `Standalone`:

```bash
cat <<'EOF' | oc apply -f -
apiVersion: v1
kind: ConfigMap
metadata:
  name: splunk-proxy-defaults
  namespace: splunk-operator
data:
  default.yml: |
    splunk:
      conf:
        - key: app
          value:
            directory: /opt/splunk/etc/apps/splunk-route-proxy/default
            content:
              install:
                state: enabled
              ui:
                is_visible: false
                label: splunk-route-proxy
        - key: web
          value:
            directory: /opt/splunk/etc/apps/splunk-route-proxy/local
            content:
              settings:
                tools.proxy.on: "true"
                tools.proxy.base: https://splunk-enterprise.ai-pod.domain.com
---
apiVersion: enterprise.splunk.com/v4
kind: Standalone
metadata:
  name: splunk
  namespace: splunk-operator
spec:
  volumes:
    - name: defaults
      configMap:
        name: splunk-proxy-defaults
  defaultsUrl: /mnt/defaults/default.yml
EOF
```

Restart the Splunk pod so it reloads the declarative defaults:

```bash
oc delete pod splunk-splunk-standalone-0 -n splunk-operator --wait=false
oc wait --for=condition=Ready pod/splunk-splunk-standalone-0 -n splunk-operator --timeout=12m
```

Verify the active external behavior:

```bash
curl -skI https://splunk-enterprise.ai-pod.domain.com/
```

Expected result:

```http
HTTP/1.1 303 See Other
location: https://splunk-enterprise.ai-pod.domain.com/en-US/
```

Verify the `Standalone` is wired to the defaults ConfigMap:

```bash
oc get standalone splunk -n splunk-operator -o yaml
oc get sts splunk-splunk-standalone -n splunk-operator -o yaml | rg '/mnt/defaults|splunk-proxy-defaults|SPLUNK_DEFAULTS_URL'
```

## 7. Extract the Admin Password

The current admin password secret is:

- Namespace: `splunk-operator`
- Secret: `splunk-splunk-standalone-secret-v1`

Extract the password with:

```bash
oc extract secret/splunk-splunk-standalone-secret-v1 -n splunk-operator --keys=password --to=-
```

Equivalent `jsonpath` form:

```bash
admin_password=$(oc get secret -n splunk-operator splunk-splunk-standalone-secret-v1 -o=jsonpath='{.data.password}' | base64 -d)
echo "$admin_password"
```

## 8. Useful Verification Commands

Check all main resources:

```bash
oc get standalone,pods,svc,pvc,route -n splunk-operator -o wide
```

Check the operator:

```bash
oc get deploy/pods -n splunk-operator
```

Check the route:

```bash
curl -skI https://splunk-enterprise.ai-pod.domain.com/
```

Check the current secret names:

```bash
oc get secrets -n splunk-operator | rg 'splunk.*secret'
```

## 9. Troubleshooting Summary

### Operator not found in OperatorHub

Use the published Splunk operator manifest directly from GitHub.

### TLS handshake failure on the route

If you see errors like:

```text
curl: (35) LibreSSL/... tlsv1 alert protocol version
```

check whether the route is using `passthrough` while the backend is actually serving plain HTTP. For this setup, the fix was to use:

```yaml
tls:
  termination: edge
  insecureEdgeTerminationPolicy: Redirect
```

### Redirect goes to `http://` instead of `https://`

Configure:

- `tools.proxy.on = true`
- `tools.proxy.base = https://splunk-enterprise.ai-pod.domain.com`

and make it declarative through `default.yml` plus `spec.defaultsUrl`.

### Brief `503 Service Unavailable` after pod restarts

This is expected while the Splunk pod is recreating and the router has no healthy backend yet.

[[Back]](../README.md)