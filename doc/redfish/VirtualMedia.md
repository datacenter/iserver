# Get Virtual Media

[[Next]](./Key.md) [[Back]](./README.md)

Note:
- add --id parameter to limit output to selected virtual media id

```
# iserver.py get redfish vmedia \
    --ip 10.10.10.10 \
    --username admin \
    --password secret 

Virtual Media [#0]
------------------

~~~
{
    "@odata.id": "/redfish/v1/Managers/CIMC/VirtualMedia/0",
    "@odata.type": "#VirtualMedia.v1_4_0.VirtualMedia",
    "@odata.context": "/redfish/v1/$metadata#VirtualMedia.VirtualMedia",
    "Description": "Virtual Media Settings",
    "TransferMethod": "Stream",
    "WriteProtected": true,
    "Inserted": false,
    "ConnectedVia": "NotConnected",
    "Status": {
        "State": "Disabled",
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

...
```

[[Back]](./README.md)