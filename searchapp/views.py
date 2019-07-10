from django.shortcuts import render
from django.views import View

#関数で書く場合
"""
def index(request):
    return render(request, 'searchapp/index.html')
"""

#クラスで書く場合
class IndexView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'searchapp/index.html')

index = IndexView.as_view() #クラスベースのViewをView関数化するためのメソッド