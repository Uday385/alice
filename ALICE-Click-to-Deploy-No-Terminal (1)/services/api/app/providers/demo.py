import math, random, datetime as dt

def price(symbol):
    base={'NIFTY':25000,'SENSEX':82000,'BANKNIFTY':57000,'VIX':14}.get(symbol,25000)
    t=dt.datetime.now().timestamp()/1800
    return base*(1+0.004*math.sin(t)+0.001*math.sin(t*3))

def candles(symbol='NIFTY',n=100):
    p=price(symbol); out=[]
    for i in range(n):
        drift=0.0004*math.sin(i/11)+0.0008*math.sin(i/23)
        close=p*(1+drift+0.0015*math.sin(i/4))
        open_=close*(1+0.0005*math.sin(i))
        high=max(open_,close)*(1+0.0015)
        low=min(open_,close)*(1-0.0015)
        out.append({'time':f'{i:02d}','open':open_,'high':high,'low':low,'close':close,'volume':100000+int(30000*abs(math.sin(i/5)))})
    return out

def chain(symbol='NIFTY'):
    p=price(symbol); step=50 if symbol!='SENSEX' else 100; atm=round(p/step)*step; rows=[]
    for k in range(-6,7):
        strike=atm+k*step; dist=abs(strike-atm)/step
        call_oi=int(100000*(1+dist*.45)*(1+0.15*math.sin(k)))
        put_oi=int(100000*(1+dist*.5)*(1-0.1*math.sin(k)))
        rows.append({'strike':strike,'call_ltp':max(5,p-strike+120-dist*8),'call_oi':call_oi,'call_chg_oi':int(call_oi*.08*math.cos(k)),'put_ltp':max(5,strike-p+120-dist*7),'put_oi':put_oi,'put_chg_oi':int(put_oi*.07*math.sin(k+1))})
    return rows
