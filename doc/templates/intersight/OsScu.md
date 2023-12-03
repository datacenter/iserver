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
DOC_TEMPLATE:scu_get.base:iserver.output.default
```

## Verify

```
DOC_TEMPLATE:scu_get.verify:iserver.output.default
```

## Create

Rules
- name must be unique
- version can be any
- url link must be syntatically valid
- organization is required if more than one organization defined under your account

When YAML file used, rules are enforced on every entry in the list.

```
DOC_TEMPLATE:scu_create.help:output
```

### Create via command line

```
DOC_TEMPLATE:scu_create.cli:iserver.output.default
```

Negative test: duplicate name

```
DOC_TEMPLATE:scu_create.duplicate:iserver.output.default
```

Negative test: no version

```
DOC_TEMPLATE:scu_create.version:iserver.output.default
```

Negative test: missing organization

```
DOC_TEMPLATE:scu_create.organization:iserver.output.default
```

Negative test: wrong link

```
DOC_TEMPLATE:scu_create.link:iserver.output.default
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
DOC_TEMPLATE:scu_create.yaml:iserver.output.default
```

## Update

Update of SCU definition can be done via command line attributes (for single object) or via YAML file (for multiple objects)

Object ID (Moid) is the only required parameter. All others are optional and will be updated when defined.

```
DOC_TEMPLATE:scu_update.help:output
```

Example:

```
DOC_TEMPLATE:scu_update.cli:iserver.output.default
```

## Delete

Delete command requires name or id (moid) of SCU metadata definition.

```
DOC_TEMPLATE:scu_delete.help:output
```

Example:

```
DOC_TEMPLATE:scu_delete.cli:iserver.output.default
```
