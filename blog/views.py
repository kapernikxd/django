from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View


from .models import Category, Post


# Create your views here.
# def home(request):
#     a = 4
#     return HttpResponse("<h1>{} привет</h1>".format(a))

# a = 4
#
# class HomeView(View):
#     def get(self, request):
#         return HttpResponse("<h1>{} привет</h1>".format(a))
#
#
#     def post(self,request):
#         pass


class HomeView(View):
    def get(self, request):
        # context = {
        #     "name":
        #         {
        #             "user": "Вадим"
        #         }
        #
        # }

        catagory_list = Category.objects.all()
        post_list = Post.objects.all()
        print(catagory_list)
        return render(request, "blog/home.html", {"categories": catagory_list, "posts": post_list})




class CategoryView(View):
    '''Вывод статей категорий'''

    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        return render(request, "blog/category_list.html", {"category": category})



class PostView(View):
    '''Вывод постов'''

    def get(self, request, post_slug):
        post = Post.objects.get(slug=post_slug)
        return render(request, "blog/post_list.html", {"post": post})