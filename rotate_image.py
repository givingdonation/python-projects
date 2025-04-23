from PIL import Image
  
# Giving The Original image Directory 
# Specified
Original_Image = Image.open("./5seg.jpg")
  
# Rotate Image By 180 Degree
rotated_image1 = Original_Image.rotate(90)

rotated_image1.save("./5seg.jpg")
