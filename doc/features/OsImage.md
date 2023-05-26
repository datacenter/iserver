# Operating System Image

OS Image is a binary iso image that needs to be downloaded from OS vendor repository, uploaded to nfs/web server and defined as metadata in Intersight.

iserver features
- create/update/delete image metadata using either command line options or YAML input file
- verify if image metadata location is reachable

Notes:
- verification reachability test is made from the location where iserver runs on. Since during OS installation, UCS server will be downloading the OS image
- verification works for URL-based locations only

## Get

```
# iserver get os-image

+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
| Organization            | Image ID                  | Image Name                 | Vendor  | Version                    | Type  | Link                                                              |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
| EMEAR-SPDC-Specialists  | 61b9c6ff6567612d30140473  | Centos 7.6 Minimal         | CentOS  | CentOS 7.6                 | url   | http://10.60.0.252/Centos/CentOS-7-x86_64-DVD-1810.iso            | 
| EMEAR-SPDC-Specialists  | 61c0ba846567612d305ffc9f  | Ubuntu Server 20.04.3 LTS  | Ubuntu  | Ubuntu Server 20.04.3 LTS  | nfs   | 10.49.234.1/home/filer/ubuntu-20.04.3-live-server-amd64.iso       | 
| EMEAR-SPDC-Specialists  | 632c42d86567612d3019ee47  | Ubuntu 20.04.3 LTS         | Ubuntu  | Ubuntu Server 20.04.3 LTS  | url   | http://10.60.0.252/2-IMAGES/ubuntu-20.04.3-live-server-amd64.iso  | 
| EMEAR-SPDC-Specialists  | 633068b96567612d304a7844  | Ubuntu 22.04LTS            | Ubuntu  | Ubuntu Server 22.04 LTS    | url   | http://10.60.0.252/2-IMAGES/ubuntu-22.04.1-live-server-amd64.iso  | 
| EMEAR-SPDC-Specialists  | 633d738a6567612d30b2d08a  | dummy                      | Ubuntu  | Ubuntu Server 22.04 LTS    | url   | http://10.1.1.1/dummy.iso                                         | 
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
```

## Verify

```
# iserver get os-image --verify

+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+-----------+
| Organization            | Image ID                  | Image Name                 | Vendor  | Version                    | Type  | Link                                                              | Verified  |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+-----------+
| EMEAR-SPDC-Specialists  | 61b9c6ff6567612d30140473  | Centos 7.6 Minimal         | CentOS  | CentOS 7.6                 | url   | http://10.60.0.252/Centos/CentOS-7-x86_64-DVD-1810.iso            | False     | 
| EMEAR-SPDC-Specialists  | 61c0ba846567612d305ffc9f  | Ubuntu Server 20.04.3 LTS  | Ubuntu  | Ubuntu Server 20.04.3 LTS  | nfs   | 10.49.234.1/home/filer/ubuntu-20.04.3-live-server-amd64.iso       | False     | 
| EMEAR-SPDC-Specialists  | 632c42d86567612d3019ee47  | Ubuntu 20.04.3 LTS         | Ubuntu  | Ubuntu Server 20.04.3 LTS  | url   | http://10.60.0.252/2-IMAGES/ubuntu-20.04.3-live-server-amd64.iso  | False     | 
| EMEAR-SPDC-Specialists  | 633068b96567612d304a7844  | Ubuntu 22.04LTS            | Ubuntu  | Ubuntu Server 22.04 LTS    | url   | http://10.60.0.252/2-IMAGES/ubuntu-22.04.1-live-server-amd64.iso  | False     | 
| EMEAR-SPDC-Specialists  | 633d738a6567612d30b2d08a  | dummy                      | Ubuntu  | Ubuntu Server 22.04 LTS    | url   | http://10.1.1.1/dummy.iso                                         | False     | 
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+-----------+
```

## Create

Rules
- name must be unique
- vendor value must be supported by Intersight
- version value must be supported by Intersight
- url link must be syntatically valid
- organization is required if more than one organization defined under your account

When YAML file used, rules are enforced on every entry in the list.

```
# iserver create os-image --help

Usage: iserver.py create os-image [OPTIONS]

  Create os image

Options:
  --iaccount TEXT      Intersight account  [default: isctl]
  --filename TEXT      Input yaml file
  --name TEXT          OS Name
  --vendor TEXT        OS Vendor
  --version TEXT       OS Version
  --link TEXT          OS HTTP Link
  --organization TEXT  Organization Name
  --devel              Developer output  [default: False]
  --help               Show this message and exit.
```

### Create via command line

```
# iserver create os-image
    --name "Image via CLI"
    --vendor Ubuntu
    --version "Ubuntu Server 20.04.3 LTS"
    --link http://10.1.1.1/ubuntu.iso
    --organization EMEAR-SPDC-Specialists

Input parameters verification...
Input parameters verified

+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
| Organization            | Image ID                  | Image Name                 | Vendor  | Version                    | Type  | Link                                                              |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
| EMEAR-SPDC-Specialists  | 61b9c6ff6567612d30140473  | Centos 7.6 Minimal         | CentOS  | CentOS 7.6                 | url   | http://10.60.0.252/Centos/CentOS-7-x86_64-DVD-1810.iso            | 
| EMEAR-SPDC-Specialists  | 61c0ba846567612d305ffc9f  | Ubuntu Server 20.04.3 LTS  | Ubuntu  | Ubuntu Server 20.04.3 LTS  | nfs   | 10.49.234.1/home/filer/ubuntu-20.04.3-live-server-amd64.iso       | 
| EMEAR-SPDC-Specialists  | 632c42d86567612d3019ee47  | Ubuntu 20.04.3 LTS         | Ubuntu  | Ubuntu Server 20.04.3 LTS  | url   | http://10.60.0.252/2-IMAGES/ubuntu-20.04.3-live-server-amd64.iso  | 
| EMEAR-SPDC-Specialists  | 633068b96567612d304a7844  | Ubuntu 22.04LTS            | Ubuntu  | Ubuntu Server 22.04 LTS    | url   | http://10.60.0.252/2-IMAGES/ubuntu-22.04.1-live-server-amd64.iso  | 
| EMEAR-SPDC-Specialists  | 633d738a6567612d30b2d08a  | dummy                      | Ubuntu  | Ubuntu Server 22.04 LTS    | url   | http://10.1.1.1/dummy.iso                                         | 
| EMEAR-SPDC-Specialists  | 63465b1f6567612d3018b497  | Image via CLI              | Ubuntu  | Ubuntu Server 20.04.3 LTS  | url   | http://10.1.1.1/ubuntu.iso                                        | 
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
```

Negative test: duplicate name

```
# iserver create os-image
    --name "Image via CLI"
    --vendor Ubuntu
    --version "Ubuntu Server 20.04.3 LTS"
    --link http://10.1.1.1/ubuntu.iso
    --organization EMEAR-SPDC-Specialists

Input parameters verification...
[ERROR] Input parameters validation failed
Name Image via CLI already defined
```

Negative test: wrong vendor

```
# iserver create os-image
    --name lalala
    --vendor NewOsVendor
    --version "Ubuntu Server 35.04.3 LTS"
    --link http://10.1.1.1/ubuntu.iso
    --organization EMEAR-SPDC-Specialists

Input parameters verification...
[ERROR] Input parameters validation failed
Vendor not found: NewOsVendor
```

Negative test: wrong vendor

```
# iserver create os-image
    --name lalala
    --vendor Ubuntu
    --version "Ubuntu Server 35.04.3 LTS"
    --link http://10.1.1.1/ubuntu.iso
    --organization EMEAR-SPDC-Specialists

Input parameters verification...
[ERROR] Input parameters validation failed
Invalid version for vendor: Ubuntu Server 35.04.3 LTS
```

Negative test: missing organization

```
# iserver create os-image
    --name lalala
    --vendor Ubuntu
    --version "Ubuntu Server 35.04.3 LTS"
    --link http://10.1.1.1/ubuntu.iso

Input parameters verification...
[ERROR] Multiple organizations found. Select single one
- EMEAR-SPDC-Specialists
- hsiad-POC
- vanniew-demo
```

Negative test: wrong link

```
# iserver create os-image
    --name lalala
    --vendor Ubuntu
    --version "Ubuntu Server 35.04.3 LTS"
    --link http://.1.1/ubuntu.iso
    --organization EMEAR-SPDC-Specialists

Input parameters verification...
[ERROR] Input parameters validation failed
Invalid version for vendor: Ubuntu Server 35.04.3 LTS
```

### Create via YAML file

File content:

```
- Link: http://10.1.1.1/centos.iso
  Name: Image via YAML
  Type: url
  Vendor: CentOS
  Version: CentOS 7.6
  Organization: EMEAR-SPDC-Specialists
```

```
# iserver create os-image --filename ./tests/os-image/new.yaml

Input parameters verification...
Input parameters verified

+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
| Organization            | Image ID                  | Image Name                 | Vendor  | Version                    | Type  | Link                                                              |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
| EMEAR-SPDC-Specialists  | 61b9c6ff6567612d30140473  | Centos 7.6 Minimal         | CentOS  | CentOS 7.6                 | url   | http://10.60.0.252/Centos/CentOS-7-x86_64-DVD-1810.iso            | 
| EMEAR-SPDC-Specialists  | 61c0ba846567612d305ffc9f  | Ubuntu Server 20.04.3 LTS  | Ubuntu  | Ubuntu Server 20.04.3 LTS  | nfs   | 10.49.234.1/home/filer/ubuntu-20.04.3-live-server-amd64.iso       | 
| EMEAR-SPDC-Specialists  | 632c42d86567612d3019ee47  | Ubuntu 20.04.3 LTS         | Ubuntu  | Ubuntu Server 20.04.3 LTS  | url   | http://10.60.0.252/2-IMAGES/ubuntu-20.04.3-live-server-amd64.iso  | 
| EMEAR-SPDC-Specialists  | 633068b96567612d304a7844  | Ubuntu 22.04LTS            | Ubuntu  | Ubuntu Server 22.04 LTS    | url   | http://10.60.0.252/2-IMAGES/ubuntu-22.04.1-live-server-amd64.iso  | 
| EMEAR-SPDC-Specialists  | 633d738a6567612d30b2d08a  | dummy                      | Ubuntu  | Ubuntu Server 22.04 LTS    | url   | http://10.1.1.1/dummy.iso                                         | 
| EMEAR-SPDC-Specialists  | 63465b1f6567612d3018b497  | Image via CLI              | Ubuntu  | Ubuntu Server 20.04.3 LTS  | url   | http://10.1.1.1/ubuntu.iso                                        | 
| EMEAR-SPDC-Specialists  | 63465b366567612d3018b583  | Image via YAML             | CentOS  | CentOS 7.6                 | url   | http://10.1.1.1/centos.iso                                        | 
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
```

### Supported vendor

Example

```
# iserver get os-vendor

+---------------------------+------------+
| Moid                      | Name       |
+---------------------------+------------+
| 5b7370f16836726e35cc7025  | CentOS     | 
| 5b7370f16836726e35cc7023  | Citrix     | 
| 5b7370f16836726e35cc7028  | Microsoft  | 
| 5b7370f16836726e35cc7022  | Oracle     | 
| 5b7370f16836726e35cc7026  | Red Hat    | 
| 5b7370f16836726e35cc7021  | SuSE       | 
| 5b7370f16836726e35cc7024  | Ubuntu     | 
| 5b7370f16836726e35cc7027  | VMware     | 
+---------------------------+------------+
```

### Supported versions

Example

```
# iserver get os-version --vendor Ubuntu

+---------------------------+-----------------+---------------------------+----------------------------+
| Vendor Moid               | Vendor Version  | Version Moid              | Version Name               |
+---------------------------+-----------------+---------------------------+----------------------------+
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc708c  | Ubuntu Server 12.04.4 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc70b8  | Ubuntu Server 12.04.5 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc706d  | Ubuntu Server 14.04 LTS    | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc703a  | Ubuntu Server 14.04.1 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc7039  | Ubuntu Server 14.04.2 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc7067  | Ubuntu Server 14.04.3 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc70bc  | Ubuntu Server 14.04.4 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc705a  | Ubuntu Server 14.04.5 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc708d  | Ubuntu Server 16.04 LTS    | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc7038  | Ubuntu Server 16.04.1 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc7075  | Ubuntu Server 16.04.2 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc702e  | Ubuntu Server 16.04.3 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc7040  | Ubuntu Server 16.04.4 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5be7eb546b707066396f9416  | Ubuntu Server 16.04.5 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5cce91556f72742d30b039c9  | Ubuntu Server 16.04.6 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5fe83f466f72742d30c88800  | Ubuntu Server 16.04.7 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5b7370f16836726e35cc702b  | Ubuntu Server 18.04 LTS    | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5be7eb546b707066396f9418  | Ubuntu Server 18.04.1 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5ce105a56f72742d30d34420  | Ubuntu Server 18.04.2 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5dd0fed16f72742d303cee94  | Ubuntu Server 18.04.3 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5e92bde16f72742d30afae7c  | Ubuntu Server 18.04.4 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5fe83f466f72742d30c88801  | Ubuntu Server 18.04.5 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 630b128a6f72742d3139e60a  | Ubuntu Server 18.04.6 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5ef840a56f72742d3030424c  | Ubuntu Server 20.04 LTS    | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 5f9523d76f72742d30055a83  | Ubuntu Server 20.04.1 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 609788846f72742d317136c5  | Ubuntu Server 20.04.2 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 61b5ac286f72742d31f49537  | Ubuntu Server 20.04.3 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 625bbb0a6f72742d31f58871  | Ubuntu Server 20.04.4 LTS  | 
| 5b7370f16836726e35cc7024  | Ubuntu          | 62f89da96f72742d31a52732  | Ubuntu Server 22.04 LTS    | 
+---------------------------+-----------------+---------------------------+----------------------------+
```

## Update

Update of image definition can be done via command line attributes (for single object) or via YAML file (for multiple objects).

Object ID (Moid) is the only required parameter. All others are optional and will be updated when defined.

```
# iserver set os-image --help

Usage: iserver.py set os-image [OPTIONS]

  Set os image objects from input yaml file

Options:
  --iaccount TEXT  Intersight account  [default: isctl]
  --filename TEXT  Input yaml file
  --id TEXT        SCU Id
  --name TEXT      OS Name
  --vendor TEXT    OS Vendor
  --version TEXT   OS Version
  --link TEXT      OS HTTP Link
  --devel          Developer output  [default: False]
  --help           Show this message and exit.
```

Example:

```
# iserver set os-image
    --id 63465b1f6567612d3018b497
    --link http://10.10.10.10/new.iso

Input parameters verification...
Input parameters verified

+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
| Organization            | Image ID                  | Image Name                 | Vendor  | Version                    | Type  | Link                                                              |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
| EMEAR-SPDC-Specialists  | 61b9c6ff6567612d30140473  | Centos 7.6 Minimal         | CentOS  | CentOS 7.6                 | url   | http://10.60.0.252/Centos/CentOS-7-x86_64-DVD-1810.iso            | 
| EMEAR-SPDC-Specialists  | 61c0ba846567612d305ffc9f  | Ubuntu Server 20.04.3 LTS  | Ubuntu  | Ubuntu Server 20.04.3 LTS  | nfs   | 10.49.234.1/home/filer/ubuntu-20.04.3-live-server-amd64.iso       | 
| EMEAR-SPDC-Specialists  | 632c42d86567612d3019ee47  | Ubuntu 20.04.3 LTS         | Ubuntu  | Ubuntu Server 20.04.3 LTS  | url   | http://10.60.0.252/2-IMAGES/ubuntu-20.04.3-live-server-amd64.iso  | 
| EMEAR-SPDC-Specialists  | 633068b96567612d304a7844  | Ubuntu 22.04LTS            | Ubuntu  | Ubuntu Server 22.04 LTS    | url   | http://10.60.0.252/2-IMAGES/ubuntu-22.04.1-live-server-amd64.iso  | 
| EMEAR-SPDC-Specialists  | 633d738a6567612d30b2d08a  | dummy                      | Ubuntu  | Ubuntu Server 22.04 LTS    | url   | http://10.1.1.1/dummy.iso                                         | 
| EMEAR-SPDC-Specialists  | 63465b1f6567612d3018b497  | Image via CLI              | Ubuntu  | Ubuntu Server 20.04.3 LTS  | url   | http://10.10.10.10/new.iso                                        | 
| EMEAR-SPDC-Specialists  | 63465b366567612d3018b583  | Image via YAML             | CentOS  | CentOS 7.6                 | url   | http://10.1.1.1/centos.iso                                        | 
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
```

## Delete

Delete command requires name or id (moid) of image metadata definition.

```
# iserver delete os-image --help

Usage: iserver.py delete os-image [OPTIONS]

  Delete operating system image metadata

Options:
  --iaccount TEXT  Intersight account  [default: isctl]
  --id TEXT        OS Image object Moid
  --name TEXT      OS Image object Name
  --devel          Developer output  [default: False]
  --help           Show this message and exit.
```

Example:

```
# iserver delete os-image --name "Image via CLI"

Object deleted: 63465b1f6567612d3018b497


+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
| Organization            | Image ID                  | Image Name                 | Vendor  | Version                    | Type  | Link                                                              |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
| EMEAR-SPDC-Specialists  | 61b9c6ff6567612d30140473  | Centos 7.6 Minimal         | CentOS  | CentOS 7.6                 | url   | http://10.60.0.252/Centos/CentOS-7-x86_64-DVD-1810.iso            | 
| EMEAR-SPDC-Specialists  | 61c0ba846567612d305ffc9f  | Ubuntu Server 20.04.3 LTS  | Ubuntu  | Ubuntu Server 20.04.3 LTS  | nfs   | 10.49.234.1/home/filer/ubuntu-20.04.3-live-server-amd64.iso       | 
| EMEAR-SPDC-Specialists  | 632c42d86567612d3019ee47  | Ubuntu 20.04.3 LTS         | Ubuntu  | Ubuntu Server 20.04.3 LTS  | url   | http://10.60.0.252/2-IMAGES/ubuntu-20.04.3-live-server-amd64.iso  | 
| EMEAR-SPDC-Specialists  | 633068b96567612d304a7844  | Ubuntu 22.04LTS            | Ubuntu  | Ubuntu Server 22.04 LTS    | url   | http://10.60.0.252/2-IMAGES/ubuntu-22.04.1-live-server-amd64.iso  | 
| EMEAR-SPDC-Specialists  | 633d738a6567612d30b2d08a  | dummy                      | Ubuntu  | Ubuntu Server 22.04 LTS    | url   | http://10.1.1.1/dummy.iso                                         | 
| EMEAR-SPDC-Specialists  | 63465b366567612d3018b583  | Image via YAML             | CentOS  | CentOS 7.6                 | url   | http://10.1.1.1/centos.iso                                        | 
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+-------------------------------------------------------------------+
```
