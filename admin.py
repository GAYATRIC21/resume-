from django.contrib import admin
from .models import Skill, Project, ProjectBullet, Experience, ExperienceBullet, Education, Contact


class ProjectBulletInline(admin.TabularInline):
    model = ProjectBullet
    extra = 1


class ExperienceBulletInline(admin.TabularInline):
    model = ExperienceBullet
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectBulletInline]
    list_display = ['title', 'tech_stack', 'featured', 'order']
    list_editable = ['featured', 'order']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    inlines = [ExperienceBulletInline]
    list_display = ['role', 'company', 'start_date', 'end_date']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_editable = ['order']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'gpa']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'submitted_at']
    readonly_fields = ['submitted_at']
