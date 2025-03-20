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

def fv_ordinary_annuity(pmt:float, n: float, r:float) -> float:
    '''
    Returns the future value of a series of equal payments made at the end of each period given:
    pmt = payment
    n = number of periods
    r = interest rate
    '''
    fv = pmt*(((1+r)**n-1)/r)
    return fv
