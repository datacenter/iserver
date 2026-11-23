# Intersight Fabric Interconnect

[[Back]](./README.md)

Use `iserver get fi` command to get fabric interconnects details connected to Intersight.

```
# iserver get fi --help
  --iaccount TEXT                   Intersight account
  --name TEXT                       Select by name
  --serial TEXT                     Select by serial
  --model TEXT                      Select by model
  -v, --view TEXT                   View options: state|eth|pc|fc|fpc|fanm|fan|psu|storage|inv|all  [default: state]
  --csv TEXT                        CSV filename supported for selected views
  -o, --output [default|json|yaml]  [default: default]
```

Notes:
- all fabric interconnects shown by default unless filtering options used
- [state](./FiViewState.md) default view
- human-readable default output

## Filtering

- [name](FiFilterName.md)
- [serial](FiFilterSerial.md)
- [model](FiFilterModel.md)

## View 

> [!NOTE]
> inventory output to csv file requires `-v inv` and `--csv filename` options

- [state](./FiViewState.md)
- [eth](./FiViewEth.md)
- [pc](./FiViewPc.md)
- [fanm](./FiViewFanModule.md)
- [fan](./FiViewFan.md)
- [inv](./FiViewInventory.md)
- [psu](./FiViewPsu.md)
- [storage](./FiViewStorage.md)

## Output

- default
- json

[[Back]](./README.md)