# RunIt - Extra configuration

[[Back]](../BareMetalCluster.md) [[Next]](./example_wait.md) [[Prev]](./example_boot.md)

Workflow
- change hostnames
- update role
- set ntp server
- define api and ingress vip

```
Change hostnames and roles
- Server [10.20.20.10] hostname [bm1-1] role [auto-assign]
- Server [10.20.20.11] hostname [bm1-2] role [auto-assign]
- Server [10.20.20.12] hostname [bm1-3] role [auto-assign]
REST API successful
Update ntp [ntp.domain.com]
REST API successful
Update api 10.10.10.100 and ingress vip 10.10.10.101
REST API successful
```

[[Back]](../BareMetalCluster.md) [[Next]](./example_wait.md) [[Prev]](./example_boot.md)