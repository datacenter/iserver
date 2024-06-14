from lib.openshift.accountsmgmt.subscription.api import AccountsMgmtSubscriptionApi
from lib.openshift.accountsmgmt.subscription.info import AccountsMgmtSubscriptionInfo


class AccountsMgmtSubscription(
        AccountsMgmtSubscriptionApi,
        AccountsMgmtSubscriptionInfo
        ):
    def __init__(self):
        AccountsMgmtSubscriptionApi.__init__(self)
        AccountsMgmtSubscriptionInfo.__init__(self)
