from django.contrib import admin

from .models import BookInfo
from .models import HeroInfo

# 可视化处理

class HerfoInfoAdmin(admin.ModelAdmin):
    list_display=['id','hname','hcomment','hbook_id']
# Register your models here.
# 注册了才会在后台显示
admin.site.register(BookInfo)
admin.site.register(HeroInfo,HerfoInfoAdmin)