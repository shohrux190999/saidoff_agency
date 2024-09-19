from django.urls import path
<<<<<<< HEAD

from service_app.views import ServiceAPIView, ServiceDescriptionAPIView, OrderAPIView, PortfolioListAPIView, \
    TagListAPIView

urlpatterns = [

    path('services/', ServiceAPIView.as_view(), name='service-list'),
    path('service_descriptions/', ServiceDescriptionAPIView.as_view(), name='service-description-list'),
    path('orders/', OrderAPIView.as_view(), name='order-list'),
    path('portfolios/', PortfolioListAPIView.as_view(), name='portfolio-list'),
    path('tags/', TagListAPIView.as_view(), name='portfolio-list'),

]
=======
from .views import ServiceList, ServiceDetail, ServiceDescriptionList, ServiceDescriptionDetail, OrderList, OrderDetail, PortfolioList, PortfolioDetail


urlpatterns = [
    path('services/', ServiceList.as_view(), name='service_list'),
    path('services/<int:pk>/', ServiceDetail.as_view(), name='service_detail'),
    path('service_descriptions/', ServiceDescriptionList.as_view(), name='service_description_list'),
    path('service_descriptions/<int:pk>/', ServiceDescriptionDetail.as_view(), name='service_description_detail'),
    path('orders/', OrderList.as_view(), name='order_list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    path('portfolios/', PortfolioList.as_view(), name='portfolio_list'),
    path('portfolios/<int:pk>/',PortfolioDetail.as_view(), name='portfolio_details'),
]
>>>>>>> d20b4f3 (Commit xabari)
