# Software Configuration Utility

Software Configuration Utility (SCU) is a binary image that needs to be downloaded from cisco.com software download pages.

SCU is required in case kickstart file is used and this is the deployment scenario supported by iserver. SCU has different versions with support of different OS vendors and versions.
iserver does not check if SCU versions supports an OS Image selected for OS installation. It is up to You to make sure that combination of SCU version and OS Image is supported.

Once downloaded, SCU needs to be also uploaded to web/nfs server so during installation the server can download it using its management (CIMC) interface.

SCU location is defined as metadata in Intersight and this is exactly where iserver helps i.e.:
- create/update/delete scu metadata using either command line options or YAML input file
- verify if scu metadata location is reachable

Notes:
- verification reachability test is made from the location where iserver runs on. Since during OS installation, UCS server will be downloading the SCU image
- verification works for URL-based locations only

## Get

```
# iserver get scu

+-------------------------+---------------------------+-------------+----------+-------+-------------------------------------------------------------------------+
| Organization            | SCU ID                    | SCU Name    | Version  | Type  | Link                                                                    |
+-------------------------+---------------------------+-------------+----------+-------+-------------------------------------------------------------------------+
| EMEAR-SPDC-Specialists  | 632afedf6567612d300aefe6  | SCU 6.1.3c  | 6.1.3c   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-cxxx-scu-6.1.3c.iso  | 
| EMEAR-SPDC-Specialists  | 632c227a6567612d30187910  | SCU 6.2.2a  | 6.2.2a   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-scu-6.2.2a.iso       | 
| EMEAR-SPDC-Specialists  | 633d73076567612d30b2ca97  | dummy       | dummy    | url   | http://10.1.1.1/dummy.iso                                               | 
+-------------------------+---------------------------+-------------+----------+-------+-------------------------------------------------------------------------+
```

## Verify

```
# iserver get scu --verify

+-------------------------+---------------------------+-------------+----------+-------+-------------------------------------------------------------------------+-----------+
| Organization            | SCU ID                    | SCU Name    | Version  | Type  | Link                                                                    | Verified  |
+-------------------------+---------------------------+-------------+----------+-------+-------------------------------------------------------------------------+-----------+
| EMEAR-SPDC-Specialists  | 632afedf6567612d300aefe6  | SCU 6.1.3c  | 6.1.3c   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-cxxx-scu-6.1.3c.iso  | False     | 
| EMEAR-SPDC-Specialists  | 632c227a6567612d30187910  | SCU 6.2.2a  | 6.2.2a   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-scu-6.2.2a.iso       | False     | 
| EMEAR-SPDC-Specialists  | 633d73076567612d30b2ca97  | dummy       | dummy    | url   | http://10.1.1.1/dummy.iso                                               | False     | 
+-------------------------+---------------------------+-------------+----------+-------+-------------------------------------------------------------------------+-----------+
```

## Create

Rules
- name must be unique
- version can be any
- url link must be syntatically valid
- organization is required if more than one organization defined under your account

When YAML file used, rules are enforced on every entry in the list.

```
# iserver create scu --help

Usage: iserver.py create scu [OPTIONS]

  Create software configuration utilities

Options:
  --iaccount TEXT      Intersight account  [default: isctl]
  --filename TEXT      Input yaml file
  --organization TEXT  Organization Name
  --name TEXT          SCU Name
  --version TEXT       SCU Version
  --link TEXT          SCU HTTP Link
  --devel              Developer output  [default: False]
  --help               Show this message and exit.
```

### Create via command line

```
# iserver create scu
    --name "SCU via CLI"
    --version 6.2.2
    --link http://10.1.1.1/ucs-scu.6.2.2.iso
    --organization EMEAR-SPDC-Specialists

Input parameters verification...
Input parameters verified

+-------------------------+---------------------------+--------------+----------+-------+-------------------------------------------------------------------------+
| Organization            | SCU ID                    | SCU Name     | Version  | Type  | Link                                                                    |
+-------------------------+---------------------------+--------------+----------+-------+-------------------------------------------------------------------------+
| EMEAR-SPDC-Specialists  | 632afedf6567612d300aefe6  | SCU 6.1.3c   | 6.1.3c   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-cxxx-scu-6.1.3c.iso  | 
| EMEAR-SPDC-Specialists  | 632c227a6567612d30187910  | SCU 6.2.2a   | 6.2.2a   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-scu-6.2.2a.iso       | 
| EMEAR-SPDC-Specialists  | 633d73076567612d30b2ca97  | dummy        | dummy    | url   | http://10.1.1.1/dummy.iso                                               | 
| EMEAR-SPDC-Specialists  | 634652336567612d30185301  | SCU via CLI  | 6.2.2    | url   | http://10.1.1.1/ucs-scu.6.2.2.iso                                       | 
+-------------------------+---------------------------+--------------+----------+-------+-------------------------------------------------------------------------+
```

Negative test: duplicate name

```
# iserver create scu
    --name "SCU via CLI"
    --version 6.2.2
    --link http://10.1.1.1/ucs-scu.6.2.2.iso
    --organization EMEAR-SPDC-Specialists

Input parameters verification...
[ERROR] Input parameters validation failed
Name SCU via CLI already defined
```

Negative test: no version

```
# iserver create scu
    --name lalala
    --link http://10.1.1.1/ucs-scu.6.2.2.iso
    --organization EMEAR-SPDC-Specialists

Input parameters verification...
[ERROR] Define version
```

Negative test: missing organization

```
# iserver create scu
    --name lalala
    --version 6.2.2
    --link http://10.1.1.1/ucs-scu.6.2.2.iso

Input parameters verification...
[ERROR] Multiple organizations found. Select single one
- EMEAR-SPDC-Specialists
- hsiad-POC
- vanniew-demo
```

Negative test: wrong link

```
# iserver create scu
    --name lalala
    --version 6.2.2
    --link http://.1.1/a.iso
    --organization EMEAR-SPDC-Specialists

Input parameters verification...
[ERROR] Input parameters validation failed
Invalid link: http://.1.1/a.iso
```

### Create via YAML file

File content:

```
- Link: http://10.1.1.1/scu1.iso
  Name: SCU via YAML
  Type: url
  Vendor: Cisco
  Version: "1.0"
  Organization: EMEAR-SPDC-Specialists
```

```
# iserver create scu --filename ./tests/scu/new.yaml

Input parameters verification...
Input parameters verified

+-------------------------+---------------------------+---------------+----------+-------+-------------------------------------------------------------------------+
| Organization            | SCU ID                    | SCU Name      | Version  | Type  | Link                                                                    |
+-------------------------+---------------------------+---------------+----------+-------+-------------------------------------------------------------------------+
| EMEAR-SPDC-Specialists  | 632afedf6567612d300aefe6  | SCU 6.1.3c    | 6.1.3c   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-cxxx-scu-6.1.3c.iso  | 
| EMEAR-SPDC-Specialists  | 632c227a6567612d30187910  | SCU 6.2.2a    | 6.2.2a   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-scu-6.2.2a.iso       | 
| EMEAR-SPDC-Specialists  | 633d73076567612d30b2ca97  | dummy         | dummy    | url   | http://10.1.1.1/dummy.iso                                               | 
| EMEAR-SPDC-Specialists  | 634652336567612d30185301  | SCU via CLI   | 6.2.2    | url   | http://10.1.1.1/ucs-scu.6.2.2.iso                                       | 
| EMEAR-SPDC-Specialists  | 634652466567612d301854be  | SCU via YAML  | 1.0      | url   | http://10.1.1.1/scu1.iso                                                | 
+-------------------------+---------------------------+---------------+----------+-------+-------------------------------------------------------------------------+
```

## Update

Update of SCU definition can be done via command line attributes (for single object) or via YAML file (for multiple objects)

Object ID (Moid) is the only required parameter. All others are optional and will be updated when defined.

```
# iserver set scu --help

Usage: iserver.py set scu [OPTIONS]

  Set software configuration utilities

Options:
  --iaccount TEXT  Intersight account  [default: isctl]
  --filename TEXT  Input yaml file
  --id TEXT        SCU Id
  --name TEXT      SCU Name
  --version TEXT   SCU Version
  --link TEXT      SCU HTTP Link
  --devel          Developer output  [default: False]
  --help           Show this message and exit.
```

Example:

```
# iserver set scu
    --id 634652336567612d30185301
    --link http://10.10.10.10/new.iso

Input parameters verification...
Input parameters verified

+-------------------------+---------------------------+---------------+----------+-------+-------------------------------------------------------------------------+
| Organization            | SCU ID                    | SCU Name      | Version  | Type  | Link                                                                    |
+-------------------------+---------------------------+---------------+----------+-------+-------------------------------------------------------------------------+
| EMEAR-SPDC-Specialists  | 632afedf6567612d300aefe6  | SCU 6.1.3c    | 6.1.3c   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-cxxx-scu-6.1.3c.iso  | 
| EMEAR-SPDC-Specialists  | 632c227a6567612d30187910  | SCU 6.2.2a    | 6.2.2a   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-scu-6.2.2a.iso       | 
| EMEAR-SPDC-Specialists  | 633d73076567612d30b2ca97  | dummy         | dummy    | url   | http://10.1.1.1/dummy.iso                                               | 
| EMEAR-SPDC-Specialists  | 634652336567612d30185301  | SCU via CLI   | 6.2.2    | url   | http://10.10.10.10/new.iso                                              | 
| EMEAR-SPDC-Specialists  | 634652466567612d301854be  | SCU via YAML  | 1.0      | url   | http://10.1.1.1/scu1.iso                                                | 
+-------------------------+---------------------------+---------------+----------+-------+-------------------------------------------------------------------------+
```

## Delete

Delete command requires name or id (moid) of SCU metadata definition.

```
# iserver delete scu --help

Usage: iserver.py delete scu [OPTIONS]

  Delete software configuration utilities

Options:
  --iaccount TEXT  Intersight account  [default: isctl]
  --id TEXT        SCU object Moid
  --name TEXT      SCU object Name
  --devel          Developer output  [default: False]
  --help           Show this message and exit.
```

Example:

```
# iserver delete scu --name "SCU via CLI"

Object deleted: 634652336567612d30185301


+-------------------------+---------------------------+---------------+----------+-------+-------------------------------------------------------------------------+
| Organization            | SCU ID                    | SCU Name      | Version  | Type  | Link                                                                    |
+-------------------------+---------------------------+---------------+----------+-------+-------------------------------------------------------------------------+
| EMEAR-SPDC-Specialists  | 632afedf6567612d300aefe6  | SCU 6.1.3c    | 6.1.3c   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-cxxx-scu-6.1.3c.iso  | 
| EMEAR-SPDC-Specialists  | 632c227a6567612d30187910  | SCU 6.2.2a    | 6.2.2a   | url   | http://10.60.0.252/2-IMAGES/cisco/ucs_c-series/ucs-scu-6.2.2a.iso       | 
| EMEAR-SPDC-Specialists  | 633d73076567612d30b2ca97  | dummy         | dummy    | url   | http://10.1.1.1/dummy.iso                                               | 
| EMEAR-SPDC-Specialists  | 634652466567612d301854be  | SCU via YAML  | 1.0      | url   | http://10.1.1.1/scu1.iso                                                | 
+-------------------------+---------------------------+---------------+----------+-------+-------------------------------------------------------------------------+
```
