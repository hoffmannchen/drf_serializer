class MyResponse():
    def __init__(self):
        self.status = 100
        self.msg = '成功'

    @property
    def get_dict(self):
        return self.__dict__
