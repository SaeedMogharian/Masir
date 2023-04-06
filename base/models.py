from django.contrib.auth.models import User
from django.db import models
from colorfield.fields import ColorField
from django_jalali.db import models as jmodels
from django.db.models import Count

CLUB_LEVELS = [
    {'day': 'اول', 'page': 'نیم صفحه از قرآن کریم: سوره بقره، آیات 183 تا 185'},
    {'day': 'دوم', 'page': 'یک صفحه از قرآن کریم: سوره آل عمران، آیات 133 تا 140'},
    {'day': 'سوم', 'page': 'یک و نیم صفحه از قرآن کریم: سوره فجر، از ابتدا تا انتها'},
    {'day': 'چهارم', 'page': 'دو صفحه از قرآن کریم: سوره تغابن، ار ابتدا تا انتها'},
    {'day': 'پنجم', 'page': 'دو و نیم صفحه از قرآن کریم: سوره بقره، آیات 262 تا 274'},
    {'day': 'ششم', 'page': 'سه صفحه از قرآن کریم: سوره الرحمان، از ابتدا تا انتها'},
    {'day': 'هفتم', 'page': 'سه و نیم صفحه از قرآن کریم: سوره هود، آیات 25 تا 53'},
    {'day': 'هشتم', 'page': 'چهار صفحه از قرآن کریم: سوره حدید، از ابتدا تا انتها'},
    {'day': 'نهم', 'page': 'چهار و نیم صفحه از قرآن کریم: سوره فتح، از ابتدا تا انتها'},
    {'day': 'دهم', 'page': 'پنج صفحه از قرآن کریم: سوره انعام، آیات 1 تا 44'},
    {'day': 'یازدهم', 'page': 'پنج و نیم صفحه از قرآن کریم: سوره‌های کهف، آیات 1 تا 45'},
    {'day': 'دوازدهم', 'page': 'شش صفحه از قرآن کریم: سوره یس، ار ابتدا تا انتها'},
    {'day': 'سیزدهم', 'page': 'شش و نیم صفحه از قرآن کریم: سوره یونس، آیات 54 تا 109'},
    {'day': 'چهاردهم', 'page': 'هفت صفحه از قرآن کریم: سوره ابراهیم، از ابتدا تا انتها'},
    {'day': 'پانزدهم', 'page': 'هفت صفحه از قرآن کریم: سوره مائده، آیات 10 تا 45'},
]

ACTIVITY_TEMPLATE_TYPE_CHOICES = (
    ('1', 'طلایی'),
    ('2', 'سنگی'),
    ('3', 'چوبی')
)

ACTIVITY_STATE_CHOICES = (
    ('1', 'ارسال شده'),
    ('2', 'در حال داوری'),
    ('3', 'داوری شده و اعلام نشده'),
    ('4', 'داوری شده'),
    ('5', 'رد شده و اعلام نشده'),
    ('6', 'رد شده'),
)

ACTIVITIES = {
    'قیام و حرکت': '010',
    'مشورت و عظم': '011',
    'حرکت جمعی': '012',
    'امر به معروف و نهی از منکر': '013',
    'شناخت و بینش': '020',
    'فرقان': '021',
    'دشمن شناسی': '022',
    'هدف و مسیر': '023',
    'صبر و استفامت': '030',
    'امید به یاری خداوند': '031',
    'آزمایش': '032',
    'استعانت': '033',
    'جهاد': '040',
    'روشنگری': '041',
    'اتحاد و تعاون': '042',
    'انقطاع': '043',
}


class Accessibility(models.Model):
    title = models.CharField(default='عنوان پیش‌فرض', max_length=100, verbose_name='عنوان')

    judge_page = models.BooleanField(default=False, verbose_name='دسترسی به داوری فعالیت‌ها')
    judge_page_edit = models.BooleanField(default=False, verbose_name='ویرایش داوری فعالیت‌ها')

    statistics_page = models.BooleanField(default=False, verbose_name='دسترسی به آمار')

    club_page = models.BooleanField(default=False, verbose_name='دسترسی به فایل‌های باشگاه')
    club_page_edit = models.BooleanField(default=False, verbose_name='ویرایش فایل‌های باشگاه')

    announcements_page = models.BooleanField(default=False, verbose_name='دسترسی به اعلانات')
    announcements_page_edit = models.BooleanField(default=False, verbose_name='ویرایش اعلانات')

    reports_page = models.BooleanField(default=False, verbose_name='دسترسی به گزارش‌ها')
    reports_page_edit = models.BooleanField(default=False, verbose_name='ویرایش گزارش‌ها')

    faq_page = models.BooleanField(default=False, verbose_name='دسترسی به پرسش‌های پرتکرار')
    faq_page_edit = models.BooleanField(default=False, verbose_name='ویرایش پرسش‌های پرتکرار')

    contact_admin_page = models.BooleanField(default=False, verbose_name='دسترسی به پیام‌های کاربران')
    contact_admin_page_edit = models.BooleanField(default=False, verbose_name='ویرایش پیام‌های کاربران')

    def __str__(self):
        return (self.title)

    class Meta:
        verbose_name = 'دسترسی'
        verbose_name_plural = 'دسترسی‌های کاربران'


class City(models.Model):
    state = models.CharField(default='نامشخص', max_length=20, verbose_name='استان')
    name = models.CharField(default='نامشخص', max_length=50, verbose_name='نام شهر')

    def __str__(self):
        return (self.state + ' | ' + self.name)

    class Meta:
        verbose_name = 'شهر'
        verbose_name_plural = 'شهرها'


class School(models.Model):
    name = models.CharField(default='نامشخص', max_length=50, verbose_name='نام مدرسه')

    def __str__(self):
        return (self.name)

    class Meta:
        verbose_name = 'مدرسه'
        verbose_name_plural = 'مدارس'


class Vote(models.Model):
    phone = models.CharField(default='9xxxxxxxxx', max_length=10, verbose_name='شماره تلفن')
    vote_image_1 = models.BooleanField(default=False, verbose_name='رای به تصویر اول')
    vote_image_2 = models.BooleanField(default=False, verbose_name='رای به تصویر دوم')
    vote_image_3 = models.BooleanField(default=False, verbose_name='رای به تصویر سوم')
    vote_image_4 = models.BooleanField(default=False, verbose_name='رای به تصویر چهارم')
    vote_image_5 = models.BooleanField(default=False, verbose_name='رای به تصویر پنجم')
    vote_music_1 = models.BooleanField(default=False, verbose_name='رای به صوت اول')
    vote_music_2 = models.BooleanField(default=False, verbose_name='رای به صوت دوم')
    vote_music_3 = models.BooleanField(default=False, verbose_name='رای به صوت سوم')
    vote_music_4 = models.BooleanField(default=False, verbose_name='رای به صوت چهارم')
    vote_music_5 = models.BooleanField(default=False, verbose_name='رای به صوت پنجم')
    vote_video_1 = models.BooleanField(default=False, verbose_name='رای به فیلم اول')
    vote_video_2 = models.BooleanField(default=False, verbose_name='رای به فیلم دوم')
    vote_video_3 = models.BooleanField(default=False, verbose_name='رای به فیلم سوم')
    vote_video_4 = models.BooleanField(default=False, verbose_name='رای به فیلم چهارم')
    vote_video_5 = models.BooleanField(default=False, verbose_name='رای به فیلم پنجم')
    code = models.IntegerField(default=0, verbose_name='کد تایید')
    is_valid = models.BooleanField(default=False, verbose_name='معتبر')
    masood_valid = models.BooleanField(default=False, verbose_name='نامعتبر معتبر شده بخاطر مسعود!')

    def get_group(self):
        user = User.objects.filter(username=self.phone).first()
        if user:
            if user.user_detail.groups.all().first():
                return (user.user_detail.groups.all().first())
            return ('بدون گروه')
        return (None)

    def get_user(self):
        return (User_Detail.objects.filter(user__username=self.phone).first())

    def __str__(self):
        if self.is_valid:
            return ('>> ' + self.phone)
        return (self.phone)

    class Meta:
        verbose_name = 'رای'
        verbose_name_plural = 'آرای کاربران'


class User_Detail(models.Model):
    user = models.OneToOneField(User, related_name='user_detail', on_delete=models.CASCADE, verbose_name='کاربر')
    accessibility = models.ForeignKey(Accessibility, null=True, related_name='users', on_delete=models.SET_NULL,
                                      verbose_name='دسترسی')
    nationalcode = models.CharField(default='xxxxxxxxxx', max_length=10, verbose_name='کد ملی')
    level = models.IntegerField(default=0, verbose_name='پایه')
    city = models.ForeignKey(City, null=True, related_name='users', on_delete=models.SET_NULL, verbose_name='شهر')
    school = models.ForeignKey(School, null=True, related_name='users', on_delete=models.SET_NULL, verbose_name='مدرسه')
    code = models.CharField(default='xxxxx', max_length=5, verbose_name='کد کاربر')

    club_level = models.IntegerField(default=0, verbose_name='قرائت‌های انجام شده')

    def get_club_level(self):
        if self.club_level < 0 or self.club_files.filter(show_public=False).first():
            return (None)
        return ('روز ' + CLUB_LEVELS[self.club_level]['day'] + ' حضور ' + str(self) + ' | قرائت ' +
                CLUB_LEVELS[self.club_level]['page'])

    def get_group(self):
        return (self.groups.all().first())

    def __str__(self):
        return (self.user.first_name + ' ' + self.user.last_name)

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'اطلاعات کاربران'


class Message(models.Model):
    name = models.CharField(default='نام پیش‌فرض', max_length=100, verbose_name='نام')
    phone = models.CharField(default='9xxxxxxxxx', max_length=10, verbose_name='شماره تلفن')
    message = models.TextField(default='متن پیام پیش‌فرض', max_length=5000, verbose_name='متن پیام')
    answer = models.TextField(null=True, blank=True, max_length=5000, verbose_name='متن پاسخ')
    support = models.ForeignKey(User_Detail, null=True, blank=True, related_name='support', on_delete=models.SET_NULL,
                                verbose_name='پشتیبان')
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ')

    def get_group(self):
        user = User.objects.filter(username=self.phone).first()
        if user:
            if user.user_detail.groups.all().first():
                return (user.user_detail.groups.all().first())
            return ('بدون گروه')
        return (None)

    def get_message(self):
        return (str(self.message).replace('\n', '<br>'))

    def get_answer(self):
        return (str(self.answer).replace('\n', '<br>'))

    def __str__(self):
        return (self.phone)

    class Meta:
        verbose_name = 'پیام‌'
        verbose_name_plural = 'پیام‌های کاربران'


class Announcement(models.Model):
    title = models.CharField(default='عنوان پیش‌فرض', max_length=100, verbose_name='عنوان اعلان')
    text = models.CharField(default='متن پیش‌فرض', max_length=1000, verbose_name='متن اعلان')
    voice = models.FileField(null=True, blank=True, upload_to='base/static/announcement/', verbose_name='فایل')
    date = jmodels.jDateField(blank=True, null=True, verbose_name='تاریخ')
    is_public = models.BooleanField(default=False, verbose_name='نمایش برای عموم')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def get_voice(self):
        return (str(self.voice)[4:])

    def __str__(self):
        if (self.is_active):
            return ('>> ' + str(self.date) + ' | ' + str(self.title))
        return (str(self.date) + '. ' + str(self.title))

    class Meta:
        verbose_name = 'اعلان'
        verbose_name_plural = 'اعلانات'


class Manzel(models.Model):
    number = models.CharField(default='منزل چندم', max_length=100, verbose_name='شماره منزل')
    title = models.CharField(default='عنوان پیش‌فرض', max_length=100, verbose_name='عنوان منزل')
    co_title = models.CharField(default='عنوان پیش‌فرض', max_length=100, verbose_name='عنوان معرفتی')
    story = models.FileField(null=True, blank=True, upload_to='base/static/manzel/', verbose_name='فایل داستان')
    back_image = models.FileField(null=True, blank=True, upload_to='base/static/manzel/',
                                  verbose_name='تصویر پس زمینه منزل')
    color = ColorField(default='FFFFFF', verbose_name='رنگ پس‌زمینه نَوبار')
    top = models.FloatField(default=0, verbose_name='درصد فاصله از بالای نقشه')
    right = models.FloatField(default=0, verbose_name='درصد فاصله از سمت راست نقشه')
    max_export_food = models.IntegerField(default=0, verbose_name='حداکثر آذوقه قابل حمل در ورودی منزل')
    food_for_next_manzel = models.IntegerField(default=0, verbose_name='آذوقه مورد نیاز برای رسیدن به منزل بعدی')
    power_for_next_manzel = models.IntegerField(default=0, verbose_name='توان مورد نیاز برای رسیدن به منزل بعدی')

    def is_first(self):
        if self.id == 1:
            return True
        return False

    def get_story(self):
        return (str(self.story)[4:])

    def get_image(self):
        return (str(self.back_image)[4:])

    def __str__(self):
        return (self.number + ' | ' + self.title)

    class Meta:
        verbose_name = 'منزل'
        verbose_name_plural = 'منزل‌ها'


class Achivement(models.Model):
    manzel = models.ForeignKey(Manzel, related_name='achivements', on_delete=models.SET_NULL, null=True, blank=True,
                               verbose_name='منزل')
    title = models.CharField(default='عنوان پیش‌فرض', max_length=100, verbose_name='عنوان دستاورد')
    text = models.CharField(default='عنوان پیش‌فرض', max_length=500, verbose_name='توضیح دستاورد')
    code = models.CharField(default='XXX_X', max_length=100, verbose_name='کد دستاورد')
    image = models.FileField(upload_to='base/static/images/achivement/', verbose_name='تصویر')

    def get_manzel(self):
        if self.manzel:
            return (self.manzel.title + ' | ' + self.manzel.co_title)
        return (None)

    def get_image(self):
        return (str(self.image)[4:])

    def __str__(self):
        return (str(self.title))

    class Meta:
        verbose_name = 'دستاورد'
        verbose_name_plural = 'دستاوردها'


class Club_File(models.Model):
    user = models.ForeignKey(User_Detail, related_name='club_files', on_delete=models.CASCADE, verbose_name='کاربر')
    link = models.CharField(default='#', max_length=1000, verbose_name='لینک فایل')
    title = models.CharField(default='عنوان پیش‌فرض', max_length=100, verbose_name='عنوان فایل')
    level = models.IntegerField(default=0, verbose_name='مرحله')
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ')
    verified = models.BooleanField(default=False, verbose_name='تایید شده')
    show_public = models.BooleanField(default=False, verbose_name='نمایش عمومی')

    def __str__(self):
        return (str(self.level) + '. ' + str(self.user) + ' | ' + self.title)

    class Meta:
        verbose_name = 'فایل‌'
        verbose_name_plural = 'فایل‌های باشگاه'


class Question(models.Model):
    Q = models.TextField(default='پرسش پیش‌فرض', max_length=5000, verbose_name='متن پرسش')
    O1 = models.TextField(default='پاسخ پیش‌فرض', max_length=5000, verbose_name='گزینه 1')
    O2 = models.TextField(default='پاسخ پیش‌فرض', max_length=5000, verbose_name='گزینه 2')
    O3 = models.TextField(default='پاسخ پیش‌فرض', max_length=5000, verbose_name='گزینه 3')
    O4 = models.TextField(default='پاسخ پیش‌فرض', max_length=5000, verbose_name='گزینه 4')
    A = models.IntegerField(default=1, verbose_name='گزینه صحیح')

    def __str__(self):
        return (str(self.Q))

    class Meta:
        verbose_name = 'پرسش'
        verbose_name_plural = 'پرسش‌های آزمون‌های دانشگاه'


class FAQ(models.Model):
    question = models.TextField(default='پرسش پیش‌فرض', max_length=500, verbose_name='متن پرسش')
    answer = models.TextField(default='پاسخ پیش‌فرض', max_length=500, verbose_name='متن پاسخ')
    is_active = models.BooleanField(default=True, verbose_name='فعال')

    def __str__(self):
        if (self.is_active):
            return ('>> ' + str(self.question))
        return (str(self.question))

    class Meta:
        verbose_name = 'پرسش'
        verbose_name_plural = 'پرسش‌های پرتکرار'


class Exam(models.Model):
    title = models.CharField(default='عنوان پیش‌فرض', max_length=100, verbose_name='نام آزمون')
    questions = models.ManyToManyField(Question, related_name='exams', verbose_name='پرسش‌های آزمون')
    active = models.BooleanField(default=False, verbose_name='فعال')

    def get_key(self):
        k = ''
        for x in self.questions.all():
            k = k + str(x.A)
        return (k)

    def __str__(self):
        if self.active:
            return ('>> ' + str(self.title))
        return (str(self.title))

    class Meta:
        verbose_name = 'آزمون'
        verbose_name_plural = 'آزمون‌های دانشگاه'


class Activity_Template(models.Model):
    title = models.CharField(default='عنوان پیش‌فرض', max_length=100, verbose_name='عنوان قالب')
    type = models.CharField(default='1', max_length=1, choices=ACTIVITY_TEMPLATE_TYPE_CHOICES, verbose_name='نوع قالب')
    max_power = models.IntegerField(default=0, verbose_name='حداکثر توان قابل کسب')
    max_food = models.IntegerField(default=0, verbose_name='حداکثر آذوقه قابل کسب')

    info = models.TextField(null=True, blank=True, default='', verbose_name='شرح')

    def __str__(self):
        return (self.title)

    class Meta:
        verbose_name = 'قالب فعالیت'
        verbose_name_plural = 'قالب‌های فعالیت‌ها'


class Activity_Topic(models.Model):
    manzel = models.ForeignKey(Manzel, null=True, blank=True, related_name='activity_topics', on_delete=models.CASCADE,
                               verbose_name='منزل')
    title = models.CharField(default='عنوان پیش‌فرض', max_length=100, verbose_name='عنوان فعالیت')
    co_title = models.CharField(default='عنوان پیش‌فرض', null=True, blank=True, max_length=100,
                                verbose_name='عنوان معرفتی')
    file = models.FileField(null=True, blank=True, upload_to='base/static/activity/',
                            verbose_name='فایل توضیحات فعالیت')
    template = models.ManyToManyField(Activity_Template, related_name='templates', blank=True, verbose_name='قالب ها')

    main = models.BooleanField(default=False, verbose_name='فعالیت اصلی؟')
    code = models.CharField(null=True, blank=True, default='', max_length=8, verbose_name='کد اکتشاف')

    def get_file(self):
        return (str(self.file)[4:])

    def if_long(self):
        if not self.manzel:
            return True
        return False

    def get_activity_templates(self):
        T = []
        for x in self.template.all():
            T.append(
                {
                    'id': x.id,
                    'title': x.title,
                    'type': x.get_type_display(),
                    'max_power': x.max_power,
                    'max_food': x.max_food,
                    'info': x.info,
                }
            )

        return (T)

    def __str__(self):
        return (self.title)

    class Meta:
        verbose_name = 'موضوع فعالیت'
        verbose_name_plural = 'موضوعات فعالیت‌ها'


class Masir_Group(models.Model):
    title = models.CharField(default='عنوان پیش‌فرض', max_length=100, verbose_name='نام گروه')
    users = models.ManyToManyField(User_Detail, related_name='groups', blank=True, verbose_name='اعضای گروه')
    supergroup = models.IntegerField(default=0, verbose_name='ابرگروه')
    manzel = models.IntegerField(default=1, verbose_name='منزل')

    discovered = models.ManyToManyField(Activity_Topic, related_name='discoverd', blank=True,
                                        verbose_name='فعالیت های اکتشاف شده')
    unlocked = models.ManyToManyField(Activity_Template, related_name='unlocked', blank=True,
                                      verbose_name='فعالیت های باز شده')

    introduced = models.BooleanField(default=False, verbose_name='گذراندن آموزش اولیه')

    def goto_supergroup(self):
        a = list(Masir_Group.objects.all().order_by(id()))[-1]
        if len(a.get_supergroupmates()) < 6:
            self.supergroup = a.supergroup
        else:
            self.supergroup = a.supergroup + 1
        self.save()

    def is_first(self):
        if self.manzel == 1 and not self.introduced:
            return True
        return False

    def has_next_manzel(self):
        if Manzel.objects.filter(id=self.manzel + 1):
            return True
        return False

    def add_mains(self):
        for x in Activity_Topic.objects.all():
            if x.main:
                self.discovered.add(x)

    def add_mains_to_all(self):
        for g in Masir_Group.objects.all():
            g.add_mains()

    def get_all_charities(self):
        c = 0.0
        for x in self.charities.all():
            c = c + x.value
        return (c)

    def get_users(self):
        u = ''
        for x in self.users.all():
            u = u + str(x) + ' - '
        return (u[:-3])

    # محاسبه آذوقه
    def get_food(self):
        f = 0
        if self.introduced:
            f += 10
        for x in self.exams.filter(show_public=True):
            f = f + x.score
        x: Activity
        for x in self.activities.filter(state='4'):
            f = f + (x.get_score() * x.template.max_food / 5)
        for x in self.charities.all():
            f = f - x.value
        for x in self.trashes.all():
            f = f - x.food
        for x in Manzel.objects.all()[:max(0, self.manzel - 1)]:
            f = f - x.food_for_next_manzel
        for x in self.discovered.exclude(main=True):
            for t in x.template.all():
                tmp = 0
                if t in self.unlocked.all():
                    tmp += 1
                if tmp > 1:
                    f -= 5

        return int(f * 100) / 100

    # محاسبه توان
    def get_power(self):
        p = 100
        for x in self.users.all():
            p = p + len(x.club_files.filter(show_public=True))
        for x in self.activities.filter(state='4'):
            if x.get_score() > 1.5:
                p = p + x.template.max_power
            else:
                p += x.template.max_power * x.get_score() / 5

        return (p)

    def set_masir_group_and_achivement_rel(self, achivement, score):
        if not self.achivements.filter(group=self, achivement=achivement).first():
            Masir_Group_And_Achivement_Rel.objects.create(
                group=self,
                achivement=achivement,
                score=score
            )

    def delete_masir_group_and_achivement_rel(self, achivements):
        for x in achivements:
            if Masir_Group_And_Achivement_Rel.objects.filter(group=self, achivement=x).first():
                Masir_Group_And_Achivement_Rel.objects.filter(group=self, achivement=x).first().delete()

    def recalculate_achivements(self):
        self.achivements.all().delete()
        for x in self.activities.filter(state='4'):
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(
                    code=ACTIVITIES[x.topic.title] + '_' + str(int(x.template.type)) + str(round(x.get_score()))),
                (4 - int(x.template.type)) * x.get_score()
            )

        if len(self.activities.filter(state='4')) >= 1:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Flg_5'),
                5
            )
        if len(self.activities.filter(state='4')) >= 5:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Flg_10'),
                15
            )
        if len(self.activities.filter(state='4')) >= 10:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Flg_15'),
                20
            )
        if len(self.activities.filter(state='4')) >= 15:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Flg_20'),
                25
            )
        if len(self.activities.filter(state='4')) >= 16:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Sun_0'),
                70
            )

        tmp = 0
        for a in self.activities.filter(state='4'):
            if a.get_score() >= 4.5:
                tmp = tmp + 1
        if tmp >= 7:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Nqs_20'),
                50
            )
        if tmp >= 5:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Nqs_15'),
                40
            )
        if tmp >= 3:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Nqs_10'),
                30
            )
        if tmp >= 1:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Nqs_5'),
                20
            )

        tmp = 0
        for u in self.users.all():
            tmp = tmp + len(u.club_files.filter(show_public=True))
        if tmp >= 14:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Qra_5'),
                    Achivement.objects.get(code='Qra_4'),
                    Achivement.objects.get(code='Qra_3'),
                    Achivement.objects.get(code='Qra_2'),
                    Achivement.objects.get(code='Qra_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Qra_5'),
                0
            )
        elif tmp >= 9:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Qra_5'),
                    Achivement.objects.get(code='Qra_4'),
                    Achivement.objects.get(code='Qra_3'),
                    Achivement.objects.get(code='Qra_2'),
                    Achivement.objects.get(code='Qra_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Qra_4'),
                0
            )
        elif tmp >= 5:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Qra_5'),
                    Achivement.objects.get(code='Qra_4'),
                    Achivement.objects.get(code='Qra_3'),
                    Achivement.objects.get(code='Qra_2'),
                    Achivement.objects.get(code='Qra_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Qra_3'),
                0
            )
        elif tmp >= 0:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Qra_5'),
                    Achivement.objects.get(code='Qra_4'),
                    Achivement.objects.get(code='Qra_3'),
                    Achivement.objects.get(code='Qra_2'),
                    Achivement.objects.get(code='Qra_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Qra_2'),
                0
            )

        if len(Club_File.objects.filter(show_public=True, user__in=self.users.all()).values('level').annotate(
                count=Count('id', distinct=True))) >= 14 or len(
            Club_File.objects.filter(show_public=True, user__in=self.users.all()).values('date__day').annotate(
                count=Count('id', distinct=True))) >= 14:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Vrz_0'),
                30
            )

        for m in range(1, 5):
            tmp = 0
            for a in self.activities.filter(topic__manzel=Manzel.objects.all()[m - 1]):
                tmp = tmp + (a.get_score() * (4 - int(a.template.type)))
            if tmp > 25:
                self.set_masir_group_and_achivement_rel(
                    Achivement.objects.get(code='Mnz_' + str(m)),
                    10
                )
        if self.manzel == 4:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Lst_0'),
                40
            )

        tmp = 0
        for e in self.exams.filter(show_public=True):
            tmp = tmp + e.score
        if tmp >= 120:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Mqz_5'),
                    Achivement.objects.get(code='Mqz_4'),
                    Achivement.objects.get(code='Mqz_3'),
                    Achivement.objects.get(code='Mqz_2'),
                    Achivement.objects.get(code='Mqz_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Mqz_5'),
                0
            )
        elif tmp >= 90:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Mqz_5'),
                    Achivement.objects.get(code='Mqz_4'),
                    Achivement.objects.get(code='Mqz_3'),
                    Achivement.objects.get(code='Mqz_2'),
                    Achivement.objects.get(code='Mqz_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Mqz_4'),
                0
            )
        elif tmp >= 60:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Mqz_5'),
                    Achivement.objects.get(code='Mqz_4'),
                    Achivement.objects.get(code='Mqz_3'),
                    Achivement.objects.get(code='Mqz_2'),
                    Achivement.objects.get(code='Mqz_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Mqz_3'),
                0
            )
        elif tmp >= 30:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Mqz_5'),
                    Achivement.objects.get(code='Mqz_4'),
                    Achivement.objects.get(code='Mqz_3'),
                    Achivement.objects.get(code='Mqz_2'),
                    Achivement.objects.get(code='Mqz_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Mqz_2'),
                0
            )
        elif tmp > 0:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Mqz_5'),
                    Achivement.objects.get(code='Mqz_4'),
                    Achivement.objects.get(code='Mqz_3'),
                    Achivement.objects.get(code='Mqz_2'),
                    Achivement.objects.get(code='Mqz_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Mqz_1'),
                0
            )

        if len(self.exams.filter(show_public=True)) >= 1:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Uni_5'),
                10
            )
        if len(self.exams.filter(show_public=True)) >= 5:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Uni_10'),
                15
            )
        if len(self.exams.filter(show_public=True)) >= 10:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Uni_15'),
                20
            )
        if len(self.exams.filter(show_public=True)) >= 15:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Uni_20'),
                25
            )

        tmp = 0
        for x in self.exams.filter(show_public=True):
            tmp = tmp + x.score
        if tmp >= 150:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Kml_0'),
                50
            )

        tmp = 0
        for x in self.charities.all():
            tmp = tmp + x.value
        if tmp >= 80:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Sdq_5'),
                    Achivement.objects.get(code='Sdq_4'),
                    Achivement.objects.get(code='Sdq_3'),
                    Achivement.objects.get(code='Sdq_2'),
                    Achivement.objects.get(code='Sdq_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Sdq_5'),
                0
            )
        elif tmp >= 60:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Sdq_5'),
                    Achivement.objects.get(code='Sdq_4'),
                    Achivement.objects.get(code='Sdq_3'),
                    Achivement.objects.get(code='Sdq_2'),
                    Achivement.objects.get(code='Sdq_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Sdq_4'),
                0
            )
        elif tmp >= 40:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Sdq_5'),
                    Achivement.objects.get(code='Sdq_4'),
                    Achivement.objects.get(code='Sdq_3'),
                    Achivement.objects.get(code='Sdq_2'),
                    Achivement.objects.get(code='Sdq_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Sdq_3'),
                0
            )
        elif tmp >= 20:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Sdq_5'),
                    Achivement.objects.get(code='Sdq_4'),
                    Achivement.objects.get(code='Sdq_3'),
                    Achivement.objects.get(code='Sdq_2'),
                    Achivement.objects.get(code='Sdq_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Sdq_2'),
                0
            )
        elif tmp > 0:
            self.delete_masir_group_and_achivement_rel(
                [
                    Achivement.objects.get(code='Sdq_5'),
                    Achivement.objects.get(code='Sdq_4'),
                    Achivement.objects.get(code='Sdq_3'),
                    Achivement.objects.get(code='Sdq_2'),
                    Achivement.objects.get(code='Sdq_1')
                ]
            )
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Sdq_1'),
                0
            )

    def get_achivements(self):
        # نشان کمال مطلق
        # نشان فانوس طلایی

        return (self.achivements.all().order_by('achivement__id'))

    def get_light(self):
        l = 14
        for x in self.get_achivements():
            l = l + x.score
        for x in self.exams.filter(show_public=True):
            l = l + x.score / 2
        for x in self.users.all():
            l = l + len(x.club_files.filter(show_public=True)) / 2
        for x in self.charities.all():
            l = l + x.value

        return int(l * 100) / 100

    def get_xp(self):
        return ([
            int(((self.get_light() % 70) / 70) * 100),
            int((self.get_light() // 70) + 1)
        ])

    def get_manzel(self):
        return Manzel.objects.filter(id=self.manzel).first()

    def get_activity_topics(self):
        return ([x.topic for x in self.activities.exclude(state='6')])

    def get_supergroupmates(self):
        SGT = [{'title': x.title, 'light': x.get_light(), 'manzel': x.manzel} for x in
               Masir_Group.objects.filter(supergroup=self.supergroup)]
        SGT.sort(key=lambda x: x.get('light'), reverse=True)
        return (SGT)

    def has_active_exam(self):
        if Exam.objects.filter(active=True).first():
            if not Masir_Group_And_Exams_Rel.objects.filter(group=self,
                                                            exam=Exam.objects.filter(active=True).first()).first():
                return (True)
        return (False)

    def __str__(self):
        return (str(self.title) + ' | ' + str(self.supergroup))

    class Meta:
        verbose_name = 'گروه'
        verbose_name_plural = 'گروه‌ها'


class Masir_Group_And_Achivement_Rel(models.Model):
    group = models.ForeignKey(Masir_Group, related_name='achivements', on_delete=models.CASCADE, verbose_name='گروه')
    achivement = models.ForeignKey(Achivement, related_name='groups', on_delete=models.CASCADE, verbose_name='دستاورد')
    score = models.FloatField(default=0, verbose_name='امتیاز')

    def __str__(self):
        return (str(self.group) + ' | ' + str(self.achivement))

    class Meta:
        verbose_name = 'ارتباط'
        verbose_name_plural = 'ارتباط میان گروه‌ها و دستاوردها'


class Masir_Group_And_Exams_Rel(models.Model):
    group = models.ForeignKey(Masir_Group, related_name='exams', on_delete=models.CASCADE, verbose_name='گروه')
    exam = models.ForeignKey(Exam, related_name='groups', on_delete=models.CASCADE, verbose_name='آزمون')
    score = models.IntegerField(default=0, verbose_name='امتیاز')
    answers = models.CharField(default='', max_length=50, verbose_name='پاسخ‌ها')
    show_public = models.BooleanField(default=False, verbose_name='نمایش عمومی')
    date = jmodels.jDateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ')

    def __str__(self):
        return (str(self.exam) + ' | ' + str(self.group))

    class Meta:
        verbose_name = 'ارتباط'
        verbose_name_plural = 'ارتباط میان گروه‌ها و آزمون‌ها'


class Trash(models.Model):
    group = models.ForeignKey(Masir_Group, related_name='trashes', on_delete=models.CASCADE, verbose_name='گروه')
    food = models.FloatField(default=0, verbose_name='مقدار')
    date = jmodels.jDateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ')

    def __str__(self):
        return (str(self.date) + ' | ' + str(self.group))

    class Meta:
        verbose_name = 'اسراف'
        verbose_name_plural = 'اسراف‌ها'


class Charity(models.Model):
    group = models.ForeignKey(Masir_Group, related_name='charities', on_delete=models.CASCADE, verbose_name='گروه')
    value = models.IntegerField(default=0, verbose_name='مقدار')
    date = jmodels.jDateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ')

    def __str__(self):
        return (str(self.date) + ' | ' + str(self.group))

    class Meta:
        verbose_name = 'صدقه'
        verbose_name_plural = 'صدقات'


class Report(models.Model):
    group = models.ForeignKey(Masir_Group, related_name='reports', on_delete=models.CASCADE, verbose_name='گروه')
    text = models.CharField(default='متن پیش‌فرض', max_length=1000, verbose_name='متن اعلان')
    date = jmodels.jDateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ')

    def __str__(self):
        return (str(self.group.title) + ' | ' + str(self.text))

    class Meta:
        verbose_name = 'گزارش'
        verbose_name_plural = 'گزارش‌ها'


class Activity(models.Model):
    topic = models.ForeignKey(Activity_Topic, related_name='activities', on_delete=models.CASCADE, verbose_name='موضوع')
    template = models.ForeignKey(Activity_Template, null=True, blank=True, related_name='activities',
                                 on_delete=models.CASCADE,
                                 verbose_name='قالب')
    group = models.ForeignKey(Masir_Group, related_name='activities', on_delete=models.CASCADE, verbose_name='گروه')
    referee = models.ForeignKey(User_Detail, null=True, blank=True, related_name='judges', on_delete=models.SET_NULL,
                                verbose_name='داور')
    link = models.CharField(default='#', max_length=1000, verbose_name='لینک فایل')
    state = models.CharField(default='1', max_length=1, choices=ACTIVITY_STATE_CHOICES, verbose_name='وضعیت')
    comment = models.TextField(null=True, blank=True, max_length=5000, verbose_name='توضیحات داور')

    score1 = models.IntegerField(default=0, verbose_name='امتیاز محتوای مناسب، غنی و منسجم')
    score2 = models.IntegerField(default=0, verbose_name='امتیاز رعایت نکات حداقلی فنی درباره‌ی هر قالب')
    score3 = models.IntegerField(default=0, verbose_name='امیتیاز خلاقیت و نوآوری')
    score4 = models.IntegerField(default=0, verbose_name='امتیاز جذابیت برای مخاطب')
    score5 = models.IntegerField(default=0,
                                 verbose_name='امتیاز اشاره به کاربردی بودن مفاهیم در زندگی امروزی، به صورت مستقیم یا غیرمستقیم')

    def get_score(self):
        return (float(
            "{:.2f}".format((self.score1 + self.score2 + self.score3 + self.score4 + self.score5) / 5)))

    def __str__(self):
        return (str(self.topic) + ' | ' + str(self.template) + ' | ' + str(self.group))

    class Meta:
        verbose_name = 'فعالیت'
        verbose_name_plural = 'فعالیت‌ها'
