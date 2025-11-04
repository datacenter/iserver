# Domain

iserver can interact with various controllers and devices as long as it has IP access to run REST API. At the same time, some devices, controllers may be physically separated or under different management entity. There may be no linkage between them, neither physical, nor logical.

Domain allows grouping of different resources into management domains. 

As an example there are two locations:

Site A:
- openshift clusters: bm10, bm11
- APIC: apic1

Site B:
- openshift cluster: bm20, bm22
- APIC: apic2

Suppose you want to discover network connectivity of openshift cluster bm10 into aci domain. Due to physical and administrative boundaries, it makes no sense to check anything in apic2. 

Adding domain attribute to openshift cluster and apic e.g. site-a and site-b, can be then leveraged by day2 operation workflows.

[[Back]](./Operations.md)