```
  {
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Ancestors": [
      {
        "ClassId": "mo.MoRef",
        "Moid": "64be8af676752d39013fb868",
        "ObjectType": "storage.Controller",
        "link": "https://intersight.com/api/v1/storage/Controllers/64be8af676752d39013fb868"
      },
      {
        "ClassId": "mo.MoRef",
        "Moid": "64be89b276752d39013f581d",
        "ObjectType": "compute.Blade",
        "link": "https://intersight.com/api/v1/compute/Blades/64be89b276752d39013f581d"
      },
      {
        "ClassId": "mo.MoRef",
        "Moid": "64be876876752d39013ea7f4",
        "ObjectType": "equipment.Chassis",
        "link": "https://intersight.com/api/v1/equipment/Chasses/64be876876752d39013ea7f4"
      }
    ],
    "ClassId": "storage.DiskGroup",
    "CreateTime": "2023-10-30T10:11:24.944Z",
    "DedicatedHotSpares": [],
    "DeviceMoId": "64be89606f726131018403d6",
    "Dn": "/redfish/v1/Systems/FCH26447781/Storage/MSTOR-RAID/DiskGroup-253-254",
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "ModTime": "2024-05-08T19:14:40.442Z",
    "Moid": "653f814c76752d39016f255b",
    "Name": "",
    "ObjectType": "storage.DiskGroup",
    "Owners": [
      "5be4b2ce67626c6d661ca38d",
      "64be6ab66f726131018165d8",
      "64be89606f726131018403d6"
    ],
    "Parent": {
      "ClassId": "mo.MoRef",
      "Moid": "64be8af676752d39013fb868",
      "ObjectType": "storage.Controller",
      "link": "https://intersight.com/api/v1/storage/Controllers/64be8af676752d39013fb868"
    },
    "PermissionResources": [
      {
        "ClassId": "mo.MoRef",
        "Moid": "5dee1d736972652d321d26b5",
        "ObjectType": "organization.Organization",
        "link": "https://intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
      },
      {
        "ClassId": "mo.MoRef",
        "Moid": "625706a06972652d3202a8f9",
        "ObjectType": "organization.Organization",
        "link": "https://intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
      },
      {
        "ClassId": "mo.MoRef",
        "Moid": "6242d1016972652d32eda017",
        "ObjectType": "organization.Organization",
        "link": "https://intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
      }
    ],
    "RaidType": "RAID1",
    "RegisteredDevice": {
      "ClassId": "mo.MoRef",
      "Moid": "64be89606f726131018403d6",
      "ObjectType": "asset.DeviceRegistration",
      "link": "https://intersight.com/api/v1/asset/DeviceRegistrations/64be89606f726131018403d6"
    },
    "Rn": "",
    "SharedScope": "",
    "Spans": [
      {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
          {
            "ClassId": "mo.MoRef",
            "Moid": "653f814c76752d39016f255b",
            "ObjectType": "storage.DiskGroup",
            "link": "https://intersight.com/api/v1/storage/DiskGroups/653f814c76752d39016f255b"
          },
          {
            "ClassId": "mo.MoRef",
            "Moid": "64be8af676752d39013fb868",
            "ObjectType": "storage.Controller",
            "link": "https://intersight.com/api/v1/storage/Controllers/64be8af676752d39013fb868"
          },
          {
            "ClassId": "mo.MoRef",
            "Moid": "64be89b276752d39013f581d",
            "ObjectType": "compute.Blade",
            "link": "https://intersight.com/api/v1/compute/Blades/64be89b276752d39013f581d"
          },
          {
            "ClassId": "mo.MoRef",
            "Moid": "64be876876752d39013ea7f4",
            "ObjectType": "equipment.Chassis",
            "link": "https://intersight.com/api/v1/equipment/Chasses/64be876876752d39013ea7f4"
          }
        ],
        "ClassId": "storage.Span",
        "CreateTime": "2023-10-30T10:11:24.947Z",
        "DeviceMoId": "64be89606f726131018403d6",
        "DiskGroup": {
          "ClassId": "mo.MoRef",
          "Moid": "653f814c76752d39016f255b",
          "ObjectType": "storage.DiskGroup",
          "link": "https://intersight.com/api/v1/storage/DiskGroups/653f814c76752d39016f255b"
        },
        "Dn": "/redfish/v1/Systems/FCH26447781/Storage/MSTOR-RAID/DiskGroup-253-254/Span-0",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "ModTime": "2023-10-30T10:11:24.96Z",
        "Moid": "653f814c76752d39016f255a",
        "ObjectType": "storage.Span",
        "Owners": [
          "5be4b2ce67626c6d661ca38d",
          "64be6ab66f726131018165d8",
          "64be89606f726131018403d6"
        ],
        "Parent": {
          "ClassId": "mo.MoRef",
          "Moid": "653f814c76752d39016f255b",
          "ObjectType": "storage.DiskGroup",
          "link": "https://intersight.com/api/v1/storage/DiskGroups/653f814c76752d39016f255b"
        },
        "PermissionResources": [
          {
            "ClassId": "mo.MoRef",
            "Moid": "5dee1d736972652d321d26b5",
            "ObjectType": "organization.Organization",
            "link": "https://intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
          },
          {
            "ClassId": "mo.MoRef",
            "Moid": "625706a06972652d3202a8f9",
            "ObjectType": "organization.Organization",
            "link": "https://intersight.com/api/v1/organization/Organizations/625706a06972652d3202a8f9"
          },
          {
            "ClassId": "mo.MoRef",
            "Moid": "6242d1016972652d32eda017",
            "ObjectType": "organization.Organization",
            "link": "https://intersight.com/api/v1/organization/Organizations/6242d1016972652d32eda017"
          }
        ],
        "PhysicalDisks": [
          {
            "ClassId": "mo.MoRef",
            "Moid": "64be8b5c76752d39013fd8ad",
            "ObjectType": "storage.PhysicalDisk",
            "link": "https://intersight.com/api/v1/storage/PhysicalDisks/64be8b5c76752d39013fd8ad"
          },
          {
            "ClassId": "mo.MoRef",
            "Moid": "64be8b5c76752d39013fd8b8",
            "ObjectType": "storage.PhysicalDisk",
            "link": "https://intersight.com/api/v1/storage/PhysicalDisks/64be8b5c76752d39013fd8b8"
          }
        ],
        "RegisteredDevice": {
          "ClassId": "mo.MoRef",
          "Moid": "64be89606f726131018403d6",
          "ObjectType": "asset.DeviceRegistration",
          "link": "https://intersight.com/api/v1/asset/DeviceRegistrations/64be89606f726131018403d6"
        },
        "Rn": "",
        "SharedScope": "",
        "Slots": [
          253,
          254
        ],
        "SpanId": 0,
        "Tags": []
      }
    ],
    "StorageController": {
      "ClassId": "mo.MoRef",
      "Moid": "64be8af676752d39013fb868",
      "ObjectType": "storage.Controller",
      "link": "https://intersight.com/api/v1/storage/Controllers/64be8af676752d39013fb868"
    },
    "Tags": [],
    "VirtualDrives": [
      {
        "ClassId": "mo.MoRef",
        "Moid": "653f814c76752d39016f2553",
        "ObjectType": "storage.VirtualDrive",
        "link": "https://intersight.com/api/v1/storage/VirtualDrives/653f814c76752d39016f2553"
      }
    ]
  }
```