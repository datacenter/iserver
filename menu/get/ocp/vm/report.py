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


@click.command("report")
@click.pass_obj
@click.option("--cluster", "cluster_name", default='', help="OCP cluster name")
@click.option("--yaml", "vm_filename", is_flag=False, show_default=False, default='', type=click.STRING, help="VM Definition YAML")
@click.option("--sections", "-s", type=click.Choice(['all', 'kvm', 'ssh', 'oc', 'snmp', 'netconf'], case_sensitive=False), default='all', show_default=True)
def get_ocp_vm_report_command(
        ctx,
        cluster_name,
        vm_filename,
        sections
        ):
    """Get ocp virtual machine report"""

    # iserver get ocp vm report

    ctx.developer = False
    ctx.output = 'default'

    try:
        if len(vm_filename) == 0:
            ctx.my_output.error('Define virtual machine deployment filename')
            raise ErrorExit

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        user_input = validations.validate_ocp_vm_yaml_file(ctx, vm_filename)
        if user_input is None:
            raise ErrorExit

        ocp_handler = validations.validate_ocp_cluster(
            ctx,
            cluster_name,
            verbose=False,
            debug=False
        )
        if ocp_handler is None:
            raise ErrorExit

        namespace = user_input['deployment']['namespace']
        vm_name = user_input['deployment']['name']

        if not ocp_handler.is_ocp_vmi(namespace, vm_name):
            ctx.busy = False
            ctx.my_output.default(
                'Virtual machine %s/%s is not running' % (
                    namespace,
                    vm_name
                )
            )

        ctx.busy = False

        ctx.my_output.default(
            'Virtual machine %s/%s is running' % (
                namespace,
                vm_name
            )
        )

        if not ocp_handler.create_vm_state_report(user_input, sections=sections):
            raise ErrorExit

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
