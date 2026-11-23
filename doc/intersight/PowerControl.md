# Power control

Group of 'set power' commands allow controlling power state of the servers
- Select the servers using the command options incl. group
- Rack and standalone servers supported only
- Some power tasks expect the server to be in proper state e.g. power cycle fails on servers in powered off state. Task execution logic will give you notification and such servers can be automitacally removed from the target list of servers
- Use --confirm option for explicit user confirmation
- Use --dry-run to check the isctl command without execution
- Use --verbose to get more details

Intent | Command | Documentation
--- | --- | ---
Power on | iserver set power on | [examples](PowerOn.md)
Power off | iserver set power off | [examples](PowerOff.md)
Power cycle | iserver set power cycle | [examples](PowerCycle.md)
Hard reset | iserver set power hard | [examples](PowerHard.md)
OS shutdown | iserver set power shut | [examples](PowerShut.md)
CIMC reboot | iserver set power reboot | [examples](PowerReboot.md)
