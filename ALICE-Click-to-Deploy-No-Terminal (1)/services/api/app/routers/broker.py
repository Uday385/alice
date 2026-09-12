from fastapi import APIRouter
router=APIRouter()
@router.get('/status')
def status(): return {'provider':'none','connected':False,'live_execution_enabled':False,'kill_switch':True,'required':['broker OAuth/token','server-side secret storage','static/registered IP if required by provider','risk limits','explicit live-mode confirmation']}
@router.post('/order/validate')
def validate(order:dict): return {'approved':False,'reason':'Live execution disabled in starter. Use paper trading until broker adapter is configured and compliance checks are complete.'}
