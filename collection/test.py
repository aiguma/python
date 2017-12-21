#Relative Strength Index  
import numpy as np
import pandas as pd

#RSI
def fnRSI(m_Df, m_N):

    U = np.where(m_Df.diff(1) > 0, m_Df.diff(1), 0)
    D = np.where(m_Df.diff(1) < 0, m_Df.diff(1) *(-1), 0)

    AU = pd.DataFrame(U).rolling( window=m_N, min_periods=m_N).mean()
    AD = pd.DataFrame(D).rolling( window=m_N, min_periods=m_N).mean()
    RSI = AU.div(AD+AU) *100
    return RSI


#Moving Average
def fnMA(m_Df, m_N, m_ColumnName='Close'):
    if m_ColumnName in m_Df.columns:
        MA= pd.Series(pd.rolling_mean(m_Df[m_ColumnName], m_N), name = 'MA_' + str(m_N))
        resultDf = m_Df.join(MA)
    else:
        raise("You didn't input a Column Name")
    return resultDf
