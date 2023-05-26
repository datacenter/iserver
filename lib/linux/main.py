from lib.linux.commands import LinuxCommands
from lib.linux.interface import LinuxInterface
from lib.linux.state import LinuxState

from lib import output_helper
from lib import ssh


class Linux(LinuxCommands, LinuxInterface, LinuxState):
    def __init__(self, ip_address, username, password=None, key_filename=None, verbose=False, debug=False):
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
            debug=debug
        )

        self.management_ip = ip_address
        self.username = username
        self.password = password
        self.key_filename = key_filename
        self.verbose = verbose
        self.debug = debug

        LinuxCommands.__init__(self)
        LinuxInterface.__init__(self)
        LinuxState.__init__(self)
