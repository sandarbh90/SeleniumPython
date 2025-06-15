import inspect

class Helper:

    @staticmethod
    def whoami():
        return inspect.stack()[1][3]