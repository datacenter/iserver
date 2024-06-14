from lib import log_helper

from lib.imc.cli.cache import ImcCliCache
from lib.imc.cli.command import ImcCliCommand

from lib.imc.cli.adapter.main import ImcCliAdapter
from lib.imc.cli.admin.main import ImcCliAdmin
from lib.imc.cli.bbu.main import ImcCliBbu
from lib.imc.cli.bios.main import ImcCliBios
from lib.imc.cli.boot.main import ImcCliBoot
from lib.imc.cli.chassis.main import ImcCliChassis
from lib.imc.cli.cpu.main import ImcCliCpu
from lib.imc.cli.dimm.main import ImcCliDimm
from lib.imc.cli.fault.main import ImcCliFault
from lib.imc.cli.flex.main import ImcCliFlex
from lib.imc.cli.fw.main import ImcCliFw
from lib.imc.cli.hardware.main import ImcCliHardware
from lib.imc.cli.hdd.main import ImcCliHdd
from lib.imc.cli.http.main import ImcCliHttp
from lib.imc.cli.ip.main import ImcCliIp
from lib.imc.cli.ipmi.main import ImcCliIpmi
from lib.imc.cli.kvm.main import ImcCliKvm
from lib.imc.cli.led.main import ImcCliLed
from lib.imc.cli.memory.main import ImcCliMemory
from lib.imc.cli.net.main import ImcCliNet
from lib.imc.cli.ntp.main import ImcCliNtp
from lib.imc.cli.pci.main import ImcCliPci
from lib.imc.cli.psu.main import ImcCliPsu
from lib.imc.cli.redfish.main import ImcCliRedfish
from lib.imc.cli.sel.main import ImcCliSel
from lib.imc.cli.sensor.main import ImcCliSensor
from lib.imc.cli.smtp.main import ImcCliSmtp
from lib.imc.cli.snmp.main import ImcCliSnmp
from lib.imc.cli.sol.main import ImcCliSol
from lib.imc.cli.ssh.main import ImcCliSsh
from lib.imc.cli.storageadapter.main import ImcCliStorageAdapter
from lib.imc.cli.syslog.main import ImcCliSyslog
from lib.imc.cli.tpm.main import ImcCliTpm
from lib.imc.cli.user import ImcCliUser
from lib.imc.cli.utilization.main import ImcCliUtilization
from lib.imc.cli.version.main import ImcCliVersion
from lib.imc.cli.vmedia.main import ImcCliVmedia
from lib.imc.cli.xml.main import ImcCliXml


class ImcCliEndpoint(
        ImcCliCache,
        ImcCliCommand,
        ImcCliAdapter,
        ImcCliAdmin,
        ImcCliBbu,
        ImcCliBios,
        ImcCliBoot,
        ImcCliChassis,
        ImcCliCpu,
        ImcCliDimm,
        ImcCliFault,
        ImcCliFlex,
        ImcCliFw,
        ImcCliHardware,
        ImcCliHdd,
        ImcCliHttp,
        ImcCliIp,
        ImcCliIpmi,
        ImcCliKvm,
        ImcCliLed,
        ImcCliMemory,
        ImcCliNet,
        ImcCliNtp,
        ImcCliPci,
        ImcCliPsu,
        ImcCliRedfish,
        ImcCliSel,
        ImcCliSensor,
        ImcCliSmtp,
        ImcCliSnmp,
        ImcCliSol,
        ImcCliSsh,
        ImcCliStorageAdapter,
        ImcCliSyslog,
        ImcCliTpm,
        ImcCliUser,
        ImcCliUtilization,
        ImcCliVersion,
        ImcCliVmedia,
        ImcCliXml
        ):
    def __init__(self, endpoint_ip, endpoint_port, username, password, cache_ttl=600, log_id=None):
        ImcCliCache.__init__(self, endpoint_ip, cache_ttl, log_id=log_id)
        ImcCliCommand.__init__(self, endpoint_ip, endpoint_port, username, password, log_id)

        ImcCliAdapter.__init__(self)
        ImcCliAdmin.__init__(self)
        ImcCliBbu.__init__(self)
        ImcCliBios.__init__(self)
        ImcCliBoot.__init__(self)
        ImcCliChassis.__init__(self)
        ImcCliCpu.__init__(self)
        ImcCliDimm.__init__(self)
        ImcCliFault.__init__(self)
        ImcCliFlex.__init__(self)
        ImcCliFw.__init__(self)
        ImcCliHardware.__init__(self)
        ImcCliHdd.__init__(self)
        ImcCliHttp.__init__(self)
        ImcCliIp.__init__(self)
        ImcCliIpmi.__init__(self)
        ImcCliKvm.__init__(self)
        ImcCliLed.__init__(self)
        ImcCliMemory.__init__(self)
        ImcCliNet.__init__(self)
        ImcCliNtp.__init__(self)
        ImcCliPci.__init__(self)
        ImcCliPsu.__init__(self)
        ImcCliRedfish.__init__(self)
        ImcCliSel.__init__(self)
        ImcCliSensor.__init__(self)
        ImcCliSmtp.__init__(self)
        ImcCliSnmp.__init__(self)
        ImcCliSol.__init__(self)
        ImcCliSsh.__init__(self)
        ImcCliStorageAdapter.__init__(self)
        ImcCliSyslog.__init__(self)
        ImcCliTpm.__init__(self)
        ImcCliUser.__init__(self)
        ImcCliUtilization.__init__(self)
        ImcCliVersion.__init__(self)
        ImcCliVmedia.__init__(self)
        ImcCliXml.__init__(self)

        self.log = log_helper.Log(log_id=log_id)
        self.endpoint_ip = endpoint_ip
        self.endpoint_port = endpoint_port
        self.username = username
        self.password = password
