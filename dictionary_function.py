

shopping_items = {
    "eggs":1.85,
    "bread":1.50,
    "peppers":0.90,
    "milk":1.80,
    "butter":3
}

print(shopping_items)

for keys,values in shopping_items():
    if keys == ["milk","butter"]:
        print("these are diary")
    else:
        print("non dairy")


