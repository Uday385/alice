from fastapi import APIRouter
from pydantic import BaseModel
router=APIRouter(); alerts=[]
class Alert(BaseModel): symbol:str; condition:str; value:float
@router.post('')
def create(a:Alert): alerts.append(a.model_dump()); return {'created':True,'alert':a}
@router.get('')
def list_alerts(): return {'items':alerts}
