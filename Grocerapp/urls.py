from django.urls import path
from.import views
urlpatterns=[
    path("",views.index),
    path('Login/',views.Login,name="Login"),
    path('check_login/',views.check_login),
    path('dashboard/',views.dashboard),
    path('categories/',views.categories),
    path('create_category/',views.create_category),
    path('save_category/',views.save_category),
    path('edit_category/<id>',views.edit_category),
    path('delete_category/<id>',views.delete_category),
    path('update_category/<id>',views.update_category),
    path('SubCategories/',views.SubCategories),
    path('create_SubCategory/',views.create_SubCategory),
    path('save_SubCategory/',views.save_SubCategory),
    path('edit_SubCategory/<id>',views.edit_SubCategory),
    path('delete_SubCategory/<id>',views.delete_SubCategory),
    path('update_SubCategory/<id>',views.update_SubCategory),
    path('Products/',views.Products),
    path('create_products/',views.create_products),
    path('save_products/',views.save_products),
    path('delete_Products/<id>',views.delete_Products),
    path('edit_Products/<id>',views.edit_Products),
    path('update_products/<id>',views.update_products),
    path('Cat_Products/<id>',views.Cat_Products),
    path('SubCatProducts/<id>',views.SubCatProducts),
    path('add_to_cart/<id>',views.add_to_cart),
    path('wishlist/',views.wishlist),
    path('add_to_wishlist/<id>',views.add_to_wishlist),
    path("checkout/",views.checkout,name="checkout"),
    path("signup/",views.signup,name="signup"),
    path('save_signup/',views.save_signup),
    path('save_order/',views.save_order),
    path('Admin_Orders/',views.Admin_Orders),
    path('Delivery_partners/',views.Delivery_partners),
    path('create_delivery_partner/',views.create_delivery_partner),
    path('save_delivery_partners/',views.save_delivery_partners),
    path('edit_deliverypartner/<id>',views.edit_deliverypartner),
    path('update_deliverypartner/<id>',views.update_deliverypartner),
    path('delete_deliverypartner/<id>',views.delete_deliverypartner),
    path('out_for_delivery_page/<id>', views.out_for_delivery_page),
    path('assign_delivery_partner/', views.assign_delivery_partner, name='assign_delivery_partner'),
    path('delivery_dashboard/',views.delivery_dashboard),
    path('delivery_orders/',views.delivery_orders),
    path('ordercomplete/<id>',views.ordercomplete),
    path('ordercancel/<id>',views.ordercancel),
    path('logoutpartner/',views.logoutpartner),
    path('Contactpage/',views.Contactpage),
    path('save_contactpage/',views.save_contactpage),
    path('contactpagetbl/',views.contactpagetbl),
    path('Logout/',views.Logout),
    path('myaccount/',views.myaccount),
    path('Logout_user/',views.Logout_user),










    path('update-order-status/<int:order_id>/', views.update_order_status, name='update_order_status'),






]
