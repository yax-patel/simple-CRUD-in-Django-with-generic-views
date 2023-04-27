from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from .form import imgFormWithModel
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import imgForm
# Create your views here.

# form using FBV

# def imgFormView(request,*args, **kwargs):
#     print(request)
#     form = imgFormWithModel(request.POST or None, request.FILES or None)
#     if form.is_valid():
#         form.save()
#         return redirect(reverse('imgform:success-url'))

#     return render(request, 'imgForm.html',{'form': form})

# form using Class
class imgFormView(CreateView):
    model = imgForm
    fields = '__all__'
    template_name = "imgForm.html"

    def get_success_url(self):
        return reverse_lazy('imgform:success-url')


class getData(ListView):
    model = imgForm
    context_object_name = "data"
    template_name = "ListView.html"

class detailData(DetailView):
    model = imgForm
    template_name = "DetailView.html"
    
class deleteData(DeleteView):
    model = imgForm
    template_name = 'delete.html'
    def get_success_url(self):
        return reverse_lazy("imgform:success-del")
    
class updateData(UpdateView):
    model = imgForm
    fields = '__all__'
    template_name = "imgForm.html"
    def get_success_url(self):
        return reverse_lazy("imgform:success-url")

def success_form(request, *args, **kwargs):
    return HttpResponse(f'''
            <script>
                alert('Data Inserted Successfully');
                window.location.href = "{reverse_lazy('imgform:getData')}";
            </script>
    ''')

def success_del(request, *args, **kwargs):
    return HttpResponse(f'''
            <script>
                alert('deleted Successfully');
                window.location.href = "{reverse_lazy('imgform:getData')}";
            </script>
    ''')