import sys
import json
import threading
import traceback
import click

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("file")
@click.pass_obj
@click.option("--yaml", "vm_filename", is_flag=False, show_default=False, default='', type=click.STRING, help="VM Definition YAML")
def get_ocp_vm_file_command(
        ctx,
        vm_filename
        ):
    """Get ocp virtual machine deployment files"""

    # iserver get ocp vm file

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

        ctx.busy = False

        for filename in validated_input['files']:
            ctx.my_output.default(
                'Filename: %s' % (filename),
                underline=True,
                before_newline=True
            )
            ctx.my_output.default(
                validated_input['files'][filename]
            )

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
