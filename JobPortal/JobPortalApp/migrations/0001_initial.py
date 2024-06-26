# Generated by Django 5.0.6 on 2024-06-20 14:35

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='IonicJobUserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('UserType', models.CharField(choices=[('Employer', 'Employer'), ('Seeker', 'Seeker')], max_length=50, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'IonicJob_User_Table',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperienceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation', models.CharField(max_length=100, null=True)),
                ('InstituteName', models.CharField(max_length=100, null=True)),
                ('Duration', models.CharField(max_length=100, null=True)),
                ('IonicUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workexperience', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'WorkExperience_Table',
            },
        ),
        migrations.CreateModel(
            name='SeekerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100, null=True)),
                ('Address', models.CharField(max_length=100, null=True)),
                ('Mobile', models.CharField(max_length=100, null=True)),
                ('DateOfBirth', models.DateField(null=True)),
                ('ProfileImg', models.ImageField(null=True, upload_to='media/seekerImage')),
                ('Resume', models.FileField(null=True, upload_to='media/seekerResume')),
                ('LastDegree', models.CharField(max_length=100, null=True)),
                ('LinkedIn', models.CharField(max_length=100, null=True)),
                ('GitHub', models.CharField(max_length=100, null=True)),
                ('IonicUser', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seekermodel', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'JobSeeker_Table',
            },
        ),
        migrations.CreateModel(
            name='QualificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DegreeName', models.CharField(max_length=100, null=True)),
                ('InstituteName', models.CharField(max_length=100, null=True)),
                ('Department', models.CharField(max_length=100, null=True)),
                ('PassingYear', models.CharField(max_length=100, null=True)),
                ('Grade', models.CharField(max_length=100, null=True)),
                ('IonicUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='qualification', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Qualification_Table',
            },
        ),
        migrations.CreateModel(
            name='JobInfoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobTitle', models.CharField(max_length=100, null=True)),
                ('JobSummary', models.TextField(null=True)),
                ('Qualification', models.CharField(max_length=100, null=True)),
                ('Salary', models.CharField(max_length=100, null=True)),
                ('Deadline', models.CharField(max_length=100, null=True)),
                ('Designation', models.CharField(max_length=100, null=True)),
                ('Experience', models.CharField(max_length=100, null=True)),
                ('TotalVacancy', models.CharField(max_length=100, null=True)),
                ('JobResponsibilities', models.TextField(null=True)),
                ('RequiredSkills', models.TextField(null=True)),
                ('AdditionalRequirement', models.TextField(null=True)),
                ('JobBenefits', models.TextField(null=True)),
                ('JobType', models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Contractual', 'Contractual'), ('Internship', 'Internship'), ('Freelance', 'Freelance')], max_length=100, null=True)),
                ('ExperienceLevel', models.CharField(choices=[('Begineer', 'Begineer'), ('Mid Level', 'Mid Level'), ('Experienced', 'Experienced'), ('TopLevel', 'TopLevel')], max_length=100, null=True)),
                ('JobCategories', models.CharField(choices=[('Manufacturer', 'Manufacturer'), ('Education', 'Education'), ('Training and Development', 'Training and Development'), ('Software Development', 'Software Development'), ('Textile/Garments', 'Textile/Garments'), ('IT Services', 'IT Services')], max_length=100, null=True)),
                ('Created_at', models.DateField(auto_now_add=True, null=True)),
                ('Updated_at', models.DateField(auto_now=True, null=True)),
                ('PostedBy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Job Info',
                'db_table': 'JobInfo_Table',
                'ordering': ['Created_at'],
            },
        ),
        migrations.CreateModel(
            name='JobApplicantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Skills', models.TextField(null=True)),
                ('Status', models.CharField(default='Pending', max_length=100, null=True)),
                ('Job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='JobPortalApp.jobinfomodel')),
                ('Applicant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicantuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Applicant_Table',
            },
        ),
        migrations.CreateModel(
            name='EmployerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CompanyName', models.CharField(max_length=100, null=True)),
                ('CompanyAddress', models.CharField(max_length=100, null=True)),
                ('CompanyDescription', models.TextField(null=True)),
                ('Mobile', models.CharField(max_length=100, null=True)),
                ('CompanyLogo', models.ImageField(null=True, upload_to='media/companylogo')),
                ('IonicUser', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employeermodel', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Employer_Table',
            },
        ),
    ]
