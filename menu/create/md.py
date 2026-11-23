import os
import sys
import traceback
import click

from lib.md import main as md
from lib.xd import main as xd

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("md")
@click.pass_obj
@click.option("--domain", "domain_name", default='', callback=validations.empty_string_to_none, help="Domain name")
@click.option("--dir", "md_directory", default='', callback=validations.empty_string_to_none, help="Target directory")
@click.option("--ttl", "user_cache_ttl", default=1, help="Cache TTL in seconds")
@click.option("--partial", "allow_partial", is_flag=True, show_default=True, default=False, help="Allow partial preparation")
@click.option("--step", type=click.Choice(['all', 'prepare', 'xd', 'md'], case_sensitive=False), default='all', show_default=True, help="Select execution steps")
@click.option("--module", "prepare_modules", multiple=True, default=[], show_default=True, help="Prepare modules")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_md_command(
        ctx,
        domain_name,
        md_directory,
        user_cache_ttl,
        allow_partial,
        step,
        prepare_modules,
        devel
        ):
    """Create git documentation"""

    ctx.developer = devel
    ctx.output = 'default'
    ctx.my_output.set_debug()

    try:
        if step in ['all', 'md']:
            if md_directory is None:
                print('Define md directory')
                raise ErrorExit

            if not os.path.isdir(md_directory):
                print('Directory does not exist: %s' % (md_directory))
                raise ErrorExit

        xd_handler = xd.CrossDomain(log_id=ctx.run_id, debug=True)
        if step in ['all', 'prepare']:
            if len(prepare_modules) == 0:
                items = None
            else:
                items = []
                for item in prepare_modules:
                    items.append(item)

            success = xd_handler.prepare(
                domain_name,
                user_cache_ttl,
                allow_partial=allow_partial,
                prepare_modules=items
            )
            if not success:
                ctx.my_output.error('Preparation failed')
                raise ErrorExit

        if step in ['all', 'xd']:
            success = xd_handler.run(domain_name)
            if not success:
                ctx.my_output.error('Cross domain analysis failed')
                raise ErrorExit

        if step in ['all', 'md']:
            md_handler = md.Md(domain_name, md_directory, log_id=ctx.run_id)
            md_handler.print()

    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
