from lib.k8s.migration_policy.api import K8sMigrationPolicyApi
from lib.k8s.migration_policy.info import K8sMigrationPolicyInfo


class K8sMigrationPolicy(
        K8sMigrationPolicyApi,
        K8sMigrationPolicyInfo
        ):
    def __init__(self):
        K8sMigrationPolicyApi.__init__(self)
        K8sMigrationPolicyInfo.__init__(self)
