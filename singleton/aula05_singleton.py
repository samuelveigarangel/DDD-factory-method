# Singletons e Metaclasses

class MetaSingleton(type):
    __instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            cls.__instance[cls] = super().__call__(*args, **kwargs)
        return cls.__instance[cls]


class Logger(metaclass=MetaSingleton):
    pass


log1 = Logger()
log2 = Logger()

print(id(log1))
print(id(log2))
