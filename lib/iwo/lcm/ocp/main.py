from lib.ocp import settings as ocp_settings

from lib.iwo.lcm.ocp.get import IwoOcpGetLcm
from lib.iwo.lcm.ocp.template import IwoOcpTemplateLcm
from lib.iwo.lcm.ocp.create import IwoOcpCreateLcm
from lib.iwo.lcm.ocp.delete import IwoOcpDeleteLcm


class IwoOcpLcm(IwoOcpTemplateLcm, IwoOcpGetLcm, IwoOcpCreateLcm, IwoOcpDeleteLcm):
    def __init__(self):
        IwoOcpGetLcm.__init__(self)
        IwoOcpTemplateLcm.__init__(self)
        IwoOcpCreateLcm.__init__(self)
        IwoOcpDeleteLcm.__init__(self)

        self.ocp_settings_handler = ocp_settings.OcpSettings(log_id=self.log_id)
