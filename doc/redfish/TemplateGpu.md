# GPU Template

[[Next]](./TemplateHw.md) [[Back]](./README.md)

```
# iserver.py get redfish template \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    -v gpu

+----+---------+------------------------------+--------------+---------------+----------+
| ID | GPU Id  | Name                         | Model        | Serial        | Firmware |
+----+---------+------------------------------+--------------+---------------+----------+
| 1  | GPU-7-0 | NVIDIA A16 PCIe FHFL DS 250W | UCSC-GPU-A16 | 1111111111111 | 22222222 | 
| 2  | GPU-7-1 | NVIDIA A16 PCIe FHFL DS 250W | UCSC-GPU-A16 | 1111111111111 | 22222222 | 
| 3  | GPU-7-2 | NVIDIA A16 PCIe FHFL DS 250W | UCSC-GPU-A16 | 1111111111111 | 22222222 | 
| 4  | GPU-7-3 | NVIDIA A16 PCIe FHFL DS 250W | UCSC-GPU-A16 | 1111111111111 | 22222222 | 
+----+---------+------------------------------+--------------+---------------+----------+

View: access, account, bios, cpu, fan, gpu, hw, identity (def), mem, net, pci, power, psu, role, storage, thermal, all
```

[[Back]](./README.md)