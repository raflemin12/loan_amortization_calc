import pandas as pd
import streamlit as st
from future_value_formula import pmt_pv_ordinary_annuity, pv_ordinary_annuity

def create_amor_dict(pv=float, n_period=float, rate=float) -> dict:
    '''
    Returns a dict of lists to resemble an amortization table of a loan given:
    pv = Present Value
    n = Number of Periods
    r = Interest rate
    '''

    pmt = pmt_pv_ordinary_annuity(pv, n_period, rate)
    balance = pv
    amor_dict = {}

    for period in range(1,n_period + 1):
        interest = round(balance * rate,2)
        principal = round(pmt - interest,2)
        amor_dict[str(period)] = [period, balance, pmt, interest, principal]
        balance = pv_ordinary_annuity(pmt, n=n_period-period, r=rate)

    return amor_dict

st.write('Annuity Calculator')

calc = create_amor_dict(pv=100000, n_period=12, rate=0.05)

df = pd.DataFrame.from_dict(calc)

st.write(df)
