from django.contrib import admin


from .models import TeamRole, TeamMate, Team, Skill


admin.site.register(Team)
admin.site.register(TeamMate)
admin.site.register(TeamRole)
admin.site.register(Skill)
