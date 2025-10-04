ele= int(input("Enter the electricity consumed: "))
total_ele= (ele * 5)
print(f"the total bill is :{total_ele}")
if total_ele > 1000:

discount = (total_ele *0.10)
total_ele -= discount
print(f"the discounted bill after exceeding 1000ru :{discount}")