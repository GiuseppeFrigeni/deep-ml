def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    res = []
    nrows = len(a)
    ncols = len(a[0])

    for i in range(ncols):
        resrow = []
        for j in range(nrows):
            resrow.append(a[j][i])
        res.append(resrow)

    return res
