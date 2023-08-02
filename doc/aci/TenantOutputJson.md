# Tenant

## JSON output

```
# iserver get aci tenant --apic apic21 --name k8s -o json

[
    {
        "__Output": {
            "health": "Green"
        },
        "descr": "Kubernetes Environment - Modified with Terraform (ttrabatt)",
        "dn": "uni/tn-k8s",
        "lcOwn": "local",
        "name": "k8s",
        "userdom": ":all:common:",
        "health": "95"
    }
]
```

[[Back]](./Tenant.md)