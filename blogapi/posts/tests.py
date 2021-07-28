from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a User
        user = User.objects.create_user(username = 'testuser', password = 'q1234')
        user.save()

        # Create a blog Post
        post = Post.objects.create(author=user, title='title post', body='body content')
        post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser')
        self.assertEqual(title, 'title post')
        self.assertEqual(body, 'body content')
