def calculate_discount(price, discount_percent):
    apply_discount = lambda p, d: p * (1 - d/100)         #lambda function to calculate the discounted price directly
    return apply_discount(price, discount_percent) if discount_percent >= 20 else price      #return the discounted price if the discount percent is >= 20
    
def main():
        original_price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))

        final_price = calculate_discount(original_price, discount_percent)

        if final_price == original_price:
             print("No discount applied. Final price is:  ", final_price)
        else:
             print("Final price after discount", final_price)

if __name__=="__main__":
     main()
