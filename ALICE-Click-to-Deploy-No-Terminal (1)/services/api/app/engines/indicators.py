import pandas as pd, numpy as np

def add_indicators(rows):
    df=pd.DataFrame(rows); c=df['close']; h=df['high']; l=df['low']; v=df['volume']
    df['ema20']=c.ewm(span=20,adjust=False).mean(); df['ema50']=c.ewm(span=50,adjust=False).mean()
    d=c.diff(); gain=d.clip(lower=0).rolling(14).mean(); loss=(-d.clip(upper=0)).rolling(14).mean(); rs=gain/(loss.replace(0,np.nan)); df['rsi']=100-(100/(1+rs))
    df['vwap']=(c*v).cumsum()/v.cumsum(); tr=pd.concat([h-l,(h-c.shift()).abs(),(l-c.shift()).abs()],axis=1).max(axis=1); df['atr']=tr.rolling(14).mean()
    return df.bfill().ffill()
