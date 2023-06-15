import os
import sys
import click

from lib import iaccount_helper


@click.command("add")
@click.pass_obj
@click.argument("iaccount-name", required=True, type=click.STRING)
@click.argument("pem-filename", required=True, type=click.STRING)
@click.argument("key-id", required=True, type=click.STRING)
def settings_iaccount_add_command(ctx, iaccount_name, pem_filename, key_id):
    """Create Intersight Account"""

    # iserver settings iaccount add

    iaccount_handler = iaccount_helper.IntersightAccount()

    if iaccount_handler.is_iaccount(iaccount_name):
        ctx.my_output.error('iaccount %s already defined' % (iaccount_name))
        sys.exit(1)

    if not os.path.isfile(pem_filename):
        ctx.my_output.error('pem file not found: %s' % (pem_filename))
        sys.exit(1)

    configuration = {}
    configuration['keyfile'] = pem_filename
    configuration['keyid'] = key_id
    configuration['output'] = 'default'
    configuration['server'] = 'intersight.com'

    if not iaccount_handler.create_iaccount(iaccount_name, configuration):
        ctx.my_output.error('Intersight Account create failed')
        sys.exit(1)

    ctx.my_output.default('Added')
