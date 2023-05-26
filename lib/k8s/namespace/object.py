import json
import traceback


class K8sNamespaceObject():
    def __init__(self):
        pass

    def convert_namespace_output_json(self, output):
        try:
            if output is None:
                return None

            output = str(output)

            if 'last-applied-configuration' in output:
                return None

            output = output.replace('\'', '\"')
            output = output.replace(': None', ': null')
            output = output.replace(': True', ': true')
            output = output.replace(': False', ': false')
            return json.loads(output)
        except BaseException:
            self.log.error(
                'convert_namespace_output_json',
                output
            )
            self.log.error(
                'convert_namespace_output_json',
                traceback.format_exc()
            )
            return None

    def convert_namespace_metadata_managed_fields(self, managed_fields):
        if managed_fields is None:
            return None

        managed_objects = []
        for managed_field in managed_fields:
            managed_object = {}
            managed_object['api_version'] = managed_field.api_version
            managed_object['fields'] = getattr(managed_field, 'fields', None)
            managed_object['manager'] = getattr(managed_field, 'manager', None)
            managed_object['operation'] = getattr(managed_field, 'operation', None)
            managed_object['time'] = self.convert_timestamp(managed_field.time)
            managed_objects.append(managed_object)

        return managed_objects

    def convert_namespace_metadata(self, metadata):
        managed_object = {}
        managed_object['uid'] = metadata.uid
        managed_object['self_link'] = metadata.self_link
        managed_object['resource_version'] = metadata.resource_version
        if metadata.owner_references is None:
            managed_object['owner_references'] = None
        else:
            managed_object['owner_references'] = str(metadata.owner_references)
        managed_object['name'] = metadata.name
        managed_object['namespace'] = metadata.namespace
        managed_object['annotations'] = self.convert_namespace_output_json(metadata.annotations)
        managed_object['labels'] = self.convert_namespace_output_json(metadata.labels)
        managed_object['managed_fields'] = self.convert_namespace_metadata_managed_fields(metadata.managed_fields)
        managed_object['creation_timestamp'] = self.convert_timestamp(metadata.creation_timestamp)

        return managed_object

    def convert_namespace(self, namespace):
        managed_object = {}
        managed_object['metadata'] = self.convert_namespace_metadata(namespace.metadata)
        managed_object['spec'] = self.convert_namespace_output_json(namespace.spec)
        managed_object['status'] = self.convert_namespace_output_json(namespace.status)

        managed_object['name'] = managed_object['metadata']['name']
        managed_object['active'] = False
        if managed_object['status']['phase'] == 'Active':
            managed_object['active'] = True

        return managed_object
