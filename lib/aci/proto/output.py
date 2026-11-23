from lib.aci.proto.arp.output import ProtocolArpOutput
from lib.aci.proto.bfd.output import ProtocolBfdOutput
from lib.aci.proto.bgp.output import ProtocolBgpOutput
from lib.aci.proto.cdp.output import ProtocolCdpOutput
from lib.aci.proto.hsrp.output import ProtocolHsrpOutput
from lib.aci.proto.ipv4.output import ProtocolIpv4Output
from lib.aci.proto.ipv6.output import ProtocolIpv6Output
from lib.aci.proto.isis.output import ProtocolIsisOutput
from lib.aci.proto.lacp.output import ProtocolLacpOutput
from lib.aci.proto.lldp.output import ProtocolLldpOutput
from lib.aci.proto.nd.output import ProtocolNdOutput


class ProtocolOutput(
    ProtocolArpOutput,
    ProtocolBfdOutput,
    ProtocolBgpOutput,
    ProtocolCdpOutput,
    ProtocolHsrpOutput,
    ProtocolIpv4Output,
    ProtocolIpv6Output,
    ProtocolIsisOutput,
    ProtocolLacpOutput,
    ProtocolLldpOutput,
    ProtocolNdOutput
    ):
    def __init__(self):
        ProtocolArpOutput.__init__(self)
        ProtocolBfdOutput.__init__(self)
        ProtocolBgpOutput.__init__(self)
        ProtocolCdpOutput.__init__(self)
        ProtocolHsrpOutput.__init__(self)
        ProtocolIpv4Output.__init__(self)
        ProtocolIpv6Output.__init__(self)
        ProtocolIsisOutput.__init__(self)
        ProtocolLacpOutput.__init__(self)
        ProtocolLldpOutput.__init__(self)
        ProtocolNdOutput.__init__(self)
