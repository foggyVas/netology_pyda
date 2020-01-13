def diag_sum(matrix):
    result = 0

    for i in range(len(matrix)):
        result += matrix[i][i]
        i += 1

    return result


print(diag_sum(data))


def diagonal_sum(matrix):
    return sum((matrix[i][i] for i in range(len(matrix))))


print()
print(diagonal_sum(data))
