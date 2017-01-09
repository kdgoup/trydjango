from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import PostForm
from django.contrib import messages

from .models import Post
# Create your views here.

def posts_list(request):
	queryset = Post.objects.all()
	context = {
		"object_list" : queryset,
		"main_header" : "list"
		}

	# if request.user.is_authenticated():
	# 	context = {
	# 	"title":"User logged in list!"
	# 	}
	# else:
	# 	context = {
	# 	"title":"List"
	# 	}
	return render(request,'posts_list.html',context)

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"created successfully")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request,"created successfully")
	context = {
		"form": form,
	}
	return render(request,'post_form.html',context)

def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	context = {
	"title": instance.title,
	"instance": instance 
	}
	return render(request,'post_detail.html',context)

def post_update(request, id=None):
	instance = get_object_or_404(Post, id=id)
	form = PostForm(request.POST or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"item saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"title": instance.title,
		"form": form,
		"instance": instance,
	}
	return render(request,'post_form.html',context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	instance.delete()
	messages.success(request,"item deleted")
	return redirect("posts:list")