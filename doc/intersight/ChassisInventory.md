# Intersight Chassis Inventory

## Command options

Filter options:
  - [name](ChassisFilterName.md)
  - [serial](ChassisFilterSerials.md)
  - [model](ChassisFilterModel.md)

View options:
  - [adv](./ChassisViewAdv.md)
  - [alarm](./ChassisViewAlarm.md)
  - [contract](./ChassisViewContract.md)
  - [exp](./ChassisViewExp.md)
  - [fan](./ChassisViewFan.md)
  - [fi](./ChassisViewFi.md)
  - [hw](./ChassisViewHw.md)
  - [io](./ChassisViewIo.md)
  - [inv](./ChassisViewInv.md)
  - [istate](./ChassisViewIstate.md)
  - [net](./ChassisViewNet.md)
  - [node](./ChassisViewNode.md)
  - [port](./ChassisViewPort.md)
  - [psu](./ChassisViewPsu.md)
  - [psuc](./ChassisViewPsuc.md)
  - [state](./ChassisViewState.md)

Output options:
  - [default](./ChassisOutputDefault.md)
  - json

```
# iserver get chassis --help

Usage: iserver.py get chassis [OPTIONS]

  Get chassis details

Options:
  --iaccount TEXT                 Intersight account  [default: demo]
  --name TEXT                     Select by name
  --serial TEXT                   Select by serial
  --model TEXT                    Select by model
  --ttl TEXT                      Cache TTL
  --inventory TEXT                Inventory CSV filename
  -v, --view TEXT                 [state|adv|alarm|contract|istate|node|fi|io|
                                  exp|port|fan|psu|psuc|hw|inv]  [default:
                                  state]
  -o, --output [default|json|yaml]
                                  [default: default]
  --anonymize                     Anonymized output
  --devel                         Developer output
  --help                          Show this message and exit.

Info: finished in 261 ms and logs saved in /tmp/iserver\e01266c6c262
```

[[Back]](./README.md)