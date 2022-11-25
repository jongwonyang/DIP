import cv2
from matplotlib import pyplot as plt
import numpy as np
import copy


def face_masking(img_path):

    # Get image
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # to show image with matplotlib, we should convert bgr -> rgb
    
    # Set subplot settings (size, location, and title)
    f = plt.figure(figsize=(13,3))
    ax1 = f.add_subplot(141)
    ax1.set_title("Original Image")
    ax2 = f.add_subplot(142)
    ax2.set_title("Masked Image")
    ax3 = f.add_subplot(143)
    ax3.set_title("Face Histogram")
    ax4=f.add_subplot(144)
    ax4.set_title('Cropped Image')
    
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
    
    crop_img = copy.deepcopy(img) # copy image for image crop
    
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
                img[i][j][1]=0
                img[i][j][2]=0
    
    # Plot masked image
    ax2.imshow(img)
    
    # Save masked image as jpg
    cv2.imwrite('./2.jpg',img)
    
    ########### Face Cropping ###############
    # Get Region of Face
    # 1. Calculate top, bottom, leftmost, rightmost of face region
    # 2. Crop image = img[top:bottom, leftmost:rightmost]
    
    top_found=False
    left_most = img_width
    right_most=0
    
    top=img_height
    bottom=0
    leftmost=img_width
    rightmost=0
    
    for i in range(img_height):
        leftmost_found=False
        for j in range(img_width):
            
            # If face region found
            # Face region of row i-th row, j-th column
            if img[i][j][0]==255 :
                # top region is i value of first face region
                if top_found==False and i!=0:
                    top=i
                    top_found=True
                # leftmost region takes j-th starting point of row and minimum of them
                if leftmost_found==False and j!=0:
                    leftmost = min(leftmost,j)
                    leftmost_found=True
                
                if j!=img_width:
                    rightmost = max(rightmost, j)
                if i!=img_height:
                    bottom = max(bottom, i)
            
    
    top = top-20 if top-20>0 else top
    bottom = bottom+20 if bottom+20<img_height else bottom
    leftmost = leftmost-20 if leftmost-20>0 else leftmost
    rightmost = rightmost+20 if rightmost+20<img_width else rightmost
    
    # Crop image based on top, bottom, leftmost, rightmost index
    crop_img = crop_img[top:bottom, leftmost:rightmost]
    
    
    # Show cropped image
    ax4.imshow(crop_img)
    # Save cropped image
    extent = ax4.get_window_extent().transformed(f.dpi_scale_trans.inverted())
    f.savefig('5.jpg',bbox_inches=extent)
    
    plt.show()
