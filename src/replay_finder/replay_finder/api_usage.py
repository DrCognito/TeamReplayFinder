from .model import WebAPIUsage, get_api_usage
from .__init__ import WEB_API_LIMIT
from .exceptions import APIOverLimit


class DecoratorUsageCheck():

    def __init__(self, session, api, limit):
        self.session = session
        self.api = api
        self.limit = limit

    def __call__(self, function):
        def wrapped_func(*args):
            usage = self.api(self.session)
            if usage.api_calls > self.limit:
                raise APIOverLimit("API limit exceeded.")
            try:
                return function(*args)
            except:
                raise
            finally:
                usage.api_calls += 1
                self.session.merge(usage)
                self.session.commit()

        return wrapped_func