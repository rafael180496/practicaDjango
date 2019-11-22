from django.shortcuts import render,get_object_or_404
from .models import Post,Category
# Create your views here.
def blog(request):
    posts =Post.objects.all()
    return render(request,"blog/blog.html",{'posts':posts})

def category(request,category_id):

    try:
        category = Category.objects.get(id=category_id)
    except Exception :
        return render(request, 'core/error.html',{'err':404})
    
    return render(request, 'blog/category.html', {'category': category})
    #category=get_object_or_404(Category,id=category_id)
    #filtrar las categorias
    #posts=Post.objects.filter(categories=cat)
    #return render(request,'blog/category.html',{'cat':cat,
    #                                            'posts':posts})


    
