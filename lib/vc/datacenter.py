# pylint: disable=no-name-in-module
from pyVmomi import vim


class VcDatacenter():
    def __init__(self):
        pass

    def is_datacenter(self, datacenter_name):
        datacenters = self.get_datacenters()
        if datacenters is None:
            return False

        for datacenter in datacenters:
            if datacenter['name'] == datacenter_name:
                return True

        return False

    def get_datacenters(self):
        if not self.vc_connect():
            return None

        datacenters = []
        content = self.vc_service_instance.RetrieveContent()

        # Get the list of all datacenters we have available to us
        datacenters_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.Datacenter],
            True
        )

        for dc_obj in datacenters_object_view.view:
            datacenter = {}
            datacenter['name'] = dc_obj.name
            datacenters.append(datacenter)

        return datacenters

    def get_datacenter_object(self, datacenter_name):
        if not self.vc_connect():
            return None

        content = self.vc_service_instance.RetrieveContent()
        datacenters_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.Datacenter],
            True
        )

        for dc_obj in datacenters_object_view.view:
            if dc_obj.name == datacenter_name:
                datacenters_object_view.Destroy()
                return dc_obj

        datacenters_object_view.Destroy()

        return None
