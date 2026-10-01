# Cert Manager - Issuer

[[Back]](../README.md) [[official doc]](https://cert-manager.io/docs/concepts/issuer/)

`Issuer` is Kubernetes custom resource that represent certificate authorities (CAs) that generate signed certificates. All cert-manager [certificates](./certificate.md) require a referenced issuer that is in a ready condition to attempt to honor the signing request.

>[!NOTE]
>`Issuer` is a namespaced resource, and it is not possible to issue certificates from an Issuer in a different namespace.

```yaml
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: ca-issuer
  namespace: cilium
spec:
  ca:
    secretName: ca-key-pair
```

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ca-key-pair
  namespace: cilium
type: kubernetes.io/tls
data:
  tls.crt: <<< certificate >>
  tls.key: <<< rsa private key >>>
```

>[!CAUTION]
>The values in `Secret` must be base64 utf-8 encoded.

Private key example

```
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAwPax8+yfdiiOgiwv/Vc3YJ/kXsgLYKMfhgyzYFe0NBbI/DtQ
....
-----END RSA PRIVATE KEY-----
```

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ca-key-pair
  namespace: cilium
type: kubernetes.io/tls
data:
  tls.crt: <<< certificate >>
  tls.key: LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLR...
```

[[Back]](../README.md) [[official doc]](https://cert-manager.io/docs/concepts/issuer/)