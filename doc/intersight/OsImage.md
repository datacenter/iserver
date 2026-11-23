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

+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
| Organization            | Image ID                  | Image Name                 | Vendor  | Version                    | Type  | Link               |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
| IntersightOrganization  | image-id                  | Image1                     | CentOS  | CentOS Version             | url   | Link1              |
| IntersightOrganization  | image-id                  | Image2                     | Ubuntu  | Ubuntu Version             | nfs   | Share1             |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
```

## Verify

```
# iserver get os-image --verify

+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+-----------+
| Organization            | Image ID                  | Image Name                 | Vendor  | Version                    | Type  | Link               |           |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+-----------+
| IntersightOrganization  | image-id                  | Image1                     | CentOS  | CentOS Version             | url   | Link1              | True      |
| IntersightOrganization  | image-id                  | Image2                     | Ubuntu  | Ubuntu Version             | nfs   | Share1             | True      |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+-----------+
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
    --name Image3
    --vendor CentOS
    --version "CentOS Version"
    --link http://10.1.1.1/my.iso
    --organization IntersightOrganization

Input parameters verification...
Input parameters verified

+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
| Organization            | Image ID                  | Image Name                 | Vendor  | Version                    | Type  | Link               |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
| IntersightOrganization  | image-id                  | Image1                     | CentOS  | CentOS Version             | url   | Link1              |
| IntersightOrganization  | image-id                  | Image2                     | Ubuntu  | Ubuntu Version             | nfs   | Share1             |
| IntersightOrganization  | image-id                  | Image3                     | CentOS  | CentOS Version             | url   | Link1              |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
```

### Create via YAML file

File content:

```
- Link: http://10.1.1.1/my.iso
  Name: Image3
  Type: url
  Vendor: CentOS
  Version: CentOS Version
  Organization: IntersightOrganization
```

```
# iserver create os-image --filename ./tests/os-image/new.yaml

Input parameters verification...
Input parameters verified

+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
| Organization            | Image ID                  | Image Name                 | Vendor  | Version                    | Type  | Link               |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
| IntersightOrganization  | image-id                  | Image1                     | CentOS  | CentOS Version             | url   | Link1              |
| IntersightOrganization  | image-id                  | Image2                     | Ubuntu  | Ubuntu Version             | nfs   | Share1             |
| IntersightOrganization  | image-id                  | Image3                     | CentOS  | CentOS Version             | url   | Link1              |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
```

### Supported vendor

Example

```
# iserver get os-vendor

+---------------------------+------------+
| Moid                      | Name       |
+---------------------------+------------+
| vendor-moid               | CentOS     |
| vendor-moid               | Citrix     |
| vendor-moid               | Microsoft  |
| vendor-moid               | Oracle     |
| vendor-moid               | Red Hat    |
| vendor-moid               | SuSE       |
| vendor-moid               | Ubuntu     |
| vendor-moid               | VMware     |
+---------------------------+------------+
```

### Supported versions

Example

```
# iserver get os-version --vendor Ubuntu

+---------------------------+-----------------+---------------------------+----------------------------+
| Vendor Moid               | Vendor Version  | Version Moid              | Version Name               |
+---------------------------+-----------------+---------------------------+----------------------------+
| vendor-moid               | Ubuntu          | version-id                | Ubuntu Server 12.04.4 LTS  |
| vendor-moid               | Ubuntu          | version-id                | Ubuntu Server 12.04.5 LTS  |
| vendor-moid               | Ubuntu          | version-id                | Ubuntu Server 14.04 LTS    |
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
    --id image-id
    --link http://10.10.10.10/new.iso

Input parameters verification...
Input parameters verified

+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
| Organization            | Image ID                  | Image Name                 | Vendor  | Version                    | Type  | Link               |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
| IntersightOrganization  | image-id                  | Image1                     | CentOS  | CentOS Version             | url   | Link1              |
| IntersightOrganization  | image-id                  | Image2                     | Ubuntu  | Ubuntu Version             | nfs   | Share1             |
| IntersightOrganization  | image-id                  | Image3                     | CentOS  | CentOS Version             | url   | Link1              |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
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
# iserver delete os-image --name Image3

Object deleted: image-id

+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
| Organization            | Image ID                  | Image Name                 | Vendor  | Version                    | Type  | Link               |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
| IntersightOrganization  | image-id                  | Image1                     | CentOS  | CentOS Version             | url   | Link1              |
| IntersightOrganization  | image-id                  | Image2                     | Ubuntu  | Ubuntu Version             | nfs   | Share1             |
+-------------------------+---------------------------+----------------------------+---------+----------------------------+-------+--------------------+
```
