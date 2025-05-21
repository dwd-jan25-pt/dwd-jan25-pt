import order_utils
import format_utils # Using 'import module_name'

# Alternative: from order_utils import calculate_grand_total, calculate_subtotal
# from format_utils import generate_order_summary

customer_order_1 = {
    "id": "ORD123",
    "customer": "Alice Wonderland",
    "items": [10.00, 25.50, 5.75] # list of prices
}

customer_order_2 = {
    "id": "ORD124",
    "customer": "Alan Smithee",
    "items": [30.00, 45.00] # list of prices
}

# Process order 2
subtotal2 = order_utils.calculate_subtotal(customer_order_2["items"])
# If using 'from x import y':
# subtotal1 = calculate_subtotal(customer_order_1["items"])

grand_total2 = order_utils.calculate_grand_total(subtotal2)
summary2 = format_utils.generate_order_summary(
    customer_order_2["id"],
    customer_order_2["customer"],
    customer_order_2["items"],
    grand_total2
)
print("--- Order 2 ---")
print(summary2)
print(f"Default Tax Rate from module: {order_utils.TAX_RATE}")
