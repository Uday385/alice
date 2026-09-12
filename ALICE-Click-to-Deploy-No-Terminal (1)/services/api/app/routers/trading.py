from fastapi import APIRouter
from pydantic import BaseModel,Field
from ..engines.risk import size,guard
router=APIRouter()
class RiskReq(BaseModel): capital:float=100000; risk_pct:float=Field(.01,ge=.001,le=.03); entry:float; stop:float; lot_size:int=1; trades_today:int=0; daily_loss:float=0
@router.post('/risk-check')
def risk_check(x:RiskReq): return {'quantity':size(x.capital,x.risk_pct,x.entry,x.stop,x.lot_size),'guard':guard(x.capital,x.risk_pct,x.daily_loss,trades_today=x.trades_today)}
@router.get('/modes')
def modes(): return {'advisory':True,'paper':True,'live':False,'reason':'Live execution is locked until broker credentials and deployment controls are configured.'}
