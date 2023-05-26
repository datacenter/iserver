from lib.ocp.lcm.vsphere.ipi.main import OcpVsphereIpi
from lib.ocp.lcm.vsphere.validate import OcpVsphereValidate

from lib.vc import vcenter


class OcpVsphere(OcpVsphereValidate, OcpVsphereIpi):
    def __init__(self):
        OcpVsphereValidate.__init__(self)
        OcpVsphereIpi.__init__(self)
        self.vcenter_handler = None

    def is_vcenter_connected(self):
        if self.vcenter_handler is None:
            return False
        return self.vcenter_handler.is_vc_connected()

    def vcenter_connect(self, vcenter_parameters):
        if self.vcenter_handler is None:
            self.vcenter_handler = vcenter.Vcenter(
                vcenter_parameters['name'],
                vcenter_parameters['username'],
                vcenter_parameters['password'],
                port=vcenter_parameters['port'],
                verbose=self.verbose,
                debug=self.debug,
                log_id=self.log_id
            )

        return self.is_vcenter_connected()
