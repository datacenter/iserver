# Provisioning CRD

[[Back]](../../README.md)

`Provisioning` contains configuration used by the Provisioning service (Ironic) to provision baremetal hosts. Provisioning is created by the OpenShift installer using admin or user provided information about the provisioning network and the NIC on the server that can be used to PXE boot it.

This CR is a singleton, created by the installer and currently only consumed by the cluster-baremetal-operator to bring up and update containers in a metal3 cluster.

## Default in assisted installed cluster

Example below for 3-node cluster installed using assisted installation method, `provisioningMacAddresses` from the main interface of every cluster node

```yaml
apiVersion: metal3.io/v1alpha1
kind: Provisioning
metadata:
  name: provisioning-configuration
spec:
  additionalNTPServers:
  - ntp.domain.com
  preProvisioningOSDownloadURLs: {}
  provisioningMacAddresses:
  - aa:aa:aa:aa:aa:aa
  - bb:bb:bb:bb:bb:bb
  - cc:cc:cc:cc:cc:cc
  provisioningNetwork: Disabled
```

## Spec

```yaml
additionalNTPServers:
    description: |-
        AdditionalNTPServers is a list of NTP Servers to be used by the
        provisioning service
    items:
        type: string
    type: array
bootIsoSource:
    description: |-
        BootIsoSource provides a way to set the location where the iso image
        to boot the nodes will be served from.
        By default the boot iso image is cached locally and served from
        the Provisioning service (Ironic) nodes using an auxiliary httpd server.
        If the boot iso image is already served by an httpd server, setting
        this option to http allows to directly provide the image from there;
        in this case, the network (either internal or external) where the
        httpd server that hosts the boot iso is needs to be accessible
        by the metal3 pod.
    enum:
    - local
    - http
    type: string
disableVirtualMediaTLS:
    description: |-
        DisableVirtualMediaTLS turns off TLS on the virtual media server,
        which may be required for hardware that cannot accept HTTPS links.
    type: boolean
externalIPs:
    description: |-
        ExternalIPs are the external-facing IP addresses used to access the Ironic service.
        Most users will not need this set. It is recommended to leave this unset unless
        actually necessary.
    items:
        type: string
    type: array
preProvisioningOSDownloadURLs:
    description: |-
        PreprovisioningOSDownloadURLs is set of CoreOS Live URLs that would be necessary to provision a worker
        either using virtual media or PXE.
    properties:
        initramfsURL:
            description: InitramfsURL Image URL to be used for PXE deployments
            type: string
        isoURL:
            description: IsoURL Image URL to be used for Live ISO deployments
            type: string
        kernelURL:
            description: KernelURL is an Image URL to be used for PXE deployments
            type: string
        rootfsURL:
            description: RootfsURL Image URL to be used for PXE deployments
            type: string
    type: object
prometheusExporter:
    description: |-
        PrometheusExporter configures sensor data collection and Prometheus metrics export.
        When enabled, this configures Ironic to collect sensor data, deploys the
        ironic-prometheus-exporter container, and creates supporting resources
        (ServiceMonitor, Service ports) to expose hardware sensor metrics for Prometheus.
    properties:
        disableDefaultPrometheusRules:
        description: |-
            DisableDefaultPrometheusRules controls whether default hardware health
            alerting rules should NOT be deployed alongside the prometheus exporter.
            When false (default), default prometheus rules are deployed.
        type: boolean
        enabled:
        description: |-
            Enabled controls whether sensor data collection is active.
            When true, configures Ironic to collect sensor data, deploys the
            ironic-prometheus-exporter container, and creates supporting resources.
        type: boolean
        sensorCollectionInterval:
        default: 60
        description: |-
            SensorCollectionInterval defines how often (in seconds) sensor data
            is collected from BMCs using Ironic. Must be at least 60 seconds.
        minimum: 60
        type: integer
    required:
    - enabled
    type: object
provisioningDHCPExternal:
    description: |-
        ProvisioningDHCPExternal indicates whether the DHCP server
        for IP addresses in the provisioning DHCP range is present
        within the metal3 cluster or external to it. This field is being
        deprecated in favor of provisioningNetwork.
    type: boolean
provisioningDHCPRange:
    description: |-
        ProvisioningDHCPRange needs to be interpreted along with
        ProvisioningDHCPExternal. If the value of
        provisioningDHCPExternal is set to False, then
        ProvisioningDHCPRange represents the range of IP addresses
        that the DHCP server running within the metal3 cluster can
        use while provisioning baremetal servers. If the value of
        ProvisioningDHCPExternal is set to True, then the value of
        ProvisioningDHCPRange will be ignored. When the value of
        ProvisioningDHCPExternal is set to False, indicating an
        internal DHCP server and the value of ProvisioningDHCPRange
        is not set, then the DHCP range is taken to be the default
        range which goes from .10 to .100 of the
        ProvisioningNetworkCIDR. This is the only value in all of
        the Provisioning configuration that can be changed after
        the installer has created the CR. This value needs to be
        two comma sererated IP addresses within the
        ProvisioningNetworkCIDR where the 1st address represents
        the start of the range and the 2nd address represents the
        last usable address in the  range.
    type: string
provisioningDNS:
    description: |-
        ProvisioningDNS allows sending the DNS information via DHCP on the
        provisionig network. It is off by default since the Provisioning
        service itself (Ironic) does not require DNS, but it may be useful
        for layered products (e.g. ZTP).
    type: boolean
provisioningIP:
    description: |-
        ProvisioningIP is the IP address assigned to the
        provisioningInterface of the baremetal server. This IP
        address should be within the provisioning subnet, and
        outside of the DHCP range.
    type: string
provisioningInterface:
    description: |-
        ProvisioningInterface is the name of the network interface
        on a baremetal server to the provisioning network. It can
        have values like eth1 or ens3.
    type: string
provisioningMacAddresses:
    description: |-
        ProvisioningMacAddresses is a list of mac addresses of network interfaces
        on a baremetal server to the provisioning network.
        Use this instead of ProvisioningInterface to allow interfaces of different
        names. If not provided it will be populated by the BMH.Spec.BootMacAddress
        of each master.
    items:
        type: string
    type: array
provisioningNetwork:
    description: |-
        ProvisioningNetwork provides a way to indicate the state of the
        underlying network configuration for the provisioning network.
        This field can have one of the following values -
        `Managed`- when the provisioning network is completely managed by
        the Baremetal IPI solution.
        `Unmanaged`- when the provsioning network is present and used but
        the user is responsible for managing DHCP. Virtual media provisioning
        is recommended but PXE is still available if required.
        `Disabled`- when the provisioning network is fully disabled. User can
        bring up the baremetal cluster using virtual media or assisted
        installation. If using metal3 for power management, BMCs must be
        accessible from the machine networks. User should provide two IPs on
        the external network that would be used for provisioning services.
    enum:
    - Managed
    - Unmanaged
    - Disabled
    type: string
provisioningNetworkCIDR:
    description: |-
        ProvisioningNetworkCIDR is the network on which the
        baremetal nodes are provisioned. The provisioningIP and the
        IPs in the dhcpRange all come from within this network. When using IPv6
        and in a network managed by the Baremetal IPI solution this cannot be a
        network larger than a /64.
    type: string
provisioningNetworkGateway:
    description: |-
        ProvisioningNetworkGateway is the IP address of the default gateway
        for the provisioning network. This gateway is provided to baremetal
        hosts via DHCP to enable routing to external networks during
        inspection and provisioning. This field is optional and only
        used when ProvisioningNetwork is set to Managed. The gateway IP
        must be within the ProvisioningNetworkCIDR but outside of the
        ProvisioningDHCPRange and must not be the same as ProvisioningIP.
    type: string
provisioningOSDownloadURL:
    description: |-
        ProvisioningOSDownloadURL is the location from which the OS
        Image used to boot baremetal host machines can be downloaded
        by the metal3 cluster.
    type: string
unsupportedConfigOverrides:
    description: |-
        UnsupportedConfigOverrides are site-specific overrides that are not
        officially supported in the Metal platform and may cause the
        deployment to fail. Carefully check the description of each field
        you modify to understand its implications for stability and
        upgradability of your cluster.
        When reporting a bug, please make sure to reproduce it with
        UnsupportedConfigOverrides set to nil.
    properties:
        ironicAgentImage:
        description: |-
            Override for the IPA container image.
            The image must be based on openshift/ironic-agent-image of the same
            release as the cluster. After each cluster upgrade, it must be
            rebased and updated immediately, before any BareMetalHosts are
            enrolled, provisioned or deprovisioned.
        type: string
    type: object
virtualMediaViaExternalNetwork:
    description: |-
        VirtualMediaViaExternalNetwork flag when set to "true" allows for workers
        to boot via Virtual Media and contact metal3 over the External Network.
        When the flag is set to "false" (which is the default), virtual media
        deployments can still happen based on the configuration specified in the
        ProvisioningNetwork i.e when in Disabled mode, over the External Network
        and over Provisioning Network when in Managed mode.
        PXE deployments will always use the Provisioning Network and will not be
        affected by this flag.
    type: boolean
watchAllNamespaces:
    description: |-
        WatchAllNamespaces provides a way to explicitly allow use of this
        Provisioning configuration across all Namespaces. It is an
        optional configuration which defaults to false and in that state
        will be used to provision baremetal hosts in only the
        openshift-machine-api namespace. When set to true, this provisioning
        configuration would be used for baremetal hosts across all namespaces.
    type: boolean
```

## Example

```yaml
apiVersion: metal3.io/v1alpha1
kind: Provisioning
metadata:
  name: provisioning-configuration
spec:
  provisioningIP: 172.18.198.35
  provisioningInterface: br-ex
  provisioningNetwork: Unmanaged
  provisioningNetworkCIDR: 172.18.198.0/24
  disableVirtualMediaTLS: false
  virtualMediaViaExternalNetwork: false
```

Notes:
- `provisioningIP` is unused IP address in `provisioningNetworkCIDR` to hand off ISO image for Ironic
- `provisioningNetwork: Unmanaged` means an external DHCP server is responsible for leasing IPs
- `provisioningNetworkCIDR` is still required for network context validation, even if externally managed

[[Back]](../../README.md)