def outer(msg):
    def inner():
        print(f"Message: {msg}")
    return inner

say_hello = outer("Hello")
say_hello()   # Output: Message: Hello