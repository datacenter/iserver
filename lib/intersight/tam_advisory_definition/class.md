```
    {
        "AccountMoid": "5960901ca94eba000127e33a",
        "Actions": [
        {
            "AffectedObjectType": "hyperflex.Cluster",
            "AlertType": "eolAdvisory",
            "ClassId": "tam.Action",
            "Identifiers": [
            {
                "ClassId": "tam.Identifiers",
                "Name": "Moid",
                "ObjectType": "tam.Identifiers",
                "Value": "ds1_Moid"
            }
            ],
            "Name": "",
            "ObjectType": "tam.Action",
            "OperationType": "create",
            "Queries": [
            {
                "ClassId": "tam.QueryEntry",
                "Name": "qds2",
                "ObjectType": "tam.QueryEntry",
                "Priority": 1,
                "Query": "SELECT * FROM ds1 where ( datediff(current_date(), '2023-02-28' ) \u003e= 0 )"
            }
            ],
            "Type": "restApi"
        }
        ],
        "AdvisoryDetails": {
        "AllMilestones": [
            {
            "ClassId": "tam.Milestone",
            "Date": "2021-11-10T00:00:00Z",
            "Description": "The date that this software version was first available for download.",
            "EndOffset": 2147483647,
            "LabelHint": "upcoming",
            "MilestoneType": "unknown",
            "Name": "Release Date",
            "ObjectType": "tam.Milestone",
            "StartOffset": 0
            },
            {
            "ClassId": "tam.Milestone",
            "Date": "2022-07-31T00:00:00Z",
            "Description": "The last date that Cisco Engineering may release any final software maintenance releases or bug fixes. After this date, Cisco Engineering may no longer develop, repair, maintain, or test the product software and only critical security updates will be provided on this release train. ",
            "EndOffset": 2147483647,
            "LabelHint": "upcoming",
            "MilestoneType": "unknown",
            "Name": "End of SW Maintenance (EOSM) Release Date",
            "ObjectType": "tam.Milestone",
            "StartOffset": 0
            },
            {
            "ClassId": "tam.Milestone",
            "Date": "2022-11-30T00:00:00Z",
            "Description": "The last date to download the software through Cisco download page. The software is no longer available for download after this date.",
            "EndOffset": 2147483647,
            "LabelHint": "upcoming",
            "MilestoneType": "unknown",
            "Name": "End-of-Download (EOD) Date",
            "ObjectType": "tam.Milestone",
            "StartOffset": 0
            },
            {
            "ClassId": "tam.Milestone",
            "Date": "2022-07-31T00:00:00Z",
            "Description": "The last date that Cisco may provide support for security vulnerabilities.",
            "EndOffset": 2147483647,
            "LabelHint": "upcoming",
            "MilestoneType": "unknown",
            "Name": "End of Security and Vulnerability Fixes",
            "ObjectType": "tam.Milestone",
            "StartOffset": 0
            },
            {
            "ClassId": "tam.Milestone",
            "Date": "2023-02-28T00:00:00Z",
            "Description": "The last date to receive service and support for the software. After this date, all support services for the software are unavailable, and the software becomes obsolete. ",
            "EndOffset": 2147483647,
            "LabelHint": "upcoming",
            "MilestoneType": "unknown",
            "Name": "Last Date of Support",
            "ObjectType": "tam.Milestone",
            "StartOffset": 0
            }
        ],
        "ClassId": "tam.EolAdvisoryDetails",
        "Description": "",
        "Milestone": {
            "ClassId": "tam.Milestone",
            "Date": "2023-02-28T00:00:00Z",
            "Description": "The last date to receive service and support for the software. After this date, all support services for the software are unavailable, and the software becomes obsolete.",
            "EndOffset": 2147483647,
            "LabelHint": "past",
            "MilestoneType": "lastDateOfSupport",
            "Name": "Last Date of Support",
            "ObjectType": "tam.Milestone",
            "StartOffset": 0
        },
        "ObjectType": "tam.EolAdvisoryDetails",
        "Release": "5.0(1x)"
        },
        "AdvisoryId": "hx-5.0.1x-ldos-critical",
        "Ancestors": [],
        "ApiDataSources": [
        {
            "ClassId": "tam.ApiDataSource",
            "MoType": "hyperflexCluster",
            "Name": "ds1",
            "ObjectType": "tam.ApiDataSource",
            "Queries": [
            {
                "ClassId": "tam.QueryEntry",
                "Name": "qds1",
                "ObjectType": "tam.QueryEntry",
                "Priority": 1,
                "Query": "SELECT ds1_Moid, ds1_AccountMoid, ds1_DomainGroupMoid, ds1_RegisteredDevice.Moid as ds1_RegisteredDeviceMoid, ds1_HxVersion FROM ds1 WHERE (ds1_HxVersion RLIKE '^5\\\\.0\\\\(1[a-z]') "
            }
            ],
            "Type": "intersightApi"
        }
        ],
        "ClassId": "tam.AdvisoryDefinition",
        "CreateTime": "2023-07-28T00:08:31.798Z",
        "DatePublished": "2022-06-28T00:00:00Z",
        "DateUpdated": "2022-06-28T00:00:00Z",
        "Description": "Software maintenance support for 5.0(1x) software release ended on July 31, 2022 as documented in the Recommended [Release Bulletin](https://www.cisco.com/c/en/us/td/docs/hyperconverged_systems/HyperFlex_HX_DataPlatformSoftware/release-guidelines-and-support-timeline/b-recommended-hx-data-platform-sw-releases.html#id_119415). No bug fixes, patches or maintenance releases will be provided for this Cisco HyperFlex Data Platform release after that date. The last date of support for Cisco Hyperflex Data Platform Software Versions 5.0(1x) is Feb 28, 2023. Software maintenance requires an active service contract.",
        "DomainGroupMoid": "5b2541877a7662743465cc89",
        "ExecuteOnPod": "tier1",
        "ExternalUrl": "https://www.cisco.com/c/en/us/products/collateral/hyperconverged-infrastructure/hyperflex-hx-series/hyperflex-data-platform-soft-rel-5-0-1x-eol.html",
        "ModTime": "2023-09-08T07:49:09.257Z",
        "Moid": "64c306ff6f636b3901e9ee16",
        "Name": "The last date to receive service and support for Hyperflex 5.0(1x) is past",
        "ObjectType": "tam.AdvisoryDefinition",
        "Organization": {
        "ClassId": "mo.MoRef",
        "Moid": "5dde9f896972652d3353a082",
        "ObjectType": "organization.Organization",
        "link": "https://www.intersight.com/api/v1/organization/Organizations/5dde9f896972652d3353a082"
        },
        "OtherRefUrls": [],
        "Owners": [
        "5960901ca94eba000127e33a",
        "shared"
        ],
        "PermissionResources": [
        {
            "ClassId": "mo.MoRef",
            "Moid": "5dde9f896972652d3353a082",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/5dde9f896972652d3353a082"
        }
        ],
        "Recommendation": "Customers currently running HyperFlex Data Platform version 5.0(1x) should upgrade by Feb 28, 2023 to the latest Recommended Release. Cisco HyperFlex Data Platform’s Software Download page to get the latest Recommended Release can be found [here](https://software.cisco.com/download/home/286305544/type/286305994/release). Recommended release can be identified by the following\n- HyperFlex Recommended Release bulletin page found [here](https://www.cisco.com/c/en/us/td/docs/hyperconverged_systems/HyperFlex_HX_DataPlatformSoftware/release-guidelines-and-support-timeline/b-recommended-hx-data-platform-sw-releases.html).\n- Star next to the release name in [the software download page](https://software.cisco.com/download/home/286305544)\n\nHyperFlex Systems documents can be found [here](https://www.cisco.com/c/en/us/support/hyperconverged-systems/hyperflex-hx-data-platform-software/tsd-products-support-series-home.html).\nInstall and upgrade guides can be found [here](https://www.cisco.com/c/en/us/support/hyperconverged-systems/hyperflex-hx-data-platform-software/products-installation-guides-list.html).",
        "S3DataSources": [],
        "Severity": {
        "ClassId": "tam.EolSeverity",
        "Level": "critical",
        "ObjectType": "tam.EolSeverity"
        },
        "SharedScope": "shared",
        "State": "ready",
        "Tags": [],
        "Type": "eolAdvisory",
        "Version": "1.0",
        "Workaround": ""
    }
```