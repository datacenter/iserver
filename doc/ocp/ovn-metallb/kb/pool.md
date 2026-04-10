# MetalLB - IP address pool

[[Back]](../README.md) [[iserver-way]](../create_pool.md)

IP addresses pool is used whe a service of type LoadBalancer needs an IP address allocation.

An `IPAddressPool` includes a list of IP addresses i.e.
- a single IP address that is set using a range, such as 1.1.1.1-1.1.1.1, 
- a range specified in CIDR notation, 
- a range specified as a starting and ending address separated by a hyphen, 
- a combination of the three.

## CRD Example

```
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  namespace: metallb-system
  name: pool1
spec:
  addresses:
  - 69.69.69.1-69.69.69.254
```

## Status

```
status:
  assignedIPv4: 1
  assignedIPv6: 0
  availableIPv4: 253
  availableIPv6: 0
```

[[Back]](../README.md) [[iserver-way]](../create_pool.md)