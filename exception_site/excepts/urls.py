from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('indexExcept/', IndexErr, name='IndexExcept'),
    path('attributeExcept/', AtttributeError, name='AttrExcept'),
    path('importExcept/', ImportErr, name='ImportExcept'),
    path('zeroDivExcept/', ZeroDivErr, name='ZeroDivExcept'),
    path('EOFExcept/', EOFErr, name='EOFExcept'),
]