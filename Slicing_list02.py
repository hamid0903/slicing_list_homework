def main(list1):
    """
    A list of several elements is given. Reverse this list.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    n=len(list1)
    return list1[::-1]
print(main([0,1,2,3,4,5]))