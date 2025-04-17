# Intersight Server

## Bot filter examples

Mix-and-match filtering options with implicit logical AND rule being applied.

```
name:p2b
ip:10.**.**.**
ip:10.**.**.*/24
serial:myserial
model:m5sn
type:blade
type:rack
alarm:high
led:on
power:off
mode:imm
mode:ucsm
cpu-core:ge128
cpu-socket:eq1
cpu-thread:ge128
cpu-vendor:amd
cpu-arch:zen
cpu-model:7413
gpu-slot:gt0
gpu-model:nvidia
mem-size:gt512
mem-dimm:gt12
mem-model:36ASF4G72PZ-2G9E2
mem-serial:myserial
pci-slot:gt6
pci-model:xxv710
pci-pid:ID25GF
sc-vendor:lsi
sc-serial:myserial
pd-type:ssd
pd-proto:sata
pd-pid:UCS-SD960G6I1X-EV
pd-model:ST1200MM0009
pd-vendor:ata
pd-serial:myserial
vd-count:gt1
mac-85ab
fan-mod:gt6
fan-unit:gt10
fan-state:nok
psu-state:nok
psu-model:ps-2112
psu-serial:myserial
psu-vendor:cisco
```

[[Back]](./ServerInventory.md)