def calculate_discount(price, discount_percentage):
    
    #alculates the final price after applying discount if >= 20%
    if discount_percentage >= 20:
        final_price = price - price *(discount_percentage/100)
        return final_price
    else:
        return price

    
price = float(input("Enter the price: R"))
discount_percentage = float(input("Enter the discount percentage: "))
    
print(f"Price : R{calculate_discount(price, discount_percentage)}")


    