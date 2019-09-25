import os
import django

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test1.settings")  # 添加环境变量，backend 是项目名称
django.setup()
from backend.models import Area, CompClass, test11, CompInfo, CompLevel

def writeArea():
    provinceList = ('全国', '北京', '天津',  '上海', '重庆', '河北', '山西', '辽宁',
                    '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西',
                    '山东', '河南',  '湖北', '湖南', '广东', '海南', '四川',
                    '贵州', '云南',  '陕西', '甘肃', '青海', '台湾', '内蒙古',
                    '广西', '西藏','宁夏', '新疆', '香港', '澳门', '全球')
    for p in provinceList:
        if not Area.objects.filter(Name=p).exists():
            Area.objects.create(Name=p)


def writeCompClass():
    classList = ("科技创新", "创业商业", "艺术爱好", "游戏动漫",
                 "广告公益", "学科竞赛", "体育竞赛")
    LogInfo = []
    for p in classList:
        if not CompClass.objects.filter(CName=p).exists():
            LogInfo.append(p)
            CompClass.objects.create(CName=p)
    print("已添加", LogInfo)


def writeCompLevel():
    levelList = (
        {"Name": "A类", "Statement": "由教育部主办，影响大的赛事"},
        {"Name": "B类", "Statement": "由省教育厅举办的赛事"},
        {"Name": "C类", "Statement": "由教指委，或全国性学会（协会）举办的赛事"},
        {"Name": "D类", "Statement": "其他或不详"},
    )
    LogInfo = []
    for p in levelList:
        LogInfo.append(p)
        CompLevel.objects.create(**p)
    print("已添加", LogInfo)

if __name__ == "__main__":
    # writeCompLevel()
    # writeArea()
    # writeCompClass()
    # test11.objects.create(name="sd")
    print(CompInfo.__doc__)