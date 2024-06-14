```
  {
    "AccountMoid": "5be4b2ce67626c6d661ca38d",
    "Ancestors": [
      {
        "ClassId": "mo.MoRef",
        "Moid": "63fa370e736c6f2d30b8c272",
        "ObjectType": "virtualization.VmwareCluster",
        "link": "https://www.intersight.com/api/v1/virtualization/VmwareClusters/63fa370e736c6f2d30b8c272"
      },
      {
        "ClassId": "mo.MoRef",
        "Moid": "63fa370e736c6f2d30b8c260",
        "ObjectType": "virtualization.VmwareDatacenter",
        "link": "https://www.intersight.com/api/v1/virtualization/VmwareDatacenters/63fa370e736c6f2d30b8c260"
      },
      {
        "ClassId": "mo.MoRef",
        "Moid": "63fa370e736c6f2d30b8c255",
        "ObjectType": "virtualization.VmwareVcenter",
        "link": "https://www.intersight.com/api/v1/virtualization/VmwareVcenters/63fa370e736c6f2d30b8c255"
      }
    ],
    "BootTime": "2023-03-01T21:34:51.554Z",
    "ClassId": "virtualization.VmwareHost",
    "Cluster": {
      "ClassId": "mo.MoRef",
      "Moid": "63fa370e736c6f2d30b8c272",
      "ObjectType": "virtualization.VmwareCluster",
      "link": "https://www.intersight.com/api/v1/virtualization/VmwareClusters/63fa370e736c6f2d30b8c272"
    },
    "ConnectionState": "connected",
    "CpuInfo": {
      "ClassId": "virtualization.CpuInfo",
      "Cores": 28,
      "Description": "Intel(R) Xeon(R) CPU E5-2695 v3 @ 2.30GHz",
      "ObjectType": "virtualization.CpuInfo",
      "Sockets": 2,
      "Speed": 2294,
      "Vendor": "intel"
    },
    "CreateTime": "2023-02-25T16:28:00.869Z",
    "Datacenter": null,
    "Datastores": [
      {
        "ClassId": "mo.MoRef",
        "Moid": "63fa371a736c6f2d30b8ce26",
        "ObjectType": "virtualization.VmwareDatastore",
        "link": "https://www.intersight.com/api/v1/virtualization/VmwareDatastores/63fa371a736c6f2d30b8ce26"
      }
    ],
    "DcInvPath": "/eu-spdc-dc",
    "DistributedNetworks": [
      {
        "ClassId": "mo.MoRef",
        "Moid": "63fa3711736c6f2d30b8c30b",
        "ObjectType": "virtualization.VmwareDistributedNetwork",
        "link": "https://www.intersight.com/api/v1/virtualization/VmwareDistributedNetworks/63fa3711736c6f2d30b8c30b"
      }
    ],
    "DnsServers": [
      "<ip>",
      "<ip>"
    ],
    "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
    "HardwareInfo": {
      "ClassId": "infra.HardwareInfo",
      "CpuCores": 28,
      "CpuSpeed": 2294,
      "MemorySize": 274759602176,
      "ObjectType": "infra.HardwareInfo"
    },
    "HwPowerState": "PoweredOn",
    "HyperFlexNode": null,
    "HypervisorType": "ESXi",
    "Identity": "HostSystem:host-2164",
    "IsSshEnabled": true,
    "MaintenanceMode": false,
    "MemoryCapacity": {
      "Capacity": 274759602176,
      "ClassId": "virtualization.MemoryCapacity",
      "Free": 124965277696,
      "ObjectType": "virtualization.MemoryCapacity",
      "Used": 149794324480
    },
    "ModTime": "2023-03-31T09:25:48.674Z",
    "Model": "UCSC-C220-M4S",
    "Moid": "63fa3710736c6f2d30b8c2b0",
    "Name": "esx10",
    "NetworkAdapterCount": 12,
    "NtpServers": [
      "<fqdn>"
    ],
    "ObjectType": "virtualization.VmwareHost",
    "Owners": [
      "5be4b2ce67626c6d661ca38d",
      "63f9ce3f6f72612d31d940f9",
      "63f9edb56f72612d395f0600",
      "63fa37046f72612d39626f62"
    ],
    "Parent": {
      "ClassId": "mo.MoRef",
      "Moid": "63fa370e736c6f2d30b8c272",
      "ObjectType": "virtualization.VmwareCluster",
      "link": "https://www.intersight.com/api/v1/virtualization/VmwareClusters/63fa370e736c6f2d30b8c272"
    },
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
    "ProcessorCapacity": {
      "Capacity": 64245,
      "ClassId": "virtualization.ComputeCapacity",
      "Free": 43088,
      "ObjectType": "virtualization.ComputeCapacity",
      "Used": 21157
    },
    "ProductInfo": {
      "Build": "19482537",
      "ClassId": "virtualization.ProductInfo",
      "ObjectType": "virtualization.ProductInfo",
      "ProductName": "VMware ESXi",
      "ProductType": "embeddedEsx",
      "ProductVendor": "VMware, Inc.",
      "Version": "7.0.3"
    },
    "RegisteredDevice": {
      "ClassId": "mo.MoRef",
      "Moid": "63fa37046f72612d39626f62",
      "ObjectType": "asset.DeviceRegistration",
      "link": "https://www.intersight.com/api/v1/asset/DeviceRegistrations/63fa37046f72612d39626f62"
    },
    "ResourceConsumed": {
      "ClassId": "virtualization.VmwareResourceConsumption",
      "CpuConsumed": 21157,
      "MemoryConsumed": 142855,
      "ObjectType": "virtualization.VmwareResourceConsumption"
    },
    "Serial": "FCH2017V0TN",
    "Server": {
      "ClassId": "mo.MoRef",
      "Moid": "5fa052a26176752d35ce6572",
      "ObjectType": "compute.PhysicalSummary",
      "link": "https://www.intersight.com/api/v1/compute/PhysicalSummaries/5fa052a26176752d35ce6572"
    },
    "SharedScope": "",
    "Status": "Ok",
    "StorageAdapterCount": 4,
    "Tags": [],
    "TimeZone": "UTC",
    "UpTime": "P29DT11H48M50S",
    "Uuid": "0785f9dd-6c2d-d047-91b1-8d1055824d36",
    "VcenterHostId": "host-2164",
    "Vendor": "Cisco Systems Inc"
    }
```