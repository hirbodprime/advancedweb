from pyexpat.errors import messages
from django.http import  HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.decorators import api_view
from .forms import  apiform
from .serializers import blogserializer
from .models import blogmodel, contactModel
from rest_framework.response import Response
from django.views.generic import DetailView , ListView , CreateView , UpdateView , DeleteView , FormView , View
from django.contrib import messages
from rest_framework import status
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin 

def searchview(req):
    sea = req.POST.get('search' , None)
    if sea == None:
        print("NOne shode")
        # return redirect('downloadpagename')
    else:
    # blog = blogmodel.objects.filter(Q(title__icontains=sea) | Q(title__startswith=sea) | Q(title__contains=sea) | Q(title__endswith=sea))
        # blog = blogmodel.objects.filter(Q(title__contains=sea) | Q(body__contains=sea))
        blog = blogmodel.objects.filter(title__contains=sea)
        return render(req , 'search.html' , {'bitch':blog , "sea":sea})

# @api_view(['GET'])
# def BlogView(req):
#     try:
#         blog = blogmodel.objects.all()
#         serialize = blogserializer(blog , many=True)
#         print(serialize.data)
#     except blogmodel.DoesNotExist:
#         dataa = {'not found':'the blog you are looking for does not exist'}
#         return Response(data=dataa)
#     return Response(serialize.data)

@api_view(['GET'])
def FindBlogAPI(req , id):
    try:
        blog = blogmodel.objects.get(id=id)
        serialize = blogserializer(blog )
    except blogmodel.DoesNotExist:
        dataa = {'not found':'the blog you are looking for does not exist'}
        return Response(data=dataa)
    return Response(serialize.data)


@api_view(['DELETE'])		
def DeleteBlogAPI(req , id):
    try:
        blog = blogmodel.objects.get(id=id)
    except blogmodel.DoesNotExist:
        dataa = {'not found':'the blog you are looking for does not exist'}
        return Response(data=dataa)
    blogid = blog.id
    blog.delete()
    data = {'smth':f'{blog.title , blogid} delete shod'}
    return Response(data)
    
@api_view(['POST'])
def AddPostAPI(req):
    serializer = blogserializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
        created = {'sakhte shod':f'{serializer.data} sakhte shod'}
        return Response(created)
    else:
        return Response('fuck you')

@api_view(['PUT'])
def UpdateBlogAPI(req , id):
    blog = blogmodel.objects.get(id=id)
    serizalizer = blogserializer(blog , data=req.data)
    if serizalizer.is_valid():
        serizalizer.save()
        messages.success(req ,'updatetd succesfully')
        return Response('update shod')


def AddPost(req):
    query = blogmodel.objects.all().order_by('date')
    form = apiform(req.POST)
    if req.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(req , 'success')
            return HttpResponseRedirect('/drf')
    else:
        form = apiform()
    return render(req , 'Addblog.html' , {'blog':query , 'form':form})


from django.core.cache import cache
# from django_redis import get_redis_connection
class DetailViewPost(View):
    
    # model = blogmodel
    # template_name = "classfunctionpage.html"
    def get(self,request , *args , **kwargs):
        
        blog_id = kwargs["pk"]        
        if cache.get(blog_id):
            bloge_id = cache.get(blog_id)
            print("Im here2")
            # get_redis_connection("default").flushall()
            from django_redis import get_redis_connection

            r = get_redis_connection("default") 
            connection_pool = r.connection_pool
            print(f"Created connections so far: {connection_pool._created_connections}" )
        else:
            try:
                bloge_id = blogmodel.objects.get(pk=blog_id)
                cache.set(blog_id,bloge_id)
                print("Im here")
            except blogmodel.DoesNotExist:
                return HttpResponse("wtf")
        return render(request , "makeitfunctioni.html" , {"model":bloge_id})


class ListViewPostall(ListView):

    
    model = blogmodel
    # context_object_name = "bitch" # when changing get_context_date method we wont need this
    template_name = "classfunctionpage2.html"
    
    # def get_queryset(self , *args, **kwargs):
    #     qs = super(ListViewPostall , self).get_queryset(*args, **kwargs)
    #     qs = qs.order_by('-date')
    #     return qs

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        # context['bitch'] = blogmodel.objects.all().order_by('-date')
        # query_set = blogmodel.objects.filter(title__startswith='t').order_by('date')
        query_set = blogmodel.objects.all().order_by('date')
        context['bitch'] = query_set
        return context

class AddPostClassBased(LoginRequiredMixin,CreateView):
    model = blogmodel
    template_name = 'Addblog.html'
    fields = ['wrtier' , 'title' , 'body']
    login_url='/admin/login'
    def get_success_url(self):
        from django.urls import reverse
        return reverse('ListViewPostallNAME')


class ContactViewClassBased(CreateView):
    model=contactModel
    template_name='Addblog.html'
    fields=['name' , 'email' , 'body']
    def get_success_url(self):
        from django.urls import reverse
        return reverse('ListViewPostallNAME')

class contactview(ListView):
    model=contactModel
    template_name='contact.html'
    # context_object_name='contact'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        query= contactModel.objects.filter(status=True)
        context['contact']=query
        return context


class UpdateViewClassBased(UpdateView):
    model=blogmodel
    fields=['wrtier','title','body']
    template_name='Addblog.html'
    def get_success_url(self):
        from django.urls import reverse
        return reverse('ListViewPostallNAME')

class DeleteViewClassBased(DeleteView):
    model=blogmodel
    template_name='deleteask.html'
    success_url=reverse_lazy('ListViewPostallNAME')



# class FormViewClassBased(FormView):
#     template_name=''
#     form_class=Contactform
#     success_url=reverse_lazy('ListViewPostallNAME')
#     def form_valid(self, form):
#         name=form.cleaned_data['name']
#         message=form.cleaned_data['message']
#         form.send_email()
#         return super().form_valid(form)

