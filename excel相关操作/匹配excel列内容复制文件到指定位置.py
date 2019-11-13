import os.path
import shutil
import pandas as pd

#df.shape[1]   返回列数
#df.shape[0]   返回行数

#定义复制文件函数    两个参数： 源文件目录，目标目录
def moveFileto(sourceDir,  targetDir):
    shutil.copy(sourceDir,  targetDir)

#main
# 将文件读取出来放一个列表里面
pwd = "C:\\Users\\Administrator\\Desktop\\test\\testadd" # 移动的源文件目录

name_list = pd.read_excel("C:\\Users\\Administrator\\Desktop\\test\\test.xls")   #获取想要复制的文件的名称
name_list_col = "姓名"    #列名称
targetDir = "C:\\Users\\Administrator\\Desktop\\test\\move"  #目标文件夹

# 新建列表，存放文件名
file_list = []

for root,dirs,files in os.walk(pwd): # 第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
    for file in files:
        file_path = os.path.join(root, file)
        file_list.append(file_path) # 使用os.path.join(dirpath, name)得到全路径
#  去除路径  只获取文件名
new_file_list=[]
for i in file_list:
    new_file_list.append(i.lstrip(pwd).strip())  #lstrip() 函数去掉路径，只留下带拓展名的文件名

# 读取需要匹配的名称列表。
found_file_list=[]
All_file_list=[]
for i in range(name_list.shape[0]):
    #print(name_list.iloc[:,[0]].loc[i,name_list_col])
    for s in file_list:
        All_file_list.append(name_list.iloc[:, [0]].loc[i, name_list_col])
        if name_list.iloc[:,[0]].loc[i,name_list_col] in  s:
            moveFileto(s,  targetDir)
            print("{0} is found".format(name_list.iloc[:, [0]].loc[i, name_list_col]))
            found_file_list.append(name_list.iloc[:, [0]].loc[i, name_list_col])
            break
diff=list(set(All_file_list).difference(set(found_file_list)))   #两个集合的差集
print("{0}没有找到".format(diff))   #excel中的 没被找到的