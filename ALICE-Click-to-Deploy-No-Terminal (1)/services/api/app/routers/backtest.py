from fastapi import APIRouter
from pydantic import BaseModel
router=APIRouter()
class BacktestReq(BaseModel): symbol:str='NIFTY'; capital:float=100000; risk_pct:float=.01
@router.post('/run')
def run(x:BacktestReq): return {'status':'DEMO','symbol':x.symbol,'metrics':{'trades':120,'win_rate':0.56,'profit_factor':1.32,'max_drawdown':0.087,'net_return':0.164},'note':'Illustrative engine response; replace with real historical candles and transaction costs before relying on results.'}
