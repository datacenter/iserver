def print_cache_ttl(ctx, output, cache_ttl):
    if output == 'default':
        if cache_ttl < 0:
            ctx.my_output.default('IMC cache disabled')
            return

        if cache_ttl == 0:
            ctx.my_output.default('IMC cache enabled: ttl any')
            return

        if cache_ttl > 0:
            ctx.my_output.default('IMC cache enabled: ttl %s seconds' % (cache_ttl))
            return
