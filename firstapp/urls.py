from django.conf.urls import url
from firstapp.views import (
    base_view,
    category_view,
    product_view,
    cart_view,
    add_to_cart_view,
    remove_from_cart_view,
    change_item_qty,
    checkout_view,
    order_create_view,
    make_order_view,
    search,
    user_login,
    logout,
    user_register
    )

urlpatterns = [
    url(r'^category/(?P<category_slug>[-\w]+)/$', category_view, name='category_detail'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', product_view, name='product_detail'),
    url(r'^add_to_cart/$', add_to_cart_view, name='add_to_cart'),
    url(r'^remove_from_cart/$', remove_from_cart_view, name='remove_from_cart'),
    url(r'^change_item_qty/$', change_item_qty, name='change_item_qty'),
    url(r'^cart/$', cart_view, name='cart'),
    url(r'^checkout/$', checkout_view, name='checkout'),
    url(r'^order/$', order_create_view, name='create_order'),
    url(r'^make_order/$', make_order_view, name='make_order'),
    url(r'^search/$', search, name='search'),
    url(r'^login/', user_login,  name='login'),
    url(r'^logout/$', logout,  name='logout'),
    url(r'^user_register/', user_register,  name='user_register'),
    url(r'^$', base_view, name = 'base'),

]