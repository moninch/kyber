from sqladmin import ModelView
from app.posts.models import Posts
from app.users.models import Users


class UsersAdmin(ModelView, model=Users):

    column_list = [
        Users.id,
        Users.login,
    ] + [Users.posts]
    column_details_exclude_list = [Users.hashed_password]
    can_delete = False
    name = 'Пользователь'
    name_plural = 'Пользователи'
    icon = 'fa-solid fa-user'

class PostsAdmin(ModelView, model=Posts):

    column_list = [c.name for c in Posts.__table__.c] + [Posts.author]

    name = 'Публикация'
    name_plural = 'Публикации'


