# Cert Manager - CertificateRequest

[[Back]](../README.md) [[official doc]](https://cert-manager.io/docs/usage/certificaterequest/)

The CertificateRequest is a namespaced resource in cert-manager that is used to request X.509 certificates from an Issuer. The resource contains a base64 encoded string of a PEM encoded certificate request which is sent to the referenced issuer. A successful issuance will return a signed certificate, based on the certificate signing request. CertificateRequests are typically consumed and managed by controllers or other systems and should not be used by humans - unless specifically needed.

Example: [hubble relay](../../cilium-hubble/kb/configuration-hubble-relay-tls.md)

```yaml
apiVersion: cert-manager.io/v1
kind: CertificateRequest
metadata:
  name: my-ca-cr
spec:
  request: ...
  isCA: false
  usages:
  - signing
  - digital signature
  - server auth
  # 90 days
  duration: 2160h
  issuerRef:
    name: ca-issuer
    # We can reference ClusterIssuers by changing the kind here.
    # The default value is Issuer (i.e. a locally namespaced Issuer)
    kind: Issuer
    group: cert-manager.io
```

[[Back]](../README.md) [[official doc]](https://cert-manager.io/docs/usage/certificaterequest/)