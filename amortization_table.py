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
        ending_balance = round(pv_ordinary_annuity(pmt, n=n_period-period, r=rate),2)
        amor_dict[str(period)] = [period, balance, pmt, interest, principal, ending_balance]
        balance = ending_balance

    return amor_dict

st.write('Loan Calculator')

loan_amount = st.number_input(label = 'Loan Amount',
                              min_value = 0.1,
                              value = 'min',
                              step = .01,
                              format ="%0.2f")

num_period = st.number_input(label = 'Number of Periods',
                             min_value = 1,
                             value = 'min',
                             step = 1)

int_rate = st.number_input(label = 'Interest Rate',
                           min_value = 0.01,
                           max_value = 0.99,
                           value = 'min',
                           step = 0.01,
                           format = "%0.2f")

calc = create_amor_dict(pv=loan_amount, n_period=num_period, rate=int_rate)

df = pd.DataFrame.from_dict(calc, orient='index', columns=
                            ['period', 'balance', 'payment', 'interest', 'principal', 'ending balance'])

st.write(df)
