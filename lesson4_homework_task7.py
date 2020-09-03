def fact(n):
    fct = 1
    for ell in range(1, n):
        fct *= ell
    print(fct)
    for ell in range(1, fct):
        yield ell


for el in fact(7):
    print(el)

