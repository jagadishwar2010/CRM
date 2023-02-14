from django.urls import include, path
from . import views

urlpatterns = [
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('', views.home, name="home"),
    path('account/', views.account_settings, name="account"),

    path('user/', views.user_page, name="user-page"),
    path('products/', views.products, name="products"),
    path('customers/<str:cust_id>', views.customers, name="customer"),
    path('create_order/<str:cust_id>', views.create_order, name="create_order"),
    path('update_order/<str:order_id>', views.update_order, name="update_order"),
    path('delete_order/<str:order_id>', views.delete_order, name="delete_order"),
]
