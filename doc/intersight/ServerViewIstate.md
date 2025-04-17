# Intersight Server

## istate view

```
# iserver get server --group test -v istate

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Advisory Summary [#8]
---------------------

+-----------+------+------+
| Server    | High | Info |
+-----------+------+------+
| Server426 | 4    | 2    |
| Server649 | 4    | 2    |
| Server433 | 3    | 2    |
| Server448 | 2    | 0    |
| Server139 | 1    | 1    |
| Server630 | 1    | 1    |
| Server397 | 1    | 1    |
| Server358 | 1    | 1    |
+-----------+------+------+

Advisory [#7]
-------------

+-----------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| Server    | Severity | Score | Name                                    | Description                              | CveIds         | DatePublished        | DateUpdated          |
+-----------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| Server426 | high     | 8.2   | Intel 2023.1 IPU - BIOS Advisory        | Potential security vulnerabilities in    | CVE-2022-26343 | 2023-02-14T00:00:00Z | 2023-02-14T00:00:00Z |
| Server649 |          |       |                                         | the BIOS firmware and Intel Trusted     | CVE-2022-30539 |                      |                      |
|           |          |       |                                         | Execution Technology (TXT) Secure        | CVE-2022-32231 |                      |                      |
|           |          |       |                                         | Initialization (SINIT) Authenticated     | CVE-2022-26837 |                      |                      |
|           |          |       |                                         | Code Modules (ACM) for some Intel       | CVE-2022-30704 |                      |                      |
|           |          |       |                                         | Processors may allow escalation of       | CVE-2021-0187  |                      |                      |
|           |          |       |                                         | privilege.  Intel is releasing BIOS      | CVE-2022-36348 |                      |                      |
|           |          |       |                                         | updates to mitigate these potential      | CVE-2022-36794 |                      |                      |
|           |          |       |                                         | vulnerabilities.- CVE-2022-26343         | CVE-2021-33124 |                      |                      |
|           |          |       |                                         | impacts only M5 servers.-                | CVE-2022-21216 |                      |                      |
|           |          |       |                                         | CVE-2022-32231 impacts both M5 and M6    | CVE-2022-33196 |                      |                      |
|           |          |       |                                         | servers.- Rest all CVEs impact only M6   | CVE-2022-38090 |                      |                      |
|           |          |       |                                         | servers.                                 | CVE-2022-33972 |                      |                      |
+-----------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| Server426 | info     |       | End-of-Life Announcement for the Cisco  | Cisco announces the end-of-sale and      |                | 2023-05-01T00:00:00Z | 2023-05-02T00:00:00Z |
| Server433 |          |       | UCS M5 Rack Servers (C220 M5, C240 M5,  | end-of-life dates for the Cisco UCS M5   |                |                      |                      |
| Server649 |          |       | C480 M5)                                | Rack Servers (C220 M5, C240 M5, C480     |                |                      |                      |
|           |          |       |                                         | M5). The last day to order the affected  |                |                      |                      |
|           |          |       |                                         | product(s) is October 30, 2023.          |                |                      |                      |
|           |          |       |                                         | Customers with active service contracts  |                |                      |                      |
|           |          |       |                                         | will continue to receive support from    |                |                      |                      |
|           |          |       |                                         | the Cisco Technical Assistance Center    |                |                      |                      |
|           |          |       |                                         | (TAC) as per EoL bulletin.               |                |                      |                      |
+-----------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| Server139 | high     | 7.2   | Intel 2023.3 IPU - BIOS and Processors  | Potential security vulnerabilities in    | CVE-2022-37343 | 2023-08-08T00:00:00Z | 2023-08-08T00:00:00Z |
| Server358 |          |       | Advisories                              | the BIOS firmware or Intel Processors   | CVE-2022-44611 |                      |                      |
| Server397 |          |       |                                         | for Cisco UCS M4, M5 and M6 generation   | CVE-2022-38083 |                      |                      |
| Server426 |          |       |                                         | of servers may allow escalation of       | CVE-2022-27879 |                      |                      |
| Server433 |          |       |                                         | privilege, information disclosure or     | CVE-2022-43505 |                      |                      |
| Server630 |          |       |                                         | denial of service. Cisco is releasing    | CVE-2022-40982 |                      |                      |
| Server649 |          |       |                                         | software updates to mitigate these       | CVE-2023-23908 |                      |                      |
|           |          |       |                                         | potential vulnerabilities.               | CVE-2022-41804 |                      |                      |
|           |          |       |                                         |                                          | CVE-2022-36392 |                      |                      |
|           |          |       |                                         |                                          | CVE-2022-38102 |                      |                      |
|           |          |       |                                         |                                          | CVE-2022-29871 |                      |                      |
+-----------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| Server426 | medium   | 6.1   | Cisco Integrated Management Controller  | A vulnerability in the web-based         | CVE-2023-20228 | 2023-08-16T16:00:00Z | 2024-02-22T20:57:00Z |
| Server433 |          |       | Cross-Site Scripting Vulnerability      | management interface of Cisco            |                |                      |                      |
| Server649 |          |       |                                         | Integrated Management Controller (IMC)   |                |                      |                      |
|           |          |       |                                         | could allow an unauthenticated, remote   |                |                      |                      |
|           |          |       |                                         | attacker to conduct a cross-site         |                |                      |                      |
|           |          |       |                                         | scripting (XSS) attack against a user    |                |                      |                      |
|           |          |       |                                         | of the interface.This vulnerability is   |                |                      |                      |
|           |          |       |                                         | due to insufficient validation of user   |                |                      |                      |
|           |          |       |                                         | input. An attacker could exploit this    |                |                      |                      |
|           |          |       |                                         | vulnerability by persuading a user of    |                |                      |                      |
|           |          |       |                                         | an affected interface to click a         |                |                      |                      |
|           |          |       |                                         | crafted link. A successful exploit       |                |                      |                      |
|           |          |       |                                         | could allow the attacker to execute      |                |                      |                      |
|           |          |       |                                         | arbitrary script code in the browser of  |                |                      |                      |
|           |          |       |                                         | the targeted user or access sensitive,   |                |                      |                      |
|           |          |       |                                         | browser-based information.Cisco has      |                |                      |                      |
|           |          |       |                                         | released software updates that address   |                |                      |                      |
|           |          |       |                                         | this vulnerability. There are no         |                |                      |                      |
|           |          |       |                                         | workarounds that address this            |                |                      |                      |
|           |          |       |                                         | vulnerability**Note**:- This             |                |                      |                      |
|           |          |       |                                         | vulnerability only impacts the specific  |                |                      |                      |
|           |          |       |                                         | rack server models (mentioned below in   |                |                      |                      |
|           |          |       |                                         | Fixed Software section) operating in     |                |                      |                      |
|           |          |       |                                         | standalone mode only.                    |                |                      |                      |
+-----------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| Server426 | high     | 8.8   | Cisco Integrated Management Controller  | A vulnerability in the CLI of the Cisco  | CVE-2024-20295 | 2024-04-17T16:00:00Z | 2024-06-28T16:06:36Z |
| Server433 |          |       | CLI Command Injection Vulnerability     | Integrated Management Controller (IMC)   |                |                      |                      |
| Server448 |          |       |                                         | could allow an authenticated, local      |                |                      |                      |
| Server649 |          |       |                                         | attacker to perform command injection    |                |                      |                      |
|           |          |       |                                         | attacks on the underlying operating      |                |                      |                      |
|           |          |       |                                         | system and elevate privileges to root.   |                |                      |                      |
|           |          |       |                                         | To exploit this vulnerability, the       |                |                      |                      |
|           |          |       |                                         | attacker must have read-only or higher   |                |                      |                      |
|           |          |       |                                         | privileges on an affected device.This    |                |                      |                      |
|           |          |       |                                         | vulnerability is due to insufficient     |                |                      |                      |
|           |          |       |                                         | validation of user-supplied input. An    |                |                      |                      |
|           |          |       |                                         | attacker could exploit this              |                |                      |                      |
|           |          |       |                                         | vulnerability by submitting a crafted    |                |                      |                      |
|           |          |       |                                         | CLI command. A successful exploit could  |                |                      |                      |
|           |          |       |                                         | allow the attacker to elevate            |                |                      |                      |
|           |          |       |                                         | privileges to root.Cisco has released    |                |                      |                      |
|           |          |       |                                         | software updates that address this       |                |                      |                      |
|           |          |       |                                         | vulnerability. There are no workarounds  |                |                      |                      |
|           |          |       |                                         | that address this                        |                |                      |                      |
|           |          |       |                                         | vulnerability.**Note**: This             |                |                      |                      |
|           |          |       |                                         | vulnerability only impacts the specific  |                |                      |                      |
|           |          |       |                                         | rack server models (mentioned below in   |                |                      |                      |
|           |          |       |                                         | Fixed Software section) operating in     |                |                      |                      |
|           |          |       |                                         | standalone mode only.                    |                |                      |                      |
+-----------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| Server426 | high     | 8.7   | Cisco Integrated Management Controller  | A vulnerability in the web-based         | CVE-2024-20356 | 2024-04-17T16:00:00Z | 2024-06-28T16:36:36Z |
| Server433 |          |       | Web-Based Management Interface Command  | management interface of Cisco            |                |                      |                      |
| Server448 |          |       | Injection Vulnerability                 | Integrated Management Controller (IMC)   |                |                      |                      |
| Server649 |          |       |                                         | could allow an authenticated, remote     |                |                      |                      |
|           |          |       |                                         | attacker with Administrator-level        |                |                      |                      |
|           |          |       |                                         | privileges to perform command injection  |                |                      |                      |
|           |          |       |                                         | attacks on an affected system and        |                |                      |                      |
|           |          |       |                                         | elevate their privileges to root.This    |                |                      |                      |
|           |          |       |                                         | vulnerability is due to insufficient     |                |                      |                      |
|           |          |       |                                         | user input validation. An attacker       |                |                      |                      |
|           |          |       |                                         | could exploit this vulnerability by      |                |                      |                      |
|           |          |       |                                         | sending crafted commands to the          |                |                      |                      |
|           |          |       |                                         | web-based management interface of the    |                |                      |                      |
|           |          |       |                                         | affected software. A successful exploit  |                |                      |                      |
|           |          |       |                                         | could allow the attacker to elevate      |                |                      |                      |
|           |          |       |                                         | their privileges to root.Cisco has       |                |                      |                      |
|           |          |       |                                         | released software updates that address   |                |                      |                      |
|           |          |       |                                         | this vulnerability. There are no         |                |                      |                      |
|           |          |       |                                         | workarounds that address this            |                |                      |                      |
|           |          |       |                                         | vulnerability.**Note**: This             |                |                      |                      |
|           |          |       |                                         | vulnerability only impacts the specific  |                |                      |                      |
|           |          |       |                                         | rack server models (mentioned below in   |                |                      |                      |
|           |          |       |                                         | Fixed Software section) operating in     |                |                      |                      |
|           |          |       |                                         | standalone mode only.                    |                |                      |                      |
+-----------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| Server139 | info     |       | End-of-Life Announcement for the Cisco  | Cisco announces the end-of-sale and      |                | 2023-05-01T00:00:00Z | 2023-05-03T00:00:00Z |
| Server358 |          |       | UCS M5 Blade Server (B200 M5)           | end-of-life dates for the Cisco UCS M5   |                |                      |                      |
| Server397 |          |       |                                         | Blade Server (B200 M5). The last day to  |                |                      |                      |
| Server630 |          |       |                                         | order the affected product(s) is         |                |                      |                      |
|           |          |       |                                         | October 30, 2023. Customers with active  |                |                      |                      |
|           |          |       |                                         | service contracts will continue to       |                |                      |                      |
|           |          |       |                                         | receive support from the Cisco           |                |                      |                      |
|           |          |       |                                         | Technical Assistance Center (TAC) based  |                |                      |                      |
|           |          |       |                                         | on EoL bulletin.                         |                |                      |                      |
+-----------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+

Advisory Url [#7]
-----------------

+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server    | Name                                    | Urls                                                                                                                                             |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server426 | Intel 2023.1 IPU - BIOS Advisory        | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00717.html                                                             |
| Server649 |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00718.html                                                             |
|           |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00700.html                                                             |
|           |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00738.html                                                             |
|           |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00767.html                                                             |
|           |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00730.html                                                             |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server426 | End-of-Life Announcement for the Cisco  | https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-m5-rack-server-c220-c240-c480-eol.html |
| Server433 | UCS M5 Rack Servers (C220 M5, C240 M5,  |                                                                                                                                                  |
| Server649 | C480 M5)                                |                                                                                                                                                  |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server139 | Intel 2023.3 IPU - BIOS and Processors  | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00813.html                                                             |
| Server358 | Advisories                              | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00783.html                                                             |
| Server397 |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00828.html                                                             |
| Server426 |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00836.html                                                             |
| Server433 |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00837.html                                                             |
| Server630 |                                         |                                                                                                                                                  |
| Server649 |                                         |                                                                                                                                                  |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server426 | Cisco Integrated Management Controller  | https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-xss-UMYtYEtr                                         |
| Server433 | Cross-Site Scripting Vulnerability      |                                                                                                                                                  |
| Server649 |                                         |                                                                                                                                                  |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server426 | Cisco Integrated Management Controller  | https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-cmd-inj-mUx4c5AJ                                     |
| Server433 | CLI Command Injection Vulnerability     |                                                                                                                                                  |
| Server448 |                                         |                                                                                                                                                  |
| Server649 |                                         |                                                                                                                                                  |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server426 | Cisco Integrated Management Controller  | https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-cmd-inj-bLuPcb                                       |
| Server433 | Web-Based Management Interface Command  |                                                                                                                                                  |
| Server448 | Injection Vulnerability                 |                                                                                                                                                  |
| Server649 |                                         |                                                                                                                                                  |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server139 | End-of-Life Announcement for the Cisco  | https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-b-series-blade-servers/ucs-m5-blade-server-b200-eol.html         |
| Server358 | UCS M5 Blade Server (B200 M5)           |                                                                                                                                                  |
| Server397 |                                         |                                                                                                                                                  |
| Server630 |                                         |                                                                                                                                                  |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Connector [#8]
--------------

+-----------+-------------------+-------------------+-----------------+--------------------------+-------------------------------+---------------+----------------------------+
| Server    | Connection Status | Connector Version | Claimed By      | Claimed Time             | Connection Status Last Update | Platform Type | Device External IP Address |
+-----------+-------------------+-------------------+-----------------+--------------------------+-------------------------------+---------------+----------------------------+
| Server426 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | IMCM5         | 66.240.195.29              |
| Server649 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | IMCM5         | 66.41.77.152               |
| Server433 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | IMCM5         | 66.154.245.192             |
| Server448 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | IMCRack       | 66.236.45.197              |
| Server139 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | UCSFI         | 66.56.216.117              |
| Server630 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | UCSFI         | 66.194.184.191             |
| Server397 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | UCSFI         | 66.137.172.248             |
| Server358 | Connected         | Version-Number    | user@domain.com | 2024-01-01T00:00:00.000Z | 2025-01-01T00:00:00.000Z      | UCSFI         | 66.7.214.144               |
+-----------+-------------------+-------------------+-----------------+--------------------------+-------------------------------+---------------+----------------------------+

Contract [#8]
-------------

+-----------+-----------------+----------------------+----------------------+--------------------------+--------------------------------------------------------------+-----------------------+--------------------+
| Server    | Contract Status | Start Date           | End Date             | Last Updated             | Service Description                                          | Purchase Order Number | Sales Order Number |
+-----------+-----------------+----------------------+----------------------+--------------------------+--------------------------------------------------------------+-----------------------+--------------------+
| Server426 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS | PO188                 | SO82               |
| Server649 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS | PO102                 | SO30               |
| Server433 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS C240 M5 10 NVMe + 16 SAS/SATA SFF w/o CPU,mem,HD,PCIe,PS | PO119                 | SO213              |
| Server448 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS C225 M6 Rack w/o CPU, mem, drv, 1U wSFF 10HDD backplane  | PO204                 | SO4                |
| Server139 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | PO218                 | SO43               |
| Server630 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | PO112                 | SO246              |
| Server397 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | PO57                  | SO248              |
| Server358 | Not Covered     | 0001-01-01T00:00:00Z | 0001-01-01T00:00:00Z | 2025-01-01T00:00:00.000Z | UCS B200 M5 Blade w/o CPU, mem, HDD, mezz (UPG)              | PO32                  | SO139              |
+-----------+-----------------+----------------------+----------------------+--------------------------+--------------------------------------------------------------+-----------------------+--------------------+

HCL Summary [#8]
----------------

+-----------+------------+
| Server    | Overall    |
+-----------+------------+
| Server426 | Incomplete |
| Server649 | Incomplete |
| Server433 | Incomplete |
| Server448 | Incomplete |
| Server139 | Not-Listed |
| Server630 | Not-Listed |
| Server397 | Not-Listed |
| Server358 | Not-Listed |
+-----------+------------+

HCL Server Hardware Compliance [#8]
-----------------------------------

+-----------+-----------+----------------+-------------------------------------------------+----------+
| Server    | Status    | Model          | CPU                                             | Firmware |
+-----------+-----------+----------------+-------------------------------------------------+----------+
| Server426 | Validated | UCSC-C240-M5SN | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
| Server649 | Validated | UCSC-C240-M5SN | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
| Server433 | Validated | UCSC-C240-M5SN | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
| Server448 | Validated | UCSC-C225-M6S  | AMD EPYC 7763 64-Core Processor                 | 1.0(1a)  |
| Server139 | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
| Server630 | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
| Server397 | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
| Server358 | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
+-----------+-----------+----------------+-------------------------------------------------+----------+

HCL Server Software Compliance [#8]
-----------------------------------

+-----------+------------+-------------------------+-----------+-------------+
| Server    | Status     | Reason                  | OS Vendor | OS Version  |
+-----------+------------+-------------------------+-----------+-------------+
| Server426 | Incomplete | Missing-Os-Info         |           |             |
| Server649 | Incomplete | Missing-Os-Info         |           |             |
| Server433 | Incomplete | Missing-Os-Info         |           |             |
| Server448 | Incomplete | Missing-Os-Info         |           |             |
| Server139 | Validated  | Incompatible-Components | VMware    | ESXi 8.0 U2 |
| Server630 | Validated  | Incompatible-Components | VMware    | ESXi 8.0 U2 |
| Server397 | Validated  | Incompatible-Components | VMware    | ESXi 8.0 U2 |
| Server358 | Validated  | Incompatible-Components | VMware    | ESXi 8.0 U2 |
+-----------+------------+-------------------------+-----------+-------------+

HCL Server Adapter Compliance [#8]
----------------------------------

+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server    | Status        | Component  | Hardware      | Software      | Reason                 | Model                                                            | Cimc Version | Driver Name | Driver Version | Firmware Version |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server426 | Not-Evaluated | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) LOM X550-T2                                             | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | UCSC-MLOM-C25Q-04                                                | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server649 | Not-Evaluated | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | UCSC-MLOM-C25Q-04                                                | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) LOM X550-T2                                             | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server433 | Not-Evaluated | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) LOM X550-T2                                             | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | UCSC-MLOM-C25Q-04                                                | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server448 | Not-Evaluated | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco Boot optimized M.2 Raid controller                         | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco 12G SAS RAID Controller with 4GB FBWC (16 Drives)          | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | UCSC-PCIE-C25Q-04                                                | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | UCSC-M-V100-04                                                   | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server139 | Not-Listed    | Not-Listed | Not-Evaluated | Not-Evaluated | Incompatible-Os-Info   | UCSB-MRAID12G-HE                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-VIC-M84-4P                                                  | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-MLOM-40G-04                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server630 | Not-Listed    | Not-Listed | Not-Evaluated | Not-Evaluated | Incompatible-Os-Info   | UCSB-MRAID12G-HE                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-VIC-M84-4P                                                  | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-MLOM-40G-04                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server397 | Not-Listed    | Not-Listed | Not-Evaluated | Not-Evaluated | Incompatible-Os-Info   | UCSB-MRAID12G-HE                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-VIC-M84-4P                                                  | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-MLOM-40G-04                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server358 | Not-Listed    | Not-Listed | Not-Evaluated | Not-Evaluated | Incompatible-Os-Info   | UCSB-MRAID12G-HE                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-MLOM-40G-04                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-VIC-M84-4P                                                  | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+

License [#8]
------------

+-----------+-----------+
| Server    | License   |
+-----------+-----------+
| Server426 | Advantage |
| Server649 | Advantage |
| Server433 | Advantage |
| Server448 | Advantage |
| Server139 | Advantage |
| Server630 | Advantage |
| Server397 | Advantage |
| Server358 | Advantage |
+-----------+-----------+

Profile [#1]
------------

+-----------+---------+------------+--------------------------+-----------------+-------------+----------------------------+--------------------------+--------+---------+
| Server    | Profile | State      | Last Modified            | Target Platform | Policy Name | Class Id                   | Modification Time        | Shared | In Sync |
+-----------+---------+------------+--------------------------+-----------------+-------------+----------------------------+--------------------------+--------+---------+
| Server448 | profile | Associated | 2025-01-01T00:00:00.000Z | Standalone      | Name-70     | bios.Policy                | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-38     | storage.StoragePolicy      | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-54     | vnic.LanConnectivityPolicy | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-67     | adapter.ConfigPolicy       | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-21     | boot.PrecisionPolicy       | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-84     | networkconfig.Policy       | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-41     | smtp.Policy                | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-32     | deviceconnector.Policy     | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-63     | ssh.Policy                 | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-99     | syslog.Policy              | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-30     | iam.EndPointUserPolicy     | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-58     | ipmioverlan.Policy         | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-27     | ntp.Policy                 | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-79     | iam.LdapPolicy             | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-87     | thermal.Policy             | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-18     | kvm.Policy                 | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-20     | firmware.Policy            | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-56     | sol.Policy                 | 2025-01-01T00:00:00.000Z | True   | True    |
|           |         |            |                          |                 | Name-22     | snmp.Policy                | 2025-01-01T00:00:00.000Z | True   | True    |
+-----------+---------+------------+--------------------------+-----------------+-------------+----------------------------+--------------------------+--------+---------+

Workflow [#0]
-------------
None

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)