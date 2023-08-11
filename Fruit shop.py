while True:
    def confirm_msg():
            pay="Payment confirmed...PAYMENT SUCCESSFUL!"
            return pay
           
    prices={
        "apple":20,
        "banana":15,
        "grape" or "grapes":30,
        "pine":30,
        "orange"or"oranges":40,
        "strawberry":10,
        "lime":60,
        "mango":32,
        "cherry":10,
        "carrot":5,
        "ginger":5.99,
        "cucumber":9.98,
        "watermelon":24,
        "pineapple":64,
        "okra":2.99,
        "paw paw":7.99,
        "Pomagranate":150,
        "lemon":7.99,
        "garlic":45,
        "raddish":23,
        "bell pepper":20,
        "cucumber":15.99,
        "cabbage":34,
        "spinach":15,
        "couli":14.20,
        "star fruit":39.55,
        "peas":3,
        "green beans":4.89,
        "aberine":1.99,
        "eggplant":8.99,
        "garden egg":10.99,
        "yam":45,
        "potato":15.99,
        "plantain":77.99,
        "pepper":9.99,
        "beetroot":45.99,
        "onion":3.99,
        "onion leaf":16.99,
        "tomato":22.99,
        "black currant":56.99,
        "pumpkin":150,
        "pumpkin leaf":70,
        "cellery":3,
        "pickles":65.99,
        "guava":30,
        "ground nut":5,
        "cashew-nut":66.99,
        
        
        
        
        
        }
    y=input(" WELCOME!......WHAT FRUIT OR VEGETABLE WOULD YOU LIKE TO BUY?\n")
    if y in prices:
        print("The price is ",prices[y],"Dollars")
        x=float(input("   TYPE IN THE PAYMENT AMOUNT\n"))
        if prices[y]==x:
            print(confirm_msg())
        else:
            print("Invalid amount!... Please be Sure you pay the exact amount offered\n")
    
    else:
        print("SORRY THIS GOOD IS NOT AVAILABLE......BE SURE NOT TO ORDER MULTIPLE FRUITS AT THE SAME TIME")
        print("AVOID PUTTING HYPHEN WHEN TYPING A GOODS NAME")
    ans=input("Do You Wish To Continue Your Purchase(s)? (Y/N)\n")
    if ans=="yes" or ans=="y":
                continue
    else:
                    print("THANK YOU FOR SERVICING WITH US")
                    break
        
    
      

            
        
    
            