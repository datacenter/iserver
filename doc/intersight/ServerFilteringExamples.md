# Intersight Server

## Filter examples

Mix-and-match filtering options with implicit logical AND rule being applied.

```
--name myserver
--ip 10.1.1.1
--ip 10.1.0.0/24
--serial abc --serial xyz
--model m5sn
--type blade
--type rack
--alarm high
--disc
--led on
--power off
--mode imm
--mode ucsm
--cpu core:ge128
--cpu socket:eq1
--cpu thread:ge128
--cpu vendor:amd
--cpu arch:zen
--cpu model:7413
--gpu slot:gt0
--gpu model:nvidia
--mem size:gt512
--mem dimm:gt12
--mem model:mymodel
--mem serial:myserial
--pci slot:gt6
--pci model:xxv710
--pci pid:ID25GF
--sc vendor:lsi
--sc serial:myserial
--pd type:ssd
--pd proto:sata
--pd pid:UCS-SD960G6I1X-EV
--pd model:ST1200MM0009
--pd vendor:ata
--pd serial:myserial
--vd count:gt1
--mac 85ab --mac 0a0d
--fan mod:gt6
--fan unit:gt10
--fan state:nok
--psu state:nok
--psu model:ps-2112
--psu serial:myserial
--psu vendor:cisco
```

[[Back]](./ServerInventory.md)