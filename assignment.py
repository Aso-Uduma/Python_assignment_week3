def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount only if it is 20% or higher.

        price (float or int): Original price.
        discount_percent (float or int): Discount percentage (e.g., 20 for 20%).

    Returns:
        price: Final price after applying the discount if eligible; otherwise, the original price.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price


def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount only if it is 20% or higher.
    """
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price


# Prompt the user for input
try:
    original_price = float(input("2000:"))
    discount_percentage = float(input("30: "))

    final_price = calculate_discount(original_price, discount_percentage)

    if discount_percentage >= 20:
        print(f"Final price after {discount_percentage}% discount: {final_price:.2f}")
    else:
        print(f"No discount applied. Original price: {final_price:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount percentage.")

