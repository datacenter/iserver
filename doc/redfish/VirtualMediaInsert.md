# Insert Virtual Media

[[Next]](./VirtualMediaEject.md) [[Back]](./README.md)

```
# iserver set redfish vmedia-insert \
    --ip 10.10.10.10 \
    --type fi \
    --inventory-type Server \
    --inventory-id ucs-1-3 \
    --username admin \
    --password secret \
    --id 3 \
    --url http://myhttp/iso/boot.iso

Virtual media inserted
Wait for virtual media inserted...

~~~
{
    "@odata.context": "/redfish/v1/$metadata#VirtualMedia.VirtualMedia",
    "@odata.id": "/redfish/v1/Managers/CIMC/VirtualMedia/3",
    "@odata.type": "#VirtualMedia.v1_4_0.VirtualMedia",
    "Actions": {
        "#VirtualMedia.EjectMedia": {
            "target": "/redfish/v1/Managers/CIMC/VirtualMedia/3/Actions/VirtualMedia.EjectMedia"
        },
        "#VirtualMedia.InsertMedia": {
            "Image@Redfish.AllowableValues": [
                "This parameter shall specify the string URI of the remote media to be attached to the virtual media. (Required)"
            ],
            "Password@Redfish.AllowableValues": [
                "This parameter shall contain a string representing the password to be used when accessing the URI specified by the Image parameter."
            ],
            "TransferProtocolType@Redfish.AllowableValues": [
                "CIFS",
                "HTTP",
                "HTTPS",
                "NFS",
                "OEM"
            ],
            "UserName@Redfish.AllowableValues": [
                "This parameter shall contain a string representing the username to be used when accessing the URI specified by the Image parameter."
            ],
            "WriteProtected@Redfish.AllowableValues": [
                "This shall contain a bool (true|false) if the media is to be write protected. (Default true)"
            ],
            "target": "/redfish/v1/Managers/CIMC/VirtualMedia/3/Actions/VirtualMedia.InsertMedia"
        }
    },
    "ConnectedVia": "URI",
    "Description": "Virtual Media Settings",
    "Id": "3",
    "Image": "http://myhttp/iso/boot.iso",
    "ImageName": "boot.iso",
    "Inserted": true,
    "MediaTypes": [
        "DVD"
    ],
    "Name": "CIMC-Mapped vDVD",
    "Oem": {
        "Cisco": {
            "@odata.type": "#CiscoUCSExtensions.v1_0_0.CiscoUCSExtensions",
            "ImageNameVariable": "boot.iso",
            "RemapOnEject": null
        }
    },
    "Password": null,
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "TransferProtocolType": "HTTP",
    "UserName": null,
    "WriteProtected": true
}
~~~
```

[[Back]](./README.md)