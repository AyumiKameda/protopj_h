from django.contrib import admin #adminサイトテンプレ読み込み
from .models import GoodsTBL #model定義TBL読み込み
from .models import CategoryTBL #model定義TBL読み込み
from .models import HighCategoryTBL #model定義TBL読み込み


#adminサイトのメソッドで以下TBL登録
admin.site.register(GoodsTBL)
admin.site.register(CategoryTBL)
admin.site.register(HighCategoryTBL)
