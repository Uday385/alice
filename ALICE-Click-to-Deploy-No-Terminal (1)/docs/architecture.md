# ALICE Ultimate architecture

## 9-stage design
1. Market dashboard: WebSocket/REST provider -> normalized ticks -> candles -> indicators.
2. Option chain: contract discovery -> chain normalization -> OI/ΔOI/IV/Greeks/PCR/max-pain -> strike map.
3. Strategy: market regime + structure + technical confluence + options context -> setup score -> NO TRADE allowed.
4. Risk: account equity + risk % + stop distance + lot size -> quantity; daily loss/trade limits; kill switch.
5. Paper: order simulator, fills, P&L, journal, positions.
6. Backtest: historical data -> strategy -> slippage/fees -> metrics -> out-of-sample validation.
7. Alerts: event rules -> queue -> notification adapters.
8. Broker: OAuth/token adapter -> account/positions/orders -> normalized broker interface.
9. Automation: risk gate -> broker validation -> explicit live mode -> order -> postback/websocket reconciliation -> kill switch.

## Provider interface
Implement `MarketDataProvider` and `BrokerProvider` interfaces so Zerodha, Upstox, Angel One or another supported provider can be added without changing the strategy engine.

## Production requirements
- server-side secrets only
- HTTPS
- authenticated users
- audit log for every signal/order decision
- idempotent order submission
- websocket reconnect/backoff
- stale-data detector
- daily loss and max-position gates
- kill switch stored server-side
- paper mode by default
- real historical data and transaction-cost model before claiming backtest validity
