from lib import filter_helper
from lib import output_helper

from lib.imc.cli.adapter.output import ImcCliAdapterOutput
from lib.imc.cli.admin.output import ImcCliAdminOutput
from lib.imc.cli.bbu.output import ImcCliBbuOutput
from lib.imc.cli.bios.output import ImcCliBiosOutput
from lib.imc.cli.boot.output import ImcCliBootOutput
from lib.imc.cli.chassis.output import ImcCliChassisOutput
from lib.imc.cli.cpu.output import ImcCliCpuOutput
from lib.imc.cli.dimm.output import ImcCliDimmOutput
from lib.imc.cli.fault.output import ImcCliFaultOutput
from lib.imc.cli.flex.output import ImcCliFlexOutput
from lib.imc.cli.fw.output import ImcCliFwOutput
from lib.imc.cli.hardware.output import ImcCliHardwareOutput
from lib.imc.cli.hdd.output import ImcCliHddOutput
from lib.imc.cli.http.output import ImcCliHttpOutput
from lib.imc.cli.ip.output import ImcCliIpOutput
from lib.imc.cli.ipmi.output import ImcCliIpmiOutput
from lib.imc.cli.kvm.output import ImcCliKvmOutput
from lib.imc.cli.led.output import ImcCliLedOutput
from lib.imc.cli.memory.output import ImcCliMemoryOutput
from lib.imc.cli.net.output import ImcCliNetOutput
from lib.imc.cli.ntp.output import ImcCliNtpOutput
from lib.imc.cli.pci.output import ImcCliPciOutput
from lib.imc.cli.psu.output import ImcCliPsuOutput
from lib.imc.cli.redfish.output import ImcCliRedfishOutput
from lib.imc.cli.sel.output import ImcCliSelOutput
from lib.imc.cli.sensor.output import ImcCliSensorOutput
from lib.imc.cli.smtp.output import ImcCliSmtpOutput
from lib.imc.cli.snmp.output import ImcCliSnmpOutput
from lib.imc.cli.sol.output import ImcCliSolOutput
from lib.imc.cli.ssh.output import ImcCliSshOutput
from lib.imc.cli.storageadapter.output import ImcCliStorageAdapterOutput
from lib.imc.cli.syslog.output import ImcCliSyslogOutput
from lib.imc.cli.tpm.output import ImcCliTpmOutput
from lib.imc.cli.utilization.output import ImcCliUtilizationOutput
from lib.imc.cli.version.output import ImcCliVersionOutput
from lib.imc.cli.vmedia.output import ImcCliVmediaOutput
from lib.imc.cli.xml.output import ImcCliXmlOutput


class ImcCliOutput(
        ImcCliAdapterOutput,
        ImcCliAdminOutput,
        ImcCliBbuOutput,
        ImcCliBiosOutput,
        ImcCliBootOutput,
        ImcCliChassisOutput,
        ImcCliCpuOutput,
        ImcCliDimmOutput,
        ImcCliFaultOutput,
        ImcCliFlexOutput,
        ImcCliFwOutput,
        ImcCliHardwareOutput,
        ImcCliHddOutput,
        ImcCliHttpOutput,
        ImcCliIpOutput,
        ImcCliIpmiOutput,
        ImcCliKvmOutput,
        ImcCliLedOutput,
        ImcCliMemoryOutput,
        ImcCliNetOutput,
        ImcCliNtpOutput,
        ImcCliPciOutput,
        ImcCliPsuOutput,
        ImcCliRedfishOutput,
        ImcCliSelOutput,
        ImcCliSensorOutput,
        ImcCliSmtpOutput,
        ImcCliSnmpOutput,
        ImcCliSolOutput,
        ImcCliSshOutput,
        ImcCliStorageAdapterOutput,
        ImcCliSyslogOutput,
        ImcCliTpmOutput,
        ImcCliUtilizationOutput,
        ImcCliVersionOutput,
        ImcCliVmediaOutput,
        ImcCliXmlOutput
    ):
    def __init__(self, verbose=False, debug=False, log_id=None):
        self.my_output = output_helper.OutputHelper(
            log_id=log_id,
            verbose=verbose,
            debug=debug
        )

        ImcCliAdapterOutput.__init__(self)
        ImcCliAdminOutput.__init__(self)
        ImcCliBbuOutput.__init__(self)
        ImcCliBiosOutput.__init__(self)
        ImcCliBootOutput.__init__(self)
        ImcCliChassisOutput.__init__(self)
        ImcCliCpuOutput.__init__(self)
        ImcCliDimmOutput.__init__(self)
        ImcCliFaultOutput.__init__(self)
        ImcCliFlexOutput.__init__(self)
        ImcCliFwOutput.__init__(self)
        ImcCliHardwareOutput.__init__(self)
        ImcCliHddOutput.__init__(self)
        ImcCliHttpOutput.__init__(self)
        ImcCliIpOutput.__init__(self)
        ImcCliIpmiOutput.__init__(self)
        ImcCliKvmOutput.__init__(self)
        ImcCliLedOutput.__init__(self)
        ImcCliMemoryOutput.__init__(self)
        ImcCliNetOutput.__init__(self)
        ImcCliNtpOutput.__init__(self)
        ImcCliPciOutput.__init__(self)
        ImcCliPsuOutput.__init__(self)
        ImcCliRedfishOutput.__init__(self)
        ImcCliSelOutput.__init__(self)
        ImcCliSensorOutput.__init__(self)
        ImcCliSmtpOutput.__init__(self)
        ImcCliSnmpOutput.__init__(self)
        ImcCliSolOutput.__init__(self)
        ImcCliSshOutput.__init__(self)
        ImcCliStorageAdapterOutput.__init__(self)
        ImcCliSyslogOutput.__init__(self)
        ImcCliTpmOutput.__init__(self)
        ImcCliUtilizationOutput.__init__(self)
        ImcCliVersionOutput.__init__(self)
        ImcCliVmediaOutput.__init__(self)
        ImcCliXmlOutput.__init__(self)

    def print_imc_cli_endpoint_settings(self, endpoints, verify=False, show_password=True, title=False):
        if title:
            self.my_output.default(
                'IMC Cli Endpoint [#%s]' % (len(endpoints)),
                underline=True,
                before_newline=True
            )

        if len(endpoints) == 0:
            self.my_output.default('None')
            return

        entries = []
        for item in endpoints:
            item['__Output'] = {}

            if 'verified' in item:
                if item['verified']:
                    item['AuthenticatedTick'] = '\u2713'
                    item['__Output']['AuthenticatedTick'] = 'Green'
                else:
                    item['AuthenticatedTick'] = '\u2717'
                    item['__Output']['AuthenticatedTick'] = 'Red'

            if not show_password:
                item['password'] = '******'

            entries.append(item)

        order = [
            'ip',
            'port',
            'username',
            'password'
        ]

        headers = [
            'IP',
            'Port',
            'Username',
            'Password'
        ]

        if verify:
            order.append('AuthenticatedTick')
            headers.append('Authenticated')

        self.my_output.my_table(
            entries,
            order=order,
            headers=headers,
            underline=True,
            table=True
        )

    def print_dict(self, info, title, add_endpoint_ip=True, underline=True, allow_order_subkeys=True):
        order = []
        headers = []

        if add_endpoint_ip:
            order.append('__IP')
            headers.append('Endpoint')

        endpoint_ip = None
        for key in info:
            if key == '__IP':
                endpoint_ip = info[key]
                continue

            if key in ['__Output', '__Key', '__Value']:
                continue

            order.append(key)
            headers.append(key)

        self.my_output.dictionary(
            info,
            title=title,
            underline=underline,
            prefix="- ",
            justify=True,
            keys=order,
            title_keys=headers,
            allow_order_subkeys=allow_order_subkeys
        )

    def print_list_table(self, info, title=None, allow_order_subkeys=False, add_endpoint_ip=True):
        if isinstance(info, dict):
            info = [info]

        if len(info) == 0:
            if title is not None:
                self.my_output.default(
                    title,
                    underline=True,
                    before_newline=True
                )
            self.my_output.default('None')
            return

        endpoints = []
        for item in info:
            if item['__IP'] not in endpoints:
                endpoints.append(item['__IP'])

        if title is not None:
            if len(endpoints) == 1:
                add_endpoint_ip = False

            if add_endpoint_ip:
                self.my_output.default(
                    title,
                    underline=True,
                    before_newline=True
                )
            else:
                self.my_output.default(
                    '%s [%s]' % (title, info[0]['__IP']),
                    underline=True,
                    before_newline=True
                )

        order = []
        headers = []

        if add_endpoint_ip:
            order.append('__IP')
            headers.append('Endpoint')

        for item in info:
            for key in item:
                if key in ['__Output', '__IP', '__Key', '__Value']:
                    continue

                if key not in order:
                    order.append(
                        key
                    )
                    headers.append(
                        key
                    )

        for item in info:
            for key in order:
                if key not in item or item[key] is None or len(item[key]) == 0:
                    item[key] = '--'

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            remove_empty_columns=False,
            underline=True,
            row_separator=False,
            allow_order_subkeys=allow_order_subkeys,
            table=True
        )

    def print_list_dict(self, info, title, allow_order_subkeys=True, add_endpoint_ip=True, underline=False):
        if isinstance(info, dict):
            info = [info]

        if len(info) == 0:
            self.my_output.default(
                title,
                underline=True,
                before_newline=True
            )
            self.my_output.default('None')
            return

        for item in info:
            self.print_dict(
                item,
                title,
                add_endpoint_ip=add_endpoint_ip,
                underline=underline,
                allow_order_subkeys=allow_order_subkeys
            )

    def print_compare(self, info, title, expand=[], max_expand_column=30):
        order = [
            'key'
        ]
        headers = [
            'Property'
        ]

        endpoint_ips = []
        for item in info:
            endpoint_ip = None
            for key in item:
                if key == '__IP':
                    endpoint_ip = item[key]

            if endpoint_ip is not None:
                if endpoint_ip not in endpoint_ips:
                    endpoint_ips.append(
                        endpoint_ip
                    )

        endpoint_ip_items = {}
        endpoint_ip_key = {}
        endpoint_ip_values = {}
        for endpoint_ip in endpoint_ips:
            endpoint_ip_items[endpoint_ip] = 0
            endpoint_ip_values[endpoint_ip] = []
            for item in info:
                if '__IP' not in item:
                    continue

                if item['__IP'] == endpoint_ip:
                    endpoint_ip_items[endpoint_ip] = endpoint_ip_items[endpoint_ip] + 1
                    if '__Key' in item:
                        endpoint_ip_key[endpoint_ip] = item['__Key']
                    if '__Value' in item:
                        if item['__Value'] not in endpoint_ip_values[endpoint_ip]:
                            endpoint_ip_values[endpoint_ip].append(
                                item['__Value']
                            )

        for endpoint_ip in endpoint_ips:
            if endpoint_ip_items[endpoint_ip] == 1:
                order.append(endpoint_ip)
                headers.append(endpoint_ip)
            else:
                if endpoint_ip not in endpoint_ip_key:
                    self.my_output.error('Input data invalid: incorrect keys')
                    return

                if endpoint_ip_items[endpoint_ip] != len(endpoint_ip_values[endpoint_ip]):
                    self.my_output.error('Input data invalid: insufficien primary key values')
                    return

                for index in range(0, endpoint_ip_items[endpoint_ip]):
                    order.append('%s #%s' % (endpoint_ip, endpoint_ip_values[endpoint_ip][index]))
                    headers.append(endpoint_ip)

        keys = []
        for item in info:
            for key in item:
                if key in ['__Output', '__IP', '__Key', '__Value']:
                    continue

                if key not in keys:
                    keys.append(
                        key
                    )

        values = []
        for key in keys:
            value = {}
            value['__Output'] = {}
            value['key'] = key

            for item in info:
                for endpoint_ip in endpoint_ips:
                    if endpoint_ip_items[endpoint_ip] == 1:
                        if item['__IP'] == endpoint_ip:
                            if key in item:
                                if key in item['__Output']:
                                    value['__Output'][endpoint_ip] = item['__Output'][key]

                                if key in expand:
                                    value[endpoint_ip] = filter_helper.get_string_chunks(
                                        item[key],
                                        max_expand_column
                                    )
                                else:
                                    value[endpoint_ip] = item[key]
                            else:
                                if key in expand:
                                    value[endpoint_ip] = ['--']
                                else:
                                    value[endpoint_ip] = '--'

                    if endpoint_ip_items[endpoint_ip] > 1:
                        for key_value in endpoint_ip_values[endpoint_ip]:
                            if item['__IP'] == endpoint_ip and item[endpoint_ip_key[endpoint_ip]] == key_value:
                                if key in item:
                                    if key in item['__Output']:
                                        value['__Output']['%s #%s' % (endpoint_ip, key_value)] = item['__Output'][key]

                                    if key in expand:
                                        value['%s #%s' % (endpoint_ip, key_value)] = filter_helper.get_string_chunks(
                                            item[key],
                                            max_expand_column
                                        )
                                    else:
                                        value['%s #%s' % (endpoint_ip, key_value)] = item[key]
                                else:
                                    if key in expand:
                                        value['%s #%s' % (endpoint_ip, key_value)] = ['--']
                                    else:
                                        value['%s #%s' % (endpoint_ip, key_value)] = '--'

            values.append(
                value
            )

        if title is not None:
            self.my_output.default(
                title,
                underline=True,
                before_newline=True
            )

        if len(expand) == 0:
            self.my_output.my_table(
                values,
                order=order,
                headers=headers,
                remove_empty_columns=False,
                underline=True,
                row_separator=False,
                table=True
            )
        else:
            self.my_output.my_table(
                self.my_output.auto_expand_lists(
                    values,
                    order
                ),
                order=order,
                headers=headers,
                remove_empty_columns=False,
                underline=True,
                row_separator=False,
                table=True
            )
