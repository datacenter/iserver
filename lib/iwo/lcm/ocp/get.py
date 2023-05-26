import json
import uuid

from lib import ssh
from lib.intersight import asset_device_registration


class IwoOcpGetLcm():
    def __init__(self):
        pass

    def is_iwo_installed(self, cluster_parameters):
        if self.get_iwo_installed(cluster_parameters) is None:
            return False
        return True

    def get_iwo_installed(self, cluster_parameters):
        ssh_handler = ssh.Ssh(
            cluster_parameters['installer']['vm']['ip'],
            cluster_parameters['installer']['vm']['username'],
            password=cluster_parameters['installer']['vm']['password']
        )
        source = '/root/.iwo_installed.json'
        if not ssh_handler.is_file(source):
            return None

        destination = '/tmp/%s' % (str(uuid.uuid4()))
        success = ssh_handler.scp_file(source, destination, put=False)
        if not success:
            self.my_output.error('IWO installation report download failed')
            return False

        try:
            with open(destination, 'r', encoding='utf-8') as file_handler:
                report = json.loads(file_handler.read())
        except BaseException:
            self.my_output.error('IWO installation report download failed')
            return None

        self.my_output.debug(
            'get_iwo_installed',
            json.dumps(
                report,
                indent=4
            )
        )
        return report

    def set_iwo_installed(self, cluster_parameters, iwo_parameters):
        ssh_handler = ssh.Ssh(
            cluster_parameters['installer']['vm']['ip'],
            cluster_parameters['installer']['vm']['username'],
            password=cluster_parameters['installer']['vm']['password']
        )
        source = '/tmp/%s' % (str(uuid.uuid4()))
        with open(source, 'w', encoding='utf-8') as file_handler:
            file_handler.write(
                json.dumps(
                    iwo_parameters,
                    indent=4
                )
            )

        destination = '/root/.iwo_installed.json'
        success = ssh_handler.scp_file(source, destination)
        if not success:
            self.my_output.error('IWO installation report failed')
            return False

        self.my_output.default('IWO installation report set')
        return True

    def get_install_device_identifier(self, cluster_parameters):
        ssh_handler = ssh.Ssh(
            cluster_parameters['installer']['vm']['ip'],
            cluster_parameters['installer']['vm']['username'],
            password=cluster_parameters['installer']['vm']['password']
        )
        filename = '/tmp/iwo_device_identifiers'
        if not ssh_handler.is_file(filename):
            self.my_output.error('IWO device identifier file not found: %s' % (filename))
            return None

        local_filename = '/tmp/%s' % (str(uuid.uuid4()))
        success = ssh_handler.scp_file(
            filename,
            local_filename,
            put=False
        )
        if not success:
            self.my_output.error('File download failed: %s' % (filename))
            return None

        try:
            with open(local_filename, 'rb') as file_handler:
                content = json.loads(file_handler.read())
            self.my_output.debug(content)

        except BaseException:
            self.my_output.error('File read failed: %s' % (filename))
            return None

        try:
            device_identifier = content[0]['Id']
        except BaseException:
            self.my_output.error('Unsupported file content: %s' % (filename))
            self.my_output.default(
                json.dumps(content, indent=4)
            )
            return None

        self.my_output.default('Device identifier: %s' % (device_identifier))
        return device_identifier

    def get_security_token(self, cluster_parameters):
        ssh_handler = ssh.Ssh(
            cluster_parameters['installer']['vm']['ip'],
            cluster_parameters['installer']['vm']['username'],
            password=cluster_parameters['installer']['vm']['password']
        )
        filename = '/tmp/iwo_security_tokens'
        if not ssh_handler.is_file(filename):
            self.my_output.error('IWO security token file not found: %s' % (filename))
            return None

        local_filename = '/tmp/%s' % (str(uuid.uuid4()))
        success = ssh_handler.scp_file(
            filename,
            local_filename,
            put=False
        )
        if not success:
            self.my_output.error('File download failed: %s' % (filename))
            return None

        try:
            with open(local_filename, 'rb') as file_handler:
                content = json.loads(file_handler.read())
            self.my_output.debug(content)

        except BaseException:
            self.my_output.error('File read failed: %s' % (filename))
            return None

        try:
            security_token = content[0]['Token']
        except BaseException:
            self.my_output.error('Unsupported file content: %s' % (filename))
            return None

        self.my_output.default('Security token: %s' % (security_token))
        return security_token

    def is_intersight_target(self, iaccount, device_identifier):
        if self.get_intersight_target_claim(iaccount, device_identifier) is None:
            return False
        return True

    def get_intersight_target_moid(self, iaccount, device_identifier):
        asset_handler = asset_device_registration.AssetDeviceRegistration(iaccount, log_id=self.log_id)
        targets = asset_handler.get_all()
        for target in targets:
            for serial in target['Serial']:
                if serial == device_identifier:
                    return target['Moid']
        return None

    def get_intersight_target_claim(self, iaccount, device_identifier):
        asset_handler = asset_device_registration.AssetDeviceRegistration(iaccount, log_id=self.log_id)
        targets = asset_handler.get_all()
        for target in targets:
            for serial in target['Serial']:
                if serial == device_identifier:
                    return target['DeviceClaim']['Moid']
        return None

    def get_lcm_state(self, installation_report):
        state = {}
        state['__Output'] = {}
        state['installed'] = False
        state['installedTick'] = '\u2717'
        state['__Output']['installedTick'] = 'Red'
        state['connected'] = False
        state['connectedTick'] = '\u2717'
        state['__Output']['connectedTick'] = 'Red'
        state['hostname'] = []
        state['ips'] = []

        if installation_report is None:
            return state

        state['installed'] = True
        state['installedTick'] = '\u2713'
        state['__Output']['installedTick'] = 'Green'

        asset_handler = asset_device_registration.AssetDeviceRegistration(
            installation_report['iaccount'],
            log_id=self.log_id
        )
        device_registration = asset_handler.get(
            installation_report['registration_id']
        )
        if device_registration is not None:
            state['target'] = device_registration
            if device_registration['ConnectionStatus'] == 'Connected':
                state['connected'] = False
                state['connectedTick'] = '\u2713'
                state['__Output']['connectedTick'] = 'Green'
                state['hostname'] = device_registration['DeviceHostname']
                state['ips'] = device_registration['DeviceIpAddress']

        return state
