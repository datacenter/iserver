from lib import output_helper

from lib.nexus.cdp.output import CdpOutput
from lib.nexus.config.output import ConfigOutput
from lib.nexus.feature.output import FeatureOutput
from lib.nexus.hardware.output import HardwareOutput
from lib.nexus.interface.output import InterfaceOutput
from lib.nexus.lacp.output import LacpOutput
from lib.nexus.lldp.output import LldpOutput
from lib.nexus.mac.output import MacOutput
from lib.nexus.mon.output import MonOutput
from lib.nexus.pc.output import PcOutput
from lib.nexus.version.output import VersionOutput
from lib.nexus.vlan.output import VlanOutput
from lib.nexus.vpc.output import VpcOutput
from lib.nexus.vrf.output import VrfOutput


class NexusOutput(
    CdpOutput,
    ConfigOutput,
    FeatureOutput,
    HardwareOutput,
    InterfaceOutput,
    LacpOutput,
    LldpOutput,
    MacOutput,
    MonOutput,
    PcOutput,
    VersionOutput,
    VlanOutput,
    VpcOutput,
    VrfOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )
        CdpOutput.__init__(self)
        ConfigOutput.__init__(self)
        FeatureOutput.__init__(self)
        HardwareOutput.__init__(self)
        InterfaceOutput.__init__(self)
        LacpOutput.__init__(self)
        LldpOutput.__init__(self)
        MacOutput.__init__(self)
        MonOutput.__init__(self)
        PcOutput.__init__(self)
        VersionOutput.__init__(self)
        VlanOutput.__init__(self)
        VpcOutput.__init__(self)
        VrfOutput.__init__(self)
