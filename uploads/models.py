# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from import_export import resources
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin


class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    sap = models.ForeignKey(
        "Student", models.DO_NOTHING, db_column="SAP"
    )  # Field name made lowercase.
    qp = models.ForeignKey("QuestionPaper", models.DO_NOTHING)
    question_no = models.IntegerField()
    answer = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "answer"
        unique_together = (("qp", "sap","question_no"),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class Course(models.Model):
    id = models.IntegerField(blank=True, null=True)
    course_number = models.CharField(primary_key=True, max_length=50)
    course_name = models.CharField(max_length=50, blank=True, null=True)
    degree = models.CharField(max_length=50, blank=True, null=True)
    course_duration = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "course"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class Exam(models.Model):
    id = models.IntegerField(blank=True, null=True)
    qp = models.OneToOneField("QuestionPaper", models.DO_NOTHING, primary_key=True)
    subject_number = models.ForeignKey(
        "Subjects", models.DO_NOTHING, db_column="subject_number"
    )

    class Meta:
        managed = True
        db_table = "exam"
        unique_together = (("qp", "subject_number"),)


class Faculty(models.Model):
    id = models.IntegerField(blank=True, null=True)
    facid = models.IntegerField(primary_key=True)
    facname = models.CharField(max_length=50, blank=True, null=True)
    qlfi = models.CharField(max_length=50, blank=True, null=True)
    subject_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = "faculty"


class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    qp = models.ForeignKey("QuestionPaper", models.DO_NOTHING)
    question_no = models.IntegerField()
    co = models.IntegerField(
        db_column="CO", blank=True, null=True
    )  # Field name made lowercase.
    so = models.IntegerField(
        db_column="SO", blank=True, null=True
    )  # Field name made lowercase.
    bl = models.IntegerField(
        db_column="BL", blank=True, null=True
    )  # Field name made lowercase.
    marks = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "question"
        unique_together = (("qp", "question_no"),)


class QuestionPaper(models.Model):
    id = models.IntegerField(blank=True, null=True)
    qp_id = models.CharField(primary_key=True, max_length=50)
    total_marks = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "question_paper"


class Semester(models.Model):
    id = models.IntegerField(blank=True, null=True)
    course_number = models.ForeignKey(
        Course, models.DO_NOTHING, db_column="course_number", blank=True, null=True
    )
    subject_number = models.ForeignKey(
        "Subjects", models.DO_NOTHING, db_column="subject_number", blank=True, null=True
    )
    semester_no = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = "semester"


class Student(models.Model):
    id = models.IntegerField(blank=True, null=True)
    sap = models.IntegerField(
        db_column="SAP", primary_key=True
    )  # Field name made lowercase.
    student_name = models.CharField(max_length=50, blank=True, null=True)
    course_number = models.ForeignKey(
        Course, models.DO_NOTHING, db_column="course_number", blank=True, null=True
    )

    class Meta:
        managed = True
        db_table = "student"


class Subjects(models.Model):
    subject_number = models.CharField(primary_key=True, max_length=50)
    subject_name = models.CharField(max_length=50, blank=True, null=True)
    subject_duration = models.IntegerField(blank=True, null=True)
    credits = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = "subjects"


class Task(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        managed = True


# class UploadsTask(models.Model):
#     name = models.CharField(max_length=256)
#     description = models.CharField(max_length=256)

#     class Meta:
#         managed = True
#         db_table = "uploads_task"


# from import_export import resources

# class StudentResources(resources.ModelResource):
#     class Meta:
#         model = Student
#         skip_unchanged = True
#         report_skipped = True
#         import_id_fields = ['sap']
#         # fields = ()
# exclude = ('id',)

