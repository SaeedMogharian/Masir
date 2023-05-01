from django.contrib.auth.models import User
from django.db import models
from colorfield.fields import ColorField
from django_jalali.db import models as jmodels
from django.db.models import Count

CLUB_LEVELS = [
    {'day': 'اول', 'page': 'نیم صفحه از قرآن کریم: سوره بقره، آیات 183 تا 185'},
    {'day': 'دوم', 'page': 'یک صفحه از قرآن کریم: سوره آل عمران، آیات 133 تا 140'},
    {'day': 'سوم', 'page': 'یک و نیم صفحه از قرآن کریم: سوره فجر، از ابتدا تا انتها'},
    {'day': 'چهارم', 'page': 'دو صفحه از قرآن کریم: سوره تغابن، از ابتدا تا انتها'},
    {'day': 'پنجم', 'page': 'دو و نیم صفحه از قرآن کریم: سوره بقره، آیات 262 تا 274'},
    {'day': 'ششم', 'page': 'سه صفحه از قرآن کریم: سوره الرحمان، از ابتدا تا انتها'},
    {'day': 'هفتم', 'page': 'سه و نیم صفحه از قرآن کریم: سوره هود، آیات 25 تا 53'},
    {'day': 'هشتم', 'page': 'چهار صفحه از قرآن کریم: سوره حدید، از ابتدا تا انتها'},
    {'day': 'نهم', 'page': 'چهار و نیم صفحه از قرآن کریم: سوره فتح، از ابتدا تا انتها'},
    {'day': 'دهم', 'page': 'پنج صفحه از قرآن کریم: سوره انعام، آیات 1 تا 44'},
    {'day': 'یازدهم', 'page': 'پنج و نیم صفحه از قرآن کریم: سوره‌های کهف، آیات 1 تا 45'},
    {'day': 'دوازدهم', 'page': 'شش صفحه از قرآن کریم: سوره یس، از ابتدا تا انتها'},
    {'day': 'سیزدهم', 'page': 'شش و نیم صفحه از قرآن کریم: سوره یونس، آیات 54 تا 109'},
    {'day': 'چهاردهم', 'page': 'هفت صفحه از قرآن کریم: سوره ابراهیم، از ابتدا تا انتها'},
    {'day': 'پانزدهم', 'page': 'هفت صفحه از قرآن کریم: سوره مائده، آیات 10 تا 45'},
    {'day': 'شانزدهم', 'page': 'هفت صفحه از قرآن کریم: سوره مائده، آیات 10 تا 45'},
    {'day': 'هفدهم', 'page': 'هفت صفحه از قرآن کریم: سوره مائده، آیات 10 تا 45'},
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
MEDIA_ROOT = 'media'
STATIC_ROOT = 'static'

ACTIVITIES = {
    'قیام و حرکت': '01',
    'مشورت و عزم': '02',
    'حرکت جمعی': '03',
    'امر به معروف و نهی از منکر': '04',
    'شناخت و بینش': '05',
    'فرقان': '06',
    'دشمن شناسی': '07',
    'هدف و مسیر': '08',
    'صبر و استقامت': '09',
    'امید به یاری خداوند': '10',
    'آزمایش': '11',
    'استعانت': '12',
    'جهاد': '13',
    'روشنگری': '14',
    'اتحاد و تعاون': '15',
    'انقطاع': '16',
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
        verbose_name_plural = 'کاربران - اطلاعات'


class Message(models.Model):
    name = models.CharField(default='نام پیش‌فرض', max_length=100, verbose_name='نام')
    phone = models.CharField(default='9xxxxxxxxx', max_length=10, verbose_name='شماره تلفن')
    message = models.TextField(default='متن پیام پیش‌فرض', max_length=5000, verbose_name='متن پیام')
    answer = models.TextField(null=True, blank=True, max_length=5000, verbose_name='متن پاسخ')
    support = models.ForeignKey(User_Detail, null=True, blank=True, related_name='support', on_delete=models.SET_NULL,
                                verbose_name='پشتیبان')
    date = jmodels.jDateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ')

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
        verbose_name_plural = 'کاربران - پیام‌ها'


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
    story = models.URLField(null=True, blank=True, max_length=200, verbose_name='فایل داستان')
    back_image = models.FileField(null=True, blank=True, upload_to='base/static/manzel/',
                                  verbose_name='تصویر پس زمینه منزل')
    color = ColorField(default='FFFFFF', verbose_name='رنگ پس‌زمینه نَوبار')
    top = models.FloatField(default=0, verbose_name='درصد فاصله از بالای نقشه')
    right = models.FloatField(default=0, verbose_name='درصد فاصله از سمت راست نقشه')
    max_export_food = models.IntegerField(default=0, verbose_name='حداکثر آذوقه قابل حمل در ورودی منزل')
    food_for_next_manzel = models.IntegerField(default=0, verbose_name='آذوقه مورد نیاز برای رسیدن به منزل بعدی')
    power_for_next_manzel = models.IntegerField(default=0, verbose_name='توان مورد نیاز برای رسیدن به منزل بعدی')

    discover_help = models.FileField(null=True, blank=True, upload_to='base/static/manzel/',
                                     verbose_name='فایل رهنمای اکتشاف')
    active = models.BooleanField(default=True, verbose_name='فعال')

    def is_first(self):
        if self.id == 1:
            return True
        return False

    def get_story(self):
        return self.story

    def get_image(self):
        return (str(self.back_image)[4:])

    def get_discover_help(self):
        return 'https://masir1402.ir/media/' + str(self.discover_help)

    def next_manzel_active(self):
        if Manzel.objects.filter(id=self.id + 1).first():
            if Manzel.objects.filter(id=self.id + 1).first().active:
                return True
        return False

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

    report = models.TextField(null=True, blank=True, default='', verbose_name='گزارش')

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
    date = jmodels.jDateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ')
    verified = models.BooleanField(default=False, verbose_name='تایید شده')
    denied = models.BooleanField(default=False, verbose_name='رد شده')
    show_public = models.BooleanField(default=False, verbose_name='نمایش عمومی')

    comment = models.TextField(null=True, blank=True, max_length=5000, verbose_name='توضیحات داور')
    referee = models.ForeignKey(User_Detail, null=True, blank=True, related_name='club_judges',
                                on_delete=models.SET_NULL,
                                verbose_name='داور باشگاه')

    def __str__(self):
        return (str(self.level) + '. ' + str(self.user) + ' | ' + self.title)

    class Meta:
        verbose_name = 'فایل‌'
        verbose_name_plural = 'گروه ها - فایل های باشگاه'


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
        verbose_name_plural = 'آزمون‌های دانشگاه - پرسش ها'


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


class Event(models.Model):
    title = models.CharField(default='عنوان پیش‌فرض', max_length=100, verbose_name='نام فراخوان')
    active = models.BooleanField(default=False, verbose_name='فعال')
    Q = models.TextField(default='پرسش پیش‌فرض', max_length=5000, verbose_name='متن فراخوان')
    O1 = models.TextField(default='پاسخ پیش‌فرض', max_length=5000, verbose_name='گزینه 1')
    O2 = models.TextField(default='پاسخ پیش‌فرض', max_length=5000, verbose_name='گزینه 2')
    O3 = models.TextField(default='پاسخ پیش‌فرض', max_length=5000, verbose_name='گزینه 3')
    O4 = models.TextField(default='پاسخ پیش‌فرض', max_length=5000, verbose_name='گزینه 4')
    A = models.IntegerField(default=1, verbose_name='گزینه صحیح')

    def get_key(self):
        return self.A

    def __str__(self):
        if self.active:
            return ('>> ' + str(self.title))
        return (str(self.title))

    class Meta:
        verbose_name = 'فراخوان'
        verbose_name_plural = 'فراخوان ها'


class Activity_Template(models.Model):
    title = models.CharField(default='عنوان پیش‌فرض', max_length=100, verbose_name='عنوان قالب')
    type = models.CharField(default='1', max_length=1, choices=ACTIVITY_TEMPLATE_TYPE_CHOICES, verbose_name='نوع قالب')
    max_power = models.IntegerField(default=0, verbose_name='حداکثر توان قابل کسب')
    max_food = models.IntegerField(default=0, verbose_name='حداکثر آذوقه قابل کسب')

    info = models.TextField(null=True, blank=True, default='', verbose_name='شرح')

    def get_title(self):
        if 'آسان' in self.title:
            return 'آسان'
        if 'متوسط' in self.title:
            return 'متوسط'
        if 'سخت' in self.title:
            return 'سخت'
        return self.title

    def __str__(self):
        return (self.title)

    class Meta:
        verbose_name = 'قالب فعالیت'
        verbose_name_plural = 'فعالیت‌ها - قالب‌ها'


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
        return 'https://masir1402.ir/media/' + str(self.file)

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
                    'title': x.get_title(),
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
        verbose_name_plural = 'فعالیت‌ها - موضوعات'


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

    def has_unjudged_activity(self):
        if self.activities.exclude(state='4').exclude(state='6').first():
            return True
        return False

    def prev_manzel(self):
        return self.manzel - 1

    def is_acted(self):
        y = []
        for x in self.get_side_activities():
            a = [t.id for t in x.template.all() if t in self.unlocked.all()]
            if len(a) != 0:
                y.append(x.id)
        return y

    def goto_supergroup(self):
        a = len([x.id for x in Masir_Group.objects.exclude(supergroup=0)])
        s = a // 6 + 1

        self.supergroup = s
        self.save()

    def get_side_activities(self):
        return [x for x in self.discovered.exclude(main=True)]

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
            g.save()

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
            f += 50
        for x in self.exams.filter(show_public=True):
            f = f + x.score
        for x in self.events.filter(show_public=True):
            f = f + (x.score * 5)
        x: Activity
        for x in self.activities.filter(state='4').exclude(cheated=True).exclude(topic__manzel=None):
            f = f + (x.get_score() * x.template.max_food / 5)
        for x in self.charities.all():
            f = f - x.value
        for x in self.trashes.all():
            f = f - x.food
        for x in Manzel.objects.all()[:max(0, self.manzel - 1)]:
            f = f - x.food_for_next_manzel
        for x in self.get_side_activities():
            a = [t.id for t in x.template.all() if x.id in self.is_acted() and t in self.unlocked.all()]
            if len(a) >= 3:
                f -= 10
            elif len(a) >= 2:
                f -= 5

        return int(f * 100) / 100

    # محاسبه توان
    def get_power(self):
        p = 100
        for x in self.users.all():
            p = p + len(x.club_files.filter(show_public=True, verified=True))
        for x in self.activities.filter(state='4').exclude(topic__manzel=None):
            if x.get_score() > 1.5:
                p = p + x.template.max_power
            else:
                p += 1

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

    # محاسبه نشان ها
    def ach_mission(self, x):
        main_score = 2 if x.topic.main else 1
        self.set_masir_group_and_achivement_rel(
            Achivement.objects.get(
                code=ACTIVITIES[x.topic.co_title] + '0' + str(4 - int(x.template.type)) + '0' + str(
                    round(x.get_score()))),
            (4 - int(x.template.type)) * x.get_score() * main_score
        )

    def ach_manzel(self, manzel_id):
        tmp = 0
        for a in Masir_Group_And_Achivement_Rel.objects.filter(group=self, achivement__manzel=Manzel.objects.filter(
                id=manzel_id).first()).exclude(achivement__code__contains='Mnz'):
            tmp += a.score
        if tmp > 35:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Mnz_' + str(manzel_id)),
                10
            )

    def ach_last(self):
        if self.manzel == 5:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Lst_0'),
                40
            )

    def ach_flg_nqs(self):
        # نشان پرچم
        for i in range(0, 16, 5):
            a = i if i != 0 else i + 1
            s = a + 10 if a != 1 else 5
            if len(self.activities.filter(state='4')) >= a:
                self.set_masir_group_and_achivement_rel(
                    Achivement.objects.get(code='Flg_' + str(a)),
                    s
                )
        if len(self.activities.filter(state='4')) >= 16:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Sun_0'),
                70
            )

        # نشان بی نقص
        tmp = 0
        for a in self.activities.filter(state='4'):
            a: Activity
            if a.get_score() >= 4.5:
                tmp += 1
        for i in range(1, 8, 2):
            if tmp >= i:
                self.set_masir_group_and_achivement_rel(
                    Achivement.objects.get(code='Nqs_' + str(i)),
                    20 + (i // 2) * 10
                )

    def ach_mng(self):
        tmp = 0
        for a in self.discovered.all():
            if not a.if_long():
                tmp += 1
        if tmp >= 16:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Mng'),
                40
            )

    def ach_qra_vrz(self):
        # نشان قاری
        tmp = 0
        for u in self.users.all():
            tmp = tmp + len(u.club_files.filter(show_public=True, verified=True))
        step = [18, 14, 9, 5, 1]
        for i in step:
            if tmp >= i:
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
                    Achivement.objects.get(code='Qra_' + str(5 - step.index(i))),
                    0
                )
                break
                # نشان ورزیده
        if len(Club_File.objects.filter(show_public=True, verified=True, user__in=self.users.all()).values(
                'level').annotate(ount=Count('id', distinct=True))) >= 14 or len(
            Club_File.objects.filter(show_public=True, verified=True, user__in=self.users.all()).values(
                'date__day').annotate(count=Count('id', distinct=True))) >= 14:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Vrz_0'),
                30
            )

    def ach_mqz_qlm_kml(self):
        # مغز متفکر
        tmp = 0
        for e in self.exams.filter(show_public=True):
            tmp += e.score
        for i in range(120, -1, -30):
            if tmp >= i and tmp > 0:
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
                    Achivement.objects.get(code='Mqz_' + str((i // 30) + 1)),
                    0
                )
                break
        # کمال مطلق
        if tmp >= 150:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Kml_0'),
                50
            )
        # قلم
        for i in range(0, 16, 5):
            a = i if i != 0 else i + 1
            if len(self.exams.filter(show_public=True)) >= a:
                self.set_masir_group_and_achivement_rel(
                    Achivement.objects.get(code='Uni_' + str(a)),
                    i + 5
                )

    def ach_sdq(self):
        tmp = 0
        for x in self.charities.all():
            tmp += x.value
        for i in range(80, -1, -20):
            if tmp >= i and tmp > 0:
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
                    Achivement.objects.get(code='Sdq_' + str((i // 20) + 1)),
                    0
                )
                break

    def ach_lng(self, x):
        if x:
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Lng_0'),
                (120 * x.get_score()) / 5
            )

    def ach_env(self):
        if self.events.filter(score=1):
            self.set_masir_group_and_achivement_rel(
                Achivement.objects.get(code='Env_0'),
                0
            )

    # محاسبه مجدد
    def recalculate_achivements(self):
        self.achivements.all().delete()
        # دستاورد ماموریت ها
        for x in self.activities.filter(state='4').exclude(topic__manzel=None):
            self.ach_mission(x)
        # نشان ذره بین
        self.ach_mng()

        # نشان پرچم
        # نشان بی نقص
        self.ach_flg_nqs()

        # نشان قاری
        # نشان ورزیده
        self.ach_qra_vrz()

        # نشان منازل
        for m in range(2, 6):
            self.ach_manzel(m)
        self.ach_last()

        # مغز متفکر
        # قلم
        # کمال مطلق
        self.ach_mqz_qlm_kml()

        # دست رحمت
        self.ach_sdq()

        # تحول
        self.ach_lng(self.activities.filter(topic__manzel=None).first())

        # فراخوان
        self.ach_env()

    def get_achivements(self):
        # نشان کمال مطلق
        # نشان فانوس طلایی

        return (self.achivements.all().order_by('achivement__id'))

    # حیات نشان‌های بی حیات!!
    def get_exam_light(self):
        l = 0
        for x in self.exams.filter(show_public=True):
            l = l + x.score / 2
        return int(l * 100) / 100

    def get_club_light(self):
        l = 0
        for x in self.users.all():
            l = l + len(x.club_files.filter(show_public=True, verified=True)) / 2
        return int(l * 100) / 100

    def get_charity_light(self):
        l = 0
        for x in self.charities.all():
            l = l + x.value
        return int(l * 100) / 100

    def get_event_light(self):
        l = 0
        for x in self.events.filter(show_public=True):
            l = l + x.score * 10
        return int(l * 100) / 100

    # حیات
    def get_light(self):
        l = 14
        for x in self.get_achivements():
            l = l + x.score
        for x in self.exams.filter(show_public=True):
            l = l + x.score / 2
        for x in self.events.filter(show_public=True):
            l = l + x.score * 10
        for x in self.users.all():
            l = l + len(x.club_files.filter(show_public=True, verified=True)) / 2
        for x in self.charities.all():
            l = l + x.value

        return int(l * 100) / 100

    # سطح
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
        SGT = [{'title': x.title, 'light': x.get_light(), 'manzel': x.get_manzel().number} for x in
               Masir_Group.objects.filter(supergroup=self.supergroup)]
        SGT.sort(key=lambda x: x.get('light'), reverse=True)
        return (SGT)

    def has_active_exam(self):
        if Exam.objects.filter(active=True).first():
            if not Masir_Group_And_Exams_Rel.objects.filter(group=self,
                                                            exam=Exam.objects.filter(active=True).first()).first():
                return (True)
        return (False)

    def has_active_event(self):
        if Event.objects.filter(active=True).first():
            if not Masir_Group_And_Event_Rel.objects.filter(group=self,
                                                            event=Event.objects.filter(active=True).first()).first():
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

    def get_score(self):
        return round(self.score, 2)

    def __str__(self):
        return (str(self.group) + ' | ' + str(self.achivement))

    class Meta:
        verbose_name = 'ارتباط'
        verbose_name_plural = 'گروه ها - دستاوردها'


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
        verbose_name_plural = 'گروه ها - ارتباط با دانشگاه ها'


class Masir_Group_And_Event_Rel(models.Model):
    group = models.ForeignKey(Masir_Group, related_name='events', on_delete=models.CASCADE, verbose_name='گروه')
    event = models.ForeignKey(Event, related_name='groups', on_delete=models.CASCADE, verbose_name='فراخوان')
    score = models.IntegerField(default=0, verbose_name='امتیاز')
    answers = models.CharField(default='', max_length=50, verbose_name='پاسخ‌ها')
    show_public = models.BooleanField(default=False, verbose_name='نمایش عمومی')
    date = jmodels.jDateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ')

    def __str__(self):
        return (str(self.event) + ' | ' + str(self.group))

    class Meta:
        verbose_name = 'ارتباط'
        verbose_name_plural = 'گروه ها - ارتباط با فراخوان ها'


class Trash(models.Model):
    group = models.ForeignKey(Masir_Group, related_name='trashes', on_delete=models.CASCADE, verbose_name='گروه')
    food = models.FloatField(default=0, verbose_name='مقدار')
    date = jmodels.jDateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ')

    def __str__(self):
        return (str(self.date) + ' | ' + str(self.group))

    class Meta:
        verbose_name = 'اسراف'
        verbose_name_plural = 'گروه ها - اسراف‌ها'


class Charity(models.Model):
    group = models.ForeignKey(Masir_Group, related_name='charities', on_delete=models.CASCADE, verbose_name='گروه')
    value = models.IntegerField(default=0, verbose_name='مقدار')
    date = jmodels.jDateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ')

    def __str__(self):
        return (str(self.date) + ' | ' + str(self.group))

    class Meta:
        verbose_name = 'صدقه'
        verbose_name_plural = 'گروه ها - صدقات'


class Report(models.Model):
    group = models.ForeignKey(Masir_Group, related_name='reports', on_delete=models.CASCADE, verbose_name='گروه')
    text = models.CharField(default='متن پیش‌فرض', max_length=1000, verbose_name='متن اعلان')
    date = jmodels.jDateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ')

    def __str__(self):
        return (str(self.group.title) + ' | ' + str(self.text))

    class Meta:
        verbose_name = 'گزارش'
        verbose_name_plural = 'گروه ها - گزارش‌ها'


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

    score1 = models.IntegerField(default=0, verbose_name='معیار 1')
    score2 = models.IntegerField(default=0, verbose_name='معیار 2')
    score3 = models.IntegerField(default=0, verbose_name='معیار 3')
    score4 = models.IntegerField(default=0, verbose_name='معیار 4')
    score5 = models.IntegerField(default=0, verbose_name='معیار 5')
    score6 = models.IntegerField(default=0, verbose_name='معیار 6')
    score7 = models.IntegerField(default=0, verbose_name='معیار 7')

    date = jmodels.jDateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='تاریخ')

    cheated = models.BooleanField(default=False, verbose_name='رفتن به منزل بعد قبل از داوری')

    def get_score(self):
        if not self.topic.if_long():
            return (float(
                "{:.2f}".format((self.score1 + self.score2 + self.score3 + self.score4 + self.score5) / 5)))
        else:
            return (float(
                "{:.2f}".format((
                                        self.score1 + self.score2 + self.score3 + self.score4 + self.score5 + self.score6 + self.score7) / 7)))

    def __str__(self):
        return (str(self.topic) + ' | ' + str(self.template) + ' | ' + str(self.group))

    class Meta:
        verbose_name = 'فعالیت'
        verbose_name_plural = 'گروه ها - فعالیت‌ها'


class Top_Work(models.Model):
    number = models.IntegerField(default=1, verbose_name='شماره')

    link = models.URLField(null=True, blank=True, max_length=200, verbose_name='لینک اثر')

    type = models.CharField(default='1', max_length=1, choices=(
        ('1', 'صوتی'),
        ('2', 'ویدیویی'),
        ('3', 'تصویری')
    ), verbose_name='نوع اثر')

    group = models.ForeignKey(Masir_Group, null=True, blank=True, related_name='topworks', on_delete=models.CASCADE,
                              verbose_name='گروه')

    def get_type_id(self):
        if self.type == '1':
            return 'audio'
        if self.type == '2':
            return 'video'
        return 'picture'

    def numberfromzero(self):
        return self.number - 1

    def get_type_name(self):
        return self.get_type_display()[:-1]

    def get_vote_count(self):
        c = 0
        for v in Vote.objects.filter(is_voted=True):
            if self in v.selections.all():
                c += 1
        return c

    def max_vote_count(self):
        m = 0
        for x in Top_Work.objects.filter(type=self.type):
            c = 0
            for v in Vote.objects.filter(is_voted=True):
                if x in v.selections.all():
                    c += 1
            if c > m: m = c
        return m

    def vote_bar(self):
        return self.get_vote_count() / self.max_vote_count() * 100

    def __str__(self):
        return str(str(self.number) + '. ' + self.get_type_display())

    class Meta:
        verbose_name = 'عنوان اثر'
        verbose_name_plural = 'آثار برتر'


class Vote(models.Model):
    phone = models.CharField(default='9xxxxxxxxx', max_length=10, verbose_name='شماره تلفن')
    selections = models.ManyToManyField(Top_Work, related_name='vote', blank=True, verbose_name='رای ها')
    code = models.IntegerField(default=0, verbose_name='کد تایید')
    is_valid = models.BooleanField(default=False, verbose_name='تایید شده')
    is_voted = models.BooleanField(default=False, verbose_name='رای داده')

    def __str__(self):
        if self.is_voted:
            return 'رای داده . ' + str(self.phone)
        if self.is_valid:
            return 'تایید شده . ' + str(self.phone)
        return str(self.phone)

    class Meta:
        verbose_name = 'رای'
        verbose_name_plural = 'آرای نظرسنجی مردمی'
