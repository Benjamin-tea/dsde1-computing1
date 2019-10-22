import math
def period(L, g):
    ii = 'invalid input'
    if isinstance(L, (int, float)) == False:
        print(ii)
        return
    if isinstance(g, (int, float)) == False:
        print(ii)
        return
    if g == 0 or (L / g) < 0:
        print(ii)
        return
    T = (2 * math.pi) * ((L / g) ** 0.5) 
    return T
