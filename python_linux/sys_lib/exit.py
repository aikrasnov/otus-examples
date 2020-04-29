import time
import sys

def bar():
    print("exit from bar")
    exit(1)

def foo():
    try:
        print("call bar")
        bar()
    except SystemExit:
        print("handle systemexit")
    finally:
        print("Finally block (exit) of foo")

foo()
# time.sleep(30)
# print("\n\n\n#####\n\n\n")
#
# def bar_se():
#     raise SystemExit(1)
#
# def foo_se():
#     try:
#         print("call bar")
#         bar_se()
#     except:
#         pass
#     finally:
#         print("Finally block (by SystemExit) in foo")
#
# foo_se()
