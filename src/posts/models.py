from django.db import models
from django.contrib.auth import get_user_model

from slugify import slugify
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase


from utils.models import BaseDateModel
from utils.views import get_path

from teams.models import Team

#Модель юзера.
User = get_user_model()


def get_img_path(instance, filename):
    return get_path(instance, filename, 'posts/')



class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Post(BaseDateModel, models.Model):
    """ Пост либо юзера либо команды  """


    title = models.CharField('Заголовок', max_length=120)
    slug = models.SlugField(blank=True, null=True, unique=True)
    img = models.ImageField('Фото', blank=True, null=True, upload_to=get_img_path)
    description = models.TextField('Описание')

    owner = models.ForeignKey(
        User, related_name='posts', verbose_name='Владелец', on_delete=models.SET_NULL, null=True, blank=True)

    team = models.ForeignKey(
        Team, related_name='posts', verbose_name='Команда',
        on_delete=models.CASCADE, null=True, blank=True, default=None
    )

    tags = TaggableManager(
        through=UUIDTaggedItem,
        verbose_name='Хэштеги',
        blank=True,
    )

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    # TODO - get_absolute_url




