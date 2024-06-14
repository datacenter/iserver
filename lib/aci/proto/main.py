from lib.aci.proto.arp.main import ProtocolArp
from lib.aci.proto.bfd.main import ProtocolBfd
from lib.aci.proto.bgp.main import ProtocolBgp
from lib.aci.proto.cdp.main import ProtocolCdp
from lib.aci.proto.hsrp.main import ProtocolHsrp
from lib.aci.proto.ipv4.main import ProtocolIpv4
from lib.aci.proto.ipv6.main import ProtocolIpv6
from lib.aci.proto.isis.main import ProtocolIsis
from lib.aci.proto.lacp.main import ProtocolLacp
from lib.aci.proto.lldp.main import ProtocolLldp
from lib.aci.proto.nd.main import ProtocolNd


class Protocol(
    ProtocolArp,
    ProtocolBfd,
    ProtocolBgp,
    ProtocolCdp,
    ProtocolHsrp,
    ProtocolIpv4,
    ProtocolIpv6,
    ProtocolIsis,
    ProtocolLacp,
    ProtocolLldp,
    ProtocolNd
    ):
    def __init__(self):
        ProtocolArp.__init__(self)
        ProtocolBfd.__init__(self)
        ProtocolBgp.__init__(self)
        ProtocolCdp.__init__(self)
        ProtocolHsrp.__init__(self)
        ProtocolIpv4.__init__(self)
        ProtocolIpv6.__init__(self)
        ProtocolIsis.__init__(self)
        ProtocolLacp.__init__(self)
        ProtocolLldp.__init__(self)
        ProtocolNd.__init__(self)

        self.protocols = [
            'arp',
            'bfd',
            'bgp',
            'cdp',
            'hsrp',
            'ipv4',
            'ipv6',
            'isis',
            'lacp',
            'lldp',
            'nd'
        ]
