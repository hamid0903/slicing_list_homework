def main(list1,n):
    """
    A list of several elements is given. Return all items from end n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    x=len(list1)
    return list1[::-n]
print(main([0,1,2,3,4,5,6,8,9],2))
