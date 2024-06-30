from hello import to_you, add, subtract

def setup_function(function):
    print(f"Running Setup: {function.__name__}")
    function.x = 10

def teardown_function(function):
    print(f"Running Teardown: {function.__name__}")
    del function.x


def test_hello_subtract():
    assert subtract(test_hello_subtract.x) == 9
    

##Run for failed test, should be 11
# def test_hello_add():
#    assert add(test_hello_add.x) == 12
