# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Answer(models.Model):
    sap = models.TextField(blank=True, null=True)
    qpid = models.TextField(blank=True, null=True)
    qno = models.IntegerField(blank=True, null=True)
    marks_aquired = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Course(models.Model):
    course_id = models.TextField(blank=True, null=True)
    course_name = models.TextField()
    course_duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Question(models.Model):
    qpid = models.TextField(blank=True, null=True)
    qno = models.IntegerField(blank=True, null=True)
    co = models.IntegerField()
    bl = models.IntegerField()
    so = models.IntegerField()
    max_marks = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'question'


class QuestionPaper(models.Model):
    qpid = models.TextField(blank=True, null=True)
    total_marks_paper = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question_paper'


class Student(models.Model):
    sap = models.TextField(blank=True, null=True)
    student_name = models.TextField()
    course_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class Subject(models.Model):
    subject_id = models.TextField(blank=True, null=True)
    subject_name = models.TextField()  # This field type is a guess.
    subject_credits = models.IntegerField()
    course_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subject'


class UploadsTask(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'uploads_task'



class UploadsCourse(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=256)
    course_duration = models.IntegerField()

    class Meta:
        managed = False
        db_table = "uploads_course"


class UploadsStudent(models.Model):
    sap = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    course_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "uploads_student"


class UploadsSubject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.TextField()
    subject_credits = models.IntegerField()
    course_id = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = "uploads_subject"



class UploadAnswer(models.Model):
    sap = models.TextField(blank=True, null=True)
    qpid = models.TextField(blank=True, null=True)
    qno = models.IntegerField()
    marks_aquired = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "upload_answer"

