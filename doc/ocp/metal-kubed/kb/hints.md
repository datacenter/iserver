#

## Automatic power off

It is possible that BMO will power off the server via Redfish, even if the host is no longer defined as `BareMetalHost` object. Delete `metal3` pod in such case and let deployment to recreate it.