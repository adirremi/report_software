def are_integers_equal(int1, int2):
    """
    Check if two integer values are equal after casting them to a common data type.

    Args:
    int1: The first integer.
    int2: The second integer.

    Returns:
    bool: True if the integers are equal, False otherwise.
    """
    common_type = int  # Choose a common data type (e.g., int or numpy.int32)
    int1_cast = common_type(int1)
    int2_cast = common_type(int2)
    return int1_cast == int2_cast