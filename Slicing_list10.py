def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    x=len(list1)
    return list1[x:n:-1]
print(main([0,1,2,3,4,5,6,7,8,9],3))