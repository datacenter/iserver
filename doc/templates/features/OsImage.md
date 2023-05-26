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
DOC_TEMPLATE:image_get.base:iserver.output.default
```

## Verify

```
DOC_TEMPLATE:image_get.verify:iserver.output.default
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
DOC_TEMPLATE:image_create.help:output
```

### Create via command line

```
DOC_TEMPLATE:image_create.cli:iserver.output.default
```

Negative test: duplicate name

```
DOC_TEMPLATE:image_create.duplicate:iserver.output.default
```

Negative test: wrong vendor

```
DOC_TEMPLATE:image_create.vendor:iserver.output.default
```

Negative test: wrong vendor

```
DOC_TEMPLATE:image_create.version:iserver.output.default
```

Negative test: missing organization

```
DOC_TEMPLATE:image_create.organization:iserver.output.default
```

Negative test: wrong link

```
DOC_TEMPLATE:image_create.link:iserver.output.default
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
DOC_TEMPLATE:image_create.yaml:iserver.output.default
```

### Supported vendor

Example

```
DOC_TEMPLATE:image_get.vendor:iserver.output.default
```

### Supported versions

Example

```
DOC_TEMPLATE:image_get.version:iserver.output.default
```

## Update

Update of image definition can be done via command line attributes (for single object) or via YAML file (for multiple objects).

Object ID (Moid) is the only required parameter. All others are optional and will be updated when defined.

```
DOC_TEMPLATE:image_update.help:output
```

Example:

```
DOC_TEMPLATE:image_update.cli:iserver.output.default
```

## Delete

Delete command requires name or id (moid) of image metadata definition.

```
DOC_TEMPLATE:image_delete.help:output
```

Example:

```
DOC_TEMPLATE:image_delete.cli:iserver.output.default
```
