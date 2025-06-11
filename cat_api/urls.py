from django.urls import path, include
from .views import CatCreateView, create_mission, list_missions, get_mission, delete_mission, complete_target, \
    update_target_notes, assign_cat_to_mission
from rest_framework.routers import DefaultRouter
from .views import CatViewSet

router = DefaultRouter()
router.register(r'cats', CatViewSet, basename='cat')

urlpatterns = [
    path('', include(router.urls)),
    path('missions/', list_missions),
    path('missions/create/', create_mission),
    path('missions/<int:pk>/', get_mission),
    path('missions/<int:pk>/delete/', delete_mission),
    path('targets/<int:target_id>/complete/', complete_target),
    path('targets/<int:target_id>/update-notes/', update_target_notes),
    path('missions/<int:mission_id>/assign-cat/', assign_cat_to_mission),
]