import os
from PIL import Image

# Specify the path to the folder containing your text files
folder_path = './yolotrain/SNU/test/labels'

# Iterate through all files in the folder
# a = set()
for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):  # Make sure it's a text file
        file_path = os.path.join(folder_path, filename)
        image_path = os.path.join(folder_path.replace('labels','images'), os.path.splitext(filename)[0] + ".jpg")

        with open(file_path, "r") as file:  
            lines = file.readlines()


        # Open the image file
        image = Image.open(image_path)

        width, height = image.size

        with open(file_path, 'w') as file:
            for line in lines:
                line = line.split()
                strng = ""
                # a.add(int(line[0]))
                for x,y  in zip(line[1::2],line[2::2]):
                    strng += f'{line[0]} {int(x)/width} {int(y)/height}'
                file.write(strng)
                file.write('\n') 
                
# print(a)
    # break


        #     strng += str(count_type_parking[str2[0]])

        #     lst1 = lst['points']
        #     for points in lst1:
        #         strng += f' {int(points[0])/width} {int(points[1])/height}'
        #     strng += f'\n'
        # # print(strng)
        # save_label_path = os.path.join(parent_path + r'\labels', os.path.splitext(filename)[0] + ".txt")
        # save_img_path = os.path.join(parent_path + r'\images', os.path.splitext(filename)[0] + ".jpg")
        # shutil.copy(image_path, save_img_path)

        # with open(save_label_path, "w") as file:
        #     file.write(strng)
        
        
        
        
        
        # Read the content of the file
        # with open(file_path, 'r') as file:
        #     lines = file.readlines()

        # # print(len(lines))
        # # Keep only the third line and overwrite the file
        # with open(file_path, 'w') as file:
        #     if len(lines)< 3:
        #         file.write("")
        #     else:
        #         file.writelines(lines[2:])
