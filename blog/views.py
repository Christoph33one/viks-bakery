from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


# Post list view / takes post model / render index.html
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    post = Post.objects.filter(approved=True)
    template_name = "index.html"
    paginate_by = 3


# Post detail view
class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Your message has been sent"
                )
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()

            },
        )


# delete comment function
@login_required(login_url='/accounts/login/')
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if (
        comment.name == request.user.username
    ):
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS,
            "Your message has been deleted"
            )
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='/accounts/login/')
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        if (
            comment.name == request.user.username
        ):
            form = CommentForm(data=request.POST)
            if form.is_valid():
                comment.body = form.cleaned_data['body']
                comment.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "You have updated your comment!"
                )
                return redirect('index')
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    "Whoops something is wrong!"
                )
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
                # return render(request, '404.html', status=404)
                # not rednering a 404????
                # return HttpResponseRedirect(reverse, "errors/404.html", status=404)

    return render(
                request,
                "edit_comment.html",
                {
                    'comment': comment,
                    'comment_form': CommentForm(instance=comment)
                }
            )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def error_404(request, exception):
    """ 404 error page """
    return render(request, '404.html', status=404)


# def error_500(request):
#     """ 500 error page """
#     return render(request, '500.html', status=500)
