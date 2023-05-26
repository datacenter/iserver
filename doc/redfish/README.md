# Redfish support

iserver supports Redfish (GET) API that can be executed on supported Redfish endpoint
- [Standard Redfish Endpoint](./EndpointStandard.md)
- [UCS Rack Standalone](./EndpointUcsc.md)
- [FI-Attached Chassis](./EndpointFi.md)
- [FI-Attached Server](./EndpointFi.md)
- [Dell](./EndpointDell.md)
- [HPE](./EndpointHpe.md)

Notes:
- Redfish API call runs directly on user defined endpoint with provided authentication details
- For Intersight managed servers you can benefit from [integration](./Integration.md) feature

## Features

- [Get resource](./Resource.md)
- [Get selected properties of resource](./Property.md)
- [Get Oem extensions](./Oem.md)
- [Get Actions](./Action.md)
- [Find property by key](./Key.md)
- [Find property by value](./Value.md)
- [Discover resource references](./Children.md)
- [Get resource description](./Description.md)
- [Get predefined set of properties (template)](./Template.md)

## Tested endpoints

Vendor | Model | Endpoint type | Redfish Resources Tree | Oem | Actions | Identity | Power | Thermal
--- | --- | --- | --- | --- | --- | --- | --- | ---
Cisco | UCSC-C220-M4S | [ucsc](./EndpointUcsc.md) | [link](../redfish-tests-cisco-ucsc-c220-m4s/Resource.md) | [link](../redfish-tests-cisco-ucsc-c220-m4s/Oem.md) | [link](../redfish-tests-cisco-ucsc-c220-m4s/Action.md) | [link](../redfish-tests-cisco-ucsc-c220-m4s/Identity.md) | [link](../redfish-tests-cisco-ucsc-c220-m4s/Power.md) | [link](../redfish-tests-cisco-ucsc-c220-m4s/Thermal.md)
Cisco | UCSC-C220-M5SX | [ucsc](./EndpointUcsc.md) | [link](../redfish-tests-cisco-ucsc-c220-m5sx/Resource.md) | [link](../redfish-tests-cisco-ucsc-c220-m5sx/Oem.md) | [link](../redfish-tests-cisco-ucsc-c220-m5sx/Action.md) | [link](../redfish-tests-cisco-ucsc-c220-m5sx/Identity.md) | [link](../redfish-tests-cisco-ucsc-c220-m5sx/Power.md) | [link](../redfish-tests-cisco-ucsc-c220-m5sx/Thermal.md)
Cisco | UCSC-C220-M6N | [ucsc](./EndpointUcsc.md) | [link](../redfish-tests-cisco-ucsc-c220-m6n/Resource.md) | [link](../redfish-tests-cisco-ucsc-c220-m6n/Oem.md) | [link](../redfish-tests-cisco-ucsc-c220-m6n/Action.md) | [link](../redfish-tests-cisco-ucsc-c220-m6n/Identity.md) | [link](../redfish-tests-cisco-ucsc-c220-m6n/Power.md) | [link](../redfish-tests-cisco-ucsc-c220-m6n/Thermal.md)
Cisco | UCSC-C225-M6S | [ucsc](./EndpointUcsc.md) | [link](../redfish-tests-cisco-ucsc-c225-m6s/Resource.md) | [link](../redfish-tests-cisco-ucsc-c225-m6s/Oem.md) | [link](../redfish-tests-cisco-ucsc-c225-m6s/Action.md) | [link](../redfish-tests-cisco-ucsc-c225-m6s/Identity.md) | [link](../redfish-tests-cisco-ucsc-c225-m6s/Power.md) | [link](../redfish-tests-cisco-ucsc-c225-m6s/Thermal.md)
Cisco | UCSC-C240-M4SX | [ucsc](./EndpointUcsc.md) | [link](../redfish-tests-cisco-ucsc-c240-m4sx/Resource.md) | [link](../redfish-tests-cisco-ucsc-c240-m4sx/Oem.md) | [link](../redfish-tests-cisco-ucsc-c240-m4sx/Action.md) | [link](../redfish-tests-cisco-ucsc-c240-m4sx/Identity.md) | [link](../redfish-tests-cisco-ucsc-c240-m4sx/Power.md) | [link](../redfish-tests-cisco-ucsc-c240-m4sx/Thermal.md)
Cisco | UCSC-C240-M5SN | [ucsc](./EndpointUcsc.md) | [link](../redfish-tests-cisco-ucsc-c240-m5sn/Resource.md) | [link](../redfish-tests-cisco-ucsc-c240-m5sn/Oem.md) | [link](../redfish-tests-cisco-ucsc-c240-m5sn/Action.md) | [link](../redfish-tests-cisco-ucsc-c240-m5sn/Identity.md) | [link](../redfish-tests-cisco-ucsc-c240-m5sn/Power.md) | [link](../redfish-tests-cisco-ucsc-c240-m5sn/Thermal.md)
Cisco | UCSC-C240-M5SX | [ucsc](./EndpointUcsc.md) | [link](../redfish-tests-cisco-ucsc-c240-m5sx/Resource.md) | [link](../redfish-tests-cisco-ucsc-c240-m5sx/Oem.md) | [link](../redfish-tests-cisco-ucsc-c240-m5sx/Action.md) | [link](../redfish-tests-cisco-ucsc-c240-m5sx/Identity.md) | [link](../redfish-tests-cisco-ucsc-c240-m5sx/Power.md) | [link](../redfish-tests-cisco-ucsc-c240-m5sx/Thermal.md)
Cisco | UCSS-S3260 | [ucsc](./EndpointUcsc.md) | [link](../redfish-tests-cisco-ucss-s3260/Resource.md) | [link](../redfish-tests-cisco-ucss-s3260/Oem.md) | [link](../redfish-tests-cisco-ucss-s3260/Action.md) | [link](../redfish-tests-cisco-ucss-s3260/Identity.md) | [link](../redfish-tests-cisco-ucss-s3260/Power.md) | [link](../redfish-tests-cisco-ucss-s3260/Thermal.md)
Cisco | UCSX-210C-M6 | [fi](./EndpointFi.md) | [link](../redfish-tests-cisco-ucsx-210c-m6/Resource.md) | [link](../redfish-tests-cisco-ucsx-210c-m6/Oem.md) | [link](../redfish-tests-cisco-ucsx-210c-m6/Action.md) | [link](../redfish-tests-cisco-ucsx-210c-m6/Identity.md) | [link](../redfish-tests-cisco-ucsx-210c-m6/Power.md) | [link](../redfish-tests-cisco-ucsx-210c-m6/Thermal.md)
Cisco | UCSX-9508 | [fi](./EndpointFi.md) | [link](../redfish-tests-cisco-ucsx-9508/Resource.md) | [link](../redfish-tests-cisco-ucsx-9508/Oem.md) | [link](../redfish-tests-cisco-ucsx-9508/Action.md) | [link](../redfish-tests-cisco-ucsx-9508/Identity.md) | [link](../redfish-tests-cisco-ucsx-9508/Power.md) | [link](../redfish-tests-cisco-ucsx-9508/Thermal.md)
Dell | vServer | [dell](./EndpointDell.md) | [link](../redfish-tests-dell-vserver/Resource.md) | [link](../redfish-tests-dell-vserver/Oem.md) | [link](../redfish-tests-dell-vserver/Action.md) | [link](../redfish-tests-dell-vserver/Identity.md) | [link](../redfish-tests-dell-vserver/Power.md) | [link](../redfish-tests-dell-vserver/Thermal.md)
HPE | vServer | [hpe](./EndpointHpe.md) | [link](../redfish-tests-hpe-vserver/Resource.md) | [link](../redfish-tests-hpe-vserver/Oem.md) | [link](../redfish-tests-hpe-vserver/Action.md) | [link](../redfish-tests-hpe-vserver/Identity.md) | [link](../redfish-tests-hpe-vserver/Power.md) | [link](../redfish-tests-hpe-vserver/Thermal.md)


Note: vServer implemented with [redfish simulator](https://github.com/michzimm/redfish_simgen)