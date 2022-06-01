def fibonacci(n: int):
    '''
        Return the fibonacci number for the index you entered starting with index 0.

                Parameters:
                            n (int): integer

                Returns:
                        fibonacci (n): return the number at index n in the fibonacci sequence
    '''
    if type(n) != type(1):
        return "Integer Values only"
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n: int):
    """
           Return the lucas number for the index you entered starting with index 0.

                   Parameters:
                               n (int): integer

                   Returns:
                           lucas (n): return the number at index n in the lucas sequence
    """
    if type(n) != type(1):
        return "Integer Values only"
    if n == 0:
        return 2
    elif n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, a=0, b=1):
    """
           Return the number in the index you entered ( n ) starting for the point you add (a , b).

                   Parameters:
                               n (int): integer
                               a (int): integer with default value 0
                               b (int): integer with default value 1
                   Returns:
                           sum_series (n ,a ,b): return the number at index n in the sequence and you can choose the starting
                           point by change the value of the a and b parameters
    """
    if n == 0:
        return a
    elif n == 1:
        return b
    return sum_series(n - 1, a, b) + sum_series(n - 2, a, b)
