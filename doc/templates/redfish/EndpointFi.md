# Fabric Interconnect Redfish Endpoint Type

Fabric Interconnect (--type fi) endpoint allows getting Redfish information from the Chassis and FI-Attached server.

Redfish API calls are executed on Fabric Interconnect for all devices connected to it.

Fabric Interconnect connected devices support [template](./TemplateFi.md).

## Step 1: List of inventory

The first step is getting the list of inventory connected to FI i.e. chassis and servers.

```
DOC_TEMPLATE:get_redfish_endpoint_fi_inventory.basic:iserver.output.default
```

## Step 2a: Chassis

Use Inventory Type and Inventory Id from the inventory list above to run Redfish calls on specific Chassis

```
DOC_TEMPLATE:get_redfish_endpoint_fi_chassis.basic:iserver.output.default
```

## Step 2b: FI-Attached Server

Use Inventory Type and Inventory Id from the inventory list to run Redfish calls on specific Server

```
DOC_TEMPLATE:get_redfish_endpoint_fi_server.basic:iserver.output.default
```
