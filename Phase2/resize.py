import cv2

image =  cv2.imread('flower.png')
if image is None:
    print('Image not Found!')
else:
    resized = cv2.resize(image, (100, 300))
    cv2.imshow("original", image)
    cv2.imshow('Resized', resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
