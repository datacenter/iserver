```
    {
        "AccountMoid": "5960901ca94eba000127e33a",
        "Actions": [
            {
            "AffectedObjectType": "compute.Blade",
            "AlertType": "psirt",
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
                "Query": "SELECT * FROM ds1 WHERE ((ds1_Firmware RLIKE '^(1|2|3|4\\\\.[01]|4\\\\.2\\\\(0|4\\\\.2\\\\(1[a-g]|4\\\\.2\\\\(2[a-b])' and ds1_Model RLIKE 'UCS.*B200.*M6') or (ds1_Firmware RLIKE '^(1|2|3|4|5\\\\.0\\\\(0|5\\\\.0\\\\(1[a-e]|5\\\\.0\\\\(2[a-b])' and ds1_Model RLIKE 'UCS.*X-210C-M6')) and ds1_SourceObjectType = 'compute.Blade'"
                }
            ],
            "Type": "restApi"
            },
            {
            "AffectedObjectType": "compute.Blade",
            "AlertType": "psirt",
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
                "Query": "SELECT * FROM ds1 WHERE (ds1_Firmware RLIKE '^(1|2|3|4\\\\.0|4\\\\.1\\\\([0-9][a-z]|4\\\\.1\\\\([1-2][0-9][a-z]|4\\\\.1\\\\(3[0-2][a-z]|4\\\\.1\\\\(33[a-g]|4\\\\.2\\\\(1[a-g])' and ds1_Model RLIKE 'UCS.*(B200|B480).*M5') and ds1_SourceObjectType = 'compute.Blade'"
                }
            ],
            "Type": "restApi"
            },
            {
            "AffectedObjectType": "compute.Blade",
            "AlertType": "psirt",
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
                "Query": "SELECT * FROM ds1 WHERE (ds1_Firmware RLIKE '^(1|2|3|4\\\\.0|4\\\\.1\\\\([0-9][a-z]|4\\\\.1\\\\([1-2][0-9][a-z]|4\\\\.1\\\\(3[0-2][a-z]|4\\\\.1\\\\(33[a])' and ds1_Model RLIKE '^(UCSB-EX-M4-2|UCSB-EX-M4-3)') and ds1_SourceObjectType = 'compute.Blade'"
                }
            ],
            "Type": "restApi"
            },
            {
            "AffectedObjectType": "compute.Blade",
            "AlertType": "psirt",
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
                "Query": "SELECT * FROM ds1 JOIN ds3 ON ds1.ds1_Moid = ds3.ds3_ComputeBladeMoid JOIN ds2 ON ds3.ds3_Moid = ds2.ds2_BiosUnitMoid WHERE ds1.ds1_Model RLIKE 'UCS.*(B200|B420).*M4' and ds1.ds1_SourceObjectType = 'compute.Blade'"
                }
            ],
            "Type": "restApi"
            },
            {
            "AffectedObjectType": "compute.Blade",
            "AlertType": "psirt",
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
                "Query": "SELECT * FROM ds1 WHERE ((ds1_Firmware RLIKE '^(1|2|3|4\\\\.0|4\\\\.1\\\\([012][a-z]|4\\\\.1\\\\(3[a-g])' and ds1_Model RLIKE 'UCS.*S3260.*M5') or (ds1_Firmware RLIKE '^(1|2|3|4\\\\.0|4\\\\.1\\\\([012][a-z]|4\\\\.1\\\\(3[a-e])' and ds1_Model RLIKE '^(UCS.*C3260.*M4|UCSC-C3K-M4)')) and ds1_SourceObjectType = 'compute.Blade'"
                }
            ],
            "Type": "restApi"
            },
            {
            "AffectedObjectType": "compute.RackUnit",
            "AlertType": "psirt",
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
                "Query": "SELECT * FROM ds1 WHERE (ds1_Firmware RLIKE '^(1|2|3|4\\\\.[01]|4\\\\.2\\\\(0|4\\\\.2\\\\(1[a-i]|4\\\\.2\\\\(2[a-b])' and ds1_Model RLIKE 'UCS.*(C220|C240).*M6') and ds1_SourceObjectType = 'compute.RackUnit'"
                }
            ],
            "Type": "restApi"
            },
            {
            "AffectedObjectType": "compute.RackUnit",
            "AlertType": "psirt",
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
                "Query": "SELECT * FROM ds1 WHERE (ds1_Firmware RLIKE '^(1|2|3|4\\\\.0|4\\\\.1\\\\([012][a-z]|4\\\\.1\\\\(3[a-g])' and ds1_Model RLIKE '^(UCS.*(C220|C240|C480).*M5|HX.*(220|240)C.*-M5)') and ds1_SourceObjectType = 'compute.RackUnit'"
                }
            ],
            "Type": "restApi"
            },
            {
            "AffectedObjectType": "compute.RackUnit",
            "AlertType": "psirt",
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
                "Query": "SELECT * FROM ds1 WHERE (ds1_Firmware RLIKE '^(1|2|3|4\\\\.0|4\\\\.1\\\\([01][a-z]|4\\\\.1\\\\(2[a-j])' and ds1_Model RLIKE '^(UCS.*(C220|C240|C460).*M4|HX.*(220|240)C.*-M4)') and ds1_SourceObjectType = 'compute.RackUnit'"
                }
            ],
            "Type": "restApi"
            }
        ],
        "AdvisoryId": "INTEL-SA-00601",
        "Ancestors": [],
        "ApiDataSources": [
            {
            "ClassId": "tam.ApiDataSource",
            "MoType": "computePhysicalSummary",
            "Name": "ds1",
            "ObjectType": "tam.ApiDataSource",
            "Queries": [
                {
                "ClassId": "tam.QueryEntry",
                "Name": "qds1",
                "ObjectType": "tam.QueryEntry",
                "Priority": 1,
                "Query": "SELECT ds1_Moid, ds1_AccountMoid, ds1_DomainGroupMoid, ds1_RegisteredDevice.Moid as ds1_RegisteredDeviceMoid, ds1_SourceObjectType, ds1_Firmware, ds1_Serial, ds1_Model FROM ds1"
                }
            ],
            "Type": "intersightApi"
            },
            {
            "ClassId": "tam.ApiDataSource",
            "MoType": "firmwareRunningFirmware",
            "Name": "ds2",
            "ObjectType": "tam.ApiDataSource",
            "Queries": [
                {
                "ClassId": "tam.QueryEntry",
                "Name": "qds2",
                "ObjectType": "tam.QueryEntry",
                "Priority": 1,
                "Query": "SELECT ds2_Moid, ds2_AccountMoid, ds2_Ancestors, ds2_RegisteredDevice.Moid as ds2_RegisteredDeviceMoid, ds2_DomainGroupMoid, ds2_Version, ds2_Type, ds2_BiosUnit.Moid as ds2_BiosUnitMoid FROM ds2 WHERE ds2_Version RLIKE '(B200M4|B420M4)((\\\\.[0123])|(\\\\.4\\\\.0)|(\\\\.4\\\\.1\\\\.[01])|(\\\\.4\\\\.1\\\\.2[a-c]))'"
                }
            ],
            "Type": "intersightApi"
            },
            {
            "ClassId": "tam.ApiDataSource",
            "MoType": "biosUnit",
            "Name": "ds3",
            "ObjectType": "tam.ApiDataSource",
            "Queries": [
                {
                "ClassId": "tam.QueryEntry",
                "Name": "qds3",
                "ObjectType": "tam.QueryEntry",
                "Priority": 1,
                "Query": "SELECT ds3_Moid,  ds3_AccountMoid, ds3_Ancestors, ds3_RegisteredDevice.Moid as ds3_RegisteredDeviceMoid, ds3_DomainGroupMoid, ds3_ComputeBlade.Moid as ds3_ComputeBladeMoid , ds3_RunningFirmware.Moid as ds3_RunningFirmwareMoid FROM ds3 WHERE ds3_Parent.ObjectType = 'compute.Blade'"
                }
            ],
            "Type": "intersightApi"
            }
        ],
        "BaseScore": 8.2,
        "ClassId": "tam.SecurityAdvisory",
        "CreateTime": "2022-07-08T01:54:22.459Z",
        "CveIds": [
            "CVE-2021-0154",
            "CVE-2021-0153",
            "CVE-2021-33123",
            "CVE-2021-0190",
            "CVE-2021-33122",
            "CVE-2021-0189",
            "CVE-2021-33124",
            "CVE-2021-33103",
            "CVE-2021-0159",
            "CVE-2021-0155",
            "CVE-2021-0188",
            "CVE-2022-0005",
            "CVE-2022-21131",
            "CVE-2022-21136",
            "CVE-2022-21151"
        ],
        "DatePublished": "2022-05-10T00:00:00Z",
        "DateUpdated": "2022-09-23T00:00:00Z",
        "Description": "Potential security vulnerabilities in the BIOS firmware or BIOS authenticated code module for Cisco UCS M4, M5 and M6 generation of servers using Intel┬« Processors may allow escalation of privilege or information disclosure.  Cisco is releasing BIOS updates to mitigate these potential vulnerabilities.\n\n",
        "DomainGroupMoid": "5b2541877a7662743465cc89",
        "EnvironmentalScore": 0,
        "ExecuteOnPod": "tier1",
        "ExternalUrl": "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00601.html",
        "ModTime": "2022-12-22T02:59:04.129Z",
        "Moid": "62c78e4e6f636b2d39834d55",
        "Name": "Intel 2022.1 IPU - BIOS Advisory",
        "ObjectType": "tam.SecurityAdvisory",
        "Organization": {
            "ClassId": "mo.MoRef",
            "Moid": "5dde9f896972652d3353a082",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/5dde9f896972652d3353a082"
        },
        "OtherRefUrls": [
            "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00614.html",
            "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00616.html",
            "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00617.html"
        ],
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
        "Recommendation": "There are no workarounds that address this vulnerability.\n\n Fixed Releases \n\n Below firmware releases and later versions have fixes for the above mentioned vulnerabilities.\n\n UCS Servers Operating in Intersight Managed Mode\n\n|Platform Model|4.1(3) Release|4.2(1) Release|4.2(2) Release|\n |-------------------|------------|------------|------------|\n |ucs-c220-m6|NA|4.2(1j)|4.2(2f)|\n |ucs-c240-m6|NA|4.2(1j)|4.2(2f)|\n |ucs-b200-m6|NA|4.2(1h)|4.2(2d)|\n |ucs-x210-m6|NA|5.0(1f)|5.0(2d)|\n |ucs-c220-m5|4.1(3h)|NA|All|\n |ucs-c240-m5|4.1(3h)|NA|All|\n |ucs-c480-m5|4.1(3h)|NA|All|\n |ucs-s3260-m5|4.1(3h)|NA|All|\n |ucs-b200-m5|4.1(33h)|4.2(1h)|All|\n |ucs-b480-m5|4.1(33h)|4.2(1h)|All|\n\n\n\n UCS Servers Operating in Standalone Mode\n\n|Platform Model|4.1(2) Release|4.1(3) Release|4.2(1) Release|4.2(2) Release|\n |-------------------|------------|------------|------------|------------|\n |ucs-c220-m6|NA|NA|4.2(1j)|4.2(2f)|\n |ucs-c240-m6|NA|NA|4.2(1j)|4.2(2f)|\n |ucs-c220-m5|NA|4.1(3h)|NA|All|\n |ucs-c240-m5|NA|4.1(3h)|NA|All|\n |ucs-c480-m5|NA|4.1(3h)|NA|All|\n |ucs-s3260-m5|NA|4.1(3h)|NA|All|\n |ucs-c220-m4|4.1(2k)|NA|NA|NA|\n |ucs-c240-m4|4.1(2k)|NA|NA|NA|\n |ucs-c3260-m4|NA|4.1(3h)|NA|NA|\n |ucs-c460-m4|4.1(2k)|NA|NA|NA|\n\n\n\n UCS Servers Operating in UCSM Mode\n\n|Platform Model|4.1(3) Release|4.2(1) Release|4.2(2) Release|\n |-------------------|------------|------------|------------|\n |All Impacted Models (except M6 models)|4.1(3i)|4.2(1n)|All|\n |All M6 Models|NA|4.2(1n)|4.2(2c)|\n\n*NA - Not Applicable\n\n\n\n Please refer to below Cisco defect IDs for more information\n\n |Bug ID|Impacted Models|\n |----------------------------|-----------------------------------------------------|\n |[CSCwb67158](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb67158)| All M4 Models (except B260, B460, C460)|\n |[CSCwb67157](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb67157)|B260-M4, B460-M4, C460-M4|\n |[CSCwb67159](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb67159)|All M5 Models|\n |[CSCwb67205](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb67205)|All M6 Models|\n",
        "Severity": {
            "ClassId": "tam.PsirtSeverity",
            "Level": "high",
            "ObjectType": "tam.PsirtSeverity"
        },
        "SharedScope": "shared",
        "State": "ready",
        "Status": "interim",
        "Tags": [],
        "TemporalScore": 0,
        "Version": "1.1",
        "Workaround": ""
    }
```