#from datetime import date ###used when getting data from views.py
from turtle import pos
from urllib import response
from django.shortcuts import get_object_or_404, render
from matplotlib.style import context
from . models import Post
from django.urls import reverse #to create url dynamically by using names of urls

from django.http import HttpResponseRedirect
from .forms import CommentForm

from django.views.generic import ListView,DetailView
from django.views import View

# Create your views here.
#####used when getting data from views.py
# all_posts=[
#     {
#         "slug":"hike-in-mountains",
#         "image":"mountain.jpg",
#         "author":"jahnavi",
#         "date":date(2022,1,23),
#         "title": "Mountain Hiking",
#         "desc":"Hike in mountains Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias, consectetur saepe temporibus",
#         "content": """
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias, consectetur saepe temporibus 
#             tempora omnis dicta accusamus? Rem velit,ex asperiores fugit, adipisci delectus earum magnam illum laudantium 
#             sequi quis! Ratione?

#             Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias, consectetur saepe temporibus 
#             tempora omnis dicta accusamus? Rem velit,ex asperiores fugit, adipisci delectus earum magnam illum laudantium 
#             sequi quis! Ratione?

#             Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias, consectetur saepe temporibus 
#             tempora omnis dicta accusamus? Rem velit,ex asperiores fugit, adipisci delectus earum magnam illum laudantium 
#             sequi quis! Ratione?
#         """
#     },
#     {
#         "slug":"coding",
#         "image":"coding.jpg",
#         "author":"jahnavi",
#         "date":date(2022,1,14),
#         "title": "Programming is fun",
#         "desc":"Coding is Fun Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias, consectetur saepe temporibus",
#         "content": """
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias, consectetur saepe temporibus 
#             tempora omnis dicta accusamus? Rem velit,ex asperiores fugit, adipisci delectus earum magnam illum laudantium 
#             sequi quis! Ratione?

#             Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias, consectetur saepe temporibus 
#             tempora omnis dicta accusamus? Rem velit,ex asperiores fugit, adipisci delectus earum magnam illum laudantium 
#             sequi quis! Ratione?

#             Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias, consectetur saepe temporibus 
#             tempora omnis dicta accusamus? Rem velit,ex asperiores fugit, adipisci delectus earum magnam illum laudantium 
#             sequi quis! Ratione?
#         """
#     },
#     {
#         "slug":"into-woods",
#         "image":"woods.jpg",
#         "author":"jahnavi",
#         "date":date(2022,1,18),
#         "title": "Forest fun",
#         "desc":"Fun in woods Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias, consectetur saepe temporibus",
#         "content": """
#             Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias, consectetur saepe temporibus 
#             tempora omnis dicta accusamus? Rem velit,ex asperiores fugit, adipisci delectus earum magnam illum laudantium 
#             sequi quis! Ratione?

#             Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias, consectetur saepe temporibus 
#             tempora omnis dicta accusamus? Rem velit,ex asperiores fugit, adipisci delectus earum magnam illum laudantium 
#             sequi quis! Ratione?

#             Lorem ipsum dolor sit amet, consectetur adipisicing elit. Molestias, consectetur saepe temporibus 
#             tempora omnis dicta accusamus? Rem velit,ex asperiores fugit, adipisci delectus earum magnam illum laudantium 
#             sequi quis! Ratione?
#         """
#     }

# ]

######used when getting data from views.py
# def get_date(post):
#     return post['date']


# def starting_page(request):
#         #used when getting data from models.py
#     latest_posts=Post.objects.all().order_by("-date")[:3] 
#     #[-3:] -> django doesn't support -ve indexing
#     #usually in python, the above stmnts refers-> django goes to DB fetches all Posts orders by them date and returns first 3posts
#     # but django is smart as 
#     #  django will convert the entire stmnt into SQL query and only fetches 3 results from DB
#     return render(request,"blog/index.html",{
#         "posts":latest_posts
#     })
#         #used when getting data from views.py
#     # sorted_posts=sorted(all_posts,key=get_date)
#     # latest_posts=sorted_posts[-3:] #last 3 items
#     # return render(request,"blog/index.html",{
#     #     "posts":latest_posts
#     # })


class StartingPageView(ListView):
    template_name= "blog/index.html"
    model=Post
    ordering = ["-date"]
    context_object_name="posts"

    def get_queryset(self):
        queryset= super().get_queryset()
        data= queryset[:3]
        return data



# def posts(request):
#         #used when getting data from models.py
#     all_posts=Post.objects.all().order_by("-date")

#     return render(request,"blog/all_posts.html",{
#         "all_posts":all_posts
#     })
#         #used when getting data from views.py
#     # return render(request,"blog/all_posts.html",{
#     #     "all_posts":all_posts
#     # })

class AllPostsView(ListView):
    template_name= "blog/all_posts.html"
    model=Post
    ordering = ["-date"]
    context_object_name="all_posts"




# def post_detail(request,slug):
#         #used when getting data from models.py
#     identifies_post=get_object_or_404(Post,slug=slug)
#     return render(request,"blog/post_detail.html",{
#         "post":identifies_post,
#         "post_tags":identifies_post.tags.all()
#     })

#         #used when getting data from views.py
#     # identifies_post=next(post for post in all_posts if post['slug']==slug)
#     # return render(request,"blog/post_detail.html",{
#     #     "post":identifies_post
#     # })



#######only for get() request
# class SinglePostView(DetailView):
#     template_name="blog/post_detail.html"
#     model= Post

#     ##to get new,hot,featured tags on our posts
#     def get_context_data(self, **kwargs):
#         mydata= super().get_context_data(**kwargs)
#         mydata["post_tags"]=self.object.tags.all()
#         mydata["comment_form"] = CommentForm()
#         return mydata

########for get and post requests
class SinglePostView(View):

    def is_stored_post(self,request,post_id):
        stored_posts=request.session.get("stored_posts")
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later=False
        return is_saved_for_later

    # template_name="blog/post_detail.html"
    # model= Post
    
    # ##to get new,hot,featured tags on our posts
    # def get_context_data(self, **kwargs):
    #     mydata= super().get_context_data(**kwargs)
    #     mydata["post_tags"]=self.object.tags.all()
    #     mydata["comment_form"] = CommentForm()
    #     return mydata

    #above can be replaced with below to handle incoming get n post requests
    def get(self,request,slug):
        post=Post.objects.get(slug=slug)
        mydata={
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form" : CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request,post.id)
        }
        return render(request,"blog/post_detail.html",mydata)


    def post(self,request,slug):
        comment_form= CommentForm(request.POST)
        post=Post.objects.get(slug=slug) #fetching the post again for given slug

        if comment_form.is_valid():
            comment= comment_form.save(commit=False) #take user comments #save the post #commit=False->calling save will not hit the database but instead will create a new model instance
            comment.post= post # add etra data
            comment.save() #save edited data back to database
            return HttpResponseRedirect(reverse("post-detail-page",args=[slug])) #then redirect and render the template 
        
        # else: #i.e if form is invalid
        mydata={      #prepare our data 
            "post": post,
            "post_tags": post.tags.all(),
            "comment_form" : comment_form,
            "comments" : post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request,post.id)
        }
        return render(request,"blog/post_detail.html",mydata) #render the template again

class ReadLaterView(View):

    def get(self,request):
        stored_posts= request.session.get("stored_posts")

        mydata={} 

        if stored_posts is None or len(stored_posts)==0:
            mydata["posts"]=[]
            mydata["has_posts"] =False
        
        else: #fetch those posts from database
            posts=Post.objects.filter(id__in=stored_posts)  #only the posts whose ids are in stored posts list 
            #id__in-> it is a modifier to check if id is in stored posts lists or not
            mydata["posts"] =posts
            mydata["has_posts"] =True

        return render(request,"blog/stored_posts.html",mydata)



    def post(self,request):
        stored_posts= request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts=[]
        
        post_id= int(request.POST["post_id"])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
            # request.session["stored_posts"] = stored_posts
            ###whenever we add a post id to stored_posts, after updating stored posts we shld reach out to reqest session
            # n then add that stored posts key n set that to stored_posts
            #i.e if it didnt eist before it is stored now
            # if it already eisting it is updated with our updated stored posts
        else:
            stored_posts.remove(post_id)
        
        request.session["stored_posts"] = stored_posts
        
        return HttpResponseRedirect("/") ##to starting page
