"""Masir1401 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout_link'),

    path('', landing_page, name='landing_page_link'),
    # path('full_map/', full_map_page, name = 'full_map_page_link'),
    path('people_judge/', people_judge_page, name='people_judge_page_link'),
    path('on_masir/', on_masir, name='on_masir_link'),
    path('forgot_password/', forgot_password_page, name='forgot_password_page_link'),
    path('home/', home_page, name='home_page_link'),

    path('home/judge/', judge_page, name='judge_page_link'),
    path('home/judge/<int:id>/', judge_detail_page, name='judge_detail_page_link'),

    path('home/longterm_judge/', longterm_judge_page, name='longterm_judge_page_link'),
    path('home/longterm_judge/<int:id>/', longterm_judge_detail_page, name='longterm_judge_detail_page_link'),

    path('home/statistics/', statistics_page, name='statistics_page_link'),
    path('home/leaderboard/', leaderboard_page, name='leaderboard_page_link'),

    path('home/club/', club_page, name='club_page_link'),
    path('home/club/<int:id>/', club_detail_page, name='club_detail_page_link'),

    path('home/announcements/', club_page, name='announcements_page_link'),

    path('home/reports/', club_page, name='reports_page_link'),

    path('home/faq/', club_page, name='faq_page_link'),

    path('home/contact_admin/', contact_admin_page, name='contact_admin_page_link'),
    path('home/contact_admin/<int:id>/', contact_admin_detail_page, name='contact_admin_detail_page_link'),

    path('home/help/', help_page, name='help_page_link')
]
