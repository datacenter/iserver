import time

# pylint: disable=no-name-in-module
from pyVmomi import vim, vmodl


class VcHostApi():
    def __init__(self):
        self.mo_host = None
        self.host_names = {}

    def get_host_name(self, host_obj):
        if host_obj is None:
            return None

        if host_obj in self.host_names:
            return self.host_names[host_obj]
        self.host_names[host_obj] = host_obj.name

        return self.host_names[host_obj]

    def get_host_ips(self):
        if not self.vc_connect():
            return None

        content = self.vc_service_instance.RetrieveContent()
        hosts_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.HostSystem],
            True
        )

        if len(hosts_object_view.view) == 0:
            self.my_output.error('No available host found')
            return None

        host_ips = []
        for host_obj in hosts_object_view.view:
            host_ips.append(host_obj.name)

        hosts_object_view.Destroy()

        return host_ips

    def match_host(self, host_info, host_filter):
        if host_filter is None or len(host_filter) == 0:
            return True

        name_filtering = False
        name_match = False
        for host_rule in host_filter:
            if host_rule.startswith('name:'):
                name_filtering = True
                name_value = host_rule[5:]
                if name_value in host_info['name']:
                    name_match = True

        if name_filtering and not name_match:
            return False

        return True

    def get_hosts_properties(self, properties):
        if not self.vc_connect():
            return None

        start_time = int(time.time() * 1000)

        content = self.vc_service_instance.RetrieveContent()
        host_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.HostSystem],
            True
        )

        filter_spec = self.get_filter_spec(
            host_object_view,
            vim.HostSystem,
            properties
        )
        options = vmodl.query.PropertyCollector.RetrieveOptions()
        result = self.vc_service_instance.content.propertyCollector.RetrievePropertiesEx([filter_spec], options)

        mo_host = []
        while True:
            for oresult in result.objects:
                item = {}
                for prop in oresult.propSet:
                    item[prop.name] = prop.val
                mo_host.append(item)

            if result.token is None:
                break

            result = self.vc_service_instance.content.propertyCollector.ContinueRetrievePropertiesEx(result.token)

        host_object_view.Destroy()

        duration = int(time.time() * 1000) - start_time
        self.log.vcenter(
            'get',
            'vim.HostSystem',
            True,
            duration
        )

        return mo_host

    def get_host_objects(self):
        if self.mo_host is not None:
            return self.mo_host

        if not self.vc_connect():
            return None

        self.mo_host = []
        content = self.vc_service_instance.RetrieveContent()

        # Get the list of all datacenters we have available to us
        hosts_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.HostSystem],
            True
        )

        for host_obj in hosts_object_view.view:
            self.mo_host.append(host_obj)

        return self.mo_host
