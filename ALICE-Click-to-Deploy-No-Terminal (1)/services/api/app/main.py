from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import market, options, trading, paper, backtest, alerts, broker
app=FastAPI(title='ALICE Ultimate API',version='1.0.0')
app.add_middleware(CORSMiddleware,allow_origins=['*'],allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
app.include_router(market.router,prefix='/api/v1/market',tags=['market'])
app.include_router(options.router,prefix='/api/v1/options',tags=['options'])
app.include_router(trading.router,prefix='/api/v1/trading',tags=['strategy-risk'])
app.include_router(paper.router,prefix='/api/v1/paper',tags=['paper'])
app.include_router(backtest.router,prefix='/api/v1/backtest',tags=['backtest'])
app.include_router(alerts.router,prefix='/api/v1/alerts',tags=['alerts'])
app.include_router(broker.router,prefix='/api/v1/broker',tags=['broker'])
@app.get('/health')
def health(): return {'ok':True,'service':'alice-api'}
