# Server Details - Profile

```
# iserver get server --name comp-5-p2b-eu-spdc-WMP2404000R --profile

+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | WF (7d) | Name                           | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+
| P- H | CRi |         | comp-5-p2b-eu-spdc-WMP2404000R | (R) UCSC-C220-M5SX | WMP2404000R | 10.58.50.45 | 2S 40C 80T | 384 [GiB] | 
+------+-----+---------+--------------------------------+--------------------+-------------+-------------+------------+-----------+

Server Profile
--------------
- Name            : vanniew-kali-import
- State           : Out-of-sync
- Last Modified   : 2022-12-21T08:24:45.224Z
- Target Platform : Standalone


+------------------------------------------+----------------------------+--------------------------+--------+---------+
| Policy Name                              | Class Id                   | Modification Time        | Shared | In Sync |
+------------------------------------------+----------------------------+--------------------------+--------+---------+
| vanniew-kali-virtual-kvm-policy          | kvm.Policy                 | 2022-12-01T16:35:17.517Z | False  | True    | 
| vanniew-kali-local-user-policy           | iam.EndPointUserPolicy     | 2022-12-01T16:08:18.971Z | False  | True    | 
| vanniew-kali-san-connectivity-policy     | vnic.SanConnectivityPolicy | 2022-12-01T15:47:10.285Z | False  | True    | 
| vanniew-kali-lan-connectivity-policy     | vnic.LanConnectivityPolicy | 2022-12-01T15:47:10.274Z | False  | True    | 
| vanniew-kali-adapter-config-policy       | adapter.ConfigPolicy       | 2022-12-01T15:47:10.263Z | False  | True    | 
| vanniew-kali-storage-policy              | storage.StoragePolicy      | 2022-12-01T15:47:10.116Z | False  | True    | 
| vanniew-kali-syslog-policy               | syslog.Policy              | 2022-12-01T15:47:09.984Z | False  | True    | 
| vanniew-kali-virtual-media-policy        | vmedia.Policy              | 2022-12-01T15:47:09.983Z | False  | False   | 
| vanniew-kali-ssh-policy                  | ssh.Policy                 | 2022-12-01T15:47:09.981Z | False  | True    | 
| vanniew-kali-serial-over-lan-policy      | sol.Policy                 | 2022-12-01T15:47:09.978Z | False  | True    | 
| vanniew-kali-snmp-policy                 | snmp.Policy                | 2022-12-01T15:47:09.976Z | False  | True    | 
| vanniew-kali-smtp-policy                 | smtp.Policy                | 2022-12-01T15:47:09.974Z | False  | True    | 
| vanniew-kali-ntp-policy                  | ntp.Policy                 | 2022-12-01T15:47:09.972Z | False  | True    | 
| vanniew-kali-network-connectivity-policy | networkconfig.Policy       | 2022-12-01T15:47:09.971Z | False  | True    | 
| vanniew-kali-ldap-policy                 | iam.LdapPolicy             | 2022-12-01T15:47:09.969Z | False  | True    | 
| vanniew-kali-ipmi-over-lan-policy        | ipmioverlan.Policy         | 2022-12-01T15:47:09.965Z | False  | True    | 
| vanniew-kali-boot-order-policy           | boot.PrecisionPolicy       | 2022-12-01T15:47:09.961Z | False  | True    | 
| vanniew-kali-bios-policy                 | bios.Policy                | 2022-12-01T15:47:09.959Z | False  | True    | 
+------------------------------------------+----------------------------+--------------------------+--------+---------+
```

JSON output

```
# iserver get server --name comp-5-p2b-eu-spdc-WMP2404000R --profile

{
    "__Output": {
        "FlagState": ":RR.G",
        "FlagManagement": ":GGY",
        "FlagWorkflow": ":"
    },
    "Moid": "5fdfdc3b6176752d35fce0a9",
    "DeviceMoId": "5fdfdc206f72612d30120ab4",
    "Name": "comp-5-p2b-eu-spdc-WMP2404000R",
    "Model": "UCSC-C220-M5SX",
    "Serial": "WMP2404000R",
    "ManagementMode": "IntersightStandalone",
    "OperPowerState": "off",
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C220-M5SX",
    "NumCpus": 2,
    "NumCpuCores": 40,
    "NumThreads": 80,
    "Cpu": "2S 40C 80T",
    "Groups": "p2b,pod2b,power",
    "AlarmSummary": {
        "__Output": {
            "Critical": "Red",
            "Warning": "Yellow",
            "Info": "Blue",
            "Cleared": "Green"
        },
        "Critical": 0,
        "Warning": 0,
        "Info": 0
    },
    "Health": "Healthy",
    "LocatorLedOn": false,
    "ManagementIp": "10.58.50.45",
    "Redfish": {
        "Capable": true,
        "Enabled": true
    },
    "UCSM": {
        "Capable": false,
        "Enabled": false
    },
    "IMC": {
        "Capable": true,
        "Enabled": false
    },
    "AvailableMemory": 393216,
    "TotalMemory": 393216,
    "UsedMemory": 0,
    "TotalMemoryUnit": "384 [GiB]",
    "TotalMemoryGB": 384,
    "AvailableMemoryUnit": "384 [GiB]",
    "AvailableMemoryGB": 384,
    "UsedMemoryUnit": "0 [KiB]",
    "UsedMemoryGB": 0,
    "UsedMemoryPct": 0,
    "UsedMemoryPctUnit": "0%",
    "ProfileInfo": {
        "__Output": {
            "ConfigState": "Red"
        },
        "Name": "vanniew-kali-import",
        "ModTime": "2022-12-21T08:24:45.224Z",
        "Moid": "6388cc2377696e2d31e0856d",
        "ServerAssignmentMode": "Static",
        "TargetPlatform": "Standalone",
        "Type": "instance",
        "ConfigState": "Out-of-sync",
        "ConfigChangeState": "Ok",
        "ConfigChangeDetails": [
            {
                "EntityMoid": "6388cc3e6275722d3050adef",
                "EntityType": "vmedia.Policy"
            }
        ],
        "Policies": [
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc356275722d3050acb4",
                "Name": "vanniew-kali-virtual-kvm-policy",
                "ModTime": "2022-12-01T16:35:17.517Z",
                "ClassId": "kvm.Policy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc336275722d3050ac67",
                "Name": "vanniew-kali-local-user-policy",
                "ModTime": "2022-12-01T16:08:18.971Z",
                "ClassId": "iam.EndPointUserPolicy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc7cf9d5e4864f8abd6c",
                "Name": "vanniew-kali-san-connectivity-policy",
                "ModTime": "2022-12-01T15:47:10.285Z",
                "ClassId": "vnic.SanConnectivityPolicy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc64f9d5e4864f8abaa0",
                "Name": "vanniew-kali-lan-connectivity-policy",
                "ModTime": "2022-12-01T15:47:10.274Z",
                "ClassId": "vnic.LanConnectivityPolicy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc4ef9d5e4864f8ab833",
                "Name": "vanniew-kali-adapter-config-policy",
                "ModTime": "2022-12-01T15:47:10.263Z",
                "ClassId": "adapter.ConfigPolicy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc4a656f6e2d30975404",
                "Name": "vanniew-kali-storage-policy",
                "ModTime": "2022-12-01T15:47:10.116Z",
                "ClassId": "storage.StoragePolicy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc3f6275722d3050ae0b",
                "Name": "vanniew-kali-syslog-policy",
                "ModTime": "2022-12-01T15:47:09.984Z",
                "ClassId": "syslog.Policy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Red"
                },
                "Moid": "6388cc3e6275722d3050adef",
                "Name": "vanniew-kali-virtual-media-policy",
                "ModTime": "2022-12-01T15:47:09.983Z",
                "ClassId": "vmedia.Policy",
                "Shared": false,
                "InSync": false
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc3d6275722d3050adc2",
                "Name": "vanniew-kali-ssh-policy",
                "ModTime": "2022-12-01T15:47:09.981Z",
                "ClassId": "ssh.Policy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc3d6275722d3050adab",
                "Name": "vanniew-kali-serial-over-lan-policy",
                "ModTime": "2022-12-01T15:47:09.978Z",
                "ClassId": "sol.Policy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc3c6275722d3050ad9f",
                "Name": "vanniew-kali-snmp-policy",
                "ModTime": "2022-12-01T15:47:09.976Z",
                "ClassId": "snmp.Policy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc3a6275722d3050ad69",
                "Name": "vanniew-kali-smtp-policy",
                "ModTime": "2022-12-01T15:47:09.974Z",
                "ClassId": "smtp.Policy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc396275722d3050ad45",
                "Name": "vanniew-kali-ntp-policy",
                "ModTime": "2022-12-01T15:47:09.972Z",
                "ClassId": "ntp.Policy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc376275722d3050ad01",
                "Name": "vanniew-kali-network-connectivity-policy",
                "ModTime": "2022-12-01T15:47:09.971Z",
                "ClassId": "networkconfig.Policy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc376275722d3050acec",
                "Name": "vanniew-kali-ldap-policy",
                "ModTime": "2022-12-01T15:47:09.969Z",
                "ClassId": "iam.LdapPolicy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc356275722d3050ac97",
                "Name": "vanniew-kali-ipmi-over-lan-policy",
                "ModTime": "2022-12-01T15:47:09.965Z",
                "ClassId": "ipmioverlan.Policy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc316275722d3050ac1f",
                "Name": "vanniew-kali-boot-order-policy",
                "ModTime": "2022-12-01T15:47:09.961Z",
                "ClassId": "boot.PrecisionPolicy",
                "Shared": false,
                "InSync": true
            },
            {
                "__Output": {
                    "InSync": "Green"
                },
                "Moid": "6388cc266275722d3050aad2",
                "Name": "vanniew-kali-bios-policy",
                "ModTime": "2022-12-01T15:47:09.959Z",
                "ClassId": "bios.Policy",
                "Shared": false,
                "InSync": true
            }
        ]
    },
    "Connected": true,
    "Workflow": {
        "Days": 7,
        "Running": null,
        "LatestMoid": null,
        "Last": []
    },
    "FlagState": "P- H",
    "FlagManagement": "CRi",
    "FlagWorkflow": ""
}
```

Developer output

```
# iserver get server --name comp-5-p2b-eu-spdc-WMP2404000R --profile

Developer output

{
    "duration": 17245,
    "isctl": {
        "read": true,
        "calls": 7,
        "success": 7,
        "failed": 0,
        "total_time": 12890
    },
    "redfish": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "path": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "path_time": 0,
        "total_time": 0
    },
    "ucsm": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "mo": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "mo_time": 0,
        "total_time": 0
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": true,
        "lines": 475
    }
}

Log: isctl
-----------

2023-01-05 18:51:19.024466	True	3117	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:51:20.839152	True	1811	10	isctl get compute blade   -o json --top 100
2023-01-05 18:51:25.825893	True	1544	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '5fdfdc206f72612d30120ab4'"  -o json --top 100
2023-01-05 18:51:27.382617	True	1555	1	isctl get server profile --filter "AssignedServer/Moid eq '5fdfdc3b6176752d35fce0a9'" --expand "ConfigChangeDetails" -o json --top 100
2023-01-05 18:51:29.184681	True	1798	18	isctl get search searchitem --filter "IndexMotypes eq 'policy.AbstractPolicy' and Profiles/any(a:a/Moid eq '6388cc2377696e2d31e0856d')"  -o json --top 100
2023-01-05 18:51:30.647795	True	1455	1	isctl get asset deviceregistration  moid 5fdfdc206f72612d30120ab4 -o json
2023-01-05 18:51:32.264388	True	1610	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:51:30.000Z"  -o json --top 100
```
