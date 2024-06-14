def validate_view(user_input, all_views, default, resolve):
    views = []

    if len(user_input) == 0:
        view = [default]
        return view

    user_views = []
    for item in user_input:
        user_views = user_views + item.split(',')

    defined_views = all_views.split('|')
    resolve_views = {}
    for item in resolve:
        (resolve_name, resolve_view) = item.split(':')
        resolve_views[resolve_name] = resolve_view

    for user_view in user_views:
        if user_view not in defined_views:
            return None

        if user_view == 'all':
            for defined_view in defined_views:
                if defined_view not in ['all', 'verbose'] and defined_view not in views and defined_view not in resolve_views:
                    views.append(
                        defined_view
                    )
            continue

        if user_view in resolve_views:
            for resolve_view in resolve_views[user_view].split(','):
                if resolve_view not in views:
                    views.append(
                        resolve_view
                    )

            continue

        if user_view not in views:
            views.append(
                user_view
            )

    return views