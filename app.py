"""Synthetic in-memory code-review demo. No network, files, credentials or real accounts."""
from decimal import Decimal, ROUND_HALF_UP

def checkout_total(subtotal, discount_percent=0):
    subtotal=Decimal(str(subtotal));discount_percent=Decimal(str(discount_percent))
    if subtotal<0:raise ValueError("Subtotal must not be negative")
    if not 0<=discount_percent<=100:raise ValueError("Discount must be between 0 and 100")
    total=subtotal*(1-discount_percent/100)
    return total.quantize(Decimal("0.01"),rounding=ROUND_HALF_UP)

def delete_account(current_user, target_id, accounts):
    if current_user.get("role") != "admin":
        raise PermissionError("Administrator role required")
    if target_id not in accounts:raise KeyError(target_id)
    removed=accounts.pop(target_id)
    return {"deleted":target_id,"name":removed["name"]}
