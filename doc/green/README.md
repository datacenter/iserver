# Power and Thermal Monitoring

Power and thermal data is collected using the combination of Intersight, Redfish and UCSM APIs
- Intersight keeps the inventory of all servers
- Integration with [Redfish](../redfish/Integration.md) used to get power and thermal data
- Integration with [UCSM](../ucsm/Integration.md) used to get power and thermal data

Requirement
- one-time [Redfish configuration](../redfish/AccessConfiguration.md)
- one-time [UCSM configuration](../ucsm/AccessConfiguration.md)

Once integration between Intersight inventory and Redfish/UCSM is configured, user does not need to know how the data is collected.

Servers (mix of Redfish and USCM)
- [power](./IntegrationServersPower.md)
- [thermal](./IntegrationServersThermal.md)
- [power and thermal](./IntegrationServersEnv.md)

Redfish Server
- [power](../redfish/IntegrationServerPower.md)
- [thermal](../redfish/IntegrationServerThermal.md)
- [power and thermal](../redfish/IntegrationServerEnv.md)

UCSM Server
- [power](../ucsm/IntegrationServerPower.md)
- [thermal](../ucsm/IntegrationServerThermal.md)
- [power and thermal](../ucsm/IntegrationServerEnv.md)
