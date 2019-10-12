#
#
# def deco(func):
#     def wrapper(*args, **kwargs):  # *args, **kwargs用于接收func的参数
#         print("入参", *args, "和", **kwargs)\
#
#         last = 0
#         arr = []
#         print(type(args))
#         for v in args:
#             last += v
#             arr.append(v)
#         arr.append(last)
#         func(last, 12, **kwargs)
#         print("func的地址：", func)
#     return wrapper
#
#
# @deco
# def myfunc(a, b):
#     print("myfunc的地址：",myfunc)
#     print(a+b)
#
#
# # myfunc = deco(myfunc) # 与上面的@deco等价
# myfunc(1, 2)
# print("***********")
# print("修改后myfunc的地址：",myfunc)


# def attrs(**kwds):
#     def decorate(s):
#         for k in kwds:
#             setattr(s, k, kwds[k])
#         return s
#
#     return decorate
#
#
# @attrs(versionadded="2.2",
#        author="Guido van Rossum")
# def mymethod(args):
#     print(getattr(mymethod,'versionadded',0))
#     print(getattr(mymethod,'author',0))
#     print(args)
#
#
# if __name__ == "__main__":
#     mymethod(2)
#     print("进入下{}, 个{}期".format("一个", "周"))
#


def three(text):
    def one(func):
        print("now you are in function one.")

        def warp(*args):
            func(*args)

        return warp

    print("input params is {}".format(text))
    return one


@three(text=5)
def two(x, y):
    print("now you are in function two.")
    print("x value is %d, y value is %d" % (x, y))


two(5, 6)
'''
input params is 5
now you are in function one.
now you are in function two.
x value is 5, y value is 6
'''
