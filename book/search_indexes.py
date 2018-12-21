from  haystack import indexes
from book.models import *


# 注意格式(模型类名+Index)
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # 给title,content设置索引
    bk_name = indexes.NgramField(model_attr='bk_name')
    intro = indexes.NgramField(model_attr='intro')

    def get_model(self):
        return MainprojectBooks

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-bk_id')
