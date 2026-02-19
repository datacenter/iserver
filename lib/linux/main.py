from lib.linux.bond.main import LinuxBond
from lib.linux.boot.main import LinuxBoot
from lib.linux.chrony.main import LinuxChrony
from lib.linux.container_policy.main import LinuxContainerPolicy
from lib.linux.commands import LinuxCommands
from lib.linux.crictl.main import LinuxCrictl
from lib.linux.genisoimage.main import LinuxGenIsoImage
from lib.linux.huge_pages.main import LinuxHugePages
from lib.linux.interface import LinuxInterface
from lib.linux.lsblk.main import LinuxLsblk
from lib.linux.lv.main import LinuxLv
from lib.linux.lvm import LinuxLvm
from lib.linux.pv.main import LinuxPv
from lib.linux.state import LinuxState
from lib.linux.sysctl.main import LinuxSysctl
from lib.linux.vg.main import LinuxVg
from lib.linux.virtctl.main import LinuxVirtctl
from lib.linux.cache import Cache
from lib.linux.common import Common

from lib import output_helper
from lib import log_helper
from lib import ssh
from lib.ocp import main as ocp


class Linux(
        Cache,
        Common,
        LinuxBond,
        LinuxBoot,
        LinuxChrony,
        LinuxContainerPolicy,
        LinuxCommands,
        LinuxCrictl,
        LinuxGenIsoImage,
        LinuxHugePages,
        LinuxInterface,
        LinuxLsblk,
        LinuxLv,
        LinuxLvm,
        LinuxPv,
        LinuxState,
        LinuxSysctl,
        LinuxVg,
        LinuxVirtctl
        ):
    def __init__(
            self, 
            ip_address, 
            username, 
            password=None, 
            key_filename=None, 
            server_name=None, 
            ocp_cluster_name=None,
            ocp_node_name=None,
            no_cache=False, 
            verbose=False, 
            debug=False, 
            log_id=None
        ):
        self.log = log_helper.Log(log_id=log_id)
        self.log_id = log_id

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

        self.ocp_cluster_name = ocp_cluster_name
        self.ocp_node_name = ocp_node_name
        self.ocp_handler = None

        Cache.__init__(self, server_name, no_cache=no_cache)
        Common.__init__(self)
        LinuxBond.__init__(self)
        LinuxBoot.__init__(self)
        LinuxChrony.__init__(self)
        LinuxContainerPolicy.__init__(self)
        LinuxCommands.__init__(self)
        LinuxCrictl.__init__(self)
        LinuxGenIsoImage.__init__(self)
        LinuxHugePages.__init__(self)
        LinuxInterface.__init__(self)
        LinuxLsblk.__init__(self)
        LinuxLv.__init__(self)
        LinuxLvm.__init__(self)
        LinuxPv.__init__(self)
        LinuxState.__init__(self)
        LinuxSysctl.__init__(self)
        LinuxVg.__init__(self)
        LinuxVirtctl.__init__(self)

    def get_ocp_handler(self):
        if self.ocp_cluster_name is None:
            return None
        
        if self.ocp_handler is None:
            self.ocp_handler = ocp.Ocp(
                self.ocp_cluster_name,
                verbose=False,
                debug=False,
                log_id=self.log_id
            )

        return self.ocp_handler
