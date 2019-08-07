# Generated by Django 2.2.4 on 2019-08-05 06:21

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('phone_status', models.CharField(choices=[('phone_status_unverified', 'g_phone_status_unverified'), ('phone_status_verified', 'g_phone_status_verified')], max_length=64)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('zip', models.CharField(blank=True, max_length=10, null=True)),
                ('image', models.CharField(default='', max_length=255)),
                ('login_status', models.CharField(choices=[('login_type_status_email', 'g_login_type_status_email'), ('login_type_status_facebook', 'g_login_type_status_facebook'), ('login_type_status_google', 'g_login_type_status_google')], max_length=64)),
                ('socialId', models.CharField(default='', max_length=255)),
                ('rating', models.DecimalField(decimal_places=3, default=0, max_digits=12)),
                ('created_time', models.DateTimeField()),
                ('role', models.IntegerField(default=-1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'model_auth_user',
                'verbose_name_plural': 'model_auth_users',
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('package_status', models.CharField(choices=[('package_status_pending', 'g_package_status_pending'), ('package_status_assigned', 'g_package_status_assigned'), ('package_status_cancelled', 'g_package_status_cancelled')], max_length=64)),
                ('departure_country', models.CharField(blank=True, max_length=100)),
                ('departure_city', models.CharField(blank=True, max_length=100)),
                ('departure_address', models.CharField(blank=True, max_length=255)),
                ('arrival_country', models.CharField(blank=True, max_length=100)),
                ('arrival_city', models.CharField(blank=True, max_length=100)),
                ('arrival_address', models.CharField(blank=True, max_length=255)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('package_name', models.CharField(blank=True, max_length=150)),
                ('width', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=50)),
                ('length', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('description_info', models.TextField(default='')),
                ('receiver_name', models.CharField(blank=True, max_length=150)),
                ('receiver_email', models.EmailField(max_length=255, unique=True)),
                ('receiver_phone', models.CharField(blank=True, max_length=15)),
                ('receiver_address', models.CharField(blank=True, max_length=255)),
                ('urgent_announcement', models.BooleanField(default=False)),
                ('no_of_days', models.IntegerField(default=0)),
                ('inform_to_receiver', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'model_package',
                'verbose_name_plural': 'model_packages',
                'db_table': 'package',
            },
        ),
        migrations.CreateModel(
            name='PackageType',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'verbose_name': 'model_package_type',
                'verbose_name_plural': 'model_package_types',
                'db_table': 'user_package_type',
            },
        ),
        migrations.CreateModel(
            name='UserTravelerInfo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('no_of_times_travel', models.IntegerField(default=0)),
                ('when_to_travel', models.CharField(blank=True, max_length=10)),
                ('package_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core1.PackageType')),
            ],
            options={
                'verbose_name': 'model_user_traveler_info',
                'verbose_name_plural': 'model_user_traveler_infos',
                'db_table': 'user_traveler_info',
            },
        ),
        migrations.CreateModel(
            name='UserInterestedCountry',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'model_user_interested_country',
                'verbose_name_plural': 'model_user_interested_countries',
                'db_table': 'user_interested_country',
            },
        ),
        migrations.CreateModel(
            name='UserExpeditorInfo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('no_of_times_travel', models.IntegerField(default=0)),
                ('when_to_send', models.CharField(blank=True, max_length=10)),
                ('package_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core1.PackageType')),
            ],
            options={
                'verbose_name': 'model_user_expeditor_info',
                'verbose_name_plural': 'model_user_expeditor_infos',
                'db_table': 'user_expeditor_info',
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('departure_country', models.CharField(blank=True, max_length=100)),
                ('departure_city', models.CharField(blank=True, max_length=100)),
                ('departure_address', models.CharField(blank=True, max_length=255)),
                ('arrival_country', models.CharField(blank=True, max_length=100)),
                ('arrival_city', models.CharField(blank=True, max_length=100)),
                ('arrival_address', models.CharField(blank=True, max_length=255)),
                ('departure_time', models.DateTimeField(blank=True, null=True)),
                ('return_time', models.DateTimeField(blank=True, null=True)),
                ('package_name', models.CharField(blank=True, max_length=150)),
                ('width', models.CharField(max_length=50)),
                ('height', models.CharField(max_length=50)),
                ('length', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('flight_info', models.TextField(default='')),
                ('is_your_travel_urgent', models.BooleanField(default=True)),
                ('created_time', models.DateTimeField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'model_trip',
                'verbose_name_plural': 'model_trips',
                'db_table': 'trip',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('transaction_id', models.CharField(blank=True, max_length=150)),
                ('created_time', models.DateTimeField()),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core1.Package')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'model_transaction',
                'verbose_name_plural': 'model_transactions',
                'db_table': 'transaction',
            },
        ),
        migrations.CreateModel(
            name='ReportUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('report_time', models.DateTimeField()),
                ('reason', models.CharField(blank=True, max_length=100)),
                ('other_info', models.TextField(default='')),
                ('reported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reported_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reported_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'model_report_user',
                'verbose_name_plural': 'model_report_users',
                'db_table': 'report_user',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=2, null=True)),
                ('comment', models.TextField(default='')),
                ('created_time', models.DateTimeField()),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core1.Package')),
                ('rating_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rating_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'model_rating',
                'verbose_name_plural': 'model_ratings',
                'db_table': 'rating',
            },
        ),
        migrations.CreateModel(
            name='PackageInvitation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('package_invitation_status', models.CharField(choices=[('package_invitation_status_pending', 'g_package_invitation_status_pending'), ('package_invitation_status_accepted', 'g_package_invitation_status_accepted'), ('package_invitation_status_cancelled', 'g_package_invitation_status_cancelled'), ('package_invitation_status_cancelled_by_own', 'g_package_invitation_status_cancelled_by_own')], max_length=64)),
                ('created_time', models.DateTimeField()),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core1.Package')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'model_package_invitation',
                'verbose_name_plural': 'model_package_invitations',
                'db_table': 'package_invitation',
            },
        ),
        migrations.AddField(
            model_name='package',
            name='package_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core1.PackageType'),
        ),
        migrations.AddField(
            model_name='package',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('notification_time', models.DateTimeField()),
                ('message', models.TextField(default='')),
                ('is_read', models.BooleanField(default=False)),
                ('tag', models.CharField(blank=True, max_length=150)),
                ('table_id', models.CharField(blank=True, max_length=150)),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notification_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'model_notification',
                'verbose_name_plural': 'model_notifications',
                'db_table': 'notification',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('message_time', models.DateTimeField()),
                ('message', models.TextField(default='')),
                ('is_read', models.BooleanField(default=False)),
                ('sender_status', models.BooleanField(default=True)),
                ('receiver_status', models.BooleanField(default=True)),
                ('receiver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'model_message',
                'verbose_name_plural': 'model_messages',
                'db_table': 'message',
            },
        ),
        migrations.CreateModel(
            name='InvitedUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('invitation_time', models.DateTimeField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'model_invited_user',
                'verbose_name_plural': 'model_invited_users',
                'db_table': 'invited_user',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(blank=True, max_length=150)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('message', models.TextField(default='')),
                ('created_time', models.DateTimeField()),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'model_contact_us',
                'verbose_name_plural': 'model_contact_us',
                'db_table': 'contact_us',
            },
        ),
        migrations.CreateModel(
            name='BlockUser',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('block_time', models.DateTimeField()),
                ('blocked_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blocked_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blocked_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'model_block_user',
                'verbose_name_plural': 'model_block_users',
                'db_table': 'block_user',
            },
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('from_time', models.DateTimeField(blank=True, null=True)),
                ('to_time', models.DateTimeField(blank=True, null=True)),
                ('bid_status', models.CharField(choices=[('bid_status_pending', 'g_bid_status_pending'), ('bid_status_accepted', 'g_bid_status_accepted'), ('bid_status_cancelled', 'g_bid_status_cancelled'), ('bid_status_cancelled_by_own', 'g_bid_status_cancelled_by_own')], max_length=64)),
                ('created_time', models.DateTimeField()),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core1.Package')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'model_bid',
                'verbose_name_plural': 'model_bids',
                'db_table': 'bid',
            },
        ),
    ]
