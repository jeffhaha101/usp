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
from studentorg.views import * #HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, CollegeList, CollegeCreateView, CollegeUpdateView, CollegeDeleteView, StudentList, StudentCreateView, StudentUpdateView, StudentDeleteView, OrgMemList, OrgMemCreateView, OrgMemUpdateView, OrgMemDeleteView, ProgramList, ProgramCreateView, ProgramUpdateView, ProgramDeleteView
from studentorg import views
from django.contrib.auth import views as auth_views
from django.urls import path, re_path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),
    path('college_list', CollegeList.as_view(), name='college-list'),
    path('college_list/add', CollegeCreateView.as_view(), name='college-add'),
    path('college_list/<pk>', CollegeUpdateView.as_view(), name='college-update'),
    path('college_list/<pk>/delete', CollegeDeleteView.as_view(), name='college-delete'),
    path('student_list', StudentList.as_view(), name='student-list'),
    path('student_list/add', StudentCreateView.as_view(), name='student-add'),
    path('student_list/<pk>', StudentUpdateView.as_view(), name='student-update'),
    path('student_list/<pk>/delete', StudentDeleteView.as_view(), name='student-delete'),
    path('orgmember_list', OrgMemList.as_view(), name='orgmember-list'),
    path('orgmember_list/add', OrgMemCreateView.as_view(), name='orgmember-add'),
    path('orgmember_list/<pk>', OrgMemUpdateView.as_view(), name='orgmember-update'),
    path('orgmember_list/<pk>/delete', OrgMemDeleteView.as_view(), name='orgmember-delete'),
    path('program_list', ProgramList.as_view(), name='program-list'),
    path('program_list/add', ProgramCreateView.as_view(), name='program-add'),
    path('program_list/<pk>', ProgramUpdateView.as_view(), name='program-update'),
    path('program_list/<pk>/delete', ProgramDeleteView.as_view(), name='program-delete'),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path('charts/', ChartView.as_view(), name='chart-view'),
    path('charts/bar_chart_data/', bar_chart_data, name='bar-chart-data'),
    path('charts/radar_chart_data/', radar_chart_data, name='radar-chart-data'),
    path('charts/polar_area_chart_data/', polar_area_chart_data, name='polar-area-chart-data'),
    path('charts/doughnut_chart_data/', doughnut_chart_data, name='doughnut-chart-data'),
    path('charts/bubble_chart_data/', bubble_chart_data, name='bubble-chart-data'),

]
