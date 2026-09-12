def size(capital,risk_pct,entry,stop,lot_size=1,max_lots=20):
    risk_amount=capital*risk_pct; per_unit=abs(entry-stop); qty=0 if per_unit<=0 else int(risk_amount/per_unit); qty=(qty//lot_size)*lot_size; return min(qty,max_lots*lot_size)
def guard(capital,risk_pct,daily_loss,max_daily=0.03,max_trades=5,trades_today=0):
    return {'allowed':risk_pct<=max_daily and daily_loss<=capital*max_daily and trades_today<max_trades,'max_loss':capital*risk_pct,'daily_limit':capital*max_daily}
