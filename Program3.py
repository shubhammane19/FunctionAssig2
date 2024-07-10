def outer():
    def inner():
        return "Greetings from inner function"
    
    return inner()

if __name__ == "__main__":
    result = outer()
    print(result)