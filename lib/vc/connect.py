import time
import atexit
import traceback

from pyVim.connect import SmartConnect, Disconnect


class VcConnect():
    def __init__(self, vcenter_ip, vcenter_port, vcenter_username, vcenter_password, disable_ssl_verification=True):
        self.vcenter_ip = vcenter_ip
        self.vcenter_port = vcenter_port
        self.vcenter_username = vcenter_username
        self.vcenter_password = vcenter_password
        self.vc_disable_ssl_verification = disable_ssl_verification

        self.vc_service_instance = None

    def is_vc_connected(self):
        if self.vc_service_instance is None:
            return False
        return True

    def vc_connect(self):
        if self.vc_service_instance is not None:
            return True

        start_time = int(time.time() * 1000)
        try:
            self.vc_service_instance = SmartConnect(
                host=self.vcenter_ip,
                user=self.vcenter_username,
                pwd=self.vcenter_password,
                port=self.vcenter_port,
                disableSslCertValidation=self.vc_disable_ssl_verification
            )

            # doing this means you don't need to remember to disconnect your script/objects
            atexit.register(Disconnect, self.vc_service_instance)

        except IOError as io_error:
            self.my_output.error('Failed to connect to vcenter instance')
            self.my_output.default(io_error)
            return False

        except BaseException:
            self.my_output.error('Failed to connect to vcenter instance')
            self.my_output.default(traceback.format_exc())
            return False

        if self.vc_service_instance is None:
            self.my_output.error('Failed to connect to vcenter instance with supplied credentials')
            return False

        duration = int(time.time() * 1000) - start_time
        self.log.vcenter(
            'connect',
            self.vcenter_ip,
            True,
            duration
        )

        return True
