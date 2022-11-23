import cv2
from matplotlib import pyplot as plt
import numpy as np
import copy




def face_masking(img_path):

    # Get image
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # to show image with matplotlib, we should convert bgr -> rgb
    
    # Set subplot settings (size, location, and title)
    f = plt.figure(figsize=(10,3))
    ax1 = f.add_subplot(131)
    ax1.set_title("Original Image")
    ax2 = f.add_subplot(132)
    ax2.set_title("Masked Image")
    ax3 = f.add_subplot(133)
    ax3.set_title("Face Histogram")
    
    # Show original image
    ax1.imshow(img)
    
    # Get image width, height and channel
    img_width = img.shape[1]
    img_height = img.shape[0]
    img_channel = img.shape[2]
    
    assert img_channel==3,'Input image is not color image, please put color image'
    
    ######## Plot histogram ##############
    r_hist = np.zeros(256)
    g_hist = np.zeros(256)
    b_hist = np.zeros(256)
    
    # Get r,g,b histogram info
    for i in range(img_height):
        for j in range(img_width):
            r_hist[img[i][j][0]]+=1
            g_hist[img[i][j][1]]+=1
            b_hist[img[i][j][2]]+=1
    
    # Plot RGB histogram
    ax3.plot(r_hist,label='R',color='red')
    ax3.plot(g_hist,label='G',color='green')
    ax3.plot(b_hist,label='B',color='blue')
    ax3.legend()
    
    # Save RGB histogram as jpg
    extent = ax3.get_window_extent().transformed(f.dpi_scale_trans.inverted())
    f.savefig('3.jpg',bbox_inches=extent)
    
    ########## Image Masking #################

    # 1. Convert RGB to YCbCr
    weight = 0.6 
    ycrcb_img = copy.deepcopy(img)
    ycrcb_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_RGB2YCrCb)
    
    Cr_hist = np.zeros(256)
    for i in range(img_height):
        for j in range(img_width):
            Cr_hist[img[i][j][1]]+=1
    
    Cr_threshold = 140
    
    # 2. Masking image via threshold
    for i in range(img_height):
        for j in range(img_width):
            
            if ycrcb_img[i][j][1] > Cr_threshold:
                img[i][j][0]=255
                img[i][j][1]=255
                img[i][j][2]=255
            else:
                img[i][j][0]=0
                img[i][j][1]=1
                img[i][j][2]=2
    
    # Plot masked image
    ax2.imshow(img)
    
    # Save masked image as jpg
    cv2.imwrite('./2.jpg',img)
    
    plt.show()
    
face_masking('C:\\DIP\\Face_Reading_AI\\data\\face_yellow.jpg')