import cv2

def apply_filter(img,f):
    img=img.copy()
    if f=='r':
        img[:,:,:2]=0
    elif f=="g":
        img[:,:,[0,2]]=0
    elif f=="b":
        img[:,:,1:]=0
    elif f=="i":
        img[:,:,2]=cv2.add(img[:,:,2],50)
    elif f=="d":
        img[:,:,0]=cv2.subtract(img[:,:,0],10)
    return img

img=cv2.imread("wallpaper_16.jpg")
f="o"

while True:
    cv2.imshow("Image",apply_filter(img,f))
    k=cv2.waitKey(1)&0xFF
    if k in map(ord,['r','g','b','i','d']):
        f=chr(k)
    elif k==ord('o'):
        f="o"
    elif k==ord("q"):
        break
cv2.destroyAllWindows()