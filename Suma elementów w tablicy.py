def sum_dziel_i_zwyciezaj(arr, l, r):
    if l == r:
        return arr[l]

    mid = (l + r) // 2
    left_sum = sum_dziel_i_zwyciezaj(arr, l, mid)
    right_sum = sum_dziel_i_zwyciezaj(arr, mid + 1, r)

    return left_sum + right_sum