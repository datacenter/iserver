```
{
    "AccountMoid": "5a0a0877b657050001659aff",
    "Ancestors": [
      {
        "ClassId": "mo.MoRef",
        "Moid": "6621228b76752d3001efbc6d",
        "ObjectType": "pci.Node",
        "link": "https://intersight.com/api/v1/pci/Nodes/6621228b76752d3001efbc6d"
      },
      {
        "ClassId": "mo.MoRef",
        "Moid": "66211b4976752d3001ec6be2",
        "ObjectType": "compute.Blade",
        "link": "https://intersight.com/api/v1/compute/Blades/66211b4976752d3001ec6be2"
      },
      {
        "ClassId": "mo.MoRef",
        "Moid": "65fa07d976752d300152cacb",
        "ObjectType": "equipment.Chassis",
        "link": "https://intersight.com/api/v1/equipment/Chasses/65fa07d976752d300152cacb"
      }
    ],
    "CardId": 0,
    "ClassId": "graphics.Card",
    "ComputeBlade": null,
    "ComputeBoard": null,
    "ComputeRackUnit": null,
    "CreateTime": "2024-04-18T13:39:23.741Z",
    "Description": "NVIDIA A40 PCIe FHFL DS 48GB GDDR6 300W",
    "DeviceId": 8757,
    "DeviceMoId": "65fa990a6f72613001fcd492",
    "Dn": "/redfish/v1/Systems/FCH25337EJ9/Processors/CHASSIS-SLOT4-RISER1A-SLOT1",
    "DomainGroupMoid": "5b2541917a7662743465cfeb",
    "ExpanderSlot": "",
    "FirmwareVersion": "94.02.5C.00.03-G133.0200.00.05",
    "GpuId": "PCIe-Node4-GPU1",
    "GraphicsControllers": [
      {
        "AccountMoid": "5a0a0877b657050001659aff",
        "Ancestors": [
          {
            "ClassId": "mo.MoRef",
            "Moid": "6621228b76752d3001efbc6f",
            "ObjectType": "graphics.Card",
            "link": "https://intersight.com/api/v1/graphics/Cards/6621228b76752d3001efbc6f"
          },
          {
            "ClassId": "mo.MoRef",
            "Moid": "6621228b76752d3001efbc6d",
            "ObjectType": "pci.Node",
            "link": "https://intersight.com/api/v1/pci/Nodes/6621228b76752d3001efbc6d"
          },
          {
            "ClassId": "mo.MoRef",
            "Moid": "66211b4976752d3001ec6be2",
            "ObjectType": "compute.Blade",
            "link": "https://intersight.com/api/v1/compute/Blades/66211b4976752d3001ec6be2"
          },
          {
            "ClassId": "mo.MoRef",
            "Moid": "65fa07d976752d300152cacb",
            "ObjectType": "equipment.Chassis",
            "link": "https://intersight.com/api/v1/equipment/Chasses/65fa07d976752d300152cacb"
          }
        ],
        "ClassId": "graphics.Controller",
        "ControllerId": 1,
        "CreateTime": "2024-04-18T13:39:23.747Z",
        "DeviceMoId": "",
        "Dn": "/redfish/v1/Systems/FCH25337EJ9/Processors/CHASSIS-SLOT4-RISER1A-SLOT1-1",
        "DomainGroupMoid": "5b2541917a7662743465cfeb",
        "GraphicsCard": {
          "ClassId": "mo.MoRef",
          "Moid": "6621228b76752d3001efbc6f",
          "ObjectType": "graphics.Card",
          "link": "https://intersight.com/api/v1/graphics/Cards/6621228b76752d3001efbc6f"
        },
        "InventoryDeviceInfo": null,
        "IsUpgraded": false,
        "ModTime": "2024-05-08T13:30:09.592Z",
        "Model": "UCSC-GPU-A40",
        "Moid": "6621228b76752d3001efbc71",
        "ObjectType": "graphics.Controller",
        "Owners": [
          "5a0a0877b657050001659aff",
          "65f9b2676f72613001fad35d",
          "65fa990a6f72613001fcd492"
        ],
        "Parent": {
          "ClassId": "mo.MoRef",
          "Moid": "6621228b76752d3001efbc6f",
          "ObjectType": "graphics.Card",
          "link": "https://intersight.com/api/v1/graphics/Cards/6621228b76752d3001efbc6f"
        },
        "PciAddr": "31:0.0",
        "PciSlot": "CHASSIS-SLOT4-RISER1A-SLOT1",
        "PermissionResources": [
          {
            "ClassId": "mo.MoRef",
            "Moid": "5ddec94c6972652d3101bdce",
            "ObjectType": "organization.Organization",
            "link": "https://intersight.com/api/v1/organization/Organizations/5ddec94c6972652d3101bdce"
          }
        ],
        "Presence": "equipped",
        "PreviousFru": null,
        "RegisteredDevice": null,
        "Revision": "",
        "Rn": "",
        "Serial": "1562721013334",
        "SharedScope": "",
        "Tags": [],
        "Vendor": "NVIDIA"
      }
    ],
    "InventoryDeviceInfo": null,
    "IsPlatformSupported": true,
    "IsUpgraded": true,
    "ModTime": "2024-05-12T23:05:04.197Z",
    "Mode": "",
    "Model": "UCSC-GPU-A40",
    "Moid": "6621228b76752d3001efbc6f",
    "NumGpus": "1",
    "ObjectType": "graphics.Card",
    "OperReason": [],
    "OperState": "OK",
    "Owners": [
      "5a0a0877b657050001659aff",
      "65f9b2676f72613001fad35d",
      "65fa990a6f72613001fcd492"
    ],
    "Parent": {
      "ClassId": "mo.MoRef",
      "Moid": "6621228b76752d3001efbc6d",
      "ObjectType": "pci.Node",
      "link": "https://intersight.com/api/v1/pci/Nodes/6621228b76752d3001efbc6d"
    },
    "PartNumber": "30-100281-01",
    "PciAddress": "",
    "PciAddressList": "",
    "PciDevice": null,
    "PciNode": {
      "AccountMoid": "5a0a0877b657050001659aff",
      "Ancestors": [
        {
          "ClassId": "mo.MoRef",
          "Moid": "66211b4976752d3001ec6be2",
          "ObjectType": "compute.Blade",
          "link": "https://intersight.com/api/v1/compute/Blades/66211b4976752d3001ec6be2"
        },
        {
          "ClassId": "mo.MoRef",
          "Moid": "65fa07d976752d300152cacb",
          "ObjectType": "equipment.Chassis",
          "link": "https://intersight.com/api/v1/equipment/Chasses/65fa07d976752d300152cacb"
        }
      ],
      "ChassisId": "1",
      "ClassId": "pci.Node",
      "ComputeBlade": {
        "ClassId": "mo.MoRef",
        "Moid": "66211b4976752d3001ec6be2",
        "ObjectType": "compute.Blade",
        "link": "https://intersight.com/api/v1/compute/Blades/66211b4976752d3001ec6be2"
      },
      "CreateTime": "2024-04-18T13:39:23.733Z",
      "DeviceMoId": "65fa990a6f72613001fcd492",
      "Dn": "/redfish/v1/Chassis/FCH261171XR/Assembly#/Assemblies/CHASSIS-SLOT4",
      "DomainGroupMoid": "5b2541917a7662743465cfeb",
      "GraphicsCards": [
        {
          "ClassId": "mo.MoRef",
          "Moid": "6621228b76752d3001efbc6f",
          "ObjectType": "graphics.Card",
          "link": "https://intersight.com/api/v1/graphics/Cards/6621228b76752d3001efbc6f"
        }
      ],
      "InventoryDeviceInfo": null,
      "IsUpgraded": false,
      "ModTime": "2024-05-08T13:30:09.583Z",
      "Model": "UCSX-440P",
      "Moid": "6621228b76752d3001efbc6d",
      "ObjectType": "pci.Node",
      "OperReason": [],
      "Owners": [
        "5a0a0877b657050001659aff",
        "65f9b2676f72613001fad35d",
        "65fa990a6f72613001fcd492"
      ],
      "Parent": {
        "ClassId": "mo.MoRef",
        "Moid": "66211b4976752d3001ec6be2",
        "ObjectType": "compute.Blade",
        "link": "https://intersight.com/api/v1/compute/Blades/66211b4976752d3001ec6be2"
      },
      "PermissionResources": [
        {
          "ClassId": "mo.MoRef",
          "Moid": "5ddec94c6972652d3101bdce",
          "ObjectType": "organization.Organization",
          "link": "https://intersight.com/api/v1/organization/Organizations/5ddec94c6972652d3101bdce"
        }
      ],
      "Presence": "equipped",
      "PreviousFru": null,
      "RegisteredDevice": {
        "ClassId": "mo.MoRef",
        "Moid": "65fa990a6f72613001fcd492",
        "ObjectType": "asset.DeviceRegistration",
        "link": "https://intersight.com/api/v1/asset/DeviceRegistrations/65fa990a6f72613001fcd492"
      },
      "Revision": "",
      "Rn": "",
      "Serial": "FCH261171XR",
      "SharedScope": "",
      "SlotId": "4",
      "Tags": [],
      "Vendor": "Cisco Systems Inc"
    },
    "PciSlot": "CHASSIS-SLOT4-RISER1A-SLOT1",
    "PermissionResources": [
      {
        "ClassId": "mo.MoRef",
        "Moid": "5ddec94c6972652d3101bdce",
        "ObjectType": "organization.Organization",
        "link": "https://intersight.com/api/v1/organization/Organizations/5ddec94c6972652d3101bdce"
      }
    ],
    "Pid": "UCSC-GPU-A40",
    "Presence": "equipped",
    "PreviousFru": null,
    "RegisteredDevice": {
      "ClassId": "mo.MoRef",
      "Moid": "65fa990a6f72613001fcd492",
      "ObjectType": "asset.DeviceRegistration",
      "link": "https://intersight.com/api/v1/asset/DeviceRegistrations/65fa990a6f72613001fcd492"
    },
    "Revision": "",
    "Rn": "",
    "RunningFirmware": [],
    "Serial": "1562721013334",
    "SharedScope": "",
    "SubDeviceId": 5210,
    "SubVendorId": 4318,
    "Tags": [],
    "Vendor": "NVIDIA",
    "VendorId": 4318
}
```