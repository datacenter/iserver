# Metal Kubed - Server operational state

[[Back]](../README.md)

`BareMetalHost` resource shows overal state of the host in `status.operationalStatus`

State | Details
--- | ---
OK | the host is healthy and operational
discovered | the host is known to Metal3 but lacks the required information for the normal operation and needs [registration](./register.md)
error | error has occurred, see the status.errorType and status.errorMessage fields for details
delayed | cannot proceed with the provisioning because the maximum number of the hosts in the given state has been reached
detached | the host is [detached](./detach.md), no provisioning actions are possible

Refer to details in [official documentation](https://book.metal3.io/bmo/state_machine.html).

[[Back]](../README.md)