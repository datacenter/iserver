import sys
import click
from lib import file_helper
from lib.openshift import helper
from menu import validations


@click.command("login")
@click.pass_obj
@click.option("--token", default='', callback=validations.empty_string_to_none, help="Redhat Console Access Token")
def get_openshift_login_command(
        ctx,
        token
        ):
    """Check openshift console login"""

    ctx.developer = False
    ctx.output = 'default'

    if token is None:
        token = helper.get_token()
        if token is None:
            ctx.my_output.error('OpenShift token not defined')
            sys.exit(1)

    ctx.my_output.default('Token: %s' % (token))
    ctx.my_output.default('Checksum: %s' % (file_helper.get_string_md5(token)))

    helper.check_openshift_authentication(
        my_output=ctx.my_output,
        log_id=ctx.run_id
    )