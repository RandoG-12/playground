# functional programming in python
# passing functions around like the sluts they are!

def announce(f):
    def wrapper():
        print("announce decorator: Before run of function...")
        f()
        print("announce decorator: After run of function...")
    return wrapper

def ignore(f):
    def wrapper():
        print("ignore decorator: I am ignoring whatever you wrote.")
    return wrapper

def hello():
    print("hello: Hello bastages - no decorator.")

@announce
def hello_announce():
    print("hello_announce: Hello bastages - with decorator.")

@ignore
def hello_ignore():
    print("hello_ignore: Hello, do not ignore me! - with decorator.")

    
hello()
hello_announce()
hello_ignore()
