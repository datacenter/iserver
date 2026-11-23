# Set Boot Override

[[Next]](./PowerCycle.md) [[Back]](./README.md)

```
# iserver set redfish boot-override \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --target None \
    --enabled Disabled

{
    "BootSourceOverrideTarget": "Cd",
    "BootSourceOverrideTarget@Redfish.AllowableValues": [
        "None",
        "Pxe",
        "Floppy",
        "Cd",
        "Hdd",
        "BiosSetup",
        "Diags"
    ],
    "BootSourceOverrideEnabled@Redfish.AllowableValues": [
        "Once",
        "Continuous",
        "Disabled"
    ],
    "BootSourceOverrideEnabled": "Once"
}

Set one time boot source: None enabled Disabled

{
    "BootSourceOverrideTarget": "None",
    "BootSourceOverrideTarget@Redfish.AllowableValues": [
        "None",
        "Pxe",
        "Floppy",
        "Cd",
        "Hdd",
        "BiosSetup",
        "Diags"
    ],
    "BootSourceOverrideEnabled@Redfish.AllowableValues": [
        "Once",
        "Continuous",
        "Disabled"
    ],
    "BootSourceOverrideEnabled": "Disabled"
}
```

[[Back]](./README.md)