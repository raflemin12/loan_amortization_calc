import pandas as pd
from future_value_formula import pmt_pv_ordinary_annuity

def create_amor_dict(pv=float, n=float, r=float) -> dict:
    '''
    Returns a dict of lists to resemble an amortization table of a loan given:
    pv = Present Value
    n = Number of Periods
    r = Interest rate
    '''

    pmt = pmt_pv_ordinary_annuity(pv, n, r)
    amor_dict = {}

    for period in range(1,n + 1):
        balance = pv
        amor_dict[str(period)] = [period, balance, pmt]

    return amor_dict
