#from datetime import date ###used when getting data from views.py
from django.shortcuts import get_object_or_404, render
from . models import Post

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


def starting_page(request):
        #used when getting data from models.py
    latest_posts=Post.objects.all().order_by("-date")[:3] 
    #[-3:] -> django doesn't support -ve indexing
    #usually in python, the above stmnts refers-> django goes to DB fetches all Posts orders by them date and returns first 3posts
    # but django is smart as 
    #  django will convert the entire stmnt into SQL query and only fetches 3 results from DB
    return render(request,"blog/index.html",{
        "posts":latest_posts
    })
    

        #used when getting data from views.py
    # sorted_posts=sorted(all_posts,key=get_date)
    # latest_posts=sorted_posts[-3:] #last 3 items
    # return render(request,"blog/index.html",{
    #     "posts":latest_posts
    # })

def posts(request):
        #used when getting data from models.py
    all_posts=Post.objects.all().order_by("-date")

    return render(request,"blog/all_posts.html",{
        "all_posts":all_posts
    })
        #used when getting data from views.py
    # return render(request,"blog/all_posts.html",{
    #     "all_posts":all_posts
    # })

def post_detail(request,slug):
        #used when getting data from models.py
    identifies_post=get_object_or_404(Post,slug=slug)
    return render(request,"blog/post_detail.html",{
        "post":identifies_post,
        "post_tags":identifies_post.tags.all()
    })

        #used when getting data from views.py
    # identifies_post=next(post for post in all_posts if post['slug']==slug)
    # return render(request,"blog/post_detail.html",{
    #     "post":identifies_post
    # })