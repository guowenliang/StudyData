import pandas as pd


data = pd.read_excel("C:\\Users\\William\\Desktop\\test\\test.xls")  #需要分类的数据
classby = "部门"


rows = data.shape[0]  # 获取行数 shape[1]获取列数
department_list = []

for i in range(rows):
    temp = data[classby][i]
    if temp not in department_list:
        department_list.append(temp)  # 将部门的分类存在一个列表中
for department in department_list:
    new_df = pd.DataFrame()

    for i in range(0, rows):
        if data[classby][i] == department:
            new_df = pd.concat([new_df, data.iloc[[i], :]], axis=0, ignore_index=True)
            new_df.to_excel(str("C:\\Users\\William\\Desktop\\test\\"+department)+ ".xls", sheet_name=department, index=False)  # 将每个部门存成一个新excel