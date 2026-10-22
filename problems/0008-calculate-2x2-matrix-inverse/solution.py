def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    (a, b), (c, d) = matrix

    det = a * d - b * c

    if det == 0:
        return None

    return [
        [d / det, -b / det],
        [-c / det, a / det]
    ]


    