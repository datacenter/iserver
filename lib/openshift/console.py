import traceback
from lib import log_helper

from lib.openshift import api
from lib.openshift import settings

from lib.openshift.assistedinstall.main import AssistedInstall
from lib.openshift.accountsmgmt.main import AccountsMgmt


class Console(AssistedInstall, AccountsMgmt):
    def __init__(self, do_strip=False, log_id=None, check_ssl=True, timeout=360):
        AssistedInstall.__init__(self)
        AccountsMgmt.__init__(self)

        self.log = log_helper.Log(log_id=log_id)

        self.settings_handler = settings.OpenShiftSettings()

        self.api_handler = None
        if self.is_ready():
            self.api_handler = api.Api(self.settings_handler.get_api_token(do_strip=do_strip), log_id=log_id, verify=check_ssl, timeout=timeout)

    def get_pull_secret(self):
        return self.settings_handler.get_pull_secret()

    def is_ready(self):
        return self.settings_handler.is_configured()

    def is_authenticated(self):
        if not self.is_ready():
            return False
        
        if self.api_handler is None:
            return False
        
        if self.api_handler.access_token is None:
            return False
        
        return True
    
    def check_token(self, my_output, do_strip):
        my_output.default('- API token filename: %s' % (self.settings_handler.openshift_api_token_filename))
        if self.settings_handler.get_api_token() is None:
            my_output.error('Failed to read token file')
            try:
                with open(self.settings_handler.openshift_api_token_filename, 'r', encoding='utf-8') as file_handler:
                    content = file_handler.read()
            except BaseException:
                my_output.default(traceback.format_exc())
            return False
        
        my_output.default('- Token file read successful')

        my_output.default('- Pull secret filename: %s' % (self.settings_handler.openshift_pull_secret_filename))
        if self.settings_handler.get_pull_secret() is None:
            my_output.error('Failed to read pull secret file')
            try:
                with open(self.settings_handler.openshift_pull_secret_filename, 'r', encoding='utf-8') as file_handler:
                    content = file_handler.read()

            except BaseException:
                my_output.default(traceback.format_exc())

            return False
        
        my_output.default('- Pull secret file read successful')

        self.api_handler = api.Api(self.settings_handler.get_api_token(do_strip=do_strip))
        if self.api_handler is None:
            my_output.error('RedHat Console API object initialization failed')
            return False
        
        my_output.default('- API handler object initialized')

        access_token, error = self.api_handler.generate_access_token()
        if access_token is None:
            my_output.error('RedHat Console API connection failed: %s' % (error))
            return False
        
        my_output.default('- RedHat Console API connection sucessfull')
        return True
