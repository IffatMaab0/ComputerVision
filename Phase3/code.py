import cv2
vid = cv2.VideoCapture('video.mp4')
while True:
    ret, frame = vid.read()
    if not ret:
        print('Could not read frame')
        break
    cv2.imshow('Webcame Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        print('quiting...')
        break
vid.release()
cv2.destroyAllWindows()    