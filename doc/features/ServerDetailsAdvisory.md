# Server Details - Advisory

```
# iserver get server --name comp7-p3b-eu-spdc-FCH2023V2A4 --advisory

+---------+-----+---------+-------------------------------+-------------------+-------------+-------------+------------+-----------+
| SF      | MF  | WF (7d) | Name                          | Model             | Serial      | IP          | CPU        | Memory    |
+---------+-----+---------+-------------------------------+-------------------+-------------+-------------+------------+-----------+
| P+ C(1) | CRi |         | comp7-p3b-eu-spdc-FCH2023V2A4 | (R) UCSC-C220-M4S | FCH2023V2A4 | 10.58.50.60 | 2S 28C 56T | 256 [GiB] | 
+---------+-----+---------+-------------------------------+-------------------+-------------+-------------+------------+-----------+

Advisory Summary
----------------
- High : 1
- Info : 0


Advisory INTEL-SA-00601
-----------------------
- Severity       : high
- Base Score     : 8.2
- Name           : Intel 2022.1 IPU - BIOS Advisory
- Description    :
	Potential security vulnerabilities in the BIOS firmware or BIOS authenticated code module for Cisco UCS M4, M5 and M6 generation of servers using Intel Processors may allow escalation of privilege or information disclosure.  Cisco is releasing BIOS updates to mitigate these potential vulnerabilities.
	
	
- Cve Ids        :
	CVE-2021-0154
	CVE-2021-0153
	CVE-2021-33123
	CVE-2021-0190
	CVE-2021-33122
	CVE-2021-0189
	CVE-2021-33124
	CVE-2021-33103
	CVE-2021-0159
	CVE-2021-0155
	CVE-2021-0188
	CVE-2022-0005
	CVE-2022-21131
	CVE-2022-21136
	CVE-2022-21151
- Date Published : 2022-05-10T00:00:00Z
- Date Updated   : 2022-09-23T00:00:00Z
- Details        :
	https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00601.html
	https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00614.html
	https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00616.html
	https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00617.html
- Recommendation :
	There are no workarounds that address this vulnerability.
	
	 Fixed Releases 
	
	 Below firmware releases and later versions have fixes for the above mentioned vulnerabilities.
	
	 UCS Servers Operating in Intersight Managed Mode
	
	|Platform Model|4.1(3) Release|4.2(1) Release|4.2(2) Release|
	 |-------------------|------------|------------|------------|
	 |ucs-c220-m6|NA|4.2(1j)|4.2(2f)|
	 |ucs-c240-m6|NA|4.2(1j)|4.2(2f)|
	 |ucs-b200-m6|NA|4.2(1h)|4.2(2d)|
	 |ucs-x210-m6|NA|5.0(1f)|5.0(2d)|
	 |ucs-c220-m5|4.1(3h)|NA|All|
	 |ucs-c240-m5|4.1(3h)|NA|All|
	 |ucs-c480-m5|4.1(3h)|NA|All|
	 |ucs-s3260-m5|4.1(3h)|NA|All|
	 |ucs-b200-m5|4.1(33h)|4.2(1h)|All|
	 |ucs-b480-m5|4.1(33h)|4.2(1h)|All|
	
	
	
	 UCS Servers Operating in Standalone Mode
	
	|Platform Model|4.1(2) Release|4.1(3) Release|4.2(1) Release|4.2(2) Release|
	 |-------------------|------------|------------|------------|------------|
	 |ucs-c220-m6|NA|NA|4.2(1j)|4.2(2f)|
	 |ucs-c240-m6|NA|NA|4.2(1j)|4.2(2f)|
	 |ucs-c220-m5|NA|4.1(3h)|NA|All|
	 |ucs-c240-m5|NA|4.1(3h)|NA|All|
	 |ucs-c480-m5|NA|4.1(3h)|NA|All|
	 |ucs-s3260-m5|NA|4.1(3h)|NA|All|
	 |ucs-c220-m4|4.1(2k)|NA|NA|NA|
	 |ucs-c240-m4|4.1(2k)|NA|NA|NA|
	 |ucs-c3260-m4|NA|4.1(3h)|NA|NA|
	 |ucs-c460-m4|4.1(2k)|NA|NA|NA|
	
	
	
	 UCS Servers Operating in UCSM Mode
	
	|Platform Model|4.1(3) Release|4.2(1) Release|4.2(2) Release|
	 |-------------------|------------|------------|------------|
	 |All Impacted Models (except M6 models)|4.1(3i)|4.2(1n)|All|
	 |All M6 Models|NA|4.2(1n)|4.2(2c)|
	
	*NA - Not Applicable
	
	
	
	 Please refer to below Cisco defect IDs for more information
	
	 |Bug ID|Impacted Models|
	 |----------------------------|-----------------------------------------------------|
	 |[CSCwb67158](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb67158)| All M4 Models (except B260, B460, C460)|
	 |[CSCwb67157](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb67157)|B260-M4, B460-M4, C460-M4|
	 |[CSCwb67159](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb67159)|All M5 Models|
	 |[CSCwb67205](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb67205)|All M6 Models|
	
```

JSON output

```
# iserver get server --name comp7-p3b-eu-spdc-FCH2023V2A4 --advisory

{
    "__Output": {
        "FlagState": ":GG.RRRR",
        "FlagManagement": ":GGY",
        "FlagWorkflow": ":"
    },
    "Moid": "637f588776752d313966cb9d",
    "DeviceMoId": "637f58116f72612d31490de7",
    "Name": "comp7-p3b-eu-spdc-FCH2023V2A4",
    "Model": "UCSC-C220-M4S",
    "Serial": "FCH2023V2A4",
    "ManagementMode": "IntersightStandalone",
    "OperPowerState": "on",
    "Type": "Rack",
    "TypeModel": "(R) UCSC-C220-M4S",
    "AdvisorySummary": {
        "__Output": {
            "High": "Red",
            "Info": "Blue"
        },
        "High": 1,
        "Info": 0
    },
    "AdvisoryInfo": [
        {
            "AdvisoryId": "INTEL-SA-00601",
            "BaseScore": 8.2,
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
            "Description": "Potential security vulnerabilities in the BIOS firmware or BIOS authenticated code module for Cisco UCS M4, M5 and M6 generation of servers using Intel\u00ae Processors may allow escalation of privilege or information disclosure.  Cisco is releasing BIOS updates to mitigate these potential vulnerabilities.\n\n",
            "ExternalUrl": "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00601.html",
            "Moid": "62c78e4e6f636b2d39834d55",
            "Name": "Intel 2022.1 IPU - BIOS Advisory",
            "OtherRefUrls": [
                "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00614.html",
                "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00616.html",
                "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00617.html"
            ],
            "Recommendation": "There are no workarounds that address this vulnerability.\n\n Fixed Releases \n\n Below firmware releases and later versions have fixes for the above mentioned vulnerabilities.\n\n UCS Servers Operating in Intersight Managed Mode\n\n|Platform Model|4.1(3) Release|4.2(1) Release|4.2(2) Release|\n |-------------------|------------|------------|------------|\n |ucs-c220-m6|NA|4.2(1j)|4.2(2f)|\n |ucs-c240-m6|NA|4.2(1j)|4.2(2f)|\n |ucs-b200-m6|NA|4.2(1h)|4.2(2d)|\n |ucs-x210-m6|NA|5.0(1f)|5.0(2d)|\n |ucs-c220-m5|4.1(3h)|NA|All|\n |ucs-c240-m5|4.1(3h)|NA|All|\n |ucs-c480-m5|4.1(3h)|NA|All|\n |ucs-s3260-m5|4.1(3h)|NA|All|\n |ucs-b200-m5|4.1(33h)|4.2(1h)|All|\n |ucs-b480-m5|4.1(33h)|4.2(1h)|All|\n\n\n\n UCS Servers Operating in Standalone Mode\n\n|Platform Model|4.1(2) Release|4.1(3) Release|4.2(1) Release|4.2(2) Release|\n |-------------------|------------|------------|------------|------------|\n |ucs-c220-m6|NA|NA|4.2(1j)|4.2(2f)|\n |ucs-c240-m6|NA|NA|4.2(1j)|4.2(2f)|\n |ucs-c220-m5|NA|4.1(3h)|NA|All|\n |ucs-c240-m5|NA|4.1(3h)|NA|All|\n |ucs-c480-m5|NA|4.1(3h)|NA|All|\n |ucs-s3260-m5|NA|4.1(3h)|NA|All|\n |ucs-c220-m4|4.1(2k)|NA|NA|NA|\n |ucs-c240-m4|4.1(2k)|NA|NA|NA|\n |ucs-c3260-m4|NA|4.1(3h)|NA|NA|\n |ucs-c460-m4|4.1(2k)|NA|NA|NA|\n\n\n\n UCS Servers Operating in UCSM Mode\n\n|Platform Model|4.1(3) Release|4.2(1) Release|4.2(2) Release|\n |-------------------|------------|------------|------------|\n |All Impacted Models (except M6 models)|4.1(3i)|4.2(1n)|All|\n |All M6 Models|NA|4.2(1n)|4.2(2c)|\n\n*NA - Not Applicable\n\n\n\n Please refer to below Cisco defect IDs for more information\n\n |Bug ID|Impacted Models|\n |----------------------------|-----------------------------------------------------|\n |[CSCwb67158](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb67158)| All M4 Models (except B260, B460, C460)|\n |[CSCwb67157](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb67157)|B260-M4, B460-M4, C460-M4|\n |[CSCwb67159](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb67159)|All M5 Models|\n |[CSCwb67205](https://bst.cloudapps.cisco.com/bugsearch/bug/CSCwb67205)|All M6 Models|\n",
            "Workaround": "",
            "Urls": [
                "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00601.html",
                "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00614.html",
                "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00616.html",
                "https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00617.html"
            ],
            "__Output": {
                "Severity": "Red"
            },
            "Severity": "high"
        }
    ],
    "NumCpus": 2,
    "NumCpuCores": 28,
    "NumThreads": 56,
    "Cpu": "2S 28C 56T",
    "Groups": "",
    "AlarmSummary": {
        "__Output": {
            "Critical": "Red",
            "Warning": "Yellow",
            "Info": "Blue",
            "Cleared": "Green"
        },
        "Critical": 1,
        "Warning": 1,
        "Info": 1
    },
    "Health": "Critical (1)",
    "LocatorLedOn": false,
    "ManagementIp": "10.58.50.60",
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
    "AvailableMemory": 262144,
    "TotalMemory": 262144,
    "UsedMemory": 0,
    "TotalMemoryUnit": "256 [GiB]",
    "TotalMemoryGB": 256,
    "AvailableMemoryUnit": "256 [GiB]",
    "AvailableMemoryGB": 256,
    "UsedMemoryUnit": "0 [KiB]",
    "UsedMemoryGB": 0,
    "UsedMemoryPct": 0,
    "UsedMemoryPctUnit": "0%",
    "Connected": true,
    "Workflow": {
        "Days": 7,
        "Running": null,
        "LatestMoid": null,
        "Last": []
    },
    "FlagState": "P+ C(1)",
    "FlagManagement": "CRi",
    "FlagWorkflow": ""
}
```

Developer output

```
# iserver get server --name comp7-p3b-eu-spdc-FCH2023V2A4 --advisory

Developer output

{
    "duration": 18895,
    "isctl": {
        "read": true,
        "calls": 7,
        "success": 7,
        "failed": 0,
        "total_time": 14156
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
        "lines": 439
    }
}

Log: isctl
-----------

2023-01-05 18:44:54.324872	True	3255	93	isctl get compute rackunit   -o json --top 100
2023-01-05 18:44:56.313143	True	1977	10	isctl get compute blade   -o json --top 100
2023-01-05 18:45:01.911516	True	1648	1	isctl get tam advisoryinstance --filter "AffectedObject/Moid eq '637f588776752d313966cb9d'"  -o json --top 100
2023-01-05 18:45:04.170140	True	2250	78	isctl get tam securityadvisory   -o json --top 100
2023-01-05 18:45:05.936483	True	1765	1	isctl get equipment locatorled --filter "RegisteredDevice/Moid eq '637f58116f72612d31490de7'"  -o json --top 100
2023-01-05 18:45:07.459375	True	1474	1	isctl get asset deviceregistration  moid 637f58116f72612d31490de7 -o json
2023-01-05 18:45:09.250401	True	1787	3	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-29T18:45:07.000Z"  -o json --top 100
```
