weather = input("What's the weather like today? (sunny/rainy/cold): ")

if weather == "sunny":
    msg = "Wear a t-shirt and sunglasses."
elif weather == "rainy":
    msg = "Don't forget your umbrella and a raincoat."
elif weather == "cold":
    msg = "Make sure to wear a warm coat and a scarf."
else:
    msg = "Sorry, I don't have recommendations for this weather."

print(msg)

