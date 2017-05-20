import urllib
import urllib.request
import cv2
import os
import numpy as np


    

  
def main():
    links = ['LINK of IMAGES']
    print (links[0])
    paths = 'hotdog'
    
    
   pic_num = 1
    if not os.path.exists(paths):
            os.makedirs(paths)
    
        
    image_urls = str(urllib.request.urlopen(links[0]).read())
    print (image_urls)
        
    for i in image_urls.split('\\n'):
            try:                
                urllib.request.urlretrieve(i, paths+"/"+str(pic_num)+".jpg")
                img = cv2.imread(paths+"/"+str(pic_num)+".jpg")             
                if img is not None:
                    cv2.imwrite(paths+"/"+str(pic_num)+".jpg",img)
                    pic_num += 1

            except Exception as e:
                    print(str(e)) 


if __name__ == "__main__":

    main()