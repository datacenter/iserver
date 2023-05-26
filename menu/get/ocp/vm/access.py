import sys
import threading
import traceback
import click

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("access")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', help="OCP cluster name")
@click.option("--yaml", "vm_filename", is_flag=False, show_default=False, default='', type=click.STRING, help="VM Definition YAML")
def get_ocp_vm_access_command(
        ctx,
        cluster_name,
        vm_filename
        ):
    """Get ocp virtual machine access info"""

    # iserver get ocp vm access

    ctx.developer = False
    ctx.output = 'default'

    try:
        if len(vm_filename) == 0:
            ctx.my_output.error('Define virtual machine deployment filename')
            raise ErrorExit

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        validated_input = validations.validate_ocp_vm_yaml_file(ctx, vm_filename)
        if validated_input is None:
            ctx.busy = False
            raise ErrorExit

        ocp_handler = validations.validate_ocp_cluster(
            ctx,
            cluster_name,
            verbose=False,
            debug=False
        )
        if ocp_handler is None:
            raise ErrorExit

        namespace = validated_input['deployment']['namespace']
        vm_name = validated_input['deployment']['name']

        if not ocp_handler.is_ocp_vmi(namespace, vm_name):
            ctx.busy = False
            ctx.my_output.default(
                'Virtual machine %s/%s is not running' % (
                    namespace,
                    vm_name
                )
            )
            raise ErrorExit

        info = ocp_handler.get_ocp_vms_info(
            name=vm_name,
            namespace=namespace
        )

        if info['special'] is None:
            ctx.busy = False
            ctx.my_output.default(
                'Virtual machine %s/%s does not have special label' % (
                    namespace,
                    vm_name
                )
            )
            raise ErrorExit

        services = ocp_handler.get_ocp_vm_services_ip_port(
            info['special'],
            deployment=validated_input
        )

        ctx.busy = False

        ocp_handler.print_deployment_service_access_info(
            services
        )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
