# Get resource properties

Redfish resource properties can be (long) list of JSON properties. If you want limited output with only few properties then you can add multiple --property parameters.

Note: iserver returns properties in JSON format so you can pipe the outcome of iserver command with iq or any other JSON parser tool to select the required properties if that's what you prefer.

## Get selected key system

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --property HostName
    --property Model
    --property Id

/redfish/v1/Systems/WZP23400AK4
-------------------------------
{
    "HostName": "aio-2-p2b-eu-spdc-WZP23400AK4",
    "Model": "UCSC-C240-M5SN",
    "Id": "WZP23400AK4"
}
```

## Get JSON subfields

If selected property is not top level one, use dot notation.

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --property ProcessorSummary.Model
    --property ProcessorSummary.Count

/redfish/v1/Systems/WZP23400AK4
-------------------------------
{
    "ProcessorSummary.Model": "Intel(R) Xeon(R) Gold 6248 CPU @ 2.50GHz",
    "ProcessorSummary.Count": 2
}
```

If property key name contains the dot itself then follow the example for the correct command execution syntax

```
# iserver get redfish endpoint
    --type ucsc
    --ip 10.58.50.42
    --username admin
    --password ******
    --uri Systems/SYSTEM_ID
    --property "Actions.'#ComputerSystem.Reset'.'ResetType@Redfish.AllowableValues'"

/redfish/v1/Systems/WZP23400AK4
-------------------------------
{
    "Actions.'#ComputerSystem.Reset'.'ResetType@Redfish.AllowableValues'": [
        "On",
        "ForceOff",
        "GracefulShutdown",
        "GracefulRestart",
        "ForceRestart",
        "Nmi",
        "PowerCycle"
    ]
}
```
