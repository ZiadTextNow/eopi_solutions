from protocol.errors import EOPINotImplementedError


class Problem8P1(object):
    class StackWithMax(object):
        def max(self):
            raise EOPINotImplementedError()

        def push(self, elem):
            raise EOPINotImplementedError()

        def pop(self):
            raise EOPINotImplementedError()
