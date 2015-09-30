from tempest_lib import exceptions


def check_jio_policy(function):
    def decorator(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except exceptions.Forbidden:
            pass
    return decorator
