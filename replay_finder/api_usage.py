from .model import APIUsage, get_api_usage
from .__init__ import WEB_API_LIMIT
from .exceptions import WebAPIOverLimit


class DecoratorUsageCheck():

    def __init__(self, session):
        self.session = session

    def __call__(self, function):
        def wrapped_func(*args):
            usage = get_api_usage(self.session)
            if usage.api_calls > WEB_API_LIMIT:
                raise WebAPIOverLimit("Web API limit exceeded.")
            try:
                return function(*args)
            except:
                raise
            finally:
                usage.api_calls += 1
                self.session.merge(usage)
                self.session.commit()

        return wrapped_func