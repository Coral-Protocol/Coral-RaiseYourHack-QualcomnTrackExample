import os
import requests
from datetime import datetime

def get_monzo_balance() -> dict:
    """
    Call Monzo /balance endpoint and return all fields, formatting numeric
    values (like balance and spend_today) as decimal strings in GBP (e.g., "129.69").
    """
    token = os.getenv("MONZO_ACCESS_TOKEN")
    acc_id = os.getenv("MONZO_ACCOUNT_ID")
    if not token or not acc_id:
        raise RuntimeError("Please set MONZO_ACCESS_TOKEN and MONZO_ACCOUNT_ID in environment")

    print(token)
    print(acc_id)

    resp = requests.get(
        "https://api.monzo.com/balance",
        headers={"Authorization": f"Bearer {token}"},
        params={"account_id": acc_id}
    )
    resp.raise_for_status()
    data = resp.json()

    def fmt(val):
        return f"{val / 100:.2f}" if isinstance(val, int) else val

    return {
        "balance": fmt(data.get("balance")),
        "total_balance": fmt(data.get("total_balance")),
        "balance_including_flexible_savings": fmt(data.get("balance_including_flexible_savings")),
        "currency": data.get("currency"),
        "spend_today": fmt(data.get("spend_today")),
        "local_currency": data.get("local_currency"),
        "local_exchange_rate": data.get("local_exchange_rate"),
        "local_spend": data.get("local_spend"),
    }

balance = get_monzo_balance()