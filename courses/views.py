from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from .forms import CourseModelForm
from .models import Course
# Create your views here.
#BASE VIEW Class = VIEW

class CourseObjectMixin(object):
    model = Course
    lookup = 'id'
    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj 

class CourseDeleteView(CourseObjectMixin, View):
    template_name = "courses/course_delete.html" # DetailView
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)
    
    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/courses/')
        return render(request, self.template_name, context)

class CourseUpdateView(View):
    template_name = "courses/course_update.html" # DetailView
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

class CourseCreateView(View):
    template_name = 'courses/course_create.html'
    def get(self, request, *args, **kwargs):
        # GET method
        form = CourseModelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # POST method
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
        form = CourseModelForm() # reintitialise the form and empty content of form
        context = {'form': form}
        return render(request, self.template_name, context)

class CourseListView(View):
    template_name = 'courses/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, id=None, *args, **kwargs):
        context = {'object_list': self.get_queryset()}
        return render(request, self.template_name, context)

# inheritance purposes; also alter url with class
# class MyListView(CourseListView):
#     queryset = Course.objects.filter(id=2)

class CourseView(CourseObjectMixin, View):
    template_name = 'courses/course_detail.html'
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {'object': self.get_object()}
        return render(request, self.template_name, context)

# class CourseDetailView(View):
#     template_name = 'about.html'
#     def get(self, request, *args, **kwargs):
#         return render(request, self.template_name, {})

#     # def get(request, *args, **kwargs):
#     #     return render(request, 'about.html', {})

# HTTP Methods
def my_fbv(request, *args, **kwargs):
    print(request, *args, **kwargs)
    return render(request, 'about.html', {})

