def find_product(*multiargs):
    if len(multiargs) < 1:
        return None
    else:
        product = 1
        for num in multiargs:
            product = product * num
    return product


prod = find_product(1, 2, 3, 4, 5)
print(prod)

