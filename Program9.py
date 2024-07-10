def outer():
    message = "I am the outer Function"

    def inner():
        return message
    return inner

if __name__ == "__main__":
    inner_fun = outer()
    result = inner_fun()
    print(result)