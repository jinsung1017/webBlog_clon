from django.views.generic import (
    CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
)
from django.urls import reverse

from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post  # 직접 입력해줘야함
    # template_name = 'posts/post_list.html'
    # 기본값이 있음, model 명을 기준으로 _list가 기본값
    # 우리의 model 명은 post / post_list.html 기본값이기에 삭제가능
    # context_object_name = 'posts' # 작성하지 않으면 post_list.html --> object_list로 전달함
    ordering = ['-dt_created']
    paginate_by = 6
    # page_kwarg = 'page' # 기본값이 page 임 post_list.html --> 이미 page로 사용중


class PostDetailView(DetailView):
    model = Post  # 입력해줘야함
    # template_name = 'posts/post_detail.html' # 기본값 모델명 + detail.html임
    # 이미 기본값 사용중 삭제 O
    # pk_url_kwarg = 'post_id'  # 기본값, pk임 urls.py 이동해서 post_id 를 pk로 수정
    # context_object_name = 'post'
    # DetailView에서 하나의 데이터를 context로 넘겨줄때는 object라는 키워드와 소문자로 적은 모델명 post가 기본적을 사용됨


class PostCreateView(CreateView):  # 상속
    model = Post
    form_class = PostForm  # form으로 전달됨, post_form 에 가면 form으로 사용중

    # template_name = 'posts/post_form.html'  # 기본값 post_form.html /post는 모델명 _form.html

    # Generic createView 는 context를 따로 작성해주지 않아요 form_class 에 해당하는 form의 키워드를 form으로 전달해줌

    def get_success_url(self):  # 글 작성 끝나고 이동할 page
        return reverse('post-detail', kwargs={'pk': self.object.id})
                                        # post_id를 pk로 변경했기 때문에 pk로 변경


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm  # form class / form 이라는 키워드로 전달됨
    # template_name = 'posts/post_form.html' # 기본값 모델명 + form.html / post_form.html
    # pk_url_kwarg = 'pk'  # 기본값은 pk

    def get_success_url(self):  # 유효성검사
        return reverse('post-detail', kwargs={'pk': self.object.id})


class PostDeleteView(DeleteView):
    model = Post
    # template_name = 'posts/post_confirm_delete.html' # 기본값 모델명 + confirm_delete.html / 기본값 사용중
    # pk_url_kwarg = 'post_id'  # pk 기본값
    # context_object_name = 'post' # DeleteView도 하나의 로직을 수행하기 때문에 모델데이터가 object와 post 라는 키로 템플릿에 전달
        # 모델 이름으로 만들어진 post로 전달 / delete.html 에 post로 사요중이기 때문에 삭제
    def get_success_url(self):
        return reverse('post-list')


class IndexRedirectView(RedirectView):
    pattern_name = 'post-list'
