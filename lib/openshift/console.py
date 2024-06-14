from lib import log_helper

from lib.openshift import api
from lib.openshift import settings

from lib.openshift.assistedinstall.main import AssistedInstall
from lib.openshift.accountsmgmt.main import AccountsMgmt


class Console(AssistedInstall, AccountsMgmt):
    def __init__(self, log_id=None):
        AssistedInstall.__init__(self)
        AccountsMgmt.__init__(self)

        self.log = log_helper.Log(log_id=log_id)

        self.settings_handler = settings.OpenShiftSettings()

        self.api_handler = None
        if self.is_ready():
            self.api_handler = api.Api(self.settings_handler.get_api_token(), log_id=log_id)

    def get_pull_secret(self):
        return self.settings_handler.get_pull_secret()

    def is_ready(self):
        return self.settings_handler.is_configured()
