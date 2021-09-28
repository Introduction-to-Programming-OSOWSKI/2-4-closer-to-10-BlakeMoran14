#WRITE YOUR CODE IN THIS FILE

def close10(x, y):
    xa = abs(x - 10)
    ya = abs(y - 10)

    if xa > ya:
        return y
    
    elif xa < ya:
        return x

    else:
        return 0