CREATE TABLE IF NOT EXISTS users(id UUID PRIMARY KEY, email TEXT UNIQUE NOT NULL, created_at TIMESTAMPTZ DEFAULT now());
CREATE TABLE IF NOT EXISTS paper_trades(id BIGSERIAL PRIMARY KEY, user_id UUID, symbol TEXT, side TEXT, entry NUMERIC, stop NUMERIC, target1 NUMERIC, target2 NUMERIC, quantity INT, status TEXT, created_at TIMESTAMPTZ DEFAULT now());
CREATE TABLE IF NOT EXISTS alerts(id BIGSERIAL PRIMARY KEY, user_id UUID, symbol TEXT, condition TEXT, value NUMERIC, enabled BOOLEAN DEFAULT TRUE, created_at TIMESTAMPTZ DEFAULT now());
CREATE TABLE IF NOT EXISTS backtests(id BIGSERIAL PRIMARY KEY, user_id UUID, strategy TEXT, params JSONB, metrics JSONB, created_at TIMESTAMPTZ DEFAULT now());
CREATE TABLE IF NOT EXISTS broker_connections(id BIGSERIAL PRIMARY KEY, user_id UUID, provider TEXT, encrypted_token_ref TEXT, live_enabled BOOLEAN DEFAULT FALSE, created_at TIMESTAMPTZ DEFAULT now());
