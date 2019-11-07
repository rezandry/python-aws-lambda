from ..vo.BaseResultVO import BaseResultVO


class SampleService:

    @classmethod
    def hello_world(cls):
        result = {'data': 'hello world'}
        return BaseResultVO(result=result)