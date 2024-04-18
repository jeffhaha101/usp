"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, OrgMemberListView, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView, StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),
    # OrgMember URLs
    path('orgmembers_list', OrgMemberListView.as_view(), name='orgmembers-list'),
    path('orgmembers_list/add', OrgMemberCreateView.as_view(), name='orgmembers-add'),
    path('orgmembers_list/<pk>', OrgMemberUpdateView.as_view(), name='orgmembers-update'),
    path('orgmembers_list/<pk>/delete', OrgMemberDeleteView.as_view(), name='orgmembers-delete'),
    # Student URLs
    path('students_list/', StudentListView.as_view(), name='students-list'),
    path('students_list/add', StudentCreateView.as_view(), name='students-add'),
    path('students_list/<pk>', StudentUpdateView.as_view(), name='students-update'),
    path('students_list/<pk>/delete', StudentDeleteView.as_view(), name='students-delete'),
    # Colleges URLs
]
