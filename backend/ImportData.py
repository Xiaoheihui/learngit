#coding=utf-8
import os
import django
import re, datetime
import xlrd as xl  # 用于写入xls

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test1.settings")  # 添加环境变量，backend 是项目名称
django.setup()
from backend.models import CompInfo, CompClass, Area, CompLevel # 数据库模型

'''
    函数列表：
        1.  Read_Table_of_ExcelFile (file_path, tableName)
        2.  Format_Conversion(col_id, value)
        3.  Excel_Write_into_DataBase(tabObj, tabData) 
            （主要功能函数：读取xls表对象后，循环读取一行，分别使用函数2做格式处理，一并记录在字典中，最终一起记录进数据库）
        4.  main
    注意：
        测试时，xls文件路径、项目名称、模型名、DB模型结构要调整
    附：
        8.31 models内容用于测试：
        -------------------------------------------------
        | class Test2(models.Model):
        |     name = models.CharField(max_length=140)
        |     startTime = models.DateField("报名开始时间")
        |     endTime = models.DateField("报名结束时间")
        -------------------------------------------------
'''

# -------------------------------------------------------------------------------
"""
由于数据表的属性顺序与Excel中的列顺序不相符，因此在此对应
{0:19, 1:7, 2:15, 3:0, 4:1, 5:2, 6:9, 7:4, 8:5, 9:11, 10:6, 11:18, 12:16}
"""
Ex_Class = 19
Ex_AreaID = 7
Ex_Level = 15
Ex_Name = 0
Ex_ApplyStartTime = 1
Ex_ApplyEndTime = 2
Ex_Organizers = 9
Ex_Object = 4
Ex_Methods = 5
Ex_Schedule = 11
Ex_Form = 6
Ex_Statement = 18
Ex_urls = 16
"""
数据表中：
0. IClass,   1. IAreaID,    2. ILevel,   3. IName, 
4. IApplyStartTime, 5. IApplyEndTime,    6. IOrganizers, 7. IObject, 
8. IMethods, 9. ISchedule,  10. IForm,   11. IStatement, 12. Iurls
"""
DB2Excel = {0:Ex_Class,    1:Ex_AreaID,     2:Ex_Level,    3:Ex_Name,
            4:Ex_ApplyStartTime,    5:Ex_ApplyEndTime,
            6:Ex_Organizers,        7:Ex_Object,        8:Ex_Methods,
            9:Ex_Schedule,          10:Ex_Form,         11:Ex_Statement,
            12:Ex_urls}
# ------------------------------------------------------------------------------------


# 读取xls文件中的表
def Read_Table_of_ExcelFile(file_path, tableName):
    # 打开xls文件
    xls_file = xl.open_workbook(file_path)
    # 参数为表名
    Tab_Obj = xls_file.sheet_by_name(tableName)

    return Tab_Obj


# 格式转换
def Format_Conversion(col_id, value):
    if col_id not in DB2Excel.values() and col_id is not Ex_Schedule+1:
        print("错误序号为：", col_id)
        raise ("Error!!")
    newValue = []
    # 1. 比赛名称：删除所有空字符只保留文字/数字
    if col_id is Ex_Name:
        newValue = re.sub('[\s]', '', value)
    # 2. 开始/结束时间：转化为时间格式，删除文字
    elif col_id is Ex_ApplyStartTime or col_id is Ex_ApplyEndTime:
        newValueStr = ''
        value = re.sub('\s', '', value)  # 删除空白字符
        newValue_strs = re.findall('[0-9]+', value) # 匹配数字
        # print(newValue_strs)
        # 数字格式不一，或缺少日期或包括小时分钟，统一处理
        if len(newValue_strs) == 0:
            newValueStr = '1900-1-1'  # 时间不详先置此时间
        elif len(newValue_strs) == 1:
            newValueStr = newValue_strs[0]+'-1-1'
        elif len(newValue_strs) == 2:
            newValueStr = newValue_strs[0] + '-' + newValue_strs[1] + '-1'
        elif len(newValue_strs) == 3:
            newValueStr = newValue_strs[0] + '-' + newValue_strs[1] + '-' + newValue_strs[2]
        # 出现其他数字,匹配20XX，确定此为年份，而后录入日期
        # 可能出现其余突发情况，再说（2019.8.31 17：23  --JieHeng）
        else:
            for d in range(len(newValue_strs)):
                if newValue_strs[d][0] == '2' and newValue_strs[d][1] == '0':
                    try:
                        newValueStr = newValue_strs[d] + '-' + newValue_strs[d+1] + '-' + newValue_strs[d+2]
                    except:
                        print("数据格式错误！")
                    break
        # 转换为标准格式
        newValue = datetime.datetime.strptime(newValueStr, '%Y-%m-%d')

    # 3. 举办方，参赛对象，参赛方式，参赛形式
    elif col_id in (Ex_Organizers, Ex_Object, Ex_Methods, Ex_Form):
        newValue = re.sub('[\s]', '', value)

    # 4. 赛事等级，匹配字母后进入CompLevel匹配
    elif col_id is Ex_Level:
        nameStr = re.findall('[A-Z]', value)# 匹配字母
        if len(nameStr) is not 0:
            nameStr = nameStr[0]+"类"
            return CompLevel.objects.get(Name=nameStr)
        else:
            return CompLevel.objects.get(Name="D类")

    # 5. 赛事分类
    elif col_id is Ex_Class:
        classList = ("科技创新", "创业商业", "艺术爱好", "游戏动漫",
                     "广告公益", "学科竞赛", "体育竞赛")
        i = 1
        output = 1
        for c in classList:
            if c is value:
                output = i
            else:
                i += 1
        return CompClass.objects.get(pk=output)

    # 6. 地区地区
    elif col_id is Ex_AreaID:
        provinceList = ('全国', '北京', '天津', '上海', '重庆', '河北', '山西', '辽宁',
                        '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西',
                        '山东', '河南', '湖北', '湖南', '广东', '海南', '四川',
                        '贵州', '云南', '陕西', '甘肃', '青海', '台湾', '内蒙古',
                        '广西', '西藏', '宁夏', '新疆', '香港', '澳门', '全球', )

        if value in provinceList:
            return Area.objects.get(Name=value)
        else:
            return Area.objects.get(Name="全国")

    # 7. 赛事官网
    elif col_id is Ex_urls:
        urls = value[5:]
        if len(urls) is 0:
            return "https://www.baidu.com"
        return urls

    # 5. 日程：
    elif col_id is Ex_Schedule or Ex_Schedule+1:
        newValue = re.sub('\t','', value)

    # 6. 赛事主体信息：
    else:
        newValue = value

    return newValue


# 将xls中的工作表写入数据库
def Excel_Write_into_DataBase(tabObj, tabData):
    DT = tabData.__doc__ # 拿到数据库所有字段(未筛选)
    Title_List = DT[DT.find('(') + 1:DT.find(')')].split(",")# 已筛选的所有数据库字段列表
    Title_List.pop(0)# 删除ID字段，用于添加ID字段外的数据
    print("数据库字段：",Title_List)
    print("总列数：", tabObj.ncols)
    # 数据库模型与excel的对应关系：

    # 循环所有行数
    for H in range(1,tabObj.nrows):
        dic = {}
        N = tabObj.row_values(H)  # excel表格当前行的数据
        # 循环所有列
        for dbi, exi in DB2Excel.items():
            # 拼接赛事日程安排
            if exi is Ex_Schedule:
                # print("当前行：", H, "当前数据库字段名：", Title_List[dbi].strip())
                value1 = Format_Conversion(exi, N[exi])  # 格式转换
                value2 = Format_Conversion(exi+1, N[exi+1])  # 格式转换
                value = value1+"\n"+value2
                value = value.replace(' ', "")
                dic[Title_List[dbi].strip()] = value  # 写入字典
            else:
                # print("当前行：", H, "当前数据库字段名：",Title_List[dbi].strip())
                value = Format_Conversion(exi, N[exi]) # 格式转换
                # print("当前行：", H, "当前数据库字段值：", value)
                dic[Title_List[dbi].strip()] = value # 写入字典

        # print("要写入数据库的数据字典：", dic)
        tabData.objects.create(**dic)  # 添加一条记录


if __name__ == "__main__":
    filePath = 'D:\资料\django\\test.xls'
    tableName = 'test'
    Tab_Obj = Read_Table_of_ExcelFile(filePath, tableName)
    Excel_Write_into_DataBase(Tab_Obj, CompInfo)