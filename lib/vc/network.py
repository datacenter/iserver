import time

# pylint: disable=no-name-in-module
from pyVmomi import vim, vmodl


class VcNetwork():
    def __init__(self):
        self.distributed_network_objects = None
        self.distributed_network_names = {}

        self.network_objects = None
        self.network_names = {}

    def get_distributed_network_name_by_key(self, key):
        if key in self.distributed_network_names:
            return self.distributed_network_names[key]

        network_objs = self.get_distributed_network_objects()
        if network_objs is None:
            return None

        network_name = None
        for network_obj in network_objs:
            if network_obj['key'] == key:
                self.distributed_network_names[key] = network_obj['name']
                network_name = self.distributed_network_names[key]
                break

        return network_name

    def is_network_distributed(self, network_obj):
        return isinstance(network_obj, vim.dvs.DistributedVirtualPortgroup)

    def get_distributed_network_objects(self):
        if self.distributed_network_objects is not None:
            return self.distributed_network_objects

        if not self.vc_connect():
            return None

        start_time = int(time.time() * 1000)

        content = self.vc_service_instance.RetrieveContent()
        networks_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.dvs.DistributedVirtualPortgroup],
            True
        )

        filter_spec = self.get_filter_spec(
            networks_object_view,
            vim.dvs.DistributedVirtualPortgroup,
            ['name', 'key', 'config']
        )
        options = vmodl.query.PropertyCollector.RetrieveOptions()
        result = self.vc_service_instance.content.propertyCollector.RetrievePropertiesEx([filter_spec], options)

        self.distributed_network_objects = []
        while True:
            for oresult in result.objects:
                item = {}
                for prop in oresult.propSet:
                    item[prop.name] = prop.val
                self.distributed_network_objects.append(item)

            if result.token is None:
                break

            result = self.vc_service_instance.content.propertyCollector.ContinueRetrievePropertiesEx(result.token)

        networks_object_view.Destroy()

        duration = int(time.time() * 1000) - start_time
        self.log.vcenter(
            'get',
            'vim.dvs.DistributedVirtualPortgroup',
            True,
            duration
        )

        return self.distributed_network_objects

    def get_distributed_network_object(self, network_name):
        network_objs = self.get_distributed_network_objects()
        if network_objs is None:
            return None

        for network_obj in network_objs:
            if network_obj['name'] == network_name:
                return network_obj

        return None

    def get_network_info(self, network_obj):
        info = {}
        info['name'] = network_obj.name
        # info['objects'] = dir(network_obj)
        # info['host'] = dir(network_obj.host)
        # info['summary'] = dir(network_obj.summary)
        # info['vm'] = dir(network_obj.vm)
        return info

    def is_network(self, network_name):
        network_obj = self.get_network_object(network_name)
        if network_obj is None:
            return False
        return True

    def get_network_objects(self):
        if self.network_objects is not None:
            return self.network_objects

        if not self.vc_connect():
            return None

        start_time = int(time.time() * 1000)

        content = self.vc_service_instance.RetrieveContent()
        networks_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.Network],
            True
        )

        self.network_objects = []
        for network_obj in networks_object_view.view:
            self.network_objects.append(network_obj)

        networks_object_view.Destroy()

        duration = int(time.time() * 1000) - start_time
        self.log.vcenter(
            'get',
            'vim.Network',
            True,
            duration
        )

        return self.network_objects

    def get_network_object(self, network_name):
        network_objs = self.get_network_objects()
        if network_objs is None:
            return None

        for network_obj in network_objs:
            if network_obj.name == network_name:
                return network_obj

        return None

    def get_network_name(self, network_obj):
        if network_obj in self.network_names:
            return self.network_names[network_obj]

        self.network_names[network_obj] = network_obj.name
        return self.network_names[network_obj]

    def get_network_names(self):
        network_objs = self.get_network_objects()
        if network_objs is None:
            return None

        network_names = []
        for network_obj in network_objs:
            network_names.append(
                network_obj.name
            )

        return sorted(network_names)

    def print_network_names(self, title=None):
        if title is not None:
            self.my_output.default(title)

        network_names = self.get_network_names()
        if network_names is None:
            self.my_output.error('No network found')
            return

        for network_name in network_names:
            self.my_output.default('- %s' % (network_name))
