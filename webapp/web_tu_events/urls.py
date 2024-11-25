from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("events/all_events.html", views.all_events, name="all_events"),
    path("events/<int:announcement_id>/", views.event_detail, name="event-detail"),
    path("events/<str:category>/", views.category_events, name="category_events"),
    path("found/create/", views.create_found_item, name="create_found_item"),
    path("found/list/", views.found_items_list, name="found_items_list"),
    path("lost/create/", views.create_lost_item, name="create_lost_item"),
    path("lost/list/", views.lost_items_list, name="lost_items_list"),
    path(
        "clubs/club_create_announcement/",
        views.club_create_announcement,
        name="clubs_create_announcement",
    ),
    path(
        "clubs/club_announcement_list/",
        views.all_club_announcement_list,
        name="clubs_announcement_list",
    ),
    path("lost/<int:lost_id>/", views.lost_detail, name="lost_detail"),
    path("found/<int:found_id>/", views.found_detail, name="found_detail"),
    path("lost/edit_lost_item/<int:lost_id>/", views.lost_edit, name="lost_edit"),
    path('lost/delete/<int:lost_id>/', views.lost_delete, name='lost_delete'),
    path("found/edit_found_item/<int:found_id>", views.found_edit, name="found_edit"),
    # path('clubs/tu_clubs', views.tu_clubs_list, name="tu_clubs"),
    # path('clubs/club_detail/<club_id>', views.club_detail , name="club_detail"),
    path('found/delete/<int:found_id>/', views.found_delete, name='found_delete'),
    path('announcement/<int:announcement_id>/interest/', views.toggle_interest, name='toggle_interest'),    
]
