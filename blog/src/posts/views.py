# from django.views import ListView
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Post
# Create your views here.

class PostFeaturedListView(ListView):
	template_name = 'posts/list.html'

	def get_queryset(self,*args,**kwargs):
		request = self.request
		return Post.objects.all().featured()
		

class PostFeaturedDetailView(DetailView):
	queryset = Post.objects.all().featured()
	template_name = 'posts/featured-detail.html'


class PostListView(ListView):
	# queryset = Post.objects.all()
	template_name = "posts/list.html"

	# def get_context_data(self, *args, ** kwargs):
	# 	context = super(PostListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context

	def get_queryset(self,*args,**kwargs):
		request = self.request
		return Post.objects.all()	

def post_list_view(request):
	queryset = Post.objects.all()
	context= {
		'object_list' : queryset
	}
	return render(request,"posts/list.html",context)
	# return render(request,"posts/snipps/card.html",context)



class PostDetailSlugView(DetailView):
	queryset = Post.objects.all()
	template_name = "posts/detail.html"

	def get_object(self,*args,**kwargs):
		request = self.request
		slug = self.kwargs.get('slug')
		try:
			instance = Post.objects.get(slug=slug,active=True)
		except Post.DoesNotExist:
			raise Http404('Post not found!')
		except Post.MultipleObjectReturned:
			qs = Post.objects.filter(slug=slug,active=True)
			instance = qs.first()
		except:
			raise Http404('Uhmmm...')
		return instance

class PostDetailView(DetailView):
	# queryset = Post.objects.all()
	template_name = "posts/detail.html"


	def get_context_data(self, *args, ** kwargs):
		context = super(PostDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		# context['abc'] = 323
		return context
	
	def get_object(self,*args,**kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		instance = Post.objects.get_by_id(pk)
		if instance is None:
			raise Http404("Post doesn't exist.")
		return instance

	def get_queryset(self,*args,**kwargs):
		request = self.request
		pk = self.kwargs.get('pk')
		return Post.objects.filter(pk=pk)


def post_detail_view(request,pk=None, *args, **kwargs):
	
	instance = Post.objects.get_by_id(pk)
	if instance is None:
		raise Http404("Post doesn't exist.")
	
	context= {
		'title'  : 'Post Details',
		'object' : instance
	}
	return render(request,"posts/detail.html",context)
