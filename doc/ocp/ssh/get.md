# SSH Access - Get keys

[[Back]](./README.md) [[Add]](./create_key.md) [[Delete]](./delete_key.md)

## Workflow

- identify machine config objects that define SSH keys; typically it will be `99-master-ssh` and `99-worker-ssh`
- download the content of machine config object into YAML file
- show public keys

## Requirements

None

## Configurable options

```
# iserver get ocp ssh
  --cluster TEXT              Cluster name
```

## Example

```
# iserver get ocp ssh --cluster bm1 

OpenShift Workflow - SSH Public Key - Get
=========================================

OpenShift Cluster: bm1

+----+--------------------------------+-------------+-------------------------+----------------+
| ID | SSH User                       | Key Type    | Key                     | OpenShift Node |
+----+--------------------------------+-------------+-------------------------+----------------+
| 1  | user@host1                     | ssh-ed25519 | AAAAC3NzaC...UDXorVCR71 | master         | 
|    |                                |             |                         | worker         | 
+----+--------------------------------+-------------+-------------------------+----------------+
| 2  | user@host2                     | ssh-ed25519 | AAAAC3NzaC...xtIULcEKAJ | master         | 
|    |                                |             |                         | worker         | 
+----+--------------------------------+-------------+-------------------------+----------------+
```

[[Back]](./README.md) [[Add]](./create_key.md) [[Delete]](./delete_key.md)