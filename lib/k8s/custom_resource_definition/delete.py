class K8sCustomResourceDefinitionDelete():
    def __init__(self):
        pass

    def delete_custom_resource_definition(self, name, my_output=None, wait=True):
        if my_output is not None:
            my_output.default('Delete Custom Resource Definition', before_newline=True, underline=True)
            my_output.default('- name: %s' % (name))

        info = self.get_custom_resource_definition(name, cache_enabled=False)
        if info is None:
            if my_output is not None:
                my_output.default('- already deleted')
            return True

        if not self.delete_custom_resource_definition_mo(info['name']):
            if my_output is not None:
                my_output.error('Failed to delete custom resource definition')
            return False

        if wait:
            if my_output is not None:
                my_output.default('- wait for no custom resource definition')

            if not self.wait_no_custom_resource_definition(info['name']):
                if my_output is not None:
                    my_output.error('Timed out')
                return False

        return True

    def delete_labeled_custom_resource_definitions(self, labels, my_output=None, wait=True):
        crds = self.get_custom_resource_definitions(cache_enabled=False)
        if crds is None:
            if my_output is not None:
                my_output.error('Failed to get custom resource definitions')
            return False

        for crd in crds:
            match = True
            for key in labels:
                if key not in crd['label']:
                    match = False
                    break

                if crd['label'][key] != labels[key]:
                    match = False
                    break

            if not match:
                continue

            success = self.delete_custom_resource_definition(
                crd['name'],
                my_output=my_output,
                wait=wait
            )
            if not success:
                return False

        return True