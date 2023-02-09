from django.urls import path

import webapp.views.cats
import webapp.views.base

urlpatterns = [
    path("", webapp.views.base.add_cat),
    path('cat_stats', webapp.views.cats.cat_stats)
]
