# yolo keras label format row : image_file_path box1 box2 ... boxN
#                         box : x_min,y_min,x_max,y_max,class_id

from xml.dom import minidom
import os
import glob

path = os.getcwd()
# EDIT HERE
# class_id = {'CLASS_NAME' : ID_NUM}
class_id = {'CLASS_NAME': 0}

def convert_xml2yolo():
    #xml name + txt
    fname_out = ('annotation'+'.txt')

    #get number of xml file
    for fname in glob.glob("*.xml"):
        object_num = 1        
        
        #parsing
        xmldoc = minidom.parse(fname)
        
        with open(fname_out, "a") as f:

            itemlist = xmldoc.getElementsByTagName('object')

            for item in itemlist:
                # get class label
                class_name =  (item.getElementsByTagName('name')[0]).firstChild.data

                # get bbox coordinates
                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data

                fname_txt = os.path.splitext(fname)

                if class_name == 'CLASS_NAME':
                    if object_num != 1:
                        f.write(" " + str(xmin) + "," + str(ymin) + "," + str(xmax) + "," + str(ymax)  + 
                                "," + str(class_id[class_name]))
                    else :
                        f.write(str(path) + "/" + str(fname_txt[0]) + ".jpg " + str(xmin) + "," + str(ymin) + 
                        "," + str(xmax) + "," + str(ymax)  + "," + str(class_id[class_name]))
                else :
                    if object_num == 1:
                        f.write(str(path) + "/" + str(fname_txt[0]) + ".jpg ")
                object_num = object_num + 1
            f.write('\n')
    print ("wrote %s" % fname_out)

convert_xml2yolo()
