from lib.openshift.accountsmgmt.api import AccountsMgmtApi
from lib.openshift.accountsmgmt.subscription.main import AccountsMgmtSubscription


class AccountsMgmt(
        AccountsMgmtApi,
        AccountsMgmtSubscription
        ):
    def __init__(self):
        AccountsMgmtApi.__init__(self)
        AccountsMgmtSubscription.__init__(self)
