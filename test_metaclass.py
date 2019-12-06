

# class Singleton(type):
#
#     _instances = {}
#
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
#
#
#
# class MyClass(metaclass=Singleton):
#     pass
#
#
# if __name__ == '__main__':
#     my1 = MyClass()
#     my2 = MyClass()
#     if my1 == my2:
#         print('ss')
#     else:
#         print('nn')




# # 强制 某个类的子类 必须实现 bar() 函数的 元类定义
#
# class BarMeta(type):
#     def __new__(cls, name, bases, namespace, **kwargs):
#         # 类名不是基类，且 函数 'bar' 也不在  自己的 namespace 中 (即: 未定义 bar 函数)
#         if name != 'Base' and 'bar' not in namespace:
#             raise TypeError('bad user class')
#         return super().__new__(cls, name, bases, namespace, **kwargs)
#
# class Base(object, metaclass=BarMeta):
#     def foo(self):
#         return self.bar()
#
#
# class Derived(Base):
#     def aar():
#         return None
#
#
# if __name__ == '__main__':
#     d = Derived()



# 查看哪些类继承了基类 Fruit
class FruitMeta(type):
    # @param cls: 类
    # @param name: 类名称
    # @param bases: 基类
    # @param namespace: 所在空间, {'__module__': '__main__', '__qualname__': 'Apple', 'aar': <function Apple.aar at 0x7fa5b6126158>}
    # @param kwargs: 其他入参
    def __init__(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        print('cls', cls)
        print('name', name)
        print('bases', bases)
        print('namespace', namespace)
        print('kwargs', kwargs)

        if not hasattr(cls, 'registory'):
            # this is the base class
            cls.registory = {}
        else:
            # this is the subclass
            cls.registory[name.lower()] = cls


class Fruit(object, metaclass=FruitMeta):
    pass

class Apple(Fruit):
    def aar():
        return None

class Orange(Fruit):
    pass


if __name__ == '__main__':
    print(Fruit.registory)
