# Intersight Server

## istate view

```
# iserver get server --group test -v istate

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

Connector [#8]
--------------

+--------------------------------+-------------------+-------------------+--------------------+--------------------------+-------------------------------+---------------+----------------------------+
| Server                         | Connection Status | Connector Version | Claimed By         | Claimed Time             | Connection Status Last Update | Platform Type | Device External IP Address |
+--------------------------------+-------------------+-------------------+--------------------+--------------------------+-------------------------------+---------------+----------------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Connected         | 1.0.11-3136       | ttrabatt@cisco.com | 2020-12-20T18:46:00.104Z | 2023-12-01T05:12:39.272Z      | IMCM5         | 173.38.209.7               | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Connected         | 1.0.11-3136       | ttrabatt@cisco.com | 2020-12-20T18:48:08.061Z | 2023-12-01T20:29:26.594Z      | IMCM5         | 173.38.209.6               | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Connected         | 1.0.11-3136       | ttrabatt@cisco.com | 2020-12-20T18:50:26.206Z | 2023-12-01T22:41:35.389Z      | IMCM5         | 173.38.209.11              | 
| comp3-p4b-eu-spdc-WZP262207UM  | Connected         | 1.0.11-3273       | ttrabatt@cisco.com | 2022-11-28T18:44:17.856Z | 2023-12-03T00:26:24.649Z      | IMCRack       | 64.103.36.135              | 
| FI-ucsb1-eu-spdc-2-1           | Connected         | 1.0.11-4665       | ttrabatt@cisco.com | 2023-09-13T15:54:45.974Z | 2023-12-01T19:41:43.272Z      | UCSFI         | 10.0.169.80                | 
| FI-ucsb1-eu-spdc-2-2           | Connected         | 1.0.11-4665       | ttrabatt@cisco.com | 2023-09-13T15:54:45.974Z | 2023-12-01T19:41:43.272Z      | UCSFI         | 10.0.169.80                | 
| FI-ucsb1-eu-spdc-2-3           | Connected         | 1.0.11-4665       | ttrabatt@cisco.com | 2023-09-13T15:54:45.974Z | 2023-12-01T19:41:43.272Z      | UCSFI         | 10.0.169.80                | 
| FI-ucsb1-eu-spdc-2-4           | Connected         | 1.0.11-4665       | ttrabatt@cisco.com | 2023-09-13T15:54:45.974Z | 2023-12-01T19:41:43.272Z      | UCSFI         | 10.0.169.80                | 
+--------------------------------+-------------------+-------------------+--------------------+--------------------------+-------------------------------+---------------+----------------------------+

Contract [#8]
-------------

+--------------------------------+-----------------+----------------------+----------------------+--------------------------+--------------------------------------------------------------+-----------------------+--------------------+
| Server                         | Contract Status | Start Date           | End Date             | Last Updated             | Service Description                                          | Purchase Order Number | Sales Order Number |
+--------------------------------+-----------------+----------------------+----------------------+--------------------------+--------------------------------------------------------------+-----------------------+--------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-02T11:39:03.345Z | UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS | 6710008753            | 110208990          | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-02T10:29:21.56Z  | UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS | 6710008753            | 110208990          | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-02T23:39:15.269Z | UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS | 6710008753            | 110208990          | 
| comp3-p4b-eu-spdc-WZP262207UM  | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-02T18:48:58.573Z | UCS C225 M6 Rack w/o CPU, mem, drv, 1U wSFF 10HDD backplane  | PR616717              | 114132936          | 
| FI-ucsb1-eu-spdc-2-1           | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-03T02:08:58.181Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | 6710008742            | 110341108          | 
| FI-ucsb1-eu-spdc-2-2           | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-03T02:08:58.181Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | 6710008742            | 110341108          | 
| FI-ucsb1-eu-spdc-2-3           | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-03T02:08:58.181Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | 6710008742            | 110341108          | 
| FI-ucsb1-eu-spdc-2-4           | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2023-12-03T02:08:58.181Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | 6710008742            | 110341108          | 
+--------------------------------+-----------------+----------------------+----------------------+--------------------------+--------------------------------------------------------------+-----------------------+--------------------+

HCL Summary [#8]
----------------

+--------------------------------+------------+
| Server                         | Overall    |
+--------------------------------+------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Validated  | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Validated  | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Incomplete | 
| comp3-p4b-eu-spdc-WZP262207UM  | Incomplete | 
| FI-ucsb1-eu-spdc-2-1           | Not-Listed | 
| FI-ucsb1-eu-spdc-2-2           | Not-Listed | 
| FI-ucsb1-eu-spdc-2-3           | Not-Listed | 
| FI-ucsb1-eu-spdc-2-4           | Not-Listed | 
+--------------------------------+------------+

HCL Server Hardware Compliance [#8]
-----------------------------------

+--------------------------------+-----------+----------------+-------------------------------------------------+----------+
| Server                         | Status    | Model          | CPU                                             | Firmware |
+--------------------------------+-----------+----------------+-------------------------------------------------+----------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Validated | UCSC-C240-M5SN | Intel Xeon Processor Scalable Family            | 4.2(2)   | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Validated | UCSC-C240-M5SN | Intel Xeon Processor Scalable Family            | 4.2(2)   | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Validated | UCSC-C240-M5SN | Intel Xeon Processor Scalable Family            | 4.2(3)   | 
| comp3-p4b-eu-spdc-WZP262207UM  | Validated | UCSC-C225-M6S  | AMD EPYC 7763 64-Core Processor                 | 4.2(3)   | 
| FI-ucsb1-eu-spdc-2-1           | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 4.2(3)   | 
| FI-ucsb1-eu-spdc-2-2           | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 4.2(3)   | 
| FI-ucsb1-eu-spdc-2-3           | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 4.2(3)   | 
| FI-ucsb1-eu-spdc-2-4           | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 4.2(3)   | 
+--------------------------------+-----------+----------------+-------------------------------------------------+----------+

HCL Server Software Compliance [#8]
-----------------------------------

+--------------------------------+------------+-------------------------+-----------+-------------+
| Server                         | Status     | Reason                  | OS Vendor | OS Version  |
+--------------------------------+------------+-------------------------+-----------+-------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Validated  | Compatible              | VMware    | ESXi 7.0 U3 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Validated  | Compatible              | VMware    | ESXi 7.0 U3 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Incomplete | Missing-Os-Info         |           |             | 
| comp3-p4b-eu-spdc-WZP262207UM  | Incomplete | Missing-Os-Info         |           |             | 
| FI-ucsb1-eu-spdc-2-1           | Validated  | Incompatible-Components | VMware    | ESXi 7.0 U3 | 
| FI-ucsb1-eu-spdc-2-2           | Validated  | Incompatible-Components | VMware    | ESXi 7.0 U3 | 
| FI-ucsb1-eu-spdc-2-3           | Validated  | Incompatible-Components | VMware    | ESXi 7.0 U3 | 
| FI-ucsb1-eu-spdc-2-4           | Validated  | Incompatible-Components | VMware    | ESXi 7.0 U3 | 
+--------------------------------+------------+-------------------------+-----------+-------------+

HCL Server Adapter Compliance [#8]
----------------------------------

+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| Server                         | Status        | Component  | Hardware      | Software            | Reason                 | Model                                                            | Cimc Version | Driver Name | Driver Version | Firmware Version   |
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Validated     | Validated  | Compatible    | Compatible          | Compatible             | Cisco(R) LOM X550-T2                                             | 4.2(2)       | ixgben      | 1.12.3.0       | 0x800016F9-1.826.0 | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 4.2(2)       | lsi_mr3     | 7.718.02.00    | 51.19.0-4296       | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(2)       | i40en       | 2.2.7.0        | 0x8000B900-1.826.0 | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(2)       | i40en       | 2.2.7.0        | 0x8000B900-1.826.0 | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | UCSC-MLOM-C25Q-04                                                | 4.2(2)       | nenic       | 1.0.42.0       | 5.2(2)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| comp-2-p2b-eu-spdc-WZP23400AK4 | Validated     | Validated  | Compatible    | Compatible          | Compatible             | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(2)       | i40en       | 2.2.7.0        | 0x8000B900-1.826.0 | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(2)       | i40en       | 2.2.7.0        | 0x8000B900-1.826.0 | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | Cisco(R) LOM X550-T2                                             | 4.2(2)       | ixgben      | 1.12.3.0       | 0x800016F9-1.826.0 | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 4.2(2)       | lsi_mr3     | 7.718.02.00    | 51.19.0-4296       | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | UCSC-MLOM-C25Q-04                                                | 4.2(2)       | nenic       | 1.0.42.0       | 5.2(2)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| comp-3-p2b-eu-spdc-WZP23400AKL | Not-Evaluated | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 4.2(3)       |             |                | 51.19.0-4532       | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | Cisco(R) LOM X550-T2                                             | 4.2(3)       |             |                | 0x800016F9-1.826.0 | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(3)       |             |                | 0x8000CC0F-1.826.0 | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(3)       |             |                | 0x8000CC0F-1.826.0 | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | UCSC-MLOM-C25Q-04                                                | 4.2(3)       |             |                | 5.2(3)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| comp3-p4b-eu-spdc-WZP262207UM  | Not-Evaluated | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | Cisco Boot optimized M.2 Raid controller                         | 4.2(3)       |             |                | 2.3.17.1014        | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | Cisco 12G SAS RAID Controller with 4GB FBWC (16 Drives)          | 4.2(3)       |             |                | 52.20.0-4523       | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | UCSC-PCIE-C25Q-04                                                | 4.2(3)       |             |                | 5.2(3)             | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | UCSC-M-V100-04                                                   | 4.2(3)       |             |                | 5.2(3)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| FI-ucsb1-eu-spdc-2-1           | Not-Listed    | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MRAID12G-HE                                                 | 4.2(3)       | lsi_mr3     | 7.718.02.00    | 24.21.0-0156       | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MLOM-40G-04                                                 | 4.2(3)       | nenic       | 1.0.42.0       | 5.2(3)             | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-VIC-M84-4P                                                  | 4.2(3)       | nenic       | 1.0.42.0       | 5.2(3)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| FI-ucsb1-eu-spdc-2-2           | Not-Listed    | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MLOM-40G-04                                                 | 4.2(3)       | nenic       | 1.0.42.0       | 5.2(3)             | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-VIC-M84-4P                                                  | 4.2(3)       | nenic       | 1.0.42.0       | 5.2(3)             | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MRAID12G-HE                                                 | 4.2(3)       | lsi_mr3     | 7.718.02.00    | 24.21.0-0156       | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| FI-ucsb1-eu-spdc-2-3           | Not-Listed    | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MLOM-40G-04                                                 | 4.2(3)       | nenic       | 1.0.33.0       | 5.2(3)             | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MRAID12G-HE                                                 | 4.2(3)       | lsi_mr3     | 7.718.02.00    | 24.21.0-0156       | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-VIC-M84-4P                                                  | 4.2(3)       | nenic       | 1.0.33.0       | 5.2(3)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| FI-ucsb1-eu-spdc-2-4           | Not-Listed    | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MRAID12G-HE                                                 | 4.2(3)       | lsi_mr3     | 7.718.02.00    | 24.21.0-0156       | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-VIC-M84-4P                                                  | 4.2(3)       | nenic       | 1.0.33.0       | 5.2(3)             | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MLOM-40G-04                                                 | 4.2(3)       | nenic       | 1.0.33.0       | 5.2(3)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+

License [#8]
------------

+--------------------------------+-----------+
| Server                         | License   |
+--------------------------------+-----------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Advantage | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Advantage | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Advantage | 
| comp3-p4b-eu-spdc-WZP262207UM  | Advantage | 
| FI-ucsb1-eu-spdc-2-1           | Advantage | 
| FI-ucsb1-eu-spdc-2-2           | Advantage | 
| FI-ucsb1-eu-spdc-2-3           | Advantage | 
| FI-ucsb1-eu-spdc-2-4           | Advantage | 
+--------------------------------+-----------+

Profile [#1]
------------

+-------------------------------+-----------+------------+--------------------------+-----------------+------------------------------------+----------------------------+--------------------------+--------+---------+
| Server                        | Profile   | State      | Last Modified            | Target Platform | Policy Name                        | Class Id                   | Modification Time        | Shared | In Sync |
+-------------------------------+-----------+------------+--------------------------+-----------------+------------------------------------+----------------------------+--------------------------+--------+---------+
| comp3-p4b-eu-spdc-WZP262207UM | amd-esx83 | Associated | 2023-12-03T00:29:52.359Z | Standalone      | MLOM-and-VIC-1-Infra               | vnic.LanConnectivityPolicy | 2023-11-03T18:48:32.289Z | True   | True    | 
|                               |           |            |                          |                 | UCS-MLOM-VIC1-no-LLDP-no-PC-no-FIP | adapter.ConfigPolicy       | 2023-11-03T18:47:16.719Z | True   | True    | 
|                               |           |            |                          |                 | KVM-Mapped-DVD-then-M2             | boot.PrecisionPolicy       | 2023-11-03T16:29:50.332Z | True   | True    | 
|                               |           |            |                          |                 | dns-emea-sp-config                 | networkconfig.Policy       | 2023-11-03T15:43:50.975Z | True   | True    | 
|                               |           |            |                          |                 | comp-smtp-policy                   | smtp.Policy                | 2023-11-02T15:08:15.565Z | True   | True    | 
|                               |           |            |                          |                 | ipmi-and-sol-allowed               | deviceconnector.Policy     | 2023-11-02T15:08:15.562Z | True   | True    | 
|                               |           |            |                          |                 | ssh-enabled                        | ssh.Policy                 | 2023-11-02T15:08:15.557Z | True   | True    | 
|                               |           |            |                          |                 | emea-sp-syslogs                    | syslog.Policy              | 2023-11-02T15:08:15.551Z | True   | True    | 
|                               |           |            |                          |                 | default-local-user                 | iam.EndPointUserPolicy     | 2023-11-02T15:08:15.549Z | True   | True    | 
|                               |           |            |                          |                 | ipmi-over-vlan-enabled             | ipmioverlan.Policy         | 2023-11-02T15:08:15.547Z | True   | True    | 
|                               |           |            |                          |                 | ntp-cisco                          | ntp.Policy                 | 2023-11-02T15:08:15.546Z | True   | True    | 
|                               |           |            |                          |                 | ldap-disabled                      | iam.LdapPolicy             | 2023-11-02T15:08:15.52Z  | True   | True    | 
|                               |           |            |                          |                 | fan-control-balanced               | thermal.Policy             | 2023-11-02T15:08:15.517Z | True   | True    | 
|                               |           |            |                          |                 | M2-MRAID-boot                      | storage.StoragePolicy      | 2023-11-02T15:08:15.515Z | True   | True    | 
|                               |           |            |                          |                 | bios-default-settings              | bios.Policy                | 2023-11-02T15:08:15.515Z | True   | True    | 
|                               |           |            |                          |                 | vKVM-enabled-not-tunneled          | kvm.Policy                 | 2023-11-02T15:08:15.511Z | True   | True    | 
|                               |           |            |                          |                 | c225-firmware-latest               | firmware.Policy            | 2023-11-02T15:08:15.509Z | True   | True    | 
|                               |           |            |                          |                 | sol-enabled-on-com0                | sol.Policy                 | 2023-11-02T15:08:15.508Z | True   | True    | 
|                               |           |            |                          |                 | comp-snmp-policy                   | snmp.Policy                | 2023-11-02T15:08:15.503Z | True   | True    | 
+-------------------------------+-----------+------------+--------------------------+-----------------+------------------------------------+----------------------------+--------------------------+--------+---------+

Workflow [#0]
-------------
None

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v istate

{
    "duration": 49261,
    "isctl": {
        "read": true,
        "calls": 18,
        "success": 18,
        "failed": 0,
        "total_time": 46449
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
        "lines": 70
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:24:28.548113	True	2174	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:24:29.963936	True	1412	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:24:31.624375	True	1587	12	isctl get compute blade   -o json --top 100
2023-12-03 15:24:33.909115	True	2252	86	isctl get tam securityadvisory   -o json --top 100
2023-12-03 15:24:36.333979	True	2369	72	isctl get tam advisorydefinition   -o json --top 100
2023-12-03 15:24:39.525816	True	3165	19	isctl get tam advisoryinstance --filter "AffectedObject/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5', '6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')"  -o json --top 100
2023-12-03 15:24:48.259699	True	8669	26	isctl get cond alarm --filter "RegisteredDevice/Moid in ('5fdf9be76f72612d300a8d81', '5fdf9c676f72612d300a9c8d', '5fdf9cf26f72612d300aaca0', '638501816f72612d317dabd7', '6501db456f726131016b7aea', '6501db456f726131016b7aea', '6501db456f726131016b7aea', '6501db456f726131016b7aea')"  -o json --top 100
2023-12-03 15:24:50.662042	True	2364	5	isctl get asset deviceregistration --filter "Moid in ('5fdf9be76f72612d300a8d81', '5fdf9c676f72612d300a9c8d', '5fdf9cf26f72612d300aaca0', '638501816f72612d317dabd7', '6501db456f726131016b7aea', '6501db456f726131016b7aea', '6501db456f726131016b7aea', '6501db456f726131016b7aea')"  -o json --top 100
2023-12-03 15:24:52.514016	True	1816	8	isctl get asset devicecontractinformation --filter "DeviceId in ('WZP23400AJW', 'WZP23400AK4', 'WZP23400AKL', 'WZP262207UM', 'FLM24140BJB', 'FLM24140B0B', 'FLM241501FB', 'FLM241501CT')"  -o json --top 100
2023-12-03 15:24:54.182709	True	1649	8	isctl get cond hclstatus --filter "ManagedObject/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5', '6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')"  -o json --top 100
2023-12-03 15:24:56.210889	True	1944	100	isctl get cond hclstatusdetail   -o json --top 100
2023-12-03 15:24:58.429151	True	2216	100	isctl get cond hclstatusdetail   -o json --top 100 --skip 100
2023-12-03 15:25:00.957502	True	2524	100	isctl get cond hclstatusdetail   -o json --top 100 --skip 200
2023-12-03 15:25:03.330404	True	2368	100	isctl get cond hclstatusdetail   -o json --top 100 --skip 300
2023-12-03 15:25:06.456518	True	3123	100	isctl get cond hclstatusdetail   -o json --top 100 --skip 400
2023-12-03 15:25:08.406666	True	1947	80	isctl get cond hclstatusdetail   -o json --top 100 --skip 500
2023-12-03 15:25:11.353278	True	2926	1	isctl get server profile --filter "AssignedServer/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5', '6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')" --expand "ConfigChangeDetails" -o json --top 100
2023-12-03 15:25:13.913355	True	1944	19	isctl get search searchitem --filter "IndexMotypes eq 'policy.AbstractPolicy' and Profiles/any(a:a/Moid eq '653fc09477696e31016b8e53')"  -o json --top 100
```

[[Back]](./ServerInventory.md)