from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts }
    return render(request,'blog/blogHome.html', context)



def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post) 
    print(request.user)
    context = {'post':post, 'comments':comments, 'user':request.user }
    return render(request,'blog/blogPost.html',context)  



def postComment(request):
    if request.method=="POST":
       comment = request.POST.get("comment")
       user = request.user
       postSno = request.POST.get("postSno")
       post = Post.objects.get(sno=postSno)
       
       comment= BlogComment(comment=comment , user=user, post= post)
       comment.save()
       messages.success(request,"your comment has been posted successfully")

        
    return redirect(f"/blog/{post.slug}")  