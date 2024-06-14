import os
import sys
import uuid
import traceback
import click

from lib import file_helper
from lib.k8s import output as k8s_output
from lib.osp import output as osp_output
from lib.workflow import osp_ocp_migration

from menu import common
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("migrate")
@click.pass_obj
@click.option("--osp", "osp_cluster_name", is_flag=False, show_default=False, default='', type=click.STRING, help="OpenStack Cluster Name")
@click.option("--src", "source_name", is_flag=False, show_default=False, default='', type=click.STRING, help="OpenStack Virtual Machine Name")
@click.option("--ocp", "ocp_cluster_name", is_flag=False, show_default=False, default='', type=click.STRING, help="OpenShift Cluster Name")
@click.option("--dest", "destination_name", is_flag=False, show_default=False, default='', type=click.STRING, help="OpenShift Virtual Machine Name")
@click.option("--rule", "deployment_directory", is_flag=False, show_default=False, default='', type=click.STRING, help="Migration rules directory")
@click.option("--confirm", "confirmation_mode", is_flag=True, show_default=False, default=False, help="Confirmation mode")
def create_ocp_migrate_command(
        ctx,
        osp_cluster_name,
        source_name,
        ocp_cluster_name,
        destination_name,
        deployment_directory,
        confirmation_mode
        ):
    """Migrate virtual machine"""

    # iocp create ocp migrate

    try:
        osp_output_handler = osp_output.OspOutput(log_id=ctx.run_id)
        if len(osp_cluster_name) == 0:
            osp_cluster_name = validations.select_osp_name(ctx)
            if osp_cluster_name is None:
                raise ErrorExit
            osp_handlers = validations.validate_osp_name(ctx, osp_cluster_name, silent=True)
        else:
            osp_handlers = validations.validate_osp_name(ctx, osp_cluster_name, silent=False)
        if osp_handlers is None:
            raise ErrorExit

        if len(source_name) == 0:
            ctx.my_output.default('Get virtual machines...', after_newline=True)

            vms = osp_handlers.get_virtual_machines(
                object_filter=[],
                tenant_info=True,
                flavor_info=True,
                image_info=True,
                volume_info=True,
                network_info=True,
                subnet_info=True
            )
            osp_virtual_machine_info = osp_output_handler.select_virtual_machine(vms)
            if osp_virtual_machine_info is None:
                raise ErrorExit

        else:
            if len(source_name.split('/')) != 2:
                ctx.my_output.error('Source format: <tenant>/<vm>')
                raise ErrorExit

            (tenant_name, vm_name) = source_name.split('/')
            osp_virtual_machine_info = osp_handlers.get_virtual_machine_by_name(
                vm_name,
                tenant_name=tenant_name,
                tenant_info=True,
                flavor_info=True,
                image_info=True,
                volume_info=True,
                network_info=True,
                subnet_info=True
            )

            if osp_virtual_machine_info is None:
                ctx.my_output.error('Virtual machine not found: %s/%s' % (tenant_name, vm_name))
                raise ErrorExit

            osp_output_handler.print_virtual_machines(
                [osp_virtual_machine_info]
            )

            osp_output_handler.print_virtual_machines_net(
                [osp_virtual_machine_info]
            )

        if len(ocp_cluster_name) == 0:
            ocp_cluster_name = validations.select_ocp_name(ctx)
            if osp_cluster_name is None:
                raise ErrorExit

        k8s_output_handler = k8s_output.K8sOutput(log_id=ctx.run_id)
        settings = validations.validate_ocp_cluster_settings(ctx, ocp_cluster_name, silent=True)
        if settings is None:
            raise ErrorExit

        if settings['virtctl'] is None:
            ctx.my_output.error('Virtctl not defined for cluster %s' % (settings['name']))
            raise ErrorExit

        k8s_handlers = validations.validate_kubernetes_name(ctx, ocp_cluster_name, cluster_type='ocp')
        if k8s_handlers is None:
            raise ErrorExit

        if len(destination_name) == 0:
            ctx.my_output.default('Get namespaces...', after_newline=True)

            namespaces = k8s_handlers.get_namespaces()
            namespace_info = k8s_output_handler.select_namespace(namespaces)
            namespace = namespace_info['name']
            if namespace is None:
                raise ErrorExit

            ctx.my_output.default('Get virtual machines...', before_newline=True, after_newline=True)

            object_filter = []
            object_filter.append(
                'namespace:%s' % (namespace)
            )
            virtual_machine_instances = k8s_handlers.get_virtual_machine_instances(
                object_filter=object_filter,
                vm_info=True,
                service_info=False
            )

            k8s_output_handler.print_virtual_machine_instances(
                virtual_machine_instances,
                title=True
            )

            vmi = input('Target virtual machine name (empty to autogenerate): ')
            if len(vmi) == 0:
                vmi = str(uuid.uuid4()).split('-')[-1]
                ctx.my_outpu.default('Generated name: %s' % (vmi))

            if k8s_handlers.is_virtual_machine_instance(namespace, vmi):
                ctx.my_output.default('Virtual machine found: %s/%s' %  (namespace, vmi))
                raise ErrorExit

        else:
            if len(destination_name.split('/')) > 2:
                ctx.my_output.error('Destination format: <namespace>/<name>')
                raise ErrorExit

            if len(destination_name.split('/')) == 1:
                namespace = 'default'
                vmi = destination_name

            if len(destination_name.split('/')) == 2:
                (namespace, vmi) = destination_name.split('/')

            if not k8s_handlers.is_namespace(namespace):
                ctx.my_output.error('Namespace not found: %s/%s' % (tenant_name, vm_name))
                raise ErrorExit

            if k8s_handlers.is_virtual_machine_instance(namespace, vmi):
                ctx.my_output.default('Virtual machine found: %s/%s' %  (namespace, vmi))
                raise ErrorExit

        if len(deployment_directory) == 0:
            deployment_directory = input('Rule files directory: ')
            if len(deployment_directory) == 0:
                raise ErrorExit

        if not os.path.isdir(deployment_directory):
            ctx.my_output.error('Directory does not exist: %s' % (deployment_directory))
            raise ErrorExit

        rules_filename = os.path.join(deployment_directory, 'rules.yaml')
        if not os.path.isfile(rules_filename):
            ctx.my_output.error(
                'Virtual machine migration rules not found: %s' % (rules_filename)
            )
            raise ErrorExit

        migration_rules = file_helper.get_file_yaml(rules_filename)
        if migration_rules is None:
            ctx.my_output.error(
                'Failed to read virtual machine migration rules: %s' % (rules_filename)
            )
            raise ErrorExit

        vmi_filename = os.path.join(deployment_directory, 'vmi.yaml')
        if not os.path.isfile(vmi_filename):
            ctx.my_output.error(
                'Virtual machine instance file not found: %s' % (vmi_filename)
            )
            raise ErrorExit

        if 'service' in migration_rules:
            for service_name in migration_rules['service']:
                service_filename = os.path.join(deployment_directory, '%s.yaml' % (service_name))
                if not os.path.isfile(service_filename):
                    ctx.my_output.error(
                        'Service file not found: %s' % (service_filename)
                    )
                    raise ErrorExit

        if 'sriov_network' in migration_rules:
            for network_name in migration_rules['sriov_network']:
                network_filename = os.path.join(deployment_directory, '%s.yaml' % (network_name))
                if not os.path.isfile(network_filename):
                    ctx.my_output.error(
                        'SRIOV network file not found: %s' % (network_filename)
                    )
                    raise ErrorExit

        ctx.my_output.default('Rules valid')

        if confirmation_mode and not common.get_confirmation():
            raise ErrorExit

        success = osp_ocp_migration.run(
            ctx,
            osp_handlers,
            osp_virtual_machine_info,
            k8s_handlers,
            namespace,
            vmi,
            settings,
            deployment_directory,
            confirmation_mode=confirmation_mode
        )
        if not success:
            raise ErrorExit

        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )

        object_filter.append(
            'name:%s' % (vmi)
        )

        virtual_machine_instances = k8s_handlers.get_virtual_machine_instances(
            object_filter=object_filter,
            vm_info=True,
            service_info=True,
            cache_enabled=False
        )

        k8s_output_handler.print_virtual_machine_instances(
            virtual_machine_instances,
            title=False
        )

        k8s_output_handler.print_virtual_machine_instances_phase(
            virtual_machine_instances,
            title=False
        )

        k8s_output_handler.print_virtual_machine_instances_interface(
            virtual_machine_instances,
            title=False
        )

        k8s_output_handler.print_virtual_machine_instances_service(
            virtual_machine_instances,
            title=False
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
