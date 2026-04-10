from lib import ip_helper


class K8sOperatorGroupCreate():
    def __init__(self):
        pass

    def get_operator_group_body(self, namespace, name=None, add_target_namespaces=True, target_namespaces=None, upgrade_strategy='Default'):
        if name is None:
            name = '%s-%s' % (
                namespace,
                ip_helper.get_short_uuid()
            )
        
        body = {}
        body['apiVersion'] = 'operators.coreos.com/v1'
        body['kind'] = 'OperatorGroup'
        body['metadata'] = {}
        body['metadata']['namespace'] = namespace
        if name is not None:
            body['metadata']['name'] = name
        else:
            body['metadata']['name'] = '%s-%s' % (
                namespace,
                ip_helper.get_short_uuid()
            )

        body['spec'] = {}

        if add_target_namespaces:
            if target_namespaces is None:
                body['spec']['targetNamespaces'] = []
                body['spec']['targetNamespaces'].append(
                    namespace
                )
            else:
                body['spec']['targetNamespaces'] = target_namespaces

        if upgrade_strategy is not None:
            body['spec']['upgradeStrategy'] = upgrade_strategy

        return body

    def create_operator_group(
            self, 
            namespace, 
            name=None, 
            add_target_namespaces=True, 
            target_namespaces=None, 
            upgrade_strategy='Default', 
            confirmation=False, 
            my_output=None, 
            wait=True
        ):
        if my_output is None:
            confirmation = False

        body = self.get_operator_group_body(
            namespace,
            name=name,
            add_target_namespaces=add_target_namespaces,
            target_namespaces=target_namespaces,
            upgrade_strategy=upgrade_strategy
        )
        if not self.create_resource(body, object_name='operator_group', my_output=my_output, confirmation=confirmation):
            return False
        
        if not wait:
            return True

        success = self.wait_operator_group(
            namespace,
            name,
            max_time=60,
            my_output=my_output
        )
        if not success:
            return False

        return True