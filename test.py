import os
import glob
import algorithm


input_path = 'F:\\underwater image\\images\\'  # 存放图片的文件夹路径
output_path = 'F:\\underwater image\\image_dcp\\'
paths = glob.glob(os.path.join(input_path, '*.jpg'))
for i in range(len(paths)):
    img = paths[i]
    algorithm.dcpmain(img,output_path)

    #m = deHaze(cv2.imread(img) / 255.0) * 255
    #cv2.imwrite(img.replace('input' , 'output'), m)
