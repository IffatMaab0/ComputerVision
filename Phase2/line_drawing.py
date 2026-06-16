import cv2

ask1 = input('Enter the FileName (ie image.png):')
image =  cv2.imread(ask1)
if image is None:
    print('Image not Found!')
else:
    ask2 = input('''
1- Press 1 to draw line.
2- Press 2 to draw rectangle.
3= Press 3 to draw Circle.
4- Press 4 to add text.                                                                                 
''')
    if ask2 == '1':
        X1 = int(input('Enter X1: '))
        Y1 = int(input('Enter Y1: '))
        pt1 = (X1, Y1)
        X2 = int(input('Enter X2: '))
        Y2 = int(input('Enter Y2: '))
        pt2 = (X2, Y2)
        color = (255,0,0)
        thickness = 5
        line= cv2.line(image, pt1, pt2, color,thickness)
        cv2.imshow('Image with Line' ,line)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        askk1 = input('Do You Wanna save it? (Y/N)? ')
        if askk1 == 'Y':
            cv2.imwrite('Line_Image.png', line)
            print('Image saved successfully!')
        else:
            print("Thank You!")    

    if ask2 == '2':
        X1 = int(input('Enter X1: '))
        Y1 = int(input('Enter Y1: '))
        pt1 = (X1, Y1)
        X2 = int(input('Enter X2: '))
        Y2 = int(input('Enter Y2: '))
        pt2 = (X2, Y2)
        color = (255,0,0)
        thickness = 5
        rec= cv2.rectangle(image, pt1, pt2, color,thickness)
        cv2.imshow('Image with Rectangle' ,rec)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        askk1 = input('Do You Wanna save it? (Y/N)? ')
        if askk1 == 'Y':
            cv2.imwrite('rectangle_Image.png', rec)
            print('Image saved successfully!')
        else:
            print("Thank You!")   

    if ask2 == '3':
        X1 = int(input('Enter X: '))
        Y1 = int(input('Enter Y: '))
        center = (X1, Y1)
        rad = int(input('Enter the radius: '))
        color = (255,0,0)
        thickness = 5
        circle= cv2.circle(image, center, rad, color, thickness)
        cv2.imshow('Image with With' ,circle)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        askk1 = input('Do You Wanna save it? (Y/N)? ')
        if askk1 == 'Y':
            cv2.imwrite('Circle_Image.png', circle)
            print('Image saved successfully!')
        else:
            print("Thank You!")

    if ask2 == '4':
        text = input('What you wanna write:')
        fontScale = float(input("What should be the size of text(1.0s, 2.0b): "))
        X1 = int(input('Enter X1: '))
        Y1 = int(input('Enter Y1: '))
        org = (X1, Y1)
        thickness = 5
        texted = cv2.putText(image, text, org, cv2.FONT_HERSHEY_COMPLEX, fontScale,(255,0,0), thickness)
        cv2.imshow('Image with Text' ,texted)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        askk1 = input('Do You Wanna save it? (Y/N)? ')
        if askk1 == 'Y':
            cv2.imwrite('Text_Image.png', texted)
            print('Image saved successfully!')
        else:
            print("Thank You!")

