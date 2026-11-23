import os
import sys
import traceback
import click

from menu import validations
from lib import file_helper
from lib.workflow.task import delete as task_handler
from lib.workflow import ocp_common


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("task")
@click.pass_obj
@click.option("--cluster", "cluster_names", multiple=True, callback=validations.validate_ocp_cluster_names, help="Cluster name")
@click.option("--filename", default='', callback=validations.validate_file_absolute, help="Tasks filename")
@click.option("--validate", "validate_only", is_flag=True, show_default=True, default=False, help="Validate only")
@click.option("--no-break", is_flag=True, show_default=True, default=False, help="Break on error")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def delete_ocp_task_command(
        ctx, 
        cluster_names, 
        filename,
        validate_only,
        no_break,
        no_confirm
    ):
    """Delete openshift cluster tasks"""

    try:
        content = file_helper.get_file_json(filename)
        if content is None:
            ctx.my_output.error('File read failed: %s' % (filename))
            raise ErrorExit
        
        tasks = ocp_common.untangle_tasks(
            cluster_names, 
            content,
            directory=os.path.dirname(filename),
            confirmation=not no_confirm,
            break_on_error=not no_break
        )

        success = task_handler.run(
            tasks,
            validate_only=validate_only,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit
                        
    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
