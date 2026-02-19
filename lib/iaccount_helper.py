import os
import traceback
import subprocess
import shutil

from lib.settings_helper import Settings
from lib import file_helper


class IntersightAccount(Settings):
    def __init__(self):
        Settings.__init__(self)

        self.isctl_configuration_filename = os.path.join(
            self.home_dir,
            '.isctl.yaml'
        )

    def get_isctl_version(self):
        try:
            command = 'isctl version'
            with subprocess.Popen(
                args=command,
                stderr=subprocess.PIPE,
                stdout=subprocess.PIPE,
                shell=True,
                env=os.environ
            ) as process:
                output, error = process.communicate()
                if process.returncode == 0:
                    return True, output.decode('utf-8')
                self.log.error('iaccount_helper.get_isctl_version', 'command execution failed')
                self.log.error('iaccount_helper.get_isctl_version', traceback.format_exc())
                return False, 'isctl command execution failed'
        except BaseException:
            self.log.error('iaccount_helper.get_isctl_version', traceback.format_exc())
            return False, 'Exception in running isctl command'

    def is_isctl(self):
        success, version = self.get_isctl_version()
        return success

    def is_iaccount(self, name):
        if self.get_iaccount_configuration(name) is None:
            return False
        return True

    def get_iaccounts(self, domain=None):
        iaccounts = []
        for name in os.listdir(self.iaccount_dir):
            if self.is_iaccount_valid(name):
                configuration = self.get_iaccount_configuration(name)
                iaccount = {}
                iaccount['name'] = name
                for key in configuration:
                    iaccount[key] = configuration[key]

                iaccount['account'] = None
                iaccount['role'] = None
                iaccount['domain'] = None

                description = self.get_iaccount_description(name)
                if description is not None:
                    if 'account' in description:
                        iaccount['account'] = description['account']
                    if 'role' in description:
                        iaccount['role'] = description['role']
                    if 'domain' in description:
                        iaccount['domain'] = description['domain']

                if domain is not None:
                    if iaccount['domain'] is None or iaccount['domain'] != domain:
                        continue

                iaccounts.append(iaccount)

        return iaccounts

    def get_iaccount_configuration_filename(self, iaccount):
        directory = os.path.join(self.iaccount_dir, iaccount)
        return os.path.join(directory, 'iaccount.yaml')

    def get_iaccount_configuration(self, iaccount):
        '''
            keyfile: /root/intersight.pem
            keyid: lalala
            output: default
            server: intersight.com
        '''
        filename = self.get_iaccount_configuration_filename(iaccount)

        content = file_helper.get_file_yaml(
            filename
        )
        if content is None:
            self.log.error(
                'iaccount_helper.get_iaccount_configuration',
                'Yaml load failed: %s' % (filename)
            )

        return content

    def get_iaccount_key(self, iaccount):
        config = self.get_iaccount_configuration(iaccount)
        if config is None:
            return None
        
        if 'keyid' not in config:
            return None
        
        return config['keyid']

    def get_iaccount_keyfile(self, iaccount):
        config = self.get_iaccount_configuration(iaccount)
        if config is None:
            return None
        
        if 'keyfile' not in config:
            return None
        
        if not os.path.isfile(config['keyfile']):
            return None
        
        return config['keyfile']

    def get_iaccount_description_filename(self, iaccount):
        directory = os.path.join(self.iaccount_dir, iaccount)
        return os.path.join(directory, 'description.yaml')

    def get_iaccount_description(self, iaccount):
        '''
        account: EU-SPN
        role: EU-SPDC-admin
        domain: xyz
        '''
        filename = self.get_iaccount_description_filename(iaccount)

        if not os.path.isfile(filename):
            return None

        content = file_helper.get_file_yaml(
            filename
        )
        if content is None:
            self.log.error(
                'iaccount_helper.get_iaccount_description',
                'Yaml load failed: %s' % (filename)
            )

        return content

    def set_iaccount_description(self, iaccount, description):
        filename = self.get_iaccount_description_filename(iaccount)
        if not file_helper.set_file_yaml(filename, description):
            self.log.error(
                'iaccount_helper.set_iaccount_description',
                'Yaml write failed: %s' % (filename)
            )
            return False
        return True

    def copy_key_file(self, iaccount, source):
        if not os.path.isfile(source):
            return None
        directory = os.path.join(self.iaccount_dir, iaccount)
        destination = os.path.join(directory, 'key.pem')
        shutil.copyfile(source, destination)
        return destination

    def set_iaccount_configuration(self, iaccount, configuration):
        '''
            keyfile: /root/intersight.pem
            keyid: lalala
            output: default
            server: intersight.com
        '''
        filename = self.get_iaccount_configuration_filename(iaccount)
        try:
            key_filename = self.copy_key_file(iaccount, configuration['keyfile'])
            if key_filename is None:
                self.log.error('iaccount_helper.set_iaccount_configuration', 'Key file copy failed')
                return False

            with open(filename, 'w', encoding='utf-8') as file_handler:
                for key in configuration:
                    if key == 'keyfile':
                        file_handler.write('%s: %s\n' % (key, key_filename))
                    else:
                        file_handler.write('%s: %s\n' % (key, configuration[key]))

        except BaseException:
            self.log.error('iaccount_helper.set_iaccount_configuration', traceback.format_exc())
            return False
        return True

    def is_iaccount_valid(self, iaccount):
        configuration = self.get_iaccount_configuration(iaccount)
        if configuration is None:
            self.log.error('iaccount_helper.is_iaccount_valid', 'isctl configuration not found')
            return False

        for key in ['keyfile', 'keyid', 'output', 'server']:
            if key not in configuration:
                self.log.error('iaccount_helper.is_iaccount_valid', 'Key %s not found' % (key))
                return False

        return True

    def create_iaccount(self, iaccount, configuration):
        directory = os.path.join(self.iaccount_dir, iaccount)
        if not os.path.isdir(directory):
            os.makedirs(directory)

        return self.set_iaccount_configuration(iaccount, configuration)

    def delete_iaccount(self, iaccount):
        try:
            directory = os.path.join(self.iaccount_dir, iaccount)
            if not os.path.isdir(directory):
                return False, 'Account does not exist'

            if self.is_default_account(iaccount):
                if not self.clear_default_iaccount():
                    return False, 'Default iaccount change failed'

            shutil.rmtree(directory)

        except BaseException:
            self.log.error('iaccount_helper.delete_iaccount', traceback.format_exc())
            return False, 'Exception'

        return True, None

    def is_default_account(self, iaccount_name):
        default_iacccount_name = self.get_setting('iaccount')
        if default_iacccount_name == iaccount_name:
            return True
        return False

    def clear_default_iaccount(self):
        return self.set_setting('iaccount', None)

    def set_default_iaccount(self, iaccount):
        if self.is_iaccount_valid(iaccount):
            return self.set_setting('iaccount', iaccount)
        return False

    def get_iaccount_json_file(self, iaccount, filename):
        directory = os.path.join(self.iaccount_dir, iaccount)
        return file_helper.get_file_json(os.path.join(directory, filename))

    def set_iaccount_json_file(self, iaccount, filename, content):
        directory = os.path.join(self.iaccount_dir, iaccount)
        return file_helper.set_file_json(os.path.join(directory, filename), content)
