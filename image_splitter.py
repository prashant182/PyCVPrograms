import cv2
img = cv2.imread('IMAGEPATH')
count=1
i=1000
j=1000
row=1
col=1
while j in range (1000,6327):
    while i in range (1000,14015):
        cv2.imwrite("IMAGEPATH"+"r"+str(row)+"c"+str(col)+".jpg",img[j:j+1000, i:i+1000])
        col=col+1
        i=i+700
        print 'col'
        print col
    j=j+700
    col=1
    i=1000
    row=row+1
    print 'row'
    print row