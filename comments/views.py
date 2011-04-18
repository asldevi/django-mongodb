# Create your views here.
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from models import Comment

def get_comments(page_no=1):
    """ get comments to show a page with page number 'page_n' """
    page_no = int(page_no)
    p = Paginator(Comment.objects.all(), 4)  # 4 comments per page

    if page_no > p.num_pages:
        return [], p.page_range
    return p.page(page_no).object_list, p.page_range

def home(req):
    """handle requests to "/" and "/?page=page_no"  """
    page_no = req.GET.get('page', 1)
    comments, page_range = get_comments(page_no)
    d = dict(comments=list(comments), page_no=int(page_no), page_range=page_range)
    return render_to_response('home.html', d, RequestContext(req))

def save(req):
    """save the comment and redirect to home """
    c = Comment(content=req.POST['content'], name=req.POST['name'])
    c.save()
    return HttpResponseRedirect(reverse('django-mongodb.comments.views.home'))

