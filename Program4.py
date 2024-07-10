def outer():
    def inner():
        return "This is inner function"
    
    return inner

if __name__ == "__main__":
    ret = outer()
    retObj = ret()
    print(retObj)