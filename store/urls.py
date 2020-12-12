from django.urls import path
from .views import StoreView, DetailsView, cart, remove_cart, OrderView, remove_single_product, Checkout, PaymentView, CategoryView, ProfileView


urlpatterns = [
    # Leave as empty string for base url
    path('', StoreView.as_view(), name="store"),
    path('details/<slug>', DetailsView.as_view(), name="details"),
    path('category/<category>', CategoryView.as_view(), name='category'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('cart/<slug>', cart, name='cart'),
    path('remove_cart/<slug>', remove_cart, name='remove_cart'),
    path('remove_single_product/<slug>/',
         remove_single_product, name='remove_single_product'),
    path('orderview/', OrderView.as_view(), name='orderview'),
    path('checkout/', Checkout.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),

]
