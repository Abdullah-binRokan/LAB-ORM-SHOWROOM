from django.urls import path
from . import views

app_name = "cars"

urlpatterns = [
    path("all/", views.all_cars_view, name="all_cars_view"),
    path("new/", views.new_car_view, name="new_car_view"),
    path("update/<car_id>/", views.update_car_view, name="update_car_view"),
    path("details/<car_id>/", views.details_car_view, name="details_car_view"),
    path("delete/<car_id>/", views.delete_car_view, name="delete_car_view"),
    path("colors/new/", views.new_color_view, name="new_color_view"),
    path("colors/update/<color_id>/", views.update_color_view, name="update_color_view"),
    path("colors/delete/<color_id>/", views.delete_color_view, name="delete_color_view"),
    path("<car_id>", views.add_review_view, name="add_review_view"),
]