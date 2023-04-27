from django.urls import path 
from imgform.views import imgFormView, success_form, getData, detailData, success_del, deleteData, updateData

app_name = 'imgform'
urlpatterns = [
    # path('', imgFormView, name='form'),
    path('', imgFormView.as_view(), name='form'),
    path('deletemsg/', success_del, name='success-del'),
    path('success/', success_form, name='success-url'),
    path('getData/', getData.as_view(), name='getData'),
    path('get/<int:pk>', detailData.as_view(), name='getDetails'),
    path('delete/<int:pk>', deleteData.as_view(), name='deleteData'),
    path('update/<int:pk>', updateData.as_view(), name='updateData'),
]