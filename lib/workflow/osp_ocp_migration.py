import os
import math
import time
import uuid

from lib import file_helper
from lib import template
from lib import ssh
from lib.k8s import output as k8s_output
from lib.osp import output as osp_output

from menu import common


def run(ctx, osp_handlers, osp_virtual_machine_info, k8s_handlers, namespace, vmi, settings, deployment_directory,confirmation_mode=False):
    k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
    osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)

    vmi_filename = os.path.join(deployment_directory, 'vmi.yaml')
    rules_filename = os.path.join(deployment_directory, 'rules.yaml')
    migration_rules = file_helper.get_file_yaml(rules_filename)

    migration_tag = str(uuid.uuid4()).split('-')[-1]
    ctx.my_output.default('Migation tag: %s' % (migration_tag))

    vm_stopped = False
    if osp_handlers.is_virtual_machine_up(osp_virtual_machine_info['id']):
        ctx.my_output.default('Stopping virtual machine')
        if not osp_handlers.stop_virtual_machine(osp_virtual_machine_info['id'], wait=True):
            ctx.my_output.error('Virtual machine stop failed')
            return False

        vm_stopped = True

    ctx.my_output.default('Virtual machine stopped')

    ctx.my_output.default('Create image snapshot of virtual machine')

    osp_virtual_machine_snapshot_image_name = 'migrate-%s' % (migration_tag)
    osp_virtual_machine_snapshot_image_id = osp_handlers.create_image_from_virtual_machine(
        osp_virtual_machine_info['id'],
        osp_virtual_machine_snapshot_image_name
    )
    if osp_virtual_machine_snapshot_image_id is None:
        ctx.my_output.error(
            'Failed to create image snapshot from virtual machine'
        )
        return False

    ctx.my_output.default(
        'Virtual machine image snapshot started: %s' % (
            osp_virtual_machine_snapshot_image_name
        )
    )

    if not osp_handlers.wait_for_image_active(osp_virtual_machine_snapshot_image_id, timeout=600):
        ctx.my_output.error(
            'Wait for image active timed out'
        )
        return False

    time.sleep(10)

    ctx.my_output.default(
        'Virtual machine image snapshot completed: %s' % (
            osp_virtual_machine_snapshot_image_name
        )
    )

    if vm_stopped:
        if confirmation_mode:
            ctx.my_output.default('Start virtual machine in openstack?')
            if not common.get_confirmation():
                return False

        if not osp_handlers.start_virtual_machine(osp_virtual_machine_info['id'], wait=True):
            ctx.my_output.error('Virtual machine start failed')
            return False

        ctx.my_output.default('Virtual machine started')

    osp_virtual_machine_snapshot_image_info = osp_handlers.get_image(image_id=osp_virtual_machine_snapshot_image_id, cache_enabled=False)
    if osp_virtual_machine_snapshot_image_info is None:
        ctx.my_output.error(
            'Failed to find image: %s' % (osp_virtual_machine_snapshot_image_id)
        )
        return False

    osp_virtual_machine_image_filename = '/tmp/migrate-%s' % (migration_tag)
    ctx.my_output.default(
        'Download image %s to local filename %s' % (
            osp_virtual_machine_snapshot_image_name,
            osp_virtual_machine_image_filename
        )
    )

    if not osp_handlers.download_image(osp_virtual_machine_snapshot_image_id, osp_virtual_machine_image_filename):
        ctx.my_output.error(
            'Image download failed'
        )
        return False

    if osp_virtual_machine_snapshot_image_info['checksum'] is None:
        ctx.my_output.default('OSP image checksum unknown. Skipping checksum verification')
    else:
        ctx.my_output.default('Verify checksum')
        local_file_checksum = file_helper.get_md5(osp_virtual_machine_image_filename)
        if local_file_checksum is None:
            ctx.my_output.error(
                'MD5 checksum failed: %s' % (osp_virtual_machine_image_filename)
            )
            return False

        if local_file_checksum != osp_virtual_machine_snapshot_image_info['checksum']:
            ctx.my_output.error(
                'Image checksum does not match'
            )
            ctx.my_output.default(
                'Image %s: %s' % (
                    osp_virtual_machine_snapshot_image_name,
                    osp_virtual_machine_snapshot_image_info['checksum']
                )
            )
            ctx.my_output.default(
                'File %s: %s' % (
                    osp_virtual_machine_image_filename,
                    local_file_checksum
                )
            )
            return False

    ctx.my_output.default('Delete snapshot image: %s' % (osp_virtual_machine_snapshot_image_name))
    if not osp_handlers.delete_image(osp_virtual_machine_snapshot_image_id):
        ctx.my_output.error(
            'Image delete failed'
        )
        return False

    pvc_namespace = namespace
    pvc_name = 'migrate-%s' % (migration_tag)
    if osp_virtual_machine_info['flavor_info']['disk'] == 0:
        ctx.my_output.default(
            'No OSP flavor info. Fallback to default 30Gi pvc size'
        )
        pvc_size = '30Gi'
    else:
        pvc_size = '%sGi' % (math.ceil(osp_virtual_machine_info['flavor_info']['disk'] * 1.05))

    if k8s_handlers.is_pvc(pvc_namespace, pvc_name, cache_enabled=False):
        if k8s_handlers.is_pvc_used(pvc_namespace, pvc_name):
            ctx.my_output.default('PVC %s/%s already exists and is used. It cannot be overwritten.' % (pvc_namespace, pvc_name))
            return False

        if confirmation_mode:
            ctx.my_output.default('PVC %s/%s already exists. Remove it?' % (pvc_namespace, pvc_name))
            if not common.get_confirmation():
                return

        if not k8s_handlers.delete_namespaced_pvc(pvc_namespace, pvc_name):
            ctx.my_output.error('PVC delete failed')
            return False

        ctx.my_output.default('PVC deleted')

    ctx.my_output.default(
        'Creating PVC %s/%s type file size %s from file %s' % (
            pvc_namespace,
            pvc_name,
            pvc_size,
            osp_virtual_machine_image_filename
        )
    )

    success = k8s_handlers.create_pvc_via_data_volume_upload(
        pvc_namespace,
        pvc_name,
        settings['tools'],
        settings['virtctl'],
        source_filename=osp_virtual_machine_image_filename,
        file_type='file',
        size=pvc_size
    )
    if not success:
        ctx.my_output.error('PVC creation failed')
        return False

    ctx.my_output.default('PVC created')

    pvcs = k8s_handlers.get_pvcs(
        object_filter=['namespace:%s' % (pvc_namespace), 'name:%s' % (pvc_name)],
        usage_info=False,
        pv_info=True,
        cache_enabled=False
    )
    k8s_output_handler.print_pvcs(
        pvcs,
        title=False
    )

    remove_file = True
    if confirmation_mode:
        ctx.my_output.default('Remove local image file?')
        if not common.get_confirmation():
            remove_file = False

    if remove_file:
        try:
            os.remove(osp_virtual_machine_image_filename)
            ctx.my_output.default(
                'Local file removed: %s' % (osp_virtual_machine_image_filename)
            )
        except BaseException:
            ctx.my_output.error(
                'Local file remove failed: %s' % (osp_virtual_machine_image_filename)
            )

    ctx.my_output.default('Preparing virtual machine deployment files')
    variables = {}
    variables['NAMESPACE'] = namespace
    variables['NAME'] = vmi
    variables['CORES'] = osp_virtual_machine_info['flavor_info']['vcpus']
    variables['SOCKETS'] = 1
    variables['THREADS'] = 1
    variables['MEMORY'] = '%sM' % (osp_virtual_machine_info['flavor_info']['ram'])
    variables['PVC_NAMESPACE'] = pvc_namespace
    variables['PVC_NAME'] = pvc_name

    interface_index = 1
    for interface_info in osp_virtual_machine_info['interface']:
        variables['INTERFACE_%s_MAC' % (interface_index)] = interface_info['mac']
        interface_index = interface_index + 1

    if 'variables' in migration_rules:
        for key in migration_rules['variables']:
            variables[key] = migration_rules['variables'][key]

    template_handler = template.Template(
        log_id=ctx.run_id
    )

    if 'sriov_network' in migration_rules:
        network_content = {}
        for network_name in migration_rules['sriov_network']:
            network_filename = os.path.join(deployment_directory, '%s.yaml' % (network_name))
            network_content[network_name] = template_handler.get_template(
                network_filename,
                variables,
                replace_variables_enabled=True,
                check_remaining_variables=True,
                yaml_conversion=True
            )
            if network_content[network_name] is None:
                ctx.my_output.error(
                    'Failed to generate network definition: %s' % (network_name)
                )
                return False

            ctx.my_output.default(
                'Preparing sriov network %s/%s' % (
                    network_content[network_name]['metadata']['namespace'],
                    network_content[network_name]['metadata']['name']
                )
            )

            network_mo = k8s_handlers.get_sriov_network(
                network_content[network_name]['metadata']['name'],
                cache_enabled=False,
                return_mo=True
            )
            if network_mo is not None:
                ctx.my_output.error('SRIOV network already exists')
                return False

            if not k8s_handlers.create_sriov_network(network_content[network_name]):
                ctx.my_output.error('SRIOV network create failed')
                return False

            ctx.my_output.default(
                'Network %s/%s created' % (
                    network_content[network_name]['metadata']['namespace'],
                    network_content[network_name]['metadata']['name']
                )
            )

    vmi_content = template_handler.get_template(
        vmi_filename,
        variables,
        replace_variables_enabled=True,
        check_remaining_variables=True,
        yaml_conversion=True
    )
    if vmi_content is None:
        ctx.my_output.error(
            'Failed to generate virtual machine instance definition'
        )
        return False

    ctx.my_output.default('Starting virtual machine instance')
    if not k8s_handlers.create_virtual_machine_instance_mo(vmi_content):
        ctx.my_output.error(
            'Create virtual machine instance request failed'
        )
        return False

    ctx.my_output.default(
        'Virtual machine %s/%s created' % (
            vmi_content['metadata']['namespace'],
            vmi_content['metadata']['name']
        )
    )

    if 'service' in migration_rules:
        service_content = {}
        for service_name in migration_rules['service']:
            service_filename = os.path.join(deployment_directory, '%s.yaml' % (service_name))
            service_content[service_name] = template_handler.get_template(
                service_filename,
                variables,
                replace_variables_enabled=True,
                check_remaining_variables=True,
                yaml_conversion=True
            )
            if service_content[service_name] is None:
                ctx.my_output.error(
                    'Failed to generate service definition: %s' % (service_name)
                )
                return False

            ctx.my_output.default(
                'Preparing service %s: %s/%s' % (
                    service_name,
                    service_content[service_name]['metadata']['namespace'],
                    service_content[service_name]['metadata']['name']
                )
            )

            service_mo = k8s_handlers.get_service(
                service_content[service_name]['metadata']['namespace'],
                service_content[service_name]['metadata']['name'],
                cache_enabled=False,
                return_mo=True
            )
            if service_mo is not None:
                ctx.my_output.error('Service already exists')
                return False

            if not k8s_handlers.create_namespaced_service(service_content[service_name]):
                ctx.my_output.error('Service create failed')
                return False

            ctx.my_output.default(
                'Serice %s/%s created' % (
                    service_content[service_name]['metadata']['namespace'],
                    service_content[service_name]['metadata']['name']
                )
            )

        if migration_rules['ssh']['enabled']:
            ssh_service_name = migration_rules['ssh']['service']
            service_namespace = service_content[ssh_service_name]['metadata']['namespace']
            service_name = service_content[ssh_service_name]['metadata']['name']
            ctx.my_output.default(
                'Wait ssh service %s/%s using (%s,%s) credentials' % (
                    service_namespace,
                    service_name,
                    migration_rules['ssh']['username'],
                    migration_rules['ssh']['password']
                )
            )

            node_ip, node_port = k8s_handlers.get_service_node_ip_port(
                service_namespace,
                service_name,
                cache_enabled=False
            )
            if node_ip is None or node_port is None:
                ctx.my_output.error(
                    'SSH service information failed'
                )
                return False

            ctx.my_output.default(
                'SSH service node port: %s:%s' % (
                    node_ip,
                    node_port
                )
            )
            ssh_handler = ssh.Ssh(
                node_ip,
                migration_rules['ssh']['username'],
                port=node_port,
                password=migration_rules['ssh']['password'],
                endpoint_type=migration_rules['ssh']['type'],
                log_id=ctx.run_id
            )
            if ssh_handler is None:
                ctx.my_output.error(
                    'Failed to initialize ssh session'
                )
                return False

            if not ssh_handler.wait_ssh(timeout=migration_rules['ssh']['timeout']):
                ctx.my_output.error(
                    'SSH check timed out'
                )
                return False

    ctx.my_output.default(
        'Migration completed'
    )

    return True
