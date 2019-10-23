import time

def bar():
    print("exit from bar")
    exit(1)

def foo():
    try:
        print("call bar")
        bar()
    except:
        pass
    finally:
        print("Finally block (exit)")

foo()
time.sleep(30)
print("\n\n\n#####\n\n\n")

def bar_se():
    raise SystemExit(1)

def foo_se():
    try:
        bar_se()
    except:
        pass
    finally:
        print("Finally block (by SystemExit)")

foo_se()
