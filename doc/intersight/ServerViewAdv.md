# Intersight Server

## adv view

```
# iserver get server --group test -v adv

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


Advisory Summary [#8]
---------------------

+--------------------------------+------+------+
| Server                         | High | Info |
+--------------------------------+------+------+
| comp-1-p2b-eu-spdc-WZP23400AJW | 2    | 2    | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | 2    | 2    | 
| comp-3-p2b-eu-spdc-WZP23400AKL | 1    | 2    | 
| comp3-p4b-eu-spdc-WZP262207UM  | 0    | 0    | 
| FI-ucsb1-eu-spdc-2-1           | 1    | 1    | 
| FI-ucsb1-eu-spdc-2-2           | 1    | 1    | 
| FI-ucsb1-eu-spdc-2-3           | 1    | 1    | 
| FI-ucsb1-eu-spdc-2-4           | 1    | 1    | 
+--------------------------------+------+------+

Advisory [#5]
-------------

+--------------------------------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| Server                         | Severity | Score | Name                                    | Description                              | CveIds         | DatePublished        | DateUpdated          |
+--------------------------------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | high     | 8.2   | Intel 2023.1 IPU - BIOS Advisory        | Potential security vulnerabilities in    | CVE-2022-26343 | 2023-02-14T00:00:00Z | 2023-02-14T00:00:00Z | 
| comp-2-p2b-eu-spdc-WZP23400AK4 |          |       |                                         | the BIOS firmware and Intel Trusted     | CVE-2022-30539 |                      |                      | 
|                                |          |       |                                         | Execution Technology (TXT) Secure        | CVE-2022-32231 |                      |                      | 
|                                |          |       |                                         | Initialization (SINIT) Authenticated     | CVE-2022-26837 |                      |                      | 
|                                |          |       |                                         | Code Modules (ACM) for some Intel       | CVE-2022-30704 |                      |                      | 
|                                |          |       |                                         | Processors may allow escalation of       | CVE-2021-0187  |                      |                      | 
|                                |          |       |                                         | privilege.  Intel is releasing BIOS      | CVE-2022-36348 |                      |                      | 
|                                |          |       |                                         | updates to mitigate these potential      | CVE-2022-36794 |                      |                      | 
|                                |          |       |                                         | vulnerabilities.- CVE-2022-26343         | CVE-2021-33124 |                      |                      | 
|                                |          |       |                                         | impacts only M5 servers.-                | CVE-2022-21216 |                      |                      | 
|                                |          |       |                                         | CVE-2022-32231 impacts both M5 and M6    | CVE-2022-33196 |                      |                      | 
|                                |          |       |                                         | servers.- Rest all CVEs impact only M6   | CVE-2022-38090 |                      |                      | 
|                                |          |       |                                         | servers.                                 | CVE-2022-33972 |                      |                      | 
+--------------------------------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | info     |       | End-of-Life Announcement for the Cisco  | Cisco announces the end-of-sale and      |                | 2023-05-01T00:00:00Z | 2023-05-02T00:00:00Z | 
| comp-2-p2b-eu-spdc-WZP23400AK4 |          |       | UCS M5 Rack Servers (C220 M5, C240 M5,  | end-of-life dates for the Cisco UCS M5   |                |                      |                      | 
| comp-3-p2b-eu-spdc-WZP23400AKL |          |       | C480 M5)                                | Rack Servers (C220 M5, C240 M5, C480     |                |                      |                      | 
|                                |          |       |                                         | M5). The last day to order the affected  |                |                      |                      | 
|                                |          |       |                                         | product(s) is October 30, 2023.          |                |                      |                      | 
|                                |          |       |                                         | Customers with active service contracts  |                |                      |                      | 
|                                |          |       |                                         | will continue to receive support from    |                |                      |                      | 
|                                |          |       |                                         | the Cisco Technical Assistance Center    |                |                      |                      | 
|                                |          |       |                                         | (TAC) as per EoL bulletin.               |                |                      |                      | 
+--------------------------------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | high     | 7.2   | Intel 2023.3 IPU - BIOS and Processors  | Potential security vulnerabilities in    | CVE-2022-37343 | 2023-08-08T00:00:00Z | 2023-08-08T00:00:00Z | 
| comp-2-p2b-eu-spdc-WZP23400AK4 |          |       | Advisories                              | the BIOS firmware or Intel Processors   | CVE-2022-44611 |                      |                      | 
| comp-3-p2b-eu-spdc-WZP23400AKL |          |       |                                         | for Cisco UCS M4, M5 and M6 generation   | CVE-2022-38083 |                      |                      | 
| FI-ucsb1-eu-spdc-2-1           |          |       |                                         | of servers may allow escalation of       | CVE-2022-27879 |                      |                      | 
| FI-ucsb1-eu-spdc-2-2           |          |       |                                         | privilege, information disclosure or     | CVE-2022-43505 |                      |                      | 
| FI-ucsb1-eu-spdc-2-3           |          |       |                                         | denial of service. Cisco is releasing    | CVE-2022-40982 |                      |                      | 
| FI-ucsb1-eu-spdc-2-4           |          |       |                                         | software updates to mitigate these       | CVE-2023-23908 |                      |                      | 
|                                |          |       |                                         | potential vulnerabilities.               | CVE-2022-41804 |                      |                      | 
|                                |          |       |                                         |                                          | CVE-2022-36392 |                      |                      | 
|                                |          |       |                                         |                                          | CVE-2022-38102 |                      |                      | 
|                                |          |       |                                         |                                          | CVE-2022-29871 |                      |                      | 
+--------------------------------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | medium   | 6.1   | Cisco Integrated Management Controller  | A vulnerability in the web-based         | CVE-2023-20228 | 2023-08-16T00:00:00Z | 2023-08-17T00:00:00Z | 
| comp-2-p2b-eu-spdc-WZP23400AK4 |          |       | Cross-Site Scripting Vulnerability      | management interface of Cisco            |                |                      |                      | 
| comp-3-p2b-eu-spdc-WZP23400AKL |          |       |                                         | Integrated Management Controller (IMC)   |                |                      |                      | 
|                                |          |       |                                         | could allow an unauthenticated, remote   |                |                      |                      | 
|                                |          |       |                                         | attacker to conduct a cross-site         |                |                      |                      | 
|                                |          |       |                                         | scripting (XSS) attack against a user    |                |                      |                      | 
|                                |          |       |                                         | of the interface.This vulnerability is   |                |                      |                      | 
|                                |          |       |                                         | due to insufficient validation of user   |                |                      |                      | 
|                                |          |       |                                         | input. An attacker could exploit this    |                |                      |                      | 
|                                |          |       |                                         | vulnerability by persuading a user of    |                |                      |                      | 
|                                |          |       |                                         | an affected interface to click a         |                |                      |                      | 
|                                |          |       |                                         | crafted link. A successful exploit       |                |                      |                      | 
|                                |          |       |                                         | could allow the attacker to execute      |                |                      |                      | 
|                                |          |       |                                         | arbitrary script code in the browser of  |                |                      |                      | 
|                                |          |       |                                         | the targeted user or access sensitive,   |                |                      |                      | 
|                                |          |       |                                         | browser-based information.Cisco has      |                |                      |                      | 
|                                |          |       |                                         | released software updates that address   |                |                      |                      | 
|                                |          |       |                                         | this vulnerability. There are no         |                |                      |                      | 
|                                |          |       |                                         | workarounds that address this            |                |                      |                      | 
|                                |          |       |                                         | vulnerability**Note**:- This             |                |                      |                      | 
|                                |          |       |                                         | vulnerability only impacts the specific  |                |                      |                      | 
|                                |          |       |                                         | rack server models (mentioned below in   |                |                      |                      | 
|                                |          |       |                                         | Fixed Software section) operating in     |                |                      |                      | 
|                                |          |       |                                         | standalone mode only.                    |                |                      |                      | 
+--------------------------------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| FI-ucsb1-eu-spdc-2-1           | info     |       | End-of-Life Announcement for the Cisco  | Cisco announces the end-of-sale and      |                | 2023-05-01T00:00:00Z | 2023-05-03T00:00:00Z | 
| FI-ucsb1-eu-spdc-2-2           |          |       | UCS M5 Blade Server (B200 M5)           | end-of-life dates for the Cisco UCS M5   |                |                      |                      | 
| FI-ucsb1-eu-spdc-2-3           |          |       |                                         | Blade Server (B200 M5). The last day to  |                |                      |                      | 
| FI-ucsb1-eu-spdc-2-4           |          |       |                                         | order the affected product(s) is         |                |                      |                      | 
|                                |          |       |                                         | October 30, 2023. Customers with active  |                |                      |                      | 
|                                |          |       |                                         | service contracts will continue to       |                |                      |                      | 
|                                |          |       |                                         | receive support from the Cisco           |                |                      |                      | 
|                                |          |       |                                         | Technical Assistance Center (TAC) based  |                |                      |                      | 
|                                |          |       |                                         | on EoL bulletin.                         |                |                      |                      | 
+--------------------------------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+

Advisory Url [#5]
-----------------

+--------------------------------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server                         | Name                                    | Urls                                                                                                                                             |
+--------------------------------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Intel 2023.1 IPU - BIOS Advisory        | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00717.html                                                             | 
| comp-2-p2b-eu-spdc-WZP23400AK4 |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00718.html                                                             | 
|                                |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00700.html                                                             | 
|                                |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00738.html                                                             | 
|                                |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00767.html                                                             | 
|                                |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00730.html                                                             | 
+--------------------------------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | End-of-Life Announcement for the Cisco  | https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-m5-rack-server-c220-c240-c480-eol.html | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | UCS M5 Rack Servers (C220 M5, C240 M5,  |                                                                                                                                                  | 
| comp-3-p2b-eu-spdc-WZP23400AKL | C480 M5)                                |                                                                                                                                                  | 
+--------------------------------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Intel 2023.3 IPU - BIOS and Processors  | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00813.html                                                             | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Advisories                              | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00783.html                                                             | 
| comp-3-p2b-eu-spdc-WZP23400AKL |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00828.html                                                             | 
| FI-ucsb1-eu-spdc-2-1           |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00836.html                                                             | 
| FI-ucsb1-eu-spdc-2-2           |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00837.html                                                             | 
| FI-ucsb1-eu-spdc-2-3           |                                         |                                                                                                                                                  | 
| FI-ucsb1-eu-spdc-2-4           |                                         |                                                                                                                                                  | 
+--------------------------------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Cisco Integrated Management Controller  | https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-xss-UMYtYEtr                                         | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Cross-Site Scripting Vulnerability      |                                                                                                                                                  | 
| comp-3-p2b-eu-spdc-WZP23400AKL |                                         |                                                                                                                                                  | 
+--------------------------------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| FI-ucsb1-eu-spdc-2-1           | End-of-Life Announcement for the Cisco  | https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-b-series-blade-servers/ucs-m5-blade-server-b200-eol.html         | 
| FI-ucsb1-eu-spdc-2-2           | UCS M5 Blade Server (B200 M5)           |                                                                                                                                                  | 
| FI-ucsb1-eu-spdc-2-3           |                                         |                                                                                                                                                  | 
| FI-ucsb1-eu-spdc-2-4           |                                         |                                                                                                                                                  | 
+--------------------------------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v adv

{
    "duration": 12321,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 10459
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
        "lines": 24
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:19:13.624325	True	2273	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:19:15.014277	True	1388	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:19:16.543869	True	1476	12	isctl get compute blade   -o json --top 100
2023-12-03 15:19:18.512707	True	1933	86	isctl get tam securityadvisory   -o json --top 100
2023-12-03 15:19:20.509289	True	1971	72	isctl get tam advisorydefinition   -o json --top 100
2023-12-03 15:19:21.952833	True	1418	19	isctl get tam advisoryinstance --filter "AffectedObject/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5', '6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')"  -o json --top 100
```

[[Back]](./ServerInventory.md)