class A:
    def __init__(self):
        self.name = 'disen'

    def __enter__(self):
        return ['a', 'b', 'c']

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_val)

        return True  # 返回True时，异常处理结束, False表示异常继续下去


if __name__ == '__main__':
    a = A()
    with a as la:
        print(a)
        raise Exception('数据量太少')
