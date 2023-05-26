Irideos

Intersight UI
- UCSX walk-through
- rack walk-through
- operations
	- profiles
	- power
	- firmware
	- os install
- extras
	- storage
	- ivs

Compute API
- redfish
- intersight

Competitive
- stateless compute
- os install
- state get
- server profiles
- what demos they do for PVT - maybe reuse

# Redfish support

iserver supports Redfish (GET) API that can be executed on:
- [Supported Redfish endpoint](./Endpoint.md) defined with endpoint type, IP address and authentication credentials
- [Intersight managed server](./Intersight.md) defined with management IP, name or serial number

Note: Redfish API call runs directly on endpoint

## Features

- [Get resource](./Resource.md)
- [Get properties of resource](./Property.md)
- [Get Oem extensions](./Oem.md)
- [Get Actions](./Action.md)
- [Find property by key](./Key.md)
- [Find property by value](./Value.md)
- [Discover resource references](./Children.md)
- [Get resource description](./Description.md)
- [Get predefined set of properties](./Template.md)

## Intersight integration features

- tbd

## Endpoint Test Results

- [UCS C220-M5](../ucs-c250m5-redfish/Overview.md)
- [UCS X9508](../ucs-x9508-redfish/Overview.md)
- [UCS C210-M6]


get server <>
- identity add redfish enabled True/False and auto-redfish true/false if enabled
- add --redfish option to get redfish details
- add --power and --thermal options that will be only supported when redfish is on
    this is tricky... cause it may depend on the intersight features
- extend psu information if redfish enabled
- add --disable-redfish

get servers
- add R-redfish flag
- add power and thermal flags (?) - note that terminal width will be blocker

set redfish
    <ip|serial|name> - it will select one or more servers

    --disable (by default false)
    --type (detected based on model) or maybe do generic|ucsc|auto and leave default empty
    --username
    --password
    --ip (detected based on model?)
    --validate True/False

    add confirmation
    show servers with redfish specific details only plus what has been defined by the user
    do not overwrite it values are not defined
    validate should run first and only apply settings if validated