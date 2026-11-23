from lib.aci.proto.lacp.bot_output import ProtocolLacpBotOutput
from lib.aci.proto.lldp.bot_output import ProtocolLldpBotOutput


class ProtocolBotOutput(
    ProtocolLacpBotOutput,
    ProtocolLldpBotOutput
    ):
    def __init__(self):
        ProtocolLacpBotOutput.__init__(self)
        ProtocolLldpBotOutput.__init__(self)
