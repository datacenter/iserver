import sys
import traceback
import click

from menu import validations
from lib.workflow.ocp_identity_htpasswd import add as ocp_add_workflow
from menu import user_inputs


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("htpasswd")
@click.pass_obj
@click.option("--cluster", "cluster_name", is_flag=False, show_default=False, default='', callback=validations.validate_ocp_cluster_name_no_prompt, type=click.STRING, help="Cluster Name")
@click.option("--provider", "provider_name", is_flag=False, show_default=False, default='', callback=validations.empty_string_to_none, type=click.STRING, help="HTPasswd Provider Name")
@click.option("--filename", "htpasswd_filename", multiple=True, help="htpasswd filename")
@click.option("--user", "userpass", is_flag=False, multiple=True, help="User:pass entries")
@click.option("--admin", "admins", is_flag=False, multiple=True, help="Admin users")
@click.option("--mode", type=click.Choice(['post', 'patch'], case_sensitive=False), default='patch', show_default=True, help="Mode of operation")
@click.option("--no-confirm", is_flag=True, show_default=True, default=False, help="Confirmation mode")
def set_ocp_htpasswd_command(ctx, cluster_name, provider_name, htpasswd_filename, userpass, admins, mode, no_confirm):
    """Set identity htpasswd in openshift cluster"""

    try:
        if provider_name is None:
            provider_name = user_inputs.get_value(ctx, prompt='Provider name', empty=True)
            if len(provider_name) == 0:
                raise ErrorExit

        if len(htpasswd_filename) == 0 and len(userpass) == 0 and len(admins) == 0:
            value = user_inputs.get_value(ctx, prompt='htpasswd file (comma-seperated)', empty=True)
            if len(value) > 0:
                htpasswd_filename = value.split(',')

            value = user_inputs.get_value(ctx, prompt='user:pass (comma-separated)', empty=True)
            if len(value) > 0:
                userpass = value.split(',')
                value = user_inputs.get_value(ctx, prompt='admins (comma-separated or __ALL__)', empty=True)
                if len(value) > 0:
                    admins = value.split(',')

        params = {}
        params['cluster'] = cluster_name
        params['provider'] = provider_name
        params['filename'] = htpasswd_filename
        params['userpass'] = userpass
        params['admins'] = admins
        params['mode'] = mode
        params['confirmation'] = not no_confirm

        success = ocp_add_workflow.run(
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
