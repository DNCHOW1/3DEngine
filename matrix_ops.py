def transpose(a):
    # Return a transposed matrix
    if type(a[0]) == int: # If a is a vector, transpose by making col representation a "row"
        return [a]
    return list(zip(*a))

def matmul(a, b):
    # Not true matrix mult, in this implementation we expect b to be a nx1 VECTOR usually.
    rows_a = len(a)
    rows_b = len(b)
    cols_a = len(a[0])
    cols_b = 1 if type(b[0]) == int else len(b[0])
    if cols_a == rows_b:
        result = [[0]*cols_b for i in range(rows_a)]
        b_trans = transpose(b)
        for i, row_a in enumerate(a):
            for j, col_b in enumerate(b_trans):
                result[i][j] = sum(row_a[k]*col_b[k] for k in range(cols_a))
        return result
    else:
        print("Columns of a and rows of b must match!!")

def matproj():
    pass 

def matrot():
    pass