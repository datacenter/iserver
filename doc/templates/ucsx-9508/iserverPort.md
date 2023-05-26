# UCSX-9508 IFM port monitoring with iserver

Use '-p|--port' option with '.|*|all' value to select all ports on all IFMs.

```
DOC_TEMPLATE:get_ucsx_port.all:iserver.output.default
```

## Show host ports only

Use '-p t:host' option to select only host (backplane) ports. Use '-m' option to further select single IFM.

```
DOC_TEMPLATE:get_ucsx_port.host:iserver.output.default
```

## Show network ports only

Use '-p t:net' option to select only network (fabric) ports. Use '-m' option to further select single IFM.

```
DOC_TEMPLATE:get_ucsx_port.net:iserver.output.default
```

## Select ports by module

Use '-p m:1|2|a|b' option to select ports by module.

```
DOC_TEMPLATE:get_ucsx_port.module:iserver.output.default
```

## Select ports by node

Use '-p n:<id>' option to select host (fabric) ports connected to node <id>

```
DOC_TEMPLATE:get_ucsx_port.node:iserver.output.default
```

## Select ports by state (up or down)

Use '-p s:up|down' option to select ports by state

```
DOC_TEMPLATE:get_ucsx_port.down:iserver.output.default
```

## JSON output

```
DOC_TEMPLATE:get_ucsx_port.json:iserver.output.default
```

## YAML output

```
DOC_TEMPLATE:get_ucsx_port.yaml:iserver.output.default
```

## Developer output

```
DOC_TEMPLATE:get_ucsx_port.all:devel.debug
```