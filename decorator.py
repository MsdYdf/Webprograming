def announce(func):
    def wraper():
        print('About to run a function')
        func()
        print('Done with the function ')
    return wraper

@announce
def hello():
    print('Hello, world!')

hello()    
