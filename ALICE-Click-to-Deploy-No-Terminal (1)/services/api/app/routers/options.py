from fastapi import APIRouter
from ..providers.demo import chain,price
router=APIRouter()
@router.get('/chain')
def option_chain(symbol:str='NIFTY'):
 rows=chain(symbol); p=price(symbol); call=sum(r['call_oi'] for r in rows); put=sum(r['put_oi'] for r in rows); return {'symbol':symbol,'spot':p,'pcr':round(put/call,2),'max_pain':min(rows,key=lambda r:abs(r['strike']-p))['strike'],'rows':rows,'source':'demo'}
