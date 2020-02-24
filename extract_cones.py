import cv2 as cv
import glob

i=0
for label_path in sorted(glob.glob('./labels/*.txt')):
    f = open(label_path, "r")
    names = label_path.split('/')
    name = names[2].split('.')
    img = cv.imread('./images/' + name[0] + '.jpg', cv.IMREAD_COLOR)

    """
    cv.imshow('image', img)
    cv.waitKey()
    cv.destroyAllWindows()
    """

    for line in f:
        label_data = line.split(' ')

        if '\n' in label_data[0]:
            continue
        if 'nan' in label_data:
            continue
         
        print(label_data)
        # Get the class
        if(label_data[0]=='0'):
            cone_type = 'yellow'
            print(cone_type)
        elif(label_data[0]=='1'):
            cone_type = 'blue'
            print(cone_type)
        elif(label_data[0]=='2'):
            cone_type = 'orange'
            print(cone_type)    
        elif(label_data[0]=='3'):
            cone_type = 'big-orange'
            print(cone_type)
        else:
            continue

        # Crop the ROI (centered square with height = width)
        xc = float(label_data[1]) * img.shape[1]
        yc = float(label_data[2]) * img.shape[0]
        width = float(label_data[3]) * img.shape[1]
        height = float(label_data[4]) * img.shape[0]

	# Assert the ROI is within the image boundaries
        xmin = int(round(min( max(0, xc - round(height/2)), img.shape[1] ))) 
        xmax = int(round(min( max(0, xc + round(height/2)), img.shape[1] )))
        ymin = int(round(min( max(0, yc - round(height/2)), img.shape[0] )))
        ymax = int(round(min( max(0, yc + round(height/2)), img.shape[0] )))

        subimg = img[ymin:ymax, xmin:xmax]

        """
        print(xmin,xmax,ymin,ymax)
        cv.imshow('image', subimg)
        cv.waitKey()
        cv.destroyAllWindows()
        """

        cv.imwrite('./cones/' + cone_type + '/' + format(i, '09d') + '.jpg', subimg, [int(cv.IMWRITE_JPEG_QUALITY), 100])
        i=i+1
