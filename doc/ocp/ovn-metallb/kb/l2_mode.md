# MetalLB - L2 Mode

[[Back]](../README.md)

> [!CAUTION]
> L2 Mode implements failover mechanism rather than load balancing mechanism

## Announcement

Once the controller allocates an IP address for the service, the speaker pods use an algorithm to determine which speaker pod on which node will announce the load balancer IP address. The algorithm involves hashing the node name and the load balancer IP address. The speaker uses **Address Resolution Protocol (ARP)** to announce IPv4 addresses and **Neighbor Discovery Protocol (NDP)** to announce IPv6 addresses.

## Traffic forwarding

Since single speaker/node advertises the load balancer IP address,  all traffic for a service IP address is routed through one node. After traffic enters the node, the service proxy for the CNI network provider distributes the traffic to all the pods for the service.

There is **no load balancing** in L2 mode.

## Failover 

Failover to another node is automatic when the node becomes unavailable. The speaker pods on the other nodes detect that a node is unavailable and a new speaker pod and node take ownership of the service IP address from the failed node.

[[Back]](../README.md)