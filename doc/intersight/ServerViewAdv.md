# Intersight Server

## adv view

```
# iserver get server --group test -v adv

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


Advisory Summary [#8]
---------------------

+-----------+------+------+
| Server    | High | Info |
+-----------+------+------+
| Server763 | 4    | 2    |
| Server816 | 4    | 2    |
| Server715 | 3    | 2    |
| Server201 | 2    | 0    |
| Server791 | 1    | 1    |
| Server534 | 1    | 1    |
| Server851 | 1    | 1    |
| Server188 | 1    | 1    |
+-----------+------+------+

Advisory [#7]
-------------

+-----------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| Server    | Severity | Score | Name                                    | Description                              | CveIds         | DatePublished        | DateUpdated          |
+-----------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| Server763 | high     | 8.2   | Intel 2023.1 IPU - BIOS Advisory        | Potential security vulnerabilities in    | CVE-2022-26343 | 2023-02-14T00:00:00Z | 2023-02-14T00:00:00Z |
| Server816 |          |       |                                         | the BIOS firmware and Intel Trusted     | CVE-2022-30539 |                      |                      |
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
| Server715 | info     |       | End-of-Life Announcement for the Cisco  | Cisco announces the end-of-sale and      |                | 2023-05-01T00:00:00Z | 2023-05-02T00:00:00Z |
| Server763 |          |       | UCS M5 Rack Servers (C220 M5, C240 M5,  | end-of-life dates for the Cisco UCS M5   |                |                      |                      |
| Server816 |          |       | C480 M5)                                | Rack Servers (C220 M5, C240 M5, C480     |                |                      |                      |
|           |          |       |                                         | M5). The last day to order the affected  |                |                      |                      |
|           |          |       |                                         | product(s) is October 30, 2023.          |                |                      |                      |
|           |          |       |                                         | Customers with active service contracts  |                |                      |                      |
|           |          |       |                                         | will continue to receive support from    |                |                      |                      |
|           |          |       |                                         | the Cisco Technical Assistance Center    |                |                      |                      |
|           |          |       |                                         | (TAC) as per EoL bulletin.               |                |                      |                      |
+-----------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| Server188 | high     | 7.2   | Intel 2023.3 IPU - BIOS and Processors  | Potential security vulnerabilities in    | CVE-2022-37343 | 2023-08-08T00:00:00Z | 2023-08-08T00:00:00Z |
| Server534 |          |       | Advisories                              | the BIOS firmware or Intel Processors   | CVE-2022-44611 |                      |                      |
| Server715 |          |       |                                         | for Cisco UCS M4, M5 and M6 generation   | CVE-2022-38083 |                      |                      |
| Server763 |          |       |                                         | of servers may allow escalation of       | CVE-2022-27879 |                      |                      |
| Server791 |          |       |                                         | privilege, information disclosure or     | CVE-2022-43505 |                      |                      |
| Server816 |          |       |                                         | denial of service. Cisco is releasing    | CVE-2022-40982 |                      |                      |
| Server851 |          |       |                                         | software updates to mitigate these       | CVE-2023-23908 |                      |                      |
|           |          |       |                                         | potential vulnerabilities.               | CVE-2022-41804 |                      |                      |
|           |          |       |                                         |                                          | CVE-2022-36392 |                      |                      |
|           |          |       |                                         |                                          | CVE-2022-38102 |                      |                      |
|           |          |       |                                         |                                          | CVE-2022-29871 |                      |                      |
+-----------+----------+-------+-----------------------------------------+------------------------------------------+----------------+----------------------+----------------------+
| Server715 | medium   | 6.1   | Cisco Integrated Management Controller  | A vulnerability in the web-based         | CVE-2023-20228 | 2023-08-16T16:00:00Z | 2024-02-22T20:57:00Z |
| Server763 |          |       | Cross-Site Scripting Vulnerability      | management interface of Cisco            |                |                      |                      |
| Server816 |          |       |                                         | Integrated Management Controller (IMC)   |                |                      |                      |
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
| Server201 | high     | 8.8   | Cisco Integrated Management Controller  | A vulnerability in the CLI of the Cisco  | CVE-2024-20295 | 2024-04-17T16:00:00Z | 2024-06-28T16:06:36Z |
| Server715 |          |       | CLI Command Injection Vulnerability     | Integrated Management Controller (IMC)   |                |                      |                      |
| Server763 |          |       |                                         | could allow an authenticated, local      |                |                      |                      |
| Server816 |          |       |                                         | attacker to perform command injection    |                |                      |                      |
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
| Server201 | high     | 8.7   | Cisco Integrated Management Controller  | A vulnerability in the web-based         | CVE-2024-20356 | 2024-04-17T16:00:00Z | 2024-06-28T16:36:36Z |
| Server715 |          |       | Web-Based Management Interface Command  | management interface of Cisco            |                |                      |                      |
| Server763 |          |       | Injection Vulnerability                 | Integrated Management Controller (IMC)   |                |                      |                      |
| Server816 |          |       |                                         | could allow an authenticated, remote     |                |                      |                      |
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
| Server188 | info     |       | End-of-Life Announcement for the Cisco  | Cisco announces the end-of-sale and      |                | 2023-05-01T00:00:00Z | 2023-05-03T00:00:00Z |
| Server534 |          |       | UCS M5 Blade Server (B200 M5)           | end-of-life dates for the Cisco UCS M5   |                |                      |                      |
| Server791 |          |       |                                         | Blade Server (B200 M5). The last day to  |                |                      |                      |
| Server851 |          |       |                                         | order the affected product(s) is         |                |                      |                      |
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
| Server763 | Intel 2023.1 IPU - BIOS Advisory        | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00717.html                                                             |
| Server816 |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00718.html                                                             |
|           |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00700.html                                                             |
|           |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00738.html                                                             |
|           |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00767.html                                                             |
|           |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00730.html                                                             |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server715 | End-of-Life Announcement for the Cisco  | https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-c-series-rack-servers/ucs-m5-rack-server-c220-c240-c480-eol.html |
| Server763 | UCS M5 Rack Servers (C220 M5, C240 M5,  |                                                                                                                                                  |
| Server816 | C480 M5)                                |                                                                                                                                                  |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server188 | Intel 2023.3 IPU - BIOS and Processors  | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00813.html                                                             |
| Server534 | Advisories                              | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00783.html                                                             |
| Server715 |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00828.html                                                             |
| Server763 |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00836.html                                                             |
| Server791 |                                         | https://www.intel.com/content/www/us/en/security-center/advisory/intel-sa-00837.html                                                             |
| Server816 |                                         |                                                                                                                                                  |
| Server851 |                                         |                                                                                                                                                  |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server715 | Cisco Integrated Management Controller  | https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-xss-UMYtYEtr                                         |
| Server763 | Cross-Site Scripting Vulnerability      |                                                                                                                                                  |
| Server816 |                                         |                                                                                                                                                  |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server201 | Cisco Integrated Management Controller  | https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-cmd-inj-mUx4c5AJ                                     |
| Server715 | CLI Command Injection Vulnerability     |                                                                                                                                                  |
| Server763 |                                         |                                                                                                                                                  |
| Server816 |                                         |                                                                                                                                                  |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server201 | Cisco Integrated Management Controller  | https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-cimc-cmd-inj-bLuPcb                                       |
| Server715 | Web-Based Management Interface Command  |                                                                                                                                                  |
| Server763 | Injection Vulnerability                 |                                                                                                                                                  |
| Server816 |                                         |                                                                                                                                                  |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Server188 | End-of-Life Announcement for the Cisco  | https://www.cisco.com/c/en/us/products/collateral/servers-unified-computing/ucs-b-series-blade-servers/ucs-m5-blade-server-b200-eol.html         |
| Server534 | UCS M5 Blade Server (B200 M5)           |                                                                                                                                                  |
| Server791 |                                         |                                                                                                                                                  |
| Server851 |                                         |                                                                                                                                                  |
+-----------+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)