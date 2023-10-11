def linearSearchProduct(productlist, targetproduct):
  indices = []
  
  for index, product in enumerate(productlist):
    if product == targetproduct:
      indices.append(index)
  return indices

products= ["Apple","Orange","Apple","Watermelon","Apple","Mango"]
target1 = "Apple"
target2 = "Tomato"
result1 = linearSearchProduct(products,target1)
print(result1)
result2 = linearSearchProduct(products,target2)
print(result2)