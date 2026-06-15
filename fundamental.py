import cv2

image = cv2.imread(r'flower.png')
if image is not None:
    print('image loaded successfully')
else:
    print('Error: Image could not load')   

cv2.imwrite('new_image', image)