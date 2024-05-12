from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from typing import Any
from django.db.models.query import QuerySet 
from django.db.models import Q

@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(OrganizationList, self) .get_queryset(*args, **kwargs)
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(name__icontains=query) |
                           Q(description__icontains=query))
        return qs

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

# OrgMember Views

class HomePageView(ListView):
    model = OrgMember
    context_object_name = 'home'
    template_name = 'home.html'

class OrgMemberListView(ListView):
    model = OrgMember
    template_name = 'orgmember_list.html'
    context_object_name = 'orgmembers'
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        qs = super(OrgMemberListView, self).get_queryset(*args, **kwargs)
        if self.request.GET.get("q") !=None:
            query = self.request.GET.get('q')
            qs = qs.filter(Q(student__lastname__icontains=query) | 
            Q(student__firstname__icontains=query) |
            Q(date_joined__icontains=query) | Q(organization_name__icontains=query))
        return qs 
class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_add.html'
    success_url = reverse_lazy('orgmembers-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_edit.html'
    success_url = reverse_lazy('orgmembers-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmembers-list')

# Student views

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'
class StudentListView(ListView):
    model = OrgMember
    template_name = 'student_list.html'
    context_object_name = 'students'
    paginate_by = 5

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('students-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('students-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('students-list')

# College views

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'
class CollegeListView(ListView):
    model = College
    template_name = 'college_list.html'
    context_object_name = 'college'
    paginate_by = 5

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

# Program views
class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'
    context_object_name = 'program'
    paginate_by = 5

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')

