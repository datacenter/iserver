from lib.k8s.migration.api import K8sMigrationApi
from lib.k8s.migration.info import K8sMigrationInfo
from lib.k8s.migration.create import K8sMigrationCreate
from lib.k8s.migration.wait import K8sMigrationWait


class K8sMigration(
        K8sMigrationApi,
        K8sMigrationInfo,
        K8sMigrationCreate,
        K8sMigrationWait
        ):
    def __init__(self):
        K8sMigrationApi.__init__(self)
        K8sMigrationInfo.__init__(self)
        K8sMigrationCreate.__init__(self)
        K8sMigrationWait.__init__(self)
