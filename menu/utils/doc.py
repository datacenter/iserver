import sys
import click

from lib import self_doc


@click.command("doc")
@click.pass_obj
@click.option("--results", "directory", is_flag=False, show_default=False, default='results', help="Results directory")
@click.option("--template", "template_names", multiple=True, help="Select template")
@click.option("--no-redfish", is_flag=True, show_default=True, default=False, help="Disable redfish tests")
@click.option("--generate", is_flag=True, show_default=True, default=False, help="Generate template from template")
@click.option("--replace", multiple=True, help="Replace pattern:value")
def utils_doc_command(ctx, directory, template_names, no_redfish, generate, replace):
    """Generate documentation"""

    # iserver utils doc

    if generate:
        success = self_doc.generate_template_docs(
            template_names
        )

    replace_dir = {}
    for item in replace:
        replace_dir[item.split(':')[0]] = item.split(':')[1]

    success = self_doc.generate_docs(
        directory,
        template_names,
        redfish_tests=not no_redfish,
        replace=replace_dir
    )

    if not success:
        sys.exit(1)
