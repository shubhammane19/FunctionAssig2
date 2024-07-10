def outer(flag):
    def inner():
        return "Thisv is true." if flag else"this is false."
    
    return inner

if __name__ == '__main__':
    true_function = outer(True)
    false_function = outer(False)

    print(true_function())
    print(false_function())