import sys
import traceback
import json
import threading
import click

from lib import file_helper
from lib.openshift import api
from lib.openshift import settings
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("login")
@click.pass_obj
@click.option("--token", default='', callback=validations.empty_string_to_none, help="Redhat Console Access Token")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_openshift_login_command(
        ctx,
        token,
        devel
        ):
    """Check openshift console login"""

    ctx.developer = devel
    ctx.output = 'default'

    try:
        if token is None:
            settings_handler = settings.OpenShiftSettings()
            token = settings_handler.get_api_token()
            ctx.my_output.debug('Token: %s' % (token))

        ctx.my_output.debug('Checksum: %s' % (file_helper.get_string_md5(token)))

        api_handler = api.Api(token, log_id=ctx.run_id)
        access_token = api_handler.get_access_token()
        if access_token is None:
            ctx.my_output.error('Authentication with token failed')
            raise ErrorExit

        ctx.my_output.default('Authentication successful')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
