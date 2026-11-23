import traceback
import click


def default_from_context(default_name):

    class OptionDefaultFromContext(click.Option):

        def get_default(self, ctx, call=False):
            try:
                self.default = ctx.obj.defaults[default_name]
                return super(OptionDefaultFromContext, self).get_default(ctx)
            except BaseException:
                print(traceback.format_exc())
                return None

    return OptionDefaultFromContext
