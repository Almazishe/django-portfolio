from django.db import models
from django.contrib.auth import get_user_model

from utils.models import BaseDateModel, OnlyUniqueNameModel
from utils.views import get_path

User = get_user_model()



def get_img_path(instance, filename):
    return get_path(instance, filename, 'teams/logos/')


class TeamRole(OnlyUniqueNameModel, models.Model):
    """ Модель роли юзера в команде """
    pass

class Skill(OnlyUniqueNameModel, models.Model):
    """ Модель скилов юзеров """
    pass


class Team(BaseDateModel, models.Model):
    """ Команда """

    owner = models.ForeignKey(
        User, verbose_name='Создатель', on_delete=models.SET_NULL, related_name='my_teams', null=True)
    name = models.CharField('Команда', max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(blank=True, null=True, upload_to=get_img_path)

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'
        ordering = ('-created_at',)


class TeamMate(BaseDateModel, models.Model):
    """ Сокомандники и их роли """

    user = models.ForeignKey(User, verbose_name='Сокомандник', related_name='teams_in', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, verbose_name='Команда', related_name='teammates', on_delete=models.CASCADE)
    role = models.ForeignKey(TeamRole, verbose_name='Роль', related_name='users', on_delete=models.SET_NULL, null=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    skills = models.ManyToManyField(Skill, verbose_name='Скилы', related_name='users')

    class Meta:
        verbose_name='Сокомандник'
        verbose_name_plural='Сокомандники'
        ordering = ('role',)

    def __str__(self):
        return f'{self.user.full_name} | {self.team.name}'


