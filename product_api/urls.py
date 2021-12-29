from django.urls import path,include
from . import views
urlpatterns = [
    # path('',views.apiOverview,name='apiOverview'),
    path('product-list/',views.ShowAll, name='product-list'),
    path('product_by_id/<int:pk>/',views.oneproduct,name='product_by_name'),
    path('create/',views.CreateProduct,name='create'),
    path('update/<int:pk>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
