

def fv_eq(pv:float, n: float, r: float) -> float:
    '''
    Returns the future value of a lump sum given:
    pv = present value
    n = number of periods
    r = interest rate
    '''
    fv = pv * (1 + r)**n
    return fv
