from lib import log_helper

from lib.imc.command import ImcCommand
from lib.imc.psu import ImcPsu
from lib.imc.redfish import ImcRedfish
from lib.imc.user import ImcUser
from lib.imc.version import ImcVersion


class ImcEndpoint(
        ImcCommand,
        ImcPsu,
        ImcRedfish,
        ImcUser,
        ImcVersion
        ):
    def __init__(self, endpoint_ip, endpoint_port, username, password, log_id=None):
        ImcCommand.__init__(self, endpoint_ip, endpoint_port, username, password, log_id)
        ImcPsu.__init__(self)
        ImcRedfish.__init__(self)
        ImcUser.__init__(self)
        ImcVersion.__init__(self)

        self.log = log_helper.Log(log_id=log_id)
        self.endpoint_ip = endpoint_ip
        self.endpoint_port = endpoint_port
        self.username = username
        self.password = password
