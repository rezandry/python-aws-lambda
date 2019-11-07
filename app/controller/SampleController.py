from app.decorator.Api import Api
from ..service.SampleService import SampleService


class SampleController:

    __service = SampleService()

    @classmethod
    @Api.route(path='/hello', method='GET')
    def hello_world(cls):
        return cls.__service.hello_world()