def main(list1):
    """A list of several elements is given. Return all items from the beginning in three steps.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    n=len(list1)
    return list1[::3]
print(main([0,1,2,3,4,5,6]))