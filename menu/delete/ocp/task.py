import os
import sys
import traceback
import click

from menu import validations
from lib import file_helper
from lib.workflow.ocp_task import delete as task_handler


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("task")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--filename", "filename", default='', callback=validations.validate_file, help="Tasks filename")
@click.option("--validate", "validate_only", is_flag=True, show_default=True, default=False, help="Validate only")
@click.option("--break", "break_on_error", is_flag=True, show_default=True, default=False, help="Break on error")
@click.option("--no-reverse", is_flag=True, show_default=True, default=False, help="No reverse")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_task_command(
        ctx, 
        cluster_name, 
        filename,
        validate_only,
        break_on_error,
        no_reverse,
        no_confirm
    ):
    """Delete openshift cluster tasks"""

    try:
        content = file_helper.get_file_json(filename)
        if content is None:
            ctx.my_output.error('File ready failed: %s' % (filename))
            raise ErrorExit
        
        k8s_handler = validations.validate_kubernetes_name(ctx, cluster_name, cluster_type='ocp', log_id=ctx.run_id, silent=True)

        cluster_settings = {}
        cluster_settings['directory'] = os.path.dirname(filename)

        success = task_handler.run(
            content,
            cluster_name,
            confirmation=not no_confirm,
            cluster_settings=cluster_settings,
            k8s_handler=k8s_handler,
            validate_only=validate_only,
            break_on_error=break_on_error,
            reverse=not no_reverse,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit
        
    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
