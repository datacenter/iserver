# Get Boot Override

[[Next]](./Power.md) [[Back]](./README.md)

```
# iserver.py get redfish boot-override \
    --ip 10.10.10.10 \
    --username admin \
    --password secret 

~~~
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
~~~
```

[[Back]](./README.md)