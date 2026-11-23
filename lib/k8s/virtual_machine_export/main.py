from lib.k8s.virtual_machine_export.api import K8sVirtualMachineExportApi
from lib.k8s.virtual_machine_export.info import K8sVirtualMachineExportInfo


class K8sVirtualMachineExport(
        K8sVirtualMachineExportApi,
        K8sVirtualMachineExportInfo
        ):
    def __init__(self):
        K8sVirtualMachineExportApi.__init__(self)
        K8sVirtualMachineExportInfo.__init__(self)
