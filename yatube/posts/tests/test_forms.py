from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.urls import reverse

from posts.models import Post, Group, User

from posts.tests.constants import PROFILE_URL,\
    CREATE_URL, EDIT_URL


class PostCreateFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='Geek')

    def setUp(self):
        self.authorized_client = Client()
        self.guest_client = Client()
        self.authorized_client.force_login(self.user)
        self.post = Post.objects.create(
            author=self.user,
            text='Тестовый постик',
        )
        self.group = Group.objects.create(
            title='Group1',
            description='Test group',
            slug='test-group',
        )

    def test_post_create(self):
        """Тест формы создания поста"""
        posts_count = Post.objects.count()
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B'
        )
        uploaded = SimpleUploadedFile(
            name='small.gif',
            content=small_gif,
            content_type='image/gif'
        )
        form_data = {
            'text': 'Тестовая запись новая',
            'author': self.post.author,
            'group': self.group.pk,
            'image': uploaded
        }
        response = self.authorized_client.post(
            reverse(CREATE_URL),
            data=form_data,
            follow=True,
        )
        self.assertEqual(Post.objects.count(), posts_count + 1)
        self.assertRedirects(
            response,
            reverse(PROFILE_URL,
                    kwargs={'username': self.user.username}))

    def test_post_edit(self):
        """Тест формы редактирования поста"""
        group = Group.objects.create(
            title='Тестовая группа_2',
            slug='test_slug',
            description='Just a test group'
        )
        post = Post.objects.create(
            author=self.user,
            text='testovii post',
            group=group
        )

        form_data = {
            'text': 'Тестовая запись новая-1',
            'author': self.post.author,
            'group': self.group.pk,
        }

        url = reverse(EDIT_URL,
                      kwargs={"post_id": post.id})
        self.response = self.authorized_client.post(
            url,
            data=form_data,
            follow=True)
        post.refresh_from_db()
        self.assertEqual(post.text, form_data['text'])
        self.assertEqual(post.group.pk, form_data['group'])
