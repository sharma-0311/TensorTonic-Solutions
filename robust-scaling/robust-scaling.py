def robust_scaling(values):
    if not values:
        return []

    sorted_vals = sorted(values)
    n = len(sorted_vals)

    # Median
    if n % 2 == 1:
        median = sorted_vals[n // 2]
        lower_half = sorted_vals[:n // 2]
        upper_half = sorted_vals[n // 2 + 1:]
    else:
        median = (sorted_vals[n // 2 - 1] + sorted_vals[n // 2]) / 2
        lower_half = sorted_vals[:n // 2]
        upper_half = sorted_vals[n // 2:]

    # Helper function for median
    def get_median(arr):
        m = len(arr)
        if m == 0:
            return 0  # safe fallback
        if m % 2 == 1:
            return arr[m // 2]
        return (arr[m // 2 - 1] + arr[m // 2]) / 2

    Q1 = get_median(lower_half)
    Q3 = get_median(upper_half)

    IQR = Q3 - Q1

    if IQR == 0:
        return [0] * n

    return [(x - median) / IQR for x in values]