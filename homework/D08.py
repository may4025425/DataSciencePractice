import numpy as np
name_list = ['小明','小華','小菁','小美','小張','John','Mark','Tom']
sex_list = ['boy','boy','girl','girl','boy','boy','boy','boy']
weight_list = [67.5,75.3,50.1,45.5,80.8,90.4,78.4,70.7]
rank_list = [8,1,5,4,7,6,2,3]
myopia_list = [True,True,False,False,True,True,False,False]
#1. 將上列list依照['name', 'sex', 'weight', 'rank', 'myopia']順序擺入array，並且資料型態順序擺入[Unicode,Unicode,float,int,boolean]
student_type = {'names':('name', 'sex', 'weight', 'rank', 'myopia'), 'formats':('U10','U6','f8','i4','?')}
students = np.zeros(8,dtype=student_type)
students['name'] = name_list
students['sex'] = sex_list
students['weight'] = weight_list
students['rank'] = rank_list
students['myopia'] = myopia_list
print(students)
#2. 呈上題，將array中體重(weight)數據集取出算出全部平均體重
print(np.mean(students['weight']))
#3. 呈上題，進一步算出男生(sex欄位是boy)平均體重
boy_index = np.where(students['sex']=='boy')[0]
print(np.mean(students['weight'][boy_index]))
#3. 呈上題，進一步算出女生(sex欄位是girl)平均體重
girl_index = np.where(students['sex']=='girl')[0]
print(np.mean(students['weight'][girl_index]))