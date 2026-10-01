def get_default_params():
    params = {}
    params['namespace'] = 'tetragon'
    params['name'] = 'tetragon-operator'
    params['operator-group-name'] = 'tetragon'
    params['catalog-namespace'] = 'tetragon'
    params['catalog-name'] = 'tetragon-catalog'
    params['operator-cm-namespace'] = 'tetragon'
    params['operator-cm-name'] = 'tetragon-operator-config'
    params['cm-namespace'] = 'tetragon'
    params['cm-name'] = 'tetragon-config'
    params['sm-namespace'] = 'tetragon'
    params['sm-name'] = 'tetragon'
    params['title'] = 'OpenShift Workflow - Tetragon'
    params['create_subscription'] = 'create_tetragon_subscription'
    params['delete_subscription'] = 'delete_tetragon_subscription'
    params['delete-namespace'] = True
    return params


def get_tetragon_crds():
        # 'TetragonNetworkPolicy',
        # 'TetragonNetworkPolicyNamespaced',
    crds = [
        'AlertRule',
        'SandboxPolicy',
        'SandboxPolicyNamespaced',
        'TracingPolicy',
        'TracingPolicyNamespaced'
    ]
    return crds


def is_tetragon_crd(kind):
    if kind in get_tetragon_crds():
        return True
    return False


def get_resource_name(name):
    resource_map = {}
    resource_map['alert_rule'] = 'AlertRule'
    resource_map['sandbox_policy'] = 'SandboxPolicy'
    resource_map['sandbox_policy_namespaced'] = 'SandboxPolicyNamespaced'
    # resource_map['tetragon_network_policy'] = 'TetragonNetworkPolicy'
    # resource_map['tetragon_network_policy_namespaced'] = 'TetragonNetworkPolicyNamespaced'
    resource_map['tracing_policy'] = 'TracingPolicy'
    resource_map['tracing_policy_namespaced'] = 'TracingPolicyNamespaced'
    return resource_map[name]


def get_resources(params):
    resource = {}
    resource['alert_rule'] = params['k8s_handler'].get_alert_rules(cache_enabled=False)
    resource['sandbox_policy'] = params['k8s_handler'].get_sandbox_policys(cache_enabled=False)
    resource['sandbox_policy_namespaced'] = params['k8s_handler'].get_sandbox_policy_namespaceds(cache_enabled=False)
    # resource['tetragon_network_policy'] = params['k8s_handler'].get_tetragon_network_policys(cache_enabled=False)
    # resource['tetragon_network_policy_namespaced'] = params['k8s_handler'].get_tetragon_network_policy_namespaceds(cache_enabled=False)
    resource['tracing_policy'] = params['k8s_handler'].get_tracing_policys(cache_enabled=False)
    resource['tracing_policy_namespaced'] = params['k8s_handler'].get_tracing_policy_namespaceds(cache_enabled=False)
    return resource


def print_resource_brief(resources, my_output):
    my_output.default('Tetragon resources', before_newline=True)

    for name in resources:
        if resources[name] is None:
            my_output.default(
                '- %s: %s' % (
                    get_resource_name(name),
                    my_output.add_color('---', 'Red')
                )
            )
        else:
            my_output.default(
                '- %s: %s' % (
                    get_resource_name(name),
                    len(resources[name])
                )
            )


def print_resource(resources, k8s_output_handler):
    for name in resources:
        if resources[name] is not None:
            getattr(k8s_output_handler, 'print_%ss_state' % (name))(resources[name])


def is_any_resource(resources):
    exists = False
    for name in resources:
        if resources[name] is not None and len(resources[name]) > 0:
            exists = True
            break
    return exists