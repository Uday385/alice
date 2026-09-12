def analyze(df):
    x=df.iloc[-1]; score=50
    if x.ema20>x.ema50: score+=18
    else: score-=18
    if x.close>x.vwap: score+=12
    else: score-=12
    if x.rsi>55: score+=10
    elif x.rsi<45: score-=10
    score=max(0,min(100,int(score))); trend='BULLISH' if score>=65 else 'BEARISH' if score<=35 else 'NEUTRAL'
    hi=float(df.high.tail(30).max()); lo=float(df.low.tail(30).min())
    return {'trend':trend,'score':score,'support':lo,'resistance':hi,'reason':'EMA/VWAP/RSI confluence'}
