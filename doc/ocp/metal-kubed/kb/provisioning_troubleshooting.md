## Provisioning - Troubleshooting

[[Back]](./provisioned.md)

## wrong checksum

the image definition contains sha256 checksum that must be correct and if verification fails, the host will enter deprovisioning state

Error log example

```
$ oc logs -n openshift-machine-api deploy/metal3 -c metal3-ironic
2026-08-19 07:43:26.825 47 DEBUG ironic.drivers.modules.agent_base [None req-14e97249-6ea1-4c02-8f8a-5943e7404e30 - - - - - -] 
  deploy command status for node c8dc9cc2-0dc6-4d2e-b0cd-fb22f2285212 on step {'step': 'write_image', 'priority': 80, 'abortable': True, 'argsinfo': None, 'interface': 'deploy'}:
    {
      'id': 'b5612add-c829-46e0-98d3-1dbf1dd822e7', 
      'command_name': 'execute_deploy_step', 
      'command_status': 'FAILED', 
      'command_error': {
        'type': 'ImageChecksumError', 
        'code': 500, 
        'message': 'Error verifying image checksum', 
        'details': 'Image failed to verify against checksum. location: CentOS-Stream-GenericCloud-9-20250930.0.x86_64.qcow2; image ID: /tmp/CentOS-Stream-GenericCloud-9-20250930.0.x86_64.qcow2; image checksum: 18f2977d77dfea1b74aee14533bd21c34f789139e949c57023b7364894b7e5e9; verification checksum: 4f6a47fbdf9094573543f05e0b44f58dc89e028c3c987b34690b7b9469294eeb'
      }, 
      'command_result': None
    }
```

## device hints fail to define target storage device

Host may have CIMC/virtual-media-mapped disks, by-path identifiers (which depend on PCI/ATA bus ordering) are more fragile in general. In such case, the recommendation is to  switch rootDeviceHints to disk's serial number instead

```
2026-08-20 06:59:47.942 47 DEBUG ironic.drivers.modules.agent_base [None req-4a66ade3-d92f-4a37-a0ac-e079d799a7ba - - - - - -] deploy command status for node 93083cee-597c-4592-8307-e548472525f8 on step {'step': 'write_image', 'priority': 80, 'abortable': True, 'argsinfo': None, 'interface': 'deploy'}: {'id': '1c24757d-097e-4ac8-b223-b64f73b5993f', 'command_name': 'execute_deploy_step', 'command_status': 'FAILED', 'command_error': {'type': 'DeviceNotFound', 'code': 404, 'message': 'Error finding the disk or partition device to deploy the image onto', 'details': "No suitable device was found for deployment using these hints {'by_path': 's== /dev/disk/by-path/pci-0000:04:00.0-ata-1.0'}"}, 'command_result': None} process_next_step /usr/lib/python3.12/site-packages/ironic/drivers/modules/agent_base.py:1112
```

## uefi mode incompatibility

tbd

[[Back]](./provisioned.md)