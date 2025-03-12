def f(*args, **kwargs):  #positional and named arguments
    print("Named:", kwargs)

# Pass a dictionary to kwargs
f(galleons=100, sickles=50, knuts=25)

