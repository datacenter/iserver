# Eject Virtual Media

[[Next]](./SetBootOverride.md) [[Back]](./README.md)

```
# iserver set redfish vmedia-eject \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --id 0

Virtual media ejected

~~~
{
    "@odata.id": "/redfish/v1/Managers/CIMC/VirtualMedia/0",
    "@odata.type": "#VirtualMedia.v1_4_0.VirtualMedia",
    "@odata.context": "/redfish/v1/$metadata#VirtualMedia.VirtualMedia",
    "Description": "Virtual Media Settings",
    "TransferMethod": "Stream",
    "WriteProtected": true,
    "Inserted": false,
    "ConnectedVia": "URI",
    "Status": {
        "State": "Updating",
        "Health": "OK"
    },
    "Id": "0",
    "Name": "Virtual CD",
    "MediaTypes": [
        "CD",
        "DVD"
    ],
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/CIMC/VirtualMedia/0/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "Image@Redfish.AllowableValues": [
                "This parameter shall specify the string URI of the remote media to be attached to the virtual media. (Required)"
            ],
            "UserName@Redfish.AllowableValues": [
                "This parameter shall contain a string representing the username to be used when accessing the URI specified by the Image parameter."
            ],
            "Password@Redfish.AllowableValues": [
                "This parameter shall contain a string representing the password to be used when accessing the URI specified by the Image parameter."
            ],
            "WriteProtected@Redfish.AllowableValues": [
                "true"
            ],
            "TransferProtocolType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "NFS"
            ],
            "TransferMethod@Redfish.AllowableValues": [
                "Stream"
            ],
            "Inserted@Redfish.AllowableValues": [
                "true"
            ],
            "target": "/redfish/v1/Managers/CIMC/VirtualMedia/0/Actions/VirtualMedia.InsertMedia"
        }
    }
}
~~~
```

[[Back]](./README.md)