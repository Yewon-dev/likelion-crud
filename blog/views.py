from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
# Create your views here.

def main(request):
    posts = Post.objects
    return render(request, 'posts.html', {'posts':posts})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)   #form 변수에 PostForm 할당
        if form.is_valid(): # form 유효성 검증
            form.save()     # 저장
            return redirect('main')     # main으로 다시 감
    else:   # GET으로 요청할 때
        form = PostForm()
    return render(request, 'create.html', {'form':form})

def detail(request, pk):    # 자세히 보기
    post = get_object_or_404(Post, pk=pk) # Post model에 있는 object 불러오기
    return render(request, 'detail.html', {'post':post})

def update(request, pk):    # pk값으로 객체 구분
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)   # instance : 저장된 내용 불러오기
        if form.is_valid(): 
            form.save() 
            return redirect('main')
    else:   # GET으로 요청할 때
        form = PostForm(instance=post)
    return render(request, 'updates.html', {'form':form})

def delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('main')

