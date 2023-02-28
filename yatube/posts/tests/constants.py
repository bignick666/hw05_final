PROFILE_URL = 'posts:profile'
EDIT_URL = 'posts:post_edit'
CREATE_URL = 'posts:create'
INDEX_URL = 'posts:index'
GROUPS_URL = 'posts:groups'
DETAIL_URL = 'posts:post_detail'
FOLLOW_URL_INDEX = 'posts:follow_index'
ADD_COMMENT_URL = 'posts:add_comment'
UNFOLLOW_URL = 'posts:profile_unfollow'

PROFILE_TEMPLATE = 'posts/profile.html'
CREATE_TEMPLATE = 'posts/create.html'
INDEX_TEMPLATE = 'posts/index.html'
GROUPS_TEMPLATE = 'posts/group_list.html'
DETAIL_TEMPLATE = 'posts/post_detail.html'
TEMPLATE_404 = 'core/404.html'
TEMPLATE_403 = 'core/403csrf.html'

SMALL_GIF = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B'
        )

UNEXPECTED_PAGE = '/unexpected_page/'
