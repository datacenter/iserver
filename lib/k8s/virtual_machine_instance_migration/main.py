from lib.k8s.virtual_machine_instance_migration.api import K8sVirtualMachineInstanceMigrationApi
from lib.k8s.virtual_machine_instance_migration.info import K8sVirtualMachineInstanceMigrationInfo


class K8sVirtualMachineInstanceMigration(
        K8sVirtualMachineInstanceMigrationApi,
        K8sVirtualMachineInstanceMigrationInfo
        ):
    def __init__(self):
        K8sVirtualMachineInstanceMigrationApi.__init__(self)
        K8sVirtualMachineInstanceMigrationInfo.__init__(self)
