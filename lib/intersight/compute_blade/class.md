```
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Adapters": [],
        "AdminPowerState": "policy",
        "AlarmSummary": {
            "ClassId": "compute.AlarmSummary",
            "Critical": 0,
            "ObjectType": "compute.AlarmSummary",
            "Warning": 0
        },
        "Alerts": [],
        "Ancestors": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "619d05ae76752d313994a00a",
                "ObjectType": "equipment.Chassis",
                "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
            }
        ],
        "AssetTag": "",
        "AvailableMemory": 393216,
        "BiosBootmode": null,
        "BiosPostComplete": false,
        "BiosTokenSettings": null,
        "BiosUnits": [],
        "BiosVfSelectMemoryRasConfiguration": null,
        "Bmc": {
            "ClassId": "mo.MoRef",
            "Moid": "63347c2776752d3139813840",
            "ObjectType": "management.Controller",
            "link": "https://www.intersight.com/api/v1/management/Controllers/63347c2776752d3139813840"
        },
        "Board": null,
        "BootCddDevices": [],
        "BootDeviceBootSecurity": null,
        "BootDeviceBootmode": null,
        "BootHddDevices": [],
        "BootIscsiDevices": [],
        "BootNvmeDevices": [],
        "BootPchStorageDevices": [],
        "BootPxeDevices": [],
        "BootSanDevices": [],
        "BootSdDevices": [],
        "BootUefiShellDevices": [],
        "BootUsbDevices": [],
        "BootVmediaDevices": [],
        "ChassisId": "2",
        "ClassId": "compute.Blade",
        "CreateTime": "2022-09-28T16:52:10.992Z",
        "DeviceMoId": "618942976f72612d309dfbe1",
        "Dn": "sys/chassis-2/blade-1",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "EquipmentChassis": {
            "ClassId": "mo.MoRef",
            "Moid": "619d05ae76752d313994a00a",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
        },
        "EquipmentIoExpanders": [],
        "FaultSummary": 0,
        "GenericInventoryHolders": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "6334904f76752d313984d14b",
                "ObjectType": "inventory.GenericInventoryHolder",
                "link": "https://www.intersight.com/api/v1/inventory/GenericInventoryHolders/6334904f76752d313984d14b"
            }
        ],
        "GraphicsCards": [],
        "HardwareUuid": "",
        "InventoryDeviceInfo": null,
        "KvmIpAddresses": [
            {
                "Address": "<ip>",
                "Category": "Equipment",
                "ClassId": "compute.IpAddress",
                "DefaultGateway": "",
                "Dn": "sys/chassis-2/blade-1/mgmt/ipv4-static-addr",
                "HttpPort": 80,
                "HttpsPort": 443,
                "KvmPort": 2068,
                "KvmVlan": 0,
                "Name": "Outband",
                "ObjectType": "compute.IpAddress",
                "Subnet": "",
                "Type": "VnicIpV4StaticAddr"
            }
        ],
        "KvmServerStateEnabled": false,
        "KvmVendor": "",
        "LocatorLed": null,
        "ManagementMode": "UCSM",
        "MemoryArrays": [],
        "MemorySpeed": "2666",
        "MgmtIdentity": null,
        "MgmtIpAddress": "<ip>",
        "ModTime": "2022-09-28T18:19:59.019Z",
        "Model": "UCSB-B200-M5",
        "Moid": "63347bba76752d313981268f",
        "Name": "FI-ucsb1-eu-spdc-2-1",
        "NumAdaptors": 2,
        "NumCpuCores": 40,
        "NumCpuCoresEnabled": 40,
        "NumCpus": 2,
        "NumEthHostInterfaces": 8,
        "NumFcHostInterfaces": 0,
        "NumThreads": 80,
        "ObjectType": "compute.Blade",
        "OperPowerState": "on",
        "OperReason": [],
        "OperState": "ok",
        "Operability": "operable",
        "Owners": [
        "5be4b2ce67626c6d661ca38d",
        "618942976f72612d309dfbe1"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "619d05ae76752d313994a00a",
            "ObjectType": "equipment.Chassis",
            "link": "https://www.intersight.com/api/v1/equipment/Chasses/619d05ae76752d313994a00a"
        },
        "PciDevices": [],
        "PciNodes": [],
        "PermissionResources": [
            {
                "ClassId": "mo.MoRef",
                "Moid": "5dee1d736972652d321d26b5",
                "ObjectType": "organization.Organization",
                "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "625706a06972652d3202a8f9",
                "ObjectType": "organization.Organization",
                "link": "https://www.intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
            },
            {
                "ClassId": "mo.MoRef",
                "Moid": "6242d1016972652d32eda017",
                "ObjectType": "organization.Organization",
                "link": "https://www.intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
            }
        ],
        "PlatformType": "UCSFI",
        "Presence": "equipped",
        "PreviousFru": null,
        "Processors": [],
        "RegisteredDevice": {
            "ClassId": "mo.MoRef",
            "Moid": "618942976f72612d309dfbe1",
            "ObjectType": "asset.DeviceRegistration",
            "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/618942976f72612d309dfbe1"
        },
        "Revision": "0",
        "Rn": "",
        "ScaledMode": "none",
        "Serial": "FLM241501FB",
        "ServiceProfile": "org-root/org-EU-SPN/ls-esx51-eu-spdc",
        "SharedScope": "",
        "SlotId": 1,
        "StorageControllers": [],
        "StorageEnclosures": [],
        "Tags": [
            {
                "Key": "Intersight.LicenseTier",
                "Value": "Premier"
            }
        ],
        "TopSystem": {
            "ClassId": "mo.MoRef",
            "Moid": "618942be76752d3139ace73b",
            "ObjectType": "top.System",
            "link": "https://www.intersight.com/api/v1/top/Systems/618942be76752d3139ace73b"
        },
        "TotalMemory": 393216,
        "TunneledKvm": false,
        "UserLabel": "",
        "Uuid": "315220a5-2121-4e5b-0101-e1dc0000010f",
        "Vendor": "Cisco Systems Inc",
        "Vmedia": null
    }
```