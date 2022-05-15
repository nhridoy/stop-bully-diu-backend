from django.urls import path
from complain import views as complain_view

urlpatterns = [
    path('complain/', complain_view.ComplainView.as_view(), name="Complain"),
    path('complain_list/', complain_view.ComplainListView.as_view(), name="Complain_list"),
    path('complain_status/<id>/', complain_view.ComplainStatusView.as_view(), name="Complain_status_change"),

]