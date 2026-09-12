# ALICE Ultimate — Click-to-Deploy Cloud F&O Assistant

ALICE is a cloud-first Indian F&O decision-support application. This repository is structured so the first deployment can be completed through GitHub, Render and Vercel in a browser — no local Python/Node/npm/pip/Terminal required.

## 9-stage architecture

1. **Market Dashboard** — NIFTY, SENSEX, BANKNIFTY, VIX and charts
2. **Option Chain** — strike/OI/ΔOI/PCR/max-pain data contract
3. **Strategy Engine** — market structure + indicators + signal state
4. **Risk Engine** — risk-per-trade, position sizing and guardrails
5. **Paper Trading** — safe simulated order workflow
6. **Backtesting** — API contract ready for real historical-data engine
7. **Alerts** — alert creation/listing API
8. **Broker Integration** — provider boundary and safety checks
9. **Automation** — deliberately locked until all live controls are satisfied

## Safety defaults

- Market data provider: `demo`
- Broker provider: `none`
- Live trading: `false`
- Kill switch: enabled
- Paper trading is the default workflow

The demo backtest response is illustrative and must not be treated as evidence of profitability.

## Cloud layout

`Browser → Vercel/Next.js → Render/FastAPI → PostgreSQL`

The application uses provider interfaces so a real market-data/broker adapter can be introduced without redesigning the UI.

## Deploy without Terminal

Read **DEPLOY-NO-TERMINAL.md** for the exact browser-only process.

### Files added for click-to-deploy

- `render.yaml` — Render API + PostgreSQL blueprint
- `vercel.json` — Vercel build configuration for the Next.js app
- `apps/web/.env.example` — frontend API URL setting
- `DEPLOY-NO-TERMINAL.md` — browser-only deployment guide

## Production warning

This is a decision-support/trading software project, not a promise of returns. Real-money trading requires current broker/API compliance, authenticated users, secure secret management, real-time market data, proper backtesting, transaction-cost modelling, monitoring, and a tested kill switch.
