import cv2

image = cv2.imread(r'flower.png')
if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('Gray_Image.png', gray)
    cv2.imshow("gray scale image" , gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:   
     print("some Error occured")