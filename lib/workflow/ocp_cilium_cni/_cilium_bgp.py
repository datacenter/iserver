import yaml
from lib import filter_helper


def get_cilium_config_filename(manifests):
    for key in manifests:
        content = yaml.safe_load(manifests[key])
        if content is not None:
            if 'kind' in content:
                if content['kind'] == 'CiliumConfig':
                    return key
    return None


def get_cilium_config(manifests):
    for key in manifests:
        content = yaml.safe_load(manifests[key])
        if content is not None:
            if 'kind' in content:
                if content['kind'] == 'CiliumConfig':
                    return content
    return None


def get_cilium_manifests_type(manifests, my_output):
    cilium_config = get_cilium_config(manifests)
    if cilium_config is None:
        my_output.error('CiliumConfig manifest not found')
        return None

    label = filter_helper.get_attr(
        cilium_config, 'metadata:labels:app.kubernetes.io/name'
    )
    if label is not None and label == 'clife':
        return 'clife'

    return 'olm'


def get_cilium_manifests_clife_version(manifests):
    for key in manifests:
        content = yaml.safe_load(manifests[key])
        if content is None:
            continue

        if filter_helper.get_attr(content, 'kind') != 'Deployment':
            continue

        if filter_helper.get_attr(content, 'metadata:name') != 'clife-controller-manager':
            continue

        containers = filter_helper.get_attr(content, 'spec:template:spec:containers')
        if isinstance(containers, list) and len(containers) > 0:
            image = filter_helper.get_attr(containers[0], 'image')
            if image is not None:
                try:
                    version = image.split(':')[1]
                    return version
                except BaseException:
                    pass

    return None


def get_cilium_manifests_olm_version(manifests):
    for key in manifests:
        content = yaml.safe_load(manifests[key])
        if content is None:
            continue

        if filter_helper.get_attr(content, 'kind') != 'Subscription':
            continue

        if filter_helper.get_attr(content, 'metadata:name') not in ['cilim', 'cilium-enterprise']:
            continue

        csv = filter_helper.get_attr(content, 'spec:startingCSV')
        if csv is not None:
            try:
                version = csv.split('%s.' % (filter_helper.get_attr(content, 'metadata:name')))[1].split('-')[0]
                return version
            except BaseException:
                pass

    return None


def replace_cilium_config_manifest(manifests, content):
    filename = get_cilium_config_filename(manifests)
    manifests[filename] = yaml.dump(content)
    return manifests


def fixup_cilium_manifests(user_settings, manifests, manifests_type):
    config = get_cilium_config(manifests)

    is_cnv = False
    if 'olm_operators' in user_settings:
        for item in user_settings['olm_operators']:
            if item['name'] == 'cnv':
                is_cnv = True

    if manifests_type == 'olm':
        if 'cilium' not in config['spec']:
            config['spec']['cilium'] = {}

        if len(user_settings['server']) == 1:
            if 'operator' not in config['spec']['cilium']:
                config['spec']['cilium']['operator'] = {}

            config['spec']['cilium']['operator']['replicas'] = 1

        if 'ipam' not in config['spec']['cilium']:
            config['spec']['cilium']['ipam'] = {}

        config['spec']['cilium']['ipam']['operator']['clusterPoolIPv4PodCIDRList'] = 'QUOTE%sQUOTE' % (user_settings['cluster_network_cidr'])
        config['spec']['cilium']['ipam']['operator']['clusterPoolIPv4MaskSize'] = user_settings['cluster_network_host_prefix']

        ipv4_cidr = filter_helper.get_attr(
            config, 'spec:cilium:nativeRoutingCIDR'
        )
        if ipv4_cidr is not None:
            config['spec']['cilium']['nativeRoutingCIDR'] = 'QUOTE%sQUOTE' % (user_settings['cluster_network_cidr'])

        if is_cnv:
            if 'socketLB' not in config['spec']['cilium']:
                config['spec']['cilium']['socketLB'] = {}

            config['spec']['cilium']['socketLB']['hostNamespaceOnly'] = True

    if manifests_type == 'clife':
        if len(user_settings['server']) == 1:
            if 'operator' not in config['spec']:
                config['spec']['operator'] = {}

            config['spec']['operator']['replicas'] = 1

        if 'ipam' not in config['spec']:
            config['spec']['ipam'] = {}

        if 'operator' not in config['spec']['ipam']:
            config['spec']['ipam']['operator'] = {}

        config['spec']['ipam']['operator']['clusterPoolIPv4PodCIDRList'] = ['QUOTE%sQUOTE' % (user_settings['cluster_network_cidr'])]
        config['spec']['ipam']['operator']['clusterPoolIPv4MaskSize'] = user_settings['cluster_network_host_prefix']

        if is_cnv:
            if 'socketLB' not in config['spec']:
                config['spec']['socketLB'] = {}

            config['spec']['socketLB']['hostNamespaceOnly'] = True

    manifests = replace_cilium_config_manifest(manifests, config)
    return manifests


def validate_cilium_manifests(user_settings, manifests, manifests_type, my_output):
    cilium_config = get_cilium_config(manifests)

    ipv4_cidr = filter_helper.get_attr(
        cilium_config, 'spec:ipam:operator:clusterPoolIPv4PodCIDRList'
    )
    if ipv4_cidr is None:
        my_output.error('CiliumConfig manifest property spec:ipam:operator:clusterPoolIPv4PodCIDRList missing')
        return None

    if manifests_type == 'olm':
        if ipv4_cidr.replace('"', '').replace('QUOTE', '') != user_settings['cluster_network_cidr']:
            my_output.error('CiliumConfig manifest property spec:ipam:operator:clusterPoolIPv4PodCIDRList not aligned with cluster.json cluster_network_cidr')
            return None

    if manifests_type == 'clife':
        for item in ipv4_cidr:
            if item.replace('"', '').replace('QUOTE', '') != user_settings['cluster_network_cidr']:
                my_output.error('CiliumConfig manifest property spec:ipam:operator:clusterPoolIPv4PodCIDRList not aligned with cluster.json cluster_network_cidr')
                return None

    ipv4_mask = filter_helper.get_attr(
        cilium_config, 'spec:ipam:operator:clusterPoolIPv4MaskSize'
    )
    if ipv4_mask is None:
        my_output.error('CiliumConfig manifest property spec:ipam:operator:clusterPoolIPv4MaskSize missing')
        return None

    if ipv4_mask != user_settings['cluster_network_host_prefix']:
        my_output.error('CiliumConfig manifest property spec:ipam:operator:clusterPoolIPv4MaskSize not aligned with cluster.json cluster_network_host_prefix')
        return None

    ipv4_cidr = filter_helper.get_attr(
        cilium_config, 'spec:cilium:nativeRoutingCIDR'
    )
    if ipv4_cidr is not None:
        if ipv4_cidr.replace('"', '').replace('QUOTE', '') != user_settings['cluster_network_cidr']:
            my_output.error('CiliumConfig manifest property spec:cilium:nativeRoutingCIDR not aligned with cluster.json cluster_network_cidr')
            return None

    return manifests


def add_kube_proxy(user_settings, manifests, manifests_type, cilium_version, my_output):
    cilium_config = get_cilium_config(manifests)
    manifests = replace_cilium_config_manifest(manifests, cilium_config)
    return manifests


def add_hubble_metrics_clife(manifests):
    cilium_config = get_cilium_config(manifests)

    if filter_helper.get_attr(cilium_config, 'spec:hubble') is None:
        cilium_config['spec']['hubble'] = {}

    cilium_config['spec']['hubble']['enabled'] = True
    cilium_config['spec']['hubble']['metrics'] = {}
    cilium_config['spec']['hubble']['metrics']['enabled'] = [
        'dns:labelsContext=source_namespace,destination_namespace',
        'drop:labelsContext=source_namespace,destination_namespace',
        'tcp:labelsContext=source_namespace,destination_namespace',
        'port-distribution:labelsContext=source_namespace,destination_namespace',
        'icmp:labelsContext=source_namespace,destination_namespace;sourceContext=workload-name|reserved-identity;destinationContext=workload-name|reserved-identity',
        'flow:sourceContext=workload-name|reserved-identity;destinationContext=workload-name|reserved-identity;labelsContext=source_namespace,destination_namespace',
        'QUOTEhttpV2:exemplars=true;labelsContext=source_ip,source_namespace,source_workload,destination_ip,destination_namespace,destination_workload,traffic_direction;sourceContext=workload-name|reserved-identity;destinationContext=workload-name|reserved-identityQUOTE',
        'QUOTEpolicy:sourceContext=app|workload-name|pod|reserved-identity;destinationContext=app|workload-name|pod|dns|reserved-identity;labelsContext=source_namespace,destination_namespaceQUOTE',
        'flow_export'
    ]

    if filter_helper.get_attr(cilium_config, 'spec:prometheus') is None:
        cilium_config['spec']['prometheus'] = {}

    cilium_config['spec']['prometheus']['enabled'] = True
    cilium_config['spec']['prometheus']['serviceMonitor'] = {}
    cilium_config['spec']['prometheus']['serviceMonitor']['enabled'] = True

    if filter_helper.get_attr(cilium_config, 'spec:operator') is None:
        cilium_config['spec']['operator'] = {}

    if filter_helper.get_attr(cilium_config, 'spec:operator:prometheus') is None:
        cilium_config['spec']['operator']['prometheus'] = {}

    cilium_config['spec']['operator']['prometheus']['enabled'] = True
    cilium_config['spec']['operator']['prometheus']['serviceMonitor'] = {}
    cilium_config['spec']['operator']['prometheus']['serviceMonitor']['enabled'] = True

    manifests = replace_cilium_config_manifest(manifests, cilium_config)
    return manifests


def add_hubble_metrics_olm(manifests):
    cilium_config = get_cilium_config(manifests)

    if filter_helper.get_attr(cilium_config, 'spec:cilium:hubble') is None:
        cilium_config['spec']['cilium']['hubble'] = {}

    cilium_config['spec']['cilium']['hubble']['enabled'] = True
    cilium_config['spec']['cilium']['hubble']['metrics'] = {}
    cilium_config['spec']['cilium']['hubble']['metrics']['enabled'] = [
        'dns:labelsContext=source_namespace,destination_namespace',
        'drop:labelsContext=source_namespace,destination_namespace',
        'tcp:labelsContext=source_namespace,destination_namespace',
        'port-distribution:labelsContext=source_namespace,destination_namespace',
        'icmp:labelsContext=source_namespace,destination_namespace;sourceContext=workload-name|reserved-identity;destinationContext=workload-name|reserved-identity',
        'flow:sourceContext=workload-name|reserved-identity;destinationContext=workload-name|reserved-identity;labelsContext=source_namespace,destination_namespace',
        'QUOTEhttpV2:exemplars=true;labelsContext=source_ip,source_namespace,source_workload,destination_ip,destination_namespace,destination_workload,traffic_direction;sourceContext=workload-name|reserved-identity;destinationContext=workload-name|reserved-identityQUOTE',
        'QUOTEpolicy:sourceContext=app|workload-name|pod|reserved-identity;destinationContext=app|workload-name|pod|dns|reserved-identity;labelsContext=source_namespace,destination_namespaceQUOTE',
        'flow_export'
    ]
    cilium_config['spec']['cilium']['hubble']['metrics']['serviceMonitor'] = {}
    cilium_config['spec']['cilium']['hubble']['metrics']['serviceMonitor']['enabled'] = True
    cilium_config['spec']['cilium']['hubble']['relay'] = {}
    cilium_config['spec']['cilium']['hubble']['relay']['enabled'] = True

    if filter_helper.get_attr(cilium_config, 'spec:cilium:operator') is None:
        cilium_config['spec']['cilium']['operator'] = {}

    if filter_helper.get_attr(cilium_config, 'spec:cilium:operator:prometheus') is None:
        cilium_config['spec']['cilium']['operator']['prometheus'] = {}

    cilium_config['spec']['cilium']['operator']['prometheus']['enabled'] = True
    cilium_config['spec']['cilium']['operator']['prometheus']['serviceMonitor'] = {}
    cilium_config['spec']['cilium']['operator']['prometheus']['serviceMonitor']['enabled'] = True

    manifests = replace_cilium_config_manifest(manifests, cilium_config)
    return manifests


def add_hubble_metrics(manifests, manifests_type):
    if manifests_type == 'clife':
        return add_hubble_metrics_clife(manifests)

    if manifests_type == 'olm':
        return add_hubble_metrics_olm(manifests)

    return None


def add_bgp_cee_clife(user_settings, manifests, manifests_type, cilium_version, my_output):
    cilium_config = get_cilium_config(manifests)

    if filter_helper.get_attr(cilium_config, 'spec:enterprise') is None:
        cilium_config['spec']['enterprise'] = {}

    cilium_config['spec']['enterprise']['bgpControlPlane'] = {}
    cilium_config['spec']['enterprise']['bgpControlPlane']['enabled'] = True
    cilium_config['spec']['enterprise']['bgpControlPlane']['secretsNamespace'] = {}
    cilium_config['spec']['enterprise']['bgpControlPlane']['secretsNamespace']['name'] = 'cilium'
    cilium_config['spec']['enterprise']['bgpControlPlane']['secretsNamespace']['create'] = False

    manifests = replace_cilium_config_manifest(manifests, cilium_config)
    return manifests


def add_bgp_cee_olm(user_settings, manifests, manifests_type, cilium_version, my_output):
    cilium_config = get_cilium_config(manifests)

    if filter_helper.get_attr(cilium_config, 'spec:cilium:enterprise') is None:
        cilium_config['spec']['cilium']['enterprise'] = {}

    cilium_config['spec']['cilium']['enterprise']['bgpControlPlane'] = {}
    cilium_config['spec']['cilium']['enterprise']['bgpControlPlane']['enabled'] = True
    cilium_config['spec']['cilium']['enterprise']['bgpControlPlane']['secretsNamespace'] = {}
    cilium_config['spec']['cilium']['enterprise']['bgpControlPlane']['secretsNamespace']['name'] = 'cilium'
    cilium_config['spec']['cilium']['enterprise']['bgpControlPlane']['secretsNamespace']['create'] = False

    manifests = replace_cilium_config_manifest(manifests, cilium_config)
    return manifests


def add_bgp_cee(user_settings, manifests, manifests_type, cilium_version, my_output):
    if manifests_type == 'clife':
        return add_bgp_cee_clife(user_settings, manifests, manifests_type, cilium_version, my_output)

    if manifests_type == 'olm':
        return add_bgp_cee_olm(user_settings, manifests, manifests_type, cilium_version, my_output)

    return None


def add_bgp_oss_clife(user_settings, manifests, manifests_type, cilium_version, my_output):
    cilium_config = get_cilium_config(manifests)

    cilium_config['spec']['bgpControlPlane'] = {}
    cilium_config['spec']['bgpControlPlane']['enabled'] = True
    cilium_config['spec']['bgpControlPlane']['secretsNamespace'] = {}
    cilium_config['spec']['bgpControlPlane']['secretsNamespace']['name'] = 'cilium'
    cilium_config['spec']['bgpControlPlane']['secretsNamespace']['create'] = False

    manifests = replace_cilium_config_manifest(manifests, cilium_config)
    return manifests


def add_bgp_oss_olm(user_settings, manifests, manifests_type, cilium_version, my_output):
    cilium_config = get_cilium_config(manifests)

    cilium_config['spec']['cilium']['bgpControlPlane'] = {}
    cilium_config['spec']['cilium']['bgpControlPlane']['enabled'] = True
    cilium_config['spec']['cilium']['bgpControlPlane']['secretsNamespace'] = {}
    cilium_config['spec']['cilium']['bgpControlPlane']['secretsNamespace']['name'] = 'cilium'
    cilium_config['spec']['cilium']['bgpControlPlane']['secretsNamespace']['create'] = False

    manifests = replace_cilium_config_manifest(manifests, cilium_config)
    return manifests


def add_bgp_oss(user_settings, manifests, manifests_type, cilium_version, my_output):
    if manifests_type == 'clife':
        return add_bgp_oss_clife(user_settings, manifests, manifests_type, cilium_version, my_output)

    if manifests_type == 'olm':
        return add_bgp_oss_olm(user_settings, manifests, manifests_type, cilium_version, my_output)

    return None


def add_bgp(user_settings, manifests, manifests_type, cilium_version, my_output):
    if cilium_version is None:
        my_output.error('Cannot configure bgp without cilium version detection')
        return None

    if 'cee' in cilium_version:
        return add_bgp_cee(user_settings, manifests, manifests_type, cilium_version, my_output)

    return add_bgp_oss(user_settings, manifests, manifests_type, cilium_version, my_output)


def add_srv6(user_settings, manifests, manifests_type, cilium_version, my_output):
    cilium_config = get_cilium_config(manifests)
    manifests = replace_cilium_config_manifest(manifests, cilium_config)
    return manifests


def get_cilium_manifests(user_settings, manifests, my_output, silent=False):
    if not user_settings['cilium']['verify']:
        if not silent:
            my_output.default('Cilium manifests verification disabled')
        return manifests

    if not silent:
        my_output.default('Cilium manifests verification', before_newline=True, underline=True)

    if not user_settings['cilium']['manage']:
        if not silent:
            my_output.default('Cilium manifests managed mode')

    manifests_type = get_cilium_manifests_type(manifests, my_output)
    if manifests_type is None:
        my_output.error('Manifest type detection failed')
        return None

    if not silent:
        my_output.default('- manifests type: %s' % (manifests_type))

    cilium_version = None
    if manifests_type == 'clife':
        cilium_version = get_cilium_manifests_clife_version(
            manifests
        )
        if cilium_version is None:
            if not silent:
                my_output.default('- cilium version: unknown')
        else:
            if not silent:
                my_output.default('- cilium version: %s' % (cilium_version))

    if manifests_type == 'olm':
        cilium_version = get_cilium_manifests_olm_version(
            manifests
        )
        if cilium_version is None:
            if not silent:
                my_output.default('- cilium version: unknown')
        else:
            if not silent:
                my_output.default('- cilium version: %s' % (cilium_version))

    if user_settings['cilium']['manage']:
        manifests = fixup_cilium_manifests(user_settings, manifests, manifests_type)
        if manifests is None:
            return None

        if user_settings['cilium']['kube-proxy']:
            manifests = add_kube_proxy(user_settings, manifests, manifests_type, cilium_version, my_output)
            if manifests is None:
                return None

        if user_settings['cilium']['hubble-metrics']:
            manifests = add_hubble_metrics(manifests, manifests_type)
            if manifests is None:
                return None

        if user_settings['cilium']['bgp'] or user_settings['cilium']['srv6']:
            manifests = add_bgp(user_settings, manifests, manifests_type, cilium_version, my_output)
            if manifests is None:
                return None

        if user_settings['cilium']['srv6']:
            manifests = add_srv6(user_settings, manifests, manifests_type, cilium_version, my_output)
            if manifests is None:
                return None

    if not silent:
        my_output.default(yaml.dump(get_cilium_config(manifests)).replace('QUOTE', '"'), wrap='~~~')

    manifests = validate_cilium_manifests(user_settings, manifests, manifests_type, my_output)
    return manifests
