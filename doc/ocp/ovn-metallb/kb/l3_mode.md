# MetalLB - L3 Mode

[[Back]](../README.md)

## Announcement

MetalLB in L3 BGP mode advertises load balancer IP addresses to BGP peers from each speaker pod. The router sends traffic to one of the nodes, so load is distributed across nodes and the router switches to another node when one becomes unavailable.

## Traffic forwarding

After traffic enters the node, the service proxy for the CNI network plugin distributes the traffic to all the pods for the service.

## Failover 

If a node becomes unavailable, the router initiates a new connection with another node that has a speaker pod that advertises the load balancer IP address.

[[Back]](../README.md)