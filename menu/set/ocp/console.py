import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_console import set


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("console")
@click.pass_obj
@click.option("--token", default='', callback=validations.empty_string_to_none, help="Token: https://console.redhat.com/openshift/token")
@click.option("--secret", default='', callback=validations.empty_string_to_none, help="Pull secret: https://console.redhat.com/openshift/install/pull-secret")
def set_ocp_console_command(
        ctx, 
        token, 
        secret
    ):
    """Set openshift console api credentials"""

    try:
        params = {}
        params['token'] = token
        params['secret'] = secret

        success = set.run(
            params,
            log_id=ctx.run_id
        )
        if not success:
            raise ErrorExit    
    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
