from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime,timezone
router=APIRouter(); trades=[]
class PaperTrade(BaseModel): symbol:str; side:str; entry:float; stop:float; target1:float; target2:float; quantity:int
@router.post('/trades')
def create(t:PaperTrade):
 x=t.model_dump(); x.update({'id':len(trades)+1,'status':'OPEN','created_at':datetime.now(timezone.utc).isoformat()}); trades.append(x); return x
@router.get('/trades')
def list_trades(): return {'items':trades}
