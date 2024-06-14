from lib.linux.bond.main import LinuxBond
from lib.linux.boot.main import LinuxBoot
from lib.linux.chrony.main import LinuxChrony
from lib.linux.container_policy.main import LinuxContainerPolicy
from lib.linux.commands import LinuxCommands
from lib.linux.genisoimage.main import LinuxGenIsoImage
from lib.linux.huge_pages.main import LinuxHugePages
from lib.linux.interface import LinuxInterface
from lib.linux.lvm import LinuxLvm
from lib.linux.state import LinuxState
from lib.linux.sysctl.main import LinuxSysctl
from lib.linux.virtctl.main import LinuxVirtctl
from lib.linux.cache import Cache
from lib.linux.common import Common

from lib import output_helper
from lib import log_helper
from lib import ssh


class Linux(
        Cache,
        Common,
        LinuxBond,
        LinuxBoot,
        LinuxChrony,
        LinuxContainerPolicy,
        LinuxCommands,
        LinuxGenIsoImage,
        LinuxHugePages,
        LinuxInterface,
        LinuxLvm,
        LinuxState,
        LinuxSysctl,
        LinuxVirtctl
        ):
    def __init__(self, ip_address, username, password=None, key_filename=None, server_name=None, no_cache=False, verbose=False, debug=False, log_id=None):
        self.log = log_helper.Log(log_id=log_id)
        self.my_output = output_helper.OutputHelper(
            verbose=verbose,
            debug=debug
        )

        self.ssh_handler = ssh.Ssh(
            ip_address,
            username,
            password=password,
            key_filename=key_filename,
            verbose=verbose,
            debug=debug,
            log_id=log_id
        )

        self.server_name = server_name
        self.management_ip = ip_address
        if server_name is None:
            self.server_display_name = ip_address
        else:
            self.server_display_name = server_name

        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.verbose = verbose
        self.debug = debug

        Cache.__init__(self, server_name, no_cache=no_cache)
        Common.__init__(self)
        LinuxBond.__init__(self)
        LinuxBoot.__init__(self)
        LinuxChrony.__init__(self)
        LinuxContainerPolicy.__init__(self)
        LinuxCommands.__init__(self)
        LinuxGenIsoImage.__init__(self)
        LinuxHugePages.__init__(self)
        LinuxInterface.__init__(self)
        LinuxLvm.__init__(self)
        LinuxState.__init__(self)
        LinuxSysctl.__init__(self)
        LinuxVirtctl.__init__(self)
