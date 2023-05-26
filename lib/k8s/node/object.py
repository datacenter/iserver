import json
import traceback


class K8sNodeObject():
    def __init__(self):
        pass

    def convert_node_output_json(self, output, fallback_to_string=True):
        try:
            output = str(output)
            output = output.replace('\'{', '{')
            output = output.replace('}\'', '}')
            output = output.replace('\'', '\"')
            output = output.replace(': None', ': null')
            output = output.replace(': True', ': true')
            output = output.replace(': False', ': false')
            return json.loads(output)

        except BaseException:
            self.log.debug('k8s_nodes.convert_node_output_json', output)
            self.log.debug('k8s_nodes.convert_node_output_json', traceback.format_exc())

            if fallback_to_string:
                return str(output)

            return None

    def convert_node_metadata_managed_fields(self, api_objects):
        try:
            if api_objects is None:
                return None

            managed_objects = []
            for api_object in api_objects:
                managed_object = {}
                managed_object['api_version'] = api_object.api_version
                managed_object['fields'] = api_object.fields_v1
                managed_object['manager'] = api_object.manager
                managed_object['operation'] = api_object.operation
                managed_object['time'] = self.convert_timestamp(api_object.time)
                managed_objects.append(managed_object)

        except BaseException:
            self.log.error(
                'k8s_nodes.convert_node_metadata_managed_fields',
                traceback.format_exc()
            )
            return None

        return managed_objects

    def convert_node_metadata(self, api_object):
        try:
            managed_object = {}
            managed_object['uid'] = api_object.uid
            managed_object['name'] = api_object.name
            managed_object['namespace'] = api_object.namespace
            managed_object['annotations'] = self.convert_node_output_json(api_object.annotations)
            managed_object['labels'] = self.convert_node_output_json(api_object.labels)
            managed_object['managed_fields'] = self.convert_node_metadata_managed_fields(api_object.managed_fields)
            managed_object['creation_timestamp'] = self.convert_timestamp(api_object.creation_timestamp)

        except BaseException:
            self.log.error(
                'k8s_nodes.convert_node_metadata',
                traceback.format_exc()
            )
            return None

        return managed_object

    def convert_taints(self, taints):
        try:
            if taints is None:
                return None

            managed_objects = []
            for taint in taints:
                managed_object = {}
                managed_object['effect'] = taint.effect
                managed_object['key'] = taint.key
                managed_object['time_added'] = taint.time_added
                managed_object['value'] = taint.value
                managed_objects.append(managed_object)

        except BaseException:
            self.log.error('k8s_nodes.convert_taint', traceback.format_exc())
            return None

        return managed_object

    def convert_node_spec(self, spec):
        try:
            managed_object = {}
            managed_object['pod_cidr'] = spec.pod_cidr
            managed_object['taints'] = self.convert_taints(spec.taints)

        except BaseException:
            self.log.error('k8s_nodes.convert_node_spec', traceback.format_exc())
            return None

        return managed_object

    def convert_node_address(self, address):
        try:
            info = {}
            info['address'] = address.address
            info['type'] = address.type

        except BaseException:
            self.log.error('k8s_nodes.convert_node_address', traceback.format_exc())
            return None

        return info

    def convert_node_addresses(self, addresses):
        try:
            if addresses is None:
                return None

            managed_objects = []
            for address in addresses:
                converted_address = self.convert_node_address(address)
                if converted_address is not None:
                    managed_objects.append(converted_address)

        except BaseException:
            self.log.error('k8s_nodes.convert_node_addresses', traceback.format_exc())
            return None

        return managed_objects

    def convert_node_condition(self, condition):
        try:
            managed_object = {}
            managed_object['last_heartbeat_time'] = self.convert_timestamp(condition.last_heartbeat_time)
            managed_object['last_transition_time'] = self.convert_timestamp(condition.last_transition_time)
            managed_object['message'] = condition.message
            managed_object['reason'] = condition.reason
            managed_object['type'] = condition.type
            managed_object['status'] = condition.status
        except BaseException:
            self.log.error('k8s_nodes.convert_node_conditions', traceback.format_exc())
            return None

        return managed_object

    def convert_node_conditions(self, conditions):
        try:
            if conditions is None:
                return None

            managed_objects = []
            for condition in conditions:
                converted_condition = self.convert_node_condition(condition)
                if converted_condition is not None:
                    managed_objects.append(converted_condition)

        except BaseException:
            self.log.error('k8s_nodes.convert_node_conditions', traceback.format_exc())
            return None

        return managed_objects

    def convert_node_config_source(self, config_source):
        try:
            if config_source is None:
                return None

            config_map = config_source.config_map
            if config_source is None:
                return None

            managed_object = {}
            managed_object['kubelet_config_key'] = config_map.kubelet_config_key
            managed_object['name'] = config_map.name
            managed_object['namespace'] = config_map.namespace
            managed_object['resource_version'] = config_map.resource_version
            managed_object['uid'] = config_map.uid

        except BaseException:
            self.log.error('k8s_nodes.convert_node_config_source', traceback.format_exc())
            return None

        return managed_object

    def convert_node_config(self, config):
        try:
            if config is None:
                return None

            managed_object = {}
            managed_object['active'] = self.convert_node_config_source(config.active)
            managed_object['assigned'] = self.convert_node_config_source(config.assigned)
            managed_object['last_known_good'] = self.convert_node_config_source(config.last_known_good)
            managed_object['error'] = config.error

        except BaseException:
            self.log.error('k8s_nodes.convert_node_config', traceback.format_exc())
            return None

        return managed_object

    def convert_node_daemon_endpoints(self, daemon_endpoints):
        try:
            if daemon_endpoints is None or daemon_endpoints.kubelet_endpoint is None:
                return None

            port = daemon_endpoints.kubelet_endpoint.port

        except BaseException:
            self.log.error('k8s_nodes.convert_node_daemon_endpoints', traceback.format_exc())
            return None

        return port

    def convert_container_image(self, image):
        try:
            managed_object = {}
            managed_object['names'] = image.names
            managed_object['size_bytes'] = image.size_bytes

        except BaseException:
            self.log.error('k8s_nodes.convert_container_image', traceback.format_exc())
            return None

        return managed_object

    def convert_container_images(self, images):
        try:
            if images is None:
                return None

            managed_objects = []
            for image in images:
                image_info = self.convert_container_image(image)
                if image_info is not None:
                    managed_objects.append(image_info)

        except BaseException:
            self.log.error('k8s_nodes.convert_container_images', traceback.format_exc())
            return None

        return managed_objects

    def convert_node_system_info(self, node):
        try:
            managed_object = {}
            managed_object['architecture'] = node.architecture
            managed_object['boot_id'] = node.boot_id
            managed_object['container_runtime_version'] = node.container_runtime_version
            managed_object['kernel_version'] = node.kernel_version
            managed_object['kube_proxy_version'] = node.kube_proxy_version
            managed_object['kubelet_version'] = node.kubelet_version
            managed_object['machine_id'] = node.machine_id
            managed_object['operating_system'] = node.operating_system
            managed_object['os_image'] = node.os_image
            managed_object['system_uuid'] = node.system_uuid

        except BaseException:
            self.log.error('k8s_nodes.convert_node_system_info', traceback.format_exc())
            return None

        return managed_object

    def convert_volume_attached(self, volume):
        try:
            managed_object = {}
            managed_object['device_path'] = volume.device_path
            managed_object['name'] = volume.name

        except BaseException:
            self.log.error('k8s_nodes.convert_volume_attached', traceback.format_exc())
            return None

        return managed_object

    def convert_volumes_attached(self, volumes_attached):
        try:
            if volumes_attached is None:
                return None

            managed_objects = []
            for volume in volumes_attached:
                volume_info = self.convert_volume_attached(volume)
                if volume_info is not None:
                    managed_objects.append(volume_info)

        except BaseException:
            self.log.error('k8s_nodes.convert_volumes_attached', traceback.format_exc())
            return None

        return managed_objects

    def convert_node_status(self, status):
        try:
            managed_object = {}

            managed_object['addresses'] = self.convert_node_addresses(status.addresses)
            managed_object['allocatable'] = status.allocatable
            managed_object['capacity'] = status.capacity
            managed_object['conditions'] = self.convert_node_conditions(status.conditions)
            managed_object['config'] = self.convert_node_config(status.config)
            managed_object['daemon_endpoints'] = self.convert_node_daemon_endpoints(status.daemon_endpoints)
            managed_object['images'] = self.convert_container_images(status.images)
            managed_object['node_info'] = self.convert_node_system_info(status.node_info)
            managed_object['volumes_attached'] = self.convert_volumes_attached(status.volumes_attached)
            managed_object['volumes_in_use'] = status.volumes_in_use

        except BaseException:
            self.log.error('k8s_nodes.convert_node_status', traceback.format_exc())
            return None

        return managed_object

    def convert_node(self, node):
        managed_object = {}
        managed_object['metadata'] = self.convert_node_metadata(node.metadata)
        managed_object['spec'] = self.convert_node_spec(node.spec)
        managed_object['status'] = self.convert_node_status(node.status)
        return managed_object
