# Revenue Data Quality Rules

## Purchase Amount

- purchase_amount must not be NULL for completed purchase transactions.
- purchase_amount may be zero for promotional or free transactions.
- Negative purchase_amount values represent refunds and are valid only when the transaction type is REFUND.
- Negative purchase_amount values for normal PURCHASE transactions should be investigated.