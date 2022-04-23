class RuntimeErrorWithCode(TypeError):
    """
    Exception raised when a specific error code is needed to be raised
    """
    def __init__(self, message, code):
        super().__init__(f'Error code {code}: {message}')
        self.code = code


#raise MyCustomError('Not a good error message.', 500)

err = RuntimeErrorWithCode('An error just happened', 500)
print(err.__doc__) # this will print the doc strings above the class name
print(err)