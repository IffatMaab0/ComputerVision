import cv2
path = input("Enter the file path i.e(color.png): ")
image = cv2.imread(path)
if image is not None:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ask = input(""" Type\n
                1-View\n
                2-Save\n
                3-Both

""")
    if (ask == "1"):
        cv2.imshow("gray scale image" , gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif (ask == "2"):
        ask2 = input("Type full FileName i.e(gray.png):")
        cv2.imwrite(ask2, gray)
    elif(ask == "3"):
        ask2 = input("Type full FileName:")
        cv2.imshow("gray scale image" , gray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.imwrite('Gray_Image.png', gray)
             

else:   
     print("some Error occured")