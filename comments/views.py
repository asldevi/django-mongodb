# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from models import Comment

comments_per_page = 4

def get_comments(page_no=1):
    page_no = int(page_no)
    p = Paginator(Comment.objects.all(), 4)  # 4 per page

    if page_no > p.num_pages:
        return [], p.page_range
    return p.page(page_no).object_list, p.page_range

def home(req):
    page_no = req.GET.get('page', 1)
    comments, page_range = get_comments(page_no)
    d = dict(comments=list(comments), page_no=int(page_no), page_range=page_range)
    return render_to_response('home.html', d, RequestContext(req))

def save(req):
    c = Comment(content=req.POST['content'], name=req.POST['name'])
    c.save()
    return HttpResponseRedirect(reverse('zesty.comments.views.home'))

