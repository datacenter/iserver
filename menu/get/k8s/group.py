import sys
import traceback
import click

from menu.get.k8s import common
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("group")
@click.pass_obj
@click.option("--cluster", default='', help="Cluster name")
@click.option("--name", default='', callback=validations.empty_string_to_none, help="Filter by name")
@click.option("--ldap-host", default='', callback=validations.empty_string_to_none, help="Synced from ldap host")
@click.option("--ldap", is_flag=True, show_default=True, default=False, help="Synced from ldap")
@click.option("--view", "-v", default=['state'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'mo', 'json'], case_sensitive=False), default='default', show_default=True)
def get_k8s_group_command(
        ctx,
        cluster,
        name,
        ldap_host,
        ldap,
        view,
        output
        ):
    """Get k8s group"""

    try:
        filter_params = dict(name=name)
        if ldap_host is not None:
            filter_params['ldap_host'] = ldap_host
            filter_params['ldap'] = 'true'

        if ldap_host is None and ldap:
            filter_params['ldap'] = 'true'

        success = common.get(
            ctx,
            cluster,
            'group',
            output,
            view,
            'state (def)',
            cluster_type='ocp',
            filter_params=filter_params,
            get_params=dict(user_info=True)
        )
        if not success:
            raise ErrorExit
        
    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
