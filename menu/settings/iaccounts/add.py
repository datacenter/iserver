import os
import sys
import click

from lib import iaccount_helper


@click.command("add")
@click.pass_obj
@click.option("--name", default='', help="Name")
@click.option("--pem", default='', help="PEM filename")
@click.option("--key", default='', help="Key")
@click.option("--server", default='intersight.com', help="Server")
def settings_iaccount_add_command(ctx, name, pem, key, server):
    """Create Intersight Account"""

    # iserver settings iaccount add

    if len(name) == 0:
        ctx.my_output.error('Define iaccount name')
        sys.exit(1)

    if len(pem) == 0:
        ctx.my_output.error('Define pem filename')
        sys.exit(1)

    if not os.path.isfile(pem):
        ctx.my_output.error('pem file not found: %s' % (pem))
        sys.exit(1)

    if len(key) == 0:
        ctx.my_output.error('Define key')
        sys.exit(1)

    iaccount_handler = iaccount_helper.IntersightAccount()

    if iaccount_handler.is_iaccount(name):
        ctx.my_output.error('iaccount %s already defined' % (name))
        sys.exit(1)

    configuration = {}
    configuration['keyfile'] = pem
    configuration['keyid'] = key
    configuration['output'] = 'default'
    configuration['server'] = server

    if not iaccount_handler.create_iaccount(name, configuration):
        ctx.my_output.error('Intersight Account create failed')
        sys.exit(1)

    ctx.my_output.default('Added')
