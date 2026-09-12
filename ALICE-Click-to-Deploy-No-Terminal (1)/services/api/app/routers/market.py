from fastapi import APIRouter
from ..providers.demo import price,candles
from ..engines.indicators import add_indicators
from ..engines.strategy import analyze
router=APIRouter()
@router.get('/snapshot')
def snapshot():
    items=[]
    for s in ['NIFTY','SENSEX','BANKNIFTY','VIX']:
        c=candles(s); df=add_indicators(c); a=analyze(df); p=price(s); items.append({'symbol':s,'price':p,'change':(df.close.iloc[-1]/df.close.iloc[-5]-1)*100,'rsi':float(df.rsi.iloc[-1]),'vwap':float(df.vwap.iloc[-1]),'ema20':float(df.ema20.iloc[-1]),'ema50':float(df.ema50.iloc[-1]),'atr':float(df.atr.iloc[-1]),**a})
    return {'items':items,'source':'demo'}
@router.get('/history')
def history(symbol:str='NIFTY'):
    df=add_indicators(candles(symbol)); cols=['time','open','high','low','close','volume','ema20','vwap']; return {'symbol':symbol,'candles':df[cols].round(2).to_dict('records'),'source':'demo'}
