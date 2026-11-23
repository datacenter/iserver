# Private Network - Delete network

[[Back]](./README.md)

## Workflow

- check cilium cni operator state
- check current cilium configuration
- check private network feature [enabled](./enable.md)
- delete private network selected by name

## Requirements

- private network [enabled](./enable.md)

## Expected outcome

- Private network deleted

## Configurable options

```
# iserver delete ocp cilium pnet --mode network
  --cluster TEXT                  Cluster Name
  --network TEXT                  Private network name
  --no-confirm                    Confirmation mode
```

## Example

```
# iserver delete ocp cilium pnet --cluster bm1 --mode network --network test


OpenShift Workflow - Cilium Private Network - Delete Private Network
====================================================================

OpenShift Cluster: bm1
Cilium cni found
Private network enabled
Private network crds found

+----+-----------------------------+---------------+--------+-----------+--------------+-----+--------+
| ID | Clusterwide Private Network | CIDRv4        | CIDRv6 | Route     | Via          | POD | Bridge |
+----+-----------------------------+---------------+--------+-----------+--------------+-----+--------+
| 1  | test                        | 10.10.10.0/24 | ---    | 0.0.0.0/0 | 10.10.10.254 | --- | ---    | 
+----+-----------------------------+---------------+--------+-----------+--------------+-----+--------+

Delete Clusterwide Private Network
----------------------------------
- name: test

Network deleted

Wait for not network...

Completed tasks
- Private Network deleted
```

[[Back]](./README.md)