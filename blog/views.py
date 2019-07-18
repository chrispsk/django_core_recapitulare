from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import PostModel
from .forms import PostModelForm
from django.contrib import messages
from django.db.models import Q

def post_model_list_view1(request):
    qs = PostModel.objects.all()
    #print(qs) # A LIST of PostModel object
    if request.user.is_authenticated:
        print('User Logged In')
    return render(request, "select.html", {'qs':qs})

# by default goes to /accounts/login
#@login_required(login_url='/login') # if not redirect to /login or I can do it from settings.py LOGIN_URL=/login/
def post_model_list_view2(request):
    qs = PostModel.objects.all()
    return render(request, "select.html", {'qs':qs})

def detail_view(request, id):
    qs = get_object_or_404(PostModel, id=id)
    return render(request, "detail.html", {'qs':qs})

def create_view(request):
    # if request.method=="POST":
    #     form = PostModelForm(request.POST)
    #     if form.is_valid():
    #         form.save(commit=False)
    #         print(form.cleaned_data)
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        #obj = form.save(commit=False)
        #print(obj.title)
        obj = form.save() # save in database
        #print(obj.title)
        messages.success(request, "Created a new blog post")
        form = PostModelForm() # to clear the input
        # return HttpResponseRedirect('/blog/{num}'.format(num=obj.id))
        #print(form.cleaned_data)
    # ERRORS IN VIEW
    # if form.has_error:
    #     print(form.errors.as_json()) #for ajax
    #     print(form.errors.as_text())
    return render(request, 'create.html', {'form':form})

def update_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    form = PostModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        #print(obj.title)
        obj.save()
        #print(obj.title)
        messages.success(request, "Updated post")
        form = PostModelForm() # to clear the input
        return HttpResponseRedirect('/blog/{num}'.format(num=obj.id))
        #print(form.cleaned_data)
    return render(request, 'update.html', {'form':form})

def delete_view(request, id=None):
    obj = get_object_or_404(PostModel, id=id)
    if request.method == "POST":
        obj.delete()
        messages.success(request, "Deleted post")
        return HttpResponseRedirect('/blog/s/')
    return render(request, "delete.html", {'obj':obj})

def search(request):
    query = request.GET.get('q') # ,None is default
    if query is not None:
        # qs = PostModel.objects.filter(title__icontains=query)
        qs = PostModel.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(slug__icontains=query)
            )
    return render(request, "select.html", {'qs':qs})







def robust_view(request, id=None):
    """THIS COMBINES ALL CRUD IN 1 VIEW"""
    obj = None
    context = {}
    success_message = 'A new post created!'
    if id is None:
        template = 'create.html'
    if id is not None:
        obj = get_object_or_404(PostModel, id=id)
        context['object'] = obj
        template = 'detail.html'
        if 'edit' in request.get_full_path():
            template = 'update.html'
    if 'delete' in request.get_full_path():
        template = 'delete.html'
        if request.method == "POST":
            obj.delete()
            messages.success(request, "Post deleted")
            return HttpResponseRedirect('/blog/s/')
    if 'edit' in request.get_full_path() or 'c' in request.get_full_path():
        form = PostModelForm(request.POST or None, instance = obj)
        context['form'] = form
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, success_message)
            if obj is not None:
                return HttpResponseRedirect('/blog/{num}'.format(num=obj.id))
            context['form'] = PostModelForm()
    return render(request, template, context)
