# ALICE — Click-to-deploy, no Terminal

This package is prepared for browser-only deployment. You do not need Python, Node.js, npm, pip, Docker, or Terminal on your computer.

## Recommended cloud setup

- Frontend: Vercel
- Python API: Render
- Database: Render PostgreSQL (created from `render.yaml`)
- Initial market provider: ALICE demo provider
- Live broker execution: OFF by default

## 1. Put the project on GitHub — browser only

1. Sign in to GitHub in your browser.
2. Create a new repository named `alice-trading-assistant`.
3. Open the repository and choose **Add file → Upload files**.
4. Extract this ZIP on your computer first, then drag the project files/folders into the GitHub upload page.
5. Click **Commit changes**.

Do not upload `.env` files or API/broker secrets.

## 2. Deploy the API and database on Render

1. Sign in to Render.
2. Choose **New → Blueprint**.
3. Connect your GitHub repository.
4. Render will detect `render.yaml`.
5. Review the `alice-api` web service and `alice-db` database.
6. Click **Apply** / **Create**.
7. Wait for the API deployment to finish.
8. Open the generated API URL and add `/health`.
9. Confirm it returns JSON containing `"ok": true`.

The API intentionally starts in demo/paper-safe mode.

## 3. Deploy the website on Vercel

1. Sign in to Vercel.
2. Choose **Add New → Project**.
3. Import the same GitHub repository.
4. Keep the repository root as the project root.
5. Vercel will use `vercel.json` and build `apps/web`.
6. Before deploying, add an Environment Variable:
   - Name: `NEXT_PUBLIC_API_URL`
   - Value: your Render API URL, for example `https://alice-api-xxxx.onrender.com`
7. Click **Deploy**.

## 4. Verify ALICE

Open the Vercel URL. The dashboard should load:

- Market dashboard
- NIFTY / SENSEX / BANKNIFTY / VIX
- Price history chart
- Option-chain demo
- Strategy state
- Risk controls
- Paper-trade API
- Backtest endpoint
- Alerts endpoint
- Broker safety status
- Live execution lock

## 5. Important before real trading

The initial deployment is NOT connected to a broker and does NOT place live orders.

Before enabling any real-money workflow, add:

1. A supported broker/data adapter.
2. Server-side secret storage.
3. User authentication and authorization.
4. Persistent paper-trade and alert storage.
5. Real historical market data for backtesting.
6. Transaction costs, slippage and expiry-aware option modelling.
7. Broker/API compliance controls.
8. A hard kill switch.
9. Explicit live-mode confirmation.
10. Monitoring and audit logs.

Never put broker access tokens in `NEXT_PUBLIC_*` variables. Those variables are exposed to the browser.

## If something goes wrong

- Website says API offline → check `NEXT_PUBLIC_API_URL` in Vercel.
- Render API is unhealthy → open Render logs and `/health`.
- CORS errors → confirm the browser is calling the correct Render URL.
- Empty/old data → the default provider is intentionally demo data.

No Terminal is required for these deployment steps.
