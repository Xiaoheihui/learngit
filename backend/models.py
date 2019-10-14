from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class CompClass(models.Model):
    """
    表中列名	    数据类型	    可否为空	        说明
    Cid	        Int	        not null(主键)	类别编号
    CName	    varchar	    not null	    类别名称
    CStatement	varchar	    null	        类别说明
    CCount	    int	        Not null	    该类别下赛事数量
    """
    Cid        = models.AutoField(primary_key=True, verbose_name=u"类别编号")
    CName      = models.CharField(max_length=10, default="未设置", verbose_name=u"类别名称")
    CStatement = models.CharField(max_length=100, null=True, verbose_name=u"类别说明")
    CCount     = models.PositiveSmallIntegerField(default=0, verbose_name=u"该类别下赛事数量")

    class mate:
        db_table = "CompClass"
        verbose_name = '赛事类别'
        verbose_name_plural = '赛事类别列表'

    def __str__(self):
        return self.CName


class CompLevel(models.Model):
    ID        = models.AutoField(primary_key=True, verbose_name=u"赛事等级编号")
    Name      = models.CharField(max_length=5, default="", verbose_name=u"赛事等级名字")
    Statement = models.CharField(max_length=100, null=True, verbose_name=u"赛事等级说明")
    class mate:
        db_table = "CompLevel"
        verbose_name = '赛事等级'
        verbose_name_plural = '赛事等级表'

    def __str__(self):
        return self.Name+"赛事"


class Area(models.Model):
    ID   = models.AutoField(primary_key=True, verbose_name=u"地区编号")
    Name = models.CharField(max_length=5, default=u"全国", verbose_name=u"地区名字")

    class mate:
        db_table = "Area"
        verbose_name = '地区'
        verbose_name_plural = '地区列表'

    def __str__(self):
        return self.Name


class UserMessage(models.Model):
    """
    表中列名	        数据类型	    可否为空	        说明
    Uid	            Int	        not null(主键)	用户编号
    UName	        char	    not null	    用户名
    UPassword 	    char	    not null	    用户密码
    UEmail	        char	    not null	    用户Email
    UBirthday	    datetime	null	        用户生日
    USex	        char	    null	        用户性别
    UStatement	    varchar	    null	        用户个人说明
    URegDate 	    datetime	not null	    用户注册时间
    ULastOnlineDate	datetime	not null	    用户最后上线时间
    UPostCount	    Int	        Not null	    用户发帖数
    URepCount	    Int	        Not null	    用户回帖数
    UIfAdmin	    bool	    Not null	    是否管理员
    Unickname       varchar     not null        昵称
    """
    UserBase = models.OneToOneField(User, on_delete=models.CASCADE)
    # 个人资料
    UBirthday  = models.DateField(u'用户生日', null=True, blank=True)
    USex       = models.CharField(u'用户性别', max_length=2, default='', null=True, blank=True)
    UStatement = models.CharField(u'用户个人说明', max_length=150, default='', null=True, blank=True)
    Unickname   = models.CharField(u'用户昵称', max_length=10, default='', blank=True)
    # 系统信息
    UPostCount      = models.PositiveSmallIntegerField( u'用户发帖数', default=0)
    URepCount       = models.PositiveSmallIntegerField( u'用户回帖数', default=0)

    class mate:
        db_table = "Users"
        verbose_name = '用户信息'
        verbose_name_plural = '用户列表'

    def __str__(self):
        return self.UserBase.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        a = UserMessage.objects.create(UserBase=instance)
        #a.save()

@receiver(post_save, sender=User)
def save_user_userMessage(sender, instance, **kwargs):
    instance.usermessage.save()


class BBSSection(models.Model):
    """
    表中列名	    数据类型	可否为空	       说明
    Sid	        Int	    Not null(主键)	版块编号
    SName	    char	Not null	版块名称
    SClassId	int	    Not null	比赛类别编号
    SStatement	Varchar	Not null	版块说明
    SClickCount	Int	    Not null	版块总点击次数
    SRepCount	int	    Not null	板块总回复数
    STopicCount	int	    Not null	版块主贴数
    """
    Sid         = models.AutoField(primary_key=True, verbose_name=u"版块编号")
    SName       = models.CharField(max_length=10,  default="", verbose_name=u"版块名称")
    SStatement  = models.CharField(max_length=200, default="", verbose_name=u"版块说明")
    SClickCount = models.PositiveSmallIntegerField(default=0,   verbose_name=u"版块总点击次数")
    SRepCount   = models.PositiveSmallIntegerField(default=0,   verbose_name=u"板块总回复数")
    STopicCount = models.PositiveSmallIntegerField(default=0,   verbose_name=u"版块主贴数")
    # 外键
    SClassId    = models.ForeignKey(CompClass, on_delete=models.CASCADE, verbose_name=u"比赛类别编号")

    class mate:
        db_table = "BBSSection"
        verbose_name = '板块信息'
        verbose_name_plural = '板块列表'


class BBSTopic(models.Model):
    """
    表中列名	  数据类型	可否为空	      说明
    Tid	        Int	    not null(主键)	主帖编号
    TSid	    Int	    not null	主帖版块编号
    TUid	    Int	    not null	主帖用户编号
    TReplyCount	Int	    not null	主帖回复次数
    TTopic 	    Varchar	not null	主帖标题
    TContents	Text	not null	主帖内容
    TTime 	   Datetime	not null	发帖时间
    TClickCount Int	    not null	主帖点击次数
    TLastClickT	Datetime not null	主帖最后点击时间
    """
    Tid         = models.AutoField(primary_key=True, verbose_name=u"主帖编号")
    # 外键
    TSid        = models.ForeignKey(BBSSection,  on_delete=models.CASCADE, verbose_name=u"主帖版块编号")
    TUid        = models.ForeignKey(UserMessage, on_delete=models.CASCADE, verbose_name=u"主帖用户编号")

    TReplyCount = models.PositiveSmallIntegerField(default=0, verbose_name=u"主帖回复次数")
    TTopic      = models.CharField(max_length=50,  default="", verbose_name=u"主帖标题")
    TContents   = models.TextField(max_length=1500, null=True, verbose_name=u"主帖内容")
    TClickCount = models.PositiveSmallIntegerField(default=0, verbose_name=u"主帖点击次数")
    TTime       = models.DateTimeField(verbose_name=u"发帖时间",  auto_now_add=True, editable=True)
    TLastClickT = models.DateTimeField(verbose_name=u"主帖最后点击时间")

    class mate:
        db_table = "BBSTopic"
        verbose_name = '主贴信息'
        verbose_name_plural = '主帖列表'


class BBSReply(models.Model):
    """
    表中列名	    数据类型	    可否为空	        说明
    Rid	        Int	        Not null(主键)  回贴编号
    RTid	    int	        Not null	    主贴编号
    RSid	    Int	        Not null	    板块编号
    RUid	    Int	        Not null	    回复者用户编号
    RTime	    datetime    Not null	    回复时间
    RContent	text	    Not null	    回复内容
    RLevelNum	int	        Not null	    在主贴中对应楼层
    """
    Rid       = models.AutoField(primary_key=True, verbose_name=u"回贴编号")
    # 外键
    RTid      = models.ForeignKey(BBSTopic, on_delete=models.CASCADE,    verbose_name=u"主贴编号")
    RSid      = models.ForeignKey(BBSSection, on_delete=models.CASCADE,  verbose_name=u"板块编号")
    RUid      = models.ForeignKey(UserMessage, on_delete=models.CASCADE, verbose_name=u"回复者用户编号")

    RTime     = models.DateTimeField(auto_now_add=True, verbose_name=u"回复时间", editable=True)
    RContent  = models.TextField(max_length=500,  default="", verbose_name=u"回复内容")
    RLevelNum = models.PositiveSmallIntegerField( default=0,  verbose_name=u"在主贴中对应楼层")

    class mate:
        db_table = "BBSReply"
        verbose_name = '回复信息'
        verbose_name_plural = '回复信息列表'


class CompInfo(models.Model):
    # """
    # 表中列名	        数据类型	    可否为空	        说明
    # Iid               Int	        not null(主键)	赛事编号
    # IName	            varchar	    not null	    赛事名称
    # IApplyStartTime	datetime	Not null	    赛事报名开始时间
    # IApplyEndTime	    datetime	Not null	    赛事报名结束时间
    # IClass	        Varchar	    Not null	    竞赛类别
    # IAreaID	        Int	        Not null	    赛事地区编号
    # IOrganizers	    Varchar	    Not null	    主办单位
    # IObject	        text        Not null	    参赛对象
    # IMethods	        text	    Not null	    参赛方法
    # ISchedule	        text	    Not null	    赛程信息
    # Iurls	            Varchar	    Null	        赛事官网
    # IStatement	    text	    Not null	    赛事介绍
    # ILevel            int         not null        赛事等级编号
    # """
    Iid     = models.AutoField(primary_key=True, verbose_name="赛事编号")
    # 外键
    IClass  = models.ForeignKey(CompClass, on_delete=models.CASCADE, verbose_name="竞赛类别编号")
    IAreaID = models.ForeignKey(Area, on_delete=models.CASCADE, default='', verbose_name="赛事地区编号")
    ILevel  = models.ForeignKey(CompLevel, on_delete=models.CASCADE, verbose_name="赛事等级编号")

    IName   = models.CharField(max_length=60, default="", verbose_name="赛事名称")
    IApplyStartTime = models.DateField(verbose_name="报名开始时间")
    IApplyEndTime   = models.DateField(verbose_name="报名结束时间")
    IOrganizers = models.CharField(max_length=100, default="", verbose_name="主办单位")
    IObject     = models.TextField(default="（空）", verbose_name="参赛对象")
    IMethods    = models.TextField(default="（空）", verbose_name="参赛方法")
    ISchedule   = models.TextField(default="（空）", verbose_name="赛程信息")
    IForm       = models.TextField(default="（空）", verbose_name="参赛形式")
    IStatement  = models.TextField(default="（空）", verbose_name="赛事介绍")
    Iurls = models.URLField(default="", verbose_name="赛事官网")

    class mate:
        db_table = "CompInfo"
        verbose_name = '赛事信息'
        verbose_name_plural = '赛事列表'

    @staticmethod
    def list_all_member(s):
        list = []
        for name, value in vars().items():
            list.append(name)
        return list

    def __str__(self):
        return self.IName


class CompRecord(models.Model):
    """
    表中列名	        数据类型	    可否为空	        说明
    RID	            Int	        not null(主键)	记录编号
    RTitle	        varchar	    not null	    记录标题
    RStatement	    varchar	    Not null	    记录简要说明
    RClassID	    int	        Not null	    赛事类别编号
    RContentID	    Int	        Not null	    赛事内容编号
    RPromulgatorID	Int	        Not null	    发布者编号
    RClickCount	    Int	        Not null	    点击数
    RTime	        Datetime	Not null	    发布日期
    RMarkCount	    Int	        Not null	    收藏人数
    RMarkUser       int         null            收藏者
    """
    RID             = models.AutoField(primary_key=True, verbose_name=u"记录编号")
    # 外键
    RClassID        = models.ForeignKey(CompClass,   on_delete=models.CASCADE, verbose_name=u"赛事类别编号")
    RContentID      = models.OneToOneField(CompInfo, on_delete=models.CASCADE, verbose_name=u"赛事内容编号")
    RPromulgatorID  = models.ForeignKey(User, on_delete=models.CASCADE,
                                        related_name="Promulgator_set", verbose_name=u"发布者编号")
    RMarkUser       = models.ManyToManyField(UserMessage, through='MarkMessage',
                                        related_name="MarkUser_set", symmetrical=False, verbose_name="收藏者")

    RTitle          = models.CharField(max_length=60,  default="", verbose_name=u"记录标题")
    RStatement      = models.CharField(max_length=100, default="", verbose_name=u"记录简要说明")
    RTime       = models.DateTimeField(auto_now_add=True, editable=True,  verbose_name=u"发布日期")
    RClickCount = models.PositiveSmallIntegerField(default=0, verbose_name=u"点击数")
    RMarkCount  = models.PositiveSmallIntegerField(default=0, verbose_name=u"收藏人数")

    class mate:
        db_table = "CompRecord"
        verbose_name = '赛事记录'
        verbose_name_plural = '赛事记录列表'


@receiver(post_save, sender=CompInfo)
def create_compRecord(sender, instance, created, **kwargs):
    if created:
        a = CompRecord.objects.create(RContentID=instance,
                                      RClassID=instance.IClass,
                                      RPromulgatorID=UserMessage.objects.get(pk=1),
                                      RTitle=instance.IName)

@receiver(post_save, sender=CompInfo)
def save_user_userMessage(sender, instance, **kwargs):
    instance.comprecord.save()


class MarkMessage(models.Model):
    """
        表中列名	        数据类型	    可否为空	        说明
        CompRecordId	Int	        not null	    记录编号
        UsersId     	Int	        not null	    用户编号
        MarkTime        datetime    not null        收藏时间
    """
    CompRecordId = models.ForeignKey(CompRecord, on_delete=models.CASCADE, verbose_name="记录编号")
    UsersId      = models.ForeignKey(UserMessage, on_delete=models.CASCADE, verbose_name="用户编号")
    MarkTime     = models.DateTimeField(auto_now_add=True, editable=True, verbose_name="收藏时间")


class test11(models.Model):
    name = models.CharField(max_length=10)