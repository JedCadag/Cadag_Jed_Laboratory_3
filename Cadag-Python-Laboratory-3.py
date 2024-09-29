def main():
    item1 = float(input("Enter the price of item 1: "))
    item2 = float(input("Enter the price of item 2: "))
    item3 = float(input("Enter the price of item 3: "))

    total_cost = item1 + item2 + item3
    print(f"\nTotal cost: ${total_cost:.2f}")

    if total_cost > 100.00:
        print("Congratulations! You qualify for a Spotify discount.")

    loyalty_points = total_cost // 110
    print(f"Loyalty points earned: {int(loyalty_points)}")

    while True:
        payment = float(input("\nEnter payment amount: "))
        if payment >= total_cost:
            change = payment - total_cost
            print(f"Payment accepted. Change: ${change:.2f}")
            break
        else:
            print("Payment must be greater than or equal to the total cost. Please try again.")

    print(f"\nFinal total price: ${total_cost:.2f}")
    print(f"Loyalty points earned: {int(loyalty_points)}")

if __name__ == "__main__":
    main()