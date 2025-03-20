def fv_lump_sum(pv:float, n: float, r: float) -> float:
    '''
    Returns the future value of a lump sum given:
    pv = present value
    n = number of periods
    r = interest rate
    '''
    fv = pv * ((1 + r)**n)
    return fv

def pv_lump_sum(fv:float, n:float, r:float) -> float:
    '''
    Returns the present value of a lump sum given:
    fv = future value
    n = number of periods
    r = interest rate
    '''
    pv = fv / ((1+r)**n)
    return pv

