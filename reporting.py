"""Reporting module - generates sales summary reports."""


def generate_daily_report(data):
    """Create a daily sales summary."""
    total_sales = sum(float(row["amount"]) for row in data)
    num_transactions = len(data)
    avg_sale = total_sales / num_transactions if num_transactions > 0 else 0

    return {
        "total_sales": total_sales,
        "num_transactions": num_transactions,
        "average_sale": round(avg_sale, 2)
    }


def generate_monthly_report(data, month):
    """Create a monthly sales summary filtered by month."""
    monthly_data = [row for row in data if row.get("month") == month]
    return generate_daily_report(monthly_data)
