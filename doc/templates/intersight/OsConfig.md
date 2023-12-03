# Operating System Configuration

Each combination of OS vendor and version that supports template-based installation, needs associated configuration file that will be attached upon boot time by SCU.

## Get

```
DOC_TEMPLATE:get_config.help:output
```

Example

```
DOC_TEMPLATE:get_config.default:iserver.output.default
```

Negative test: not enough parameters

```
DOC_TEMPLATE:get_config.params:iserver.output.default
```

Negative test: wrong vendor

```
DOC_TEMPLATE:get_config.vendor:iserver.output.default
```

Negative test: wrong version

```
DOC_TEMPLATE:get_config.version:iserver.output.default
```
