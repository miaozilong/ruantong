import re
import string

if __name__ == '__main__':
   #从文件中读取出信息写入列表
   with open('info.txt','rb') as f:
       info_list = f.read().decode('utf-8').split('\n')

   fuhao = string.punctuation

    # 进行数据整理为如下顺序：班级,学号,姓名,性别,手机号
   re_class = re.compile(r'电信\d{4}?班')
   re_id = re.compile(r'\d{8}?')
   re_name = re.compile(r'[^电信\d{4}班%s\s][\u4e00-\u9fa5]+'%(fuhao))
   re_sex = re.compile('男|女')
   re_phone = re.compile(r'\d{11}?')

   for n in range(0,len(info_list)):
       class_info = re_class.search(info_list[n]).group()
       id_info = re_id.search(info_list[n]).group()
       name_info = re_name.search(info_list[n]).group()
       sex_info = re_sex.search(info_list[n]).group()
       phone_info = re_phone.search(info_list[n]).group()
       info_list[n] = f'{class_info},{id_info},{name_info},{sex_info},{phone_info}'

   #插入数据头
   info_list.insert(0,'班级,学号,姓名,性别,手机号')

   #将整理后的数据重新写入文件
   with open('整理后学生信息.csv','w') as f:
       for line in info_list:
           f.write(line+'\n')
