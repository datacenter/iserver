# UCSX-9508 IFM monitoring with iserver

Use '-m|--module' option with '.|*|all' value to select all modules.

```
DOC_TEMPLATE:get_ucsx_ifm.all:iserver.output.default
```

## Select module by slot ID

Use '-m|--module 1|2' option to select module by slot ID

```
DOC_TEMPLATE:get_ucsx_ifm.single_by_slot:iserver.output.default
```

## Select module by fabric path

Use '-m|--module a|b|A|B' option to select module by fabric path

```
DOC_TEMPLATE:get_ucsx_ifm.single_by_path:iserver.output.default
```

## JSON output

```
DOC_TEMPLATE:get_ucsx_ifm.json:iserver.output.default
```

## YAML output

```
DOC_TEMPLATE:get_ucsx_ifm.yaml:iserver.output.default
```

## Developer output

```
DOC_TEMPLATE:get_ucsx_ifm.all:devel.debug
```