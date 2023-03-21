from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.db.models import Count
from base.models import *
from random import randint
import requests
import json


UserApiKey = "75e39256d38148ec86e785d5"
SecretKey = "ERT345rfv@ERT345rfv"


def set_masir_group_and_achivement_rel(group, achivement, score):
  if not group.achivements.filter(group = group, achivement = achivement).first():
    Masir_Group_And_Achivement_Rel.objects.create(
      group = group,
      achivement = achivement,
      score = score
    )

def delete_masir_group_and_achivement_rel(group, achivements):
  for x in achivements:
    if Masir_Group_And_Achivement_Rel.objects.filter(group = group, achivement = x).first():
      Masir_Group_And_Achivement_Rel.objects.filter(group = group, achivement = x).first().delete()



def select_user(username):
  user = User.objects.filter(username = username).first()
  if not user:
    return(None)
  return(user.user_detail)	

def get_message_public(name, phone, message):
  return(None)

def get_city(name):
  if City.objects.filter(name = name).first():
    return(City.objects.filter(name = name).first())
  return(
    City.objects.create(
      name = name
    )
  )

def get_school(name):
  if School.objects.filter(name = name).first():
    return(School.objects.filter(name = name).first())
  return(
    School.objects.create(
      name = name
    )
  )

def SMS(UserApiKey, SecretKey, Code, MobileNumber):
	url = "https://RestfulSms.com/api/Token"
	payload = json.dumps({
		"UserApiKey": UserApiKey,
		"SecretKey": SecretKey
	})
	headers = {
		'Content-Type': 'application/json'
	}
	response = requests.request("POST", url, headers=headers, data=payload)
	
	x = response.text
	a = 0
	while (x[a] != ':'):
		a = a + 1
	a = a + 2
	b = a
	while (x[b] != '"'):
		b = b + 1

	url = "https://RestfulSms.com/api/VerificationCode"
	payload = json.dumps({
		"Code": Code,
		"MobileNumber": MobileNumber
	})
	headers = {
		'Content-Type': 'application/json',
		'x-sms-ir-secure-token': x[a:b]
	}
	response = requests.request("POST", url, headers=headers, data=payload)



def landing_page(request):
  """
  for x in Vote.objects.filter(is_valid = True):
    x.masood_valid = True
    x.save()
  
  for x in Vote.objects.filter(is_valid = False).order_by('-id'):
    if not Vote.objects.filter(phone = x.phone, is_valid = True).first():
      x.masood_valid = True
      x.save()
  
  new_cities = [
    [1052, 801],
    [1053, 1042],
    [1054, 834],
    [1055, 976],
    [1056, 708],
    [1058, 809],
    [1059, 783],
    [1060, 1024],
    [1061, 782],
    [1062, 882],
    [1063, 801],
    [1064, 792],
    [1065, 801],  
    [1067, 852],
    [1068, 792]
  ]

  for city in new_cities:
    for user in City.objects.filter(id = city[0]).first().users.all():
      user.city = City.objects.filter(id = city[1]).first()
      user.save()
  
  schools = [
    [1, 'سمپاد - دبیرستان دوره اول علامه حلی 2 تهران'],
    [2, 'سمپاد - دبیرستان دوره اول علامه حلی 2 تهران'],
    [3, 'سمپاد - دبیرستان دوره اول علامه حلی 2 تهران'],
    [4, 'سمپاد - دبیرستان دوره اول علامه حلی 2 تهران'],
    [5, 'سمپاد - دبیرستان دوره اول علامه حلی 10 تهران'],
    [6, 'سمپاد - دبیرستان دوره اول علامه حلی 2 تهران'],
    [7, 'سمپاد - دبیرستان دوره اول علامه حلی 3 تهران'],
    [8, 'سمپاد - دبیرستان دوره اول علامه حلی 3 تهران'],
    [9, 'سمپاد - شهید بهشتی'],
    [10, 'سمپاد - دبیرستان دوره اول علامه حلی 3 تهران'],
    [11, 'سمپاد - شهید باهنر 3'],
    [12, 'شهید بابایی دوره اول'],
    [13, 'سمپاد - دبیرستان دوره اول شهید دستغیب 1'],
    [14, 'سمپاد - شهید ذوالفقاری'],
    [15, 'دکتر قیصر امین پور'],
    [16, 'سمپاد - دبیرستان دوره اول علامه حلی 2 تهران'],
    [17, 'سمپاد - شهید ستاری'],
    [18, 'سمپاد - شهید ستاری'],
    [19, 'سمپاد - فرزانگان'],
    [20, 'سمپاد - شهید ذوالفقاری'],
    [21, 'سمپاد - دبیرستان دوره اول علامه حلی 1 تهران'],
    [22, 'سمپاد - شهید باهنر 4'],
    [23, 'سمپاد - شهید بهشتی'],
    [24, 'دبیرستان خرد ۱'],
    [25, 'سمپاد - شهید ذوالفقاری'],
    [26, 'سمپاد - شهید ذوالفقاری'],
    [27, 'سمپاد - شهید بهشتی'],
    [28, 'سمپاد - شهید دستغیب'],
    [29, 'سمپاد - شهید هاشمی‌نژاد 4'],
    [30, 'سمپاد - شهید بهشتی'],
    [31, 'سمپاد - دبیرستان دوره اول علامه حلی 2 تهران'],
    [32, 'سمپاد - شهید بهشتی'],
    [33, 'سمپاد - شهید بهشتی'],
    [34, 'سمپاد - دبیرستان دوره اول شهید اژه‌ای 1'],
    [35, 'سمپاد - شهید بهشتی 1'],
    [36, 'امام صادق علیه‌السلام'],
    [37, 'سمپاد - زنده یاد کردی برازجان '],
    [38, 'سمپاد - شهید هاشمی‌نژاد 3'],
    [39, 'شاهد - شهید عباس راصد'],
    [40, 'فرزانگان شهدا'],
    [41, 'حاج احمد سینائیان '],
    [42, 'دبیرستان دوره اول ولایت'],
    [43, 'سمپاد - فرزانگان'],
    [44, 'سمپاد - شهید هاشمی‌نژاد 4'],
    [45, 'سمپاد - دبیرستان دوره اول علامه حلی 1 تهران'],
    [46, 'امام محمد باقر علیه‌السلام'],
    [47, 'سمپاد - فرزانگان'],
    [48, 'علم و ایمان'],
    [49, 'علم و ایمان'],
    [50, 'نامشخص'],
    [51, 'سمپاد - شهید بهشتی 2'],
    [52, 'مدرسه ثامن الائمه'],
    [53, 'سمپاد - دبیرستان دوره اول علامه حلی 6 تهران'],
    [54, 'سمپاد - فرزانگان'],
    [55, 'سمپاد - فرزانگان'],
    [56, 'دبیرستان دوره اول فرزانگان حضرت زینب سلام‌الله‌علیها'],
    [57, 'دبیرستان دوره اول ولایت'],
    [58, 'دبیرستان دوره اول ولایت'],
    [59, 'حنان'],
    [60, 'سمپاد - دبیرستان دوره اول فرزانگان 2 تهران'],
    [61, 'حاج احمد سینائیان '],
    [62, 'سمپاد - شهید بهشتی 2'],
    [63, 'شاهد - امام حسین علیه‌السلام'],
    [64, 'سمپاد - دبیرستان دوره اول فرزانگان 2 تهران'],
    [65, 'بهارستان'],
    [66, 'سمپاد - شهید اژه‌ای'],
    [67, 'سمپاد - فرزانگان'],
    [68, 'سمپاد'],
    [69, 'سمپاد - دبیرستان دوره اول علامه حلی 6 تهران'],
    [70, 'شاهد - شهید نورعلی'],
    [71, 'کمیل '],
    [72, 'کمیل'],
    [73, 'دبیرستان پسرانه مهر فرهنگ'],
    [74, 'فضیلت'],
    [75, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [76, 'کریمه اهل بیت'],
    [77, 'سمپاد - دبیرستان دوره اول علامه حلی 2 تهران'],
    [78, 'سمپاد'],
    [79, 'سمپاد - دبیرستان دوره اول علامه حلی 3 تهران'],
    [80, 'سمپاد - فرزانگان'],
    [81, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [82, 'سمپاد - دبیرستان دوره اول فرزانگان 3 کرج'],
    [83, 'سمپاد - شهید هاشمی‌نژاد 4'],
    [84, 'سمپاد - دبیرستان دوره اول علامه حلی 2 تهران'],
    [85, 'سمپاد - فرزانگان'],
    [86, 'حنان'],
    [87, 'سمپاد - دبیرستان دوره اول علامه حلی 2 تهران'],
    [88, 'سمپاد - دبیرستان دوره اول فرزانگان 8 تهران'],
    [89, 'سمپاد - دبیرستان دوره اول فرزانگان 6 تهران'],
    [90, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [91, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [92, 'نامشخص'],
    [93, 'سمپاد - دبیرستان دوره اول فرزانگان 2 تهران'],
    [94, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [95, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [96, 'سمپاد'],
    [97, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [98, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [99, 'سمپاد - علامه حلی'],
    [100, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [101, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [102, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [103, 'نامشخص'],
    [104, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [105, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [106, 'سمپاد - دبیرستان دوره اول فرزانگان 1 تهران'],
    [107, 'سمپاد - جابر بن حیان'],
    [108, 'سمپاد - جابر بن حیان'],
    [109, 'سمپاد - دبیرستان دوره اول علامه حلی 9 تهران']
  ]

  for school in schools:
    s = School.objects.filter(id = school[0]).first()
    s.name = school[1]
    s.save()

  f = open('messages.txt', 'w', encoding = 'utf-8')
  for x in Message.objects.all():
    f.write(str(x.phone) + '\t' + str(x.name) + '\t' + str(x.get_group()) + '\t' + str(x.message) + '\t' + str(x.answer) + '\n')
  f.close()

  f = open('votes.txt', 'w', encoding = 'utf-8')
  for x in Vote.objects.all():
    f.write(str(x.phone) + '\t' + str(x.get_user()) + '\t' + str(x.get_group()) + '\t' + str(x.is_valid) + '\t' + str(x.masood_valid) + '\t' + str(x.vote_image_1) + '\t' + str(x.vote_image_2) + '\t' + str(x.vote_image_3) + '\t' + str(x.vote_image_4) + '\t' + str(x.vote_image_5) + '\t' + str(x.vote_music_1) + '\t' + str(x.vote_music_2) + '\t' + str(x.vote_music_3) + '\t' + str(x.vote_music_4) + '\t' + str(x.vote_music_5) + '\t' + str(x.vote_video_1) + '\t' + str(x.vote_video_2) + '\t' + str(x.vote_video_3) + '\t' + str(x.vote_video_4) + '\t' + str(x.vote_video_5) + '\n')
  f.close()

  f = open('users.txt', 'w', encoding = 'utf-8')
  for x in User_Detail.objects.all():
    f.write(str(x.get_group()) + '\t' + str(x) + '\t' + str(x.user) + '\t' + str(x.nationalcode) + '\t' + str(x.level) + '\t' + str(x.city) + '\t' + str(x.school) + '\t' + str(len(x.club_files.filter(show_public = True))) + '\t' + str(len(x.club_files.filter(show_public = True))) + '\n')
  f.close()

  f = open('announcements.txt', 'w', encoding = 'utf-8')
  for x in Announcement.objects.all():
    f.write(str(x.date) + '\t' + str(x.title) + '\t' + str(x.text) + '\n')
  f.close()

  f = open('achivements.txt', 'w', encoding = 'utf-8')
  for x in Achivement.objects.all():
    f.write(str(x.title) + '\t' + str(x.get_manzel()) + '\t' + str(x.text) + '\t' + str(len(x.groups.all())) + '\n')
  f.close()

  f = open('club_files.txt', 'w', encoding = 'utf-8')
  for x in Club_File.objects.filter(show_public = True):
    f.write(str(x.user) + '\t' + str(x.title) + '\t' + str(x.link) + '\t' + str(x.date) + '\n')
  f.close()

  f = open('faqs.txt', 'w', encoding = 'utf-8')
  for x in FAQ.objects.all():
    f.write(str(x) + '\t' + str(x.answer) + '\n')
  f.close()

  f = open('exams.txt', 'w', encoding = 'utf-8')
  for x in Exam.objects.all():
    f.write(str(x.title) + '\t' + str(len(x.groups.all())) + '\n')
  f.close()

  f = open('groups.txt', 'w', encoding = 'utf-8')
  for x in Masir_Group.objects.all():
    f.write(str(x.title) + '\t' + str(x.get_users()) + '\t' + str(x.supergroup) + '\t' + str(x.manzel) + '\t' + str(len(x.activities.all())) + '\t' + str(x.get_food()) + '\t' + str(x.get_power()) + '\t' + str(x.get_light()) + '\t' + str(x.get_all_charities()) + '\n')
  f.close()

  f = open('groups-achivements.txt', 'w', encoding = 'utf-8')
  for x in Masir_Group_And_Achivement_Rel.objects.all():
    f.write(str(x.group) + '\t' + str(x.achivement) + '\n')
  f.close()

  f = open('groups-exams.txt', 'w', encoding = 'utf-8')
  for x in Masir_Group_And_Exams_Rel.objects.all():
    f.write(str(x.group) + '\t' + str(x.exam) + '\t' + str(x.score) + '\t' + str(x.answers) + '\t' + str(x.exam.get_key()) + '\n')
  f.close()

  f = open('trashes.txt', 'w', encoding = 'utf-8')
  for x in Trash.objects.all():
    f.write(str(x.group) + '\t' + str(x.food) + '\t' + str(x.date) + '\n')
  f.close()

  f = open('charities.txt', 'w', encoding = 'utf-8')
  for x in Charity.objects.all():
    f.write(str(x.group) + '\t' + str(x.value) + '\t' + str(x.date) + '\n')
  f.close()

  f = open('activity-topics.txt', 'w', encoding = 'utf-8')
  for x in Activity_Topic.objects.all():
    f.write(str(x.manzel) + '\t' + str(x.title) + '\t' + str(len(x.activities.all())) + '\n')
  f.close()

  f = open('activity-templates.txt', 'w', encoding = 'utf-8')
  for x in Activity_Template.objects.all():
    f.write(str(x.title) + '\t' + str(x.get_type_display()) + '\t' + str(x.chance) + '\t' + str(x.max_food) + '\t' + str(x.max_power) + '\t' + str(len(x.activities.all())) + '\n')
  f.close()
  
  f = open('activity.txt', 'w', encoding = 'utf-8')
  for x in Activity.objects.all():
    f.write(str(x.get_state_display()) + '\t' + str(x.topic) + '\t' + str(x.template) + '\t' + str(x.group) + '\t' + str(x.referee) + '\t' + str(x.link) + '\t' + str(x.comment) + '\t' + str(x.score1) + '\t' + str(x.score2) + '\t' + str(x.score3) + '\t' + str(x.score4) + '\t' + str(x.score5) + '\t' + str(x.score6) + '\t' + str(x.get_score()) + '\n')
  f.close()
  """

  if request.method == 'POST':
    if 'message_form' in request.POST:
      Message.objects.create(
        name = request.POST['contact_us_name'],
        phone = request.POST['contact_us_phone'],
        message = request.POST['contact_us_message']
      )
      return(
        render(
          request,
          'landing_page.html',
          {
            'MESSAGE': 'پیام شما با موفقیت ثبت شد.',
            'cities': City.objects.all().order_by('name'),
            'schools': School.objects.all().order_by('name'),
            'announcements': Announcement.objects.filter(is_public = True)
          }
        )
      )
    if 'login_form' in request.POST:
      user = authenticate(
        username = request.POST['login_phone'],
        password = request.POST['login_password']
      )
      if user and user.is_active:
        if user.user_detail.groups.all().first() or user.user_detail.accessibility != Accessibility.objects.get(title = 'دسترسی دانش‌آموزی'):
          login(request, user)
          return(redirect('home_page_link'))
        
        return(
          render(
            request,
            'landing_page.html',
            {
              'MESSAGE': str(user.user_detail)
                        + ' عزیز! مسابقه شروع شده است و ثبت نام شما با موفقیت انجام شده است ولی شما هنوز تیم ندارید. کد شما عبارت است از:'
                        + '<br>' + str(user.user_detail.code) + '<br>'
                        + 'برای تشکیل تیم و شروع مسابقه به این کد نیاز خواهید داشت.'
                        + '<br> <br>' + 'چند نکته بسیار مهم:'
                        + '<ul>'
                        + '<li>' + 'برای شرکت در مسابقه حتما لازم است گروه‌های خود را در سایت ثبت کنید (یکی از افراد گروه، با در دست داشتن کد اعضای دیگر، وارد سایت شده و در بخش ثبت نام گروهی اقدام می کند).' + '</li>'
                        + '<li>' + 'مسابقه از هفته دوم ماه مبارک رمضان آغاز شده است.' + '</li>'
                        + '<li>' + 'حتما و حتما در یکی از کانالهای مسابقه عضو شوید تا اطلاعیه‌های بعدی را دریافت نمایید.' + '</li>'
                        + '</ul>',
              'cities': City.objects.all().order_by('name'),
              'schools': School.objects.all().order_by('name'),
              'announcements': Announcement.objects.filter(is_public = True)
            }
          )
        )
      return(
        render(
          request,
          'landing_page.html',
          {
            'MESSAGE': 'شماره تلفن یا رمز عبور اشتباه وارد شده است.',
            'cities': City.objects.all().order_by('name'),
            'schools': School.objects.all().order_by('name'),
            'announcements': Announcement.objects.filter(is_public = True)
          }
        )
      )
    if 'register_form' in request.POST:
      user = User.objects.filter(username = request.POST['register_phone']).first()
      if user:
        if user.is_active:
          return(
            render(
              request,
              'landing_page.html',
              {
                'MESSAGE': 'شماره تلفن ' + request.POST['register_phone'] + ' قبلا ثبت شده است.',
                'cities': City.objects.all().order_by('name'),
                'schools': School.objects.all().order_by('name'),
                'announcements': Announcement.objects.filter(is_public = True)
              }
            )
          )
        user.delete()
      
      if User.objects.filter(user_detail__nationalcode = request.POST['register_nationalcode']).first():
        return(
          render(
            request,
            'landing_page.html',
            {
              'MESSAGE': 'کد ملی ' + request.POST['register_nationalcode'] + ' قبلا ثبت شده است.',
              'cities': City.objects.all().order_by('name'),
              'schools': School.objects.all().order_by('name'),
              'announcements': Announcement.objects.filter(is_public = True)
            }
          )
        )

      user = User.objects.create_user(
        first_name = request.POST['register_firstname'],
        last_name = request.POST['register_lastname'],
        username = request.POST['register_phone'],
        password = request.POST['register_password']
      )
      user.is_active = False
      user.save()
        

      User_Detail.objects.create(
        user = user,
        accessibility = Accessibility.objects.get(title = 'دسترسی دانش‌آموزی'),
        nationalcode = request.POST['register_nationalcode'],
        level = int(request.POST['register_level']),
        city = get_city(request.POST['register_city']),
        school = get_school(request.POST['register_school']),
        code = str(randint(10000, 100000))
      )

      SMS(UserApiKey, SecretKey, user.user_detail.code, '0' + user.username)

      return(
        render(
          request,
          'verification_page.html',
          {
            'phone': user.username
          }
        )
      )
    if 'verification_form' in request.POST:
      user = User.objects.filter(username = request.POST['verification_phone']).first()
      if user and user.user_detail.code == request.POST['verification_code']:
        user.is_active = True
        user.save()
        return(
          render(
            request,
            'landing_page.html',
            {
              'MESSAGE': str(user.user_detail)
                        + ' عزیز! ثبت نام شما با موفقیت انجام شد. کد شما عبارت است از:'
                        + '<br>' + str(user.user_detail.code) + '<br>'
                        + 'برای تشکیل تیم و شروع مسابقه به این کد نیاز خواهید داشت.'
                        + '<br> <br>' + 'چند نکته بسیار مهم:'
                        + '<ul>'
                        + '<li>' + 'برای شرکت در مسابقه حتما لازم است گروه‌های خود را در سایت ثبت کنید (یکی از افراد گروه، با در دست داشتن کد اعضای دیگر، وارد سایت شده و در بخش ثبت نام گروهی اقدام می کند).' + '</li>'
                        + '<li>' + 'مسابقه از هفته دوم ماه مبارک رمضان آغاز خواهد شد.' + '</li>'
                        + '<li>' + 'حتما و حتما در یکی از کانالهای مسابقه عضو شوید تا اطلاعیه‌های بعدی را دریافت نمایید.' + '</li>'
                        + '</ul>',
              'cities': City.objects.all().order_by('name'),
              'schools': School.objects.all().order_by('name'),
              'announcements': Announcement.objects.filter(is_public = True)
            }
          )
        )
      return(
        render(
          request,
          'landing_page.html',
          {
            'MESSAGE': 'کد وارد شده صحیح نیست!',
            'cities': City.objects.all().order_by('name'),
            'schools': School.objects.all().order_by('name'),
            'announcements': Announcement.objects.filter(is_public = True)
          }
        )
      )
    if 'group_register_form' in request.POST:
      user1 = User_Detail.objects.filter(user__username = request.POST['group_register_phone_1'], code = request.POST['group_register_code_1']).first()
      user2 = User_Detail.objects.filter(user__username = request.POST['group_register_phone_2'], code = request.POST['group_register_code_2']).first()
      user3 = User_Detail.objects.filter(user__username = request.POST['group_register_phone_3'], code = request.POST['group_register_code_3']).first()
      
      if user1 and user2 and user3 and user1 != user2 and user2 != user3 and user3 != user1:
        if not user1.groups.all() and not user2.groups.all() and not user3.groups.all():
          g = Masir_Group.objects.create(
            title = request.POST['group_register_title']
          )
          g.users.add(user1)
          g.users.add(user2)
          g.users.add(user3)
          g.save()
          
          Report.objects.create(
            group = g,
            text = 'گروه شما با عنوان «' + str(g.title) + '» ثبت شد.'
          )
          
          return(
            render(
              request,
              'landing_page.html',
              {
                'MESSAGE': 'گروه شما با عنوان '
                          + str(g.title)
                          + ' ثبت شد.'
                          + '<br>'
                          + 'اعضای گروه عبارتند از:'
                          + '<br>'
                          + g.get_users_name()
                          + '<br> <br>'
                          + 'چند نکته مهم:'
                          + '<ul>'
                          + '<li>' + 'مسابقه از هفته دوم ماه مبارک رمضان آغاز خواهد شد.' + '</li>'
                          + '<li>' + 'حتما و حتما در یکی از کانالهای مسابقه عضو شوید تا اطلاعیه‌های بعدی را دریافت نمایید.' + '</li>'
                          + '</ul>',
                'cities': City.objects.all().order_by('name'),
                'schools': School.objects.all().order_by('name'),
                'announcements': Announcement.objects.filter(is_public = True)
              }
            )
          )
        return(
          render(
            request,
            'landing_page.html',
            {
              'MESSAGE': 'اعضای گروه نباید در گروه دیگری عضو باشند.',
              'cities': City.objects.all().order_by('name'),
              'schools': School.objects.all().order_by('name'),
              'announcements': Announcement.objects.filter(is_public = True)
            }
          )
        )
      return(
        render(
          request,
          'landing_page.html',
          {
            'MESSAGE': 'اطلاعات وارد شده صحیح نیست.',
            'cities': City.objects.all().order_by('name'),
            'schools': School.objects.all().order_by('name'),
            'announcements': Announcement.objects.filter(is_public = True)
          }
        )
      )
     
  user = select_user(request.user)
  if user:
    if user.groups.all().first() or user.accessibility != Accessibility.objects.get(title = 'دسترسی دانش‌آموزی'):
      return(redirect('home_page_link'))
    return(
      render(
        request,
        'landing_page.html',
        {
          'MESSAGE': str(user)
                    + ' عزیز! مسابقه شروع شده است و ثبت نام شما با موفقیت انجام شده است ولی شما هنوز تیم ندارید. کد شما عبارت است از:'
                    + '<br>' + str(user.code) + '<br>'
                    + 'برای تشکیل تیم و شروع مسابقه به این کد نیاز خواهید داشت.'
                    + '<br> <br>' + 'چند نکته بسیار مهم:'
                    + '<ul>'
                    + '<li>' + 'برای شرکت در مسابقه حتما لازم است گروه‌های خود را در سایت ثبت کنید (یکی از افراد گروه، با در دست داشتن کد اعضای دیگر، وارد سایت شده و در بخش ثبت نام گروهی اقدام می کند).' + '</li>'
                    + '<li>' + 'مسابقه از هفته دوم ماه مبارک رمضان آغاز شده است.' + '</li>'
                    + '<li>' + 'حتما و حتما در یکی از کانالهای مسابقه عضو شوید تا اطلاعیه‌های بعدی را دریافت نمایید.' + '</li>'
                    + '</ul>',
          'cities': City.objects.all().order_by('name'),
          'schools': School.objects.all().order_by('name'),
          'announcements': Announcement.objects.filter(is_public = True)
        }
      )
    )

  return(
    render(
      request,
      'landing_page.html',
      {
        'MESSAGE': None,
        'cities': City.objects.all().order_by('name'),
        'schools': School.objects.all().order_by('name'),
        'announcements': Announcement.objects.filter(is_public = True)
      }
    )
  )

def full_map_page(request):
  return(
    render(
      request,
      'full_map_page.html',
      {
        'MESSAGE': 'صفحه نهایی بازی برای یک گروه فرضی!',
        'manazel': Manzel.objects.all().order_by('right')[0:7],
        'manzel_achievements': Achivement.objects.exclude(manzel = None).order_by('manzel__id'),
        'none_manzel_achievements': Achivement.objects.filter(manzel = None),
        'exam': Exam.objects.all().last(),
        'announcements': Announcement.objects.filter(is_public = True),
        'FAQ': FAQ.objects.filter(is_active = True)
      }
    )
  )

def people_judge_page(request):
  if request.method == 'POST':
    if 'people_judge_form' in request.POST:
      if Vote.objects.filter(phone = request.POST['people_judge_phone'], is_valid = True).first():
        return(
          render(
            request,
            'landing_page.html',
            {
              'MESSAGE': 'شماره تلفن ' + request.POST['people_judge_phone'] + ' قبلا رای داده است.',
              'cities': City.objects.all().order_by('name'),
              'schools': School.objects.all().order_by('name'),
              'announcements': Announcement.objects.filter(is_public = True)
            }
          )
        )
      
      v = Vote.objects.create(
        phone = request.POST['people_judge_phone'],
        code = randint(10000, 100000)
      )
      
      try:
        if request.POST['people_judge_image_1'] == 'on':
          v.vote_image_1 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_image_2'] == 'on':
          v.vote_image_2 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_image_3'] == 'on':
          v.vote_image_3 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_image_4'] == 'on':
          v.vote_image_4 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_image_5'] == 'on':
          v.vote_image_5 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_music_1'] == 'on':
          v.vote_music_1 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_music_2'] == 'on':
          v.vote_music_2 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_music_3'] == 'on':
          v.vote_music_3 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_music_4'] == 'on':
          v.vote_music_4 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_music_5'] == 'on':
          v.vote_music_5 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_video_1'] == 'on':
          v.vote_video_1 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_video_2'] == 'on':
          v.vote_video_2 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_video_3'] == 'on':
          v.vote_video_3 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_video_4'] == 'on':
          v.vote_video_4 = True
          v.save()
      except:
        pass
      try:
        if request.POST['people_judge_video_5'] == 'on':
          v.vote_video_5 = True
          v.save()
      except:
        pass
      
      SMS(UserApiKey, SecretKey, str(v.code), '0' + str(v.phone))
      
      return(
        render(
          request,
          'verification_page.html',
          {
            'phone': v.phone
          }
        )
      )
    
    if 'verification_form' in request.POST:
      v = Vote.objects.filter(phone = request.POST['verification_phone']).last()
      if not v:
        return(
          render(
            request,
            'landing_page.html',
            {
              'MESSAGE': 'در تایید رای شما مشکلی پیش آمده است. مجددا سعی کنید.',
              'cities': City.objects.all().order_by('name'),
              'schools': School.objects.all().order_by('name'),
              'announcements': Announcement.objects.filter(is_public = True)
            }
          )
        )
      
      if str(v.code) == request.POST['verification_code']:
        v.is_valid = True
        v.save()

        return(
          render(
            request,
            'landing_page.html',
            {
              'MESSAGE': 'رای شما با موفقیت ثبت شد.',
              'cities': City.objects.all().order_by('name'),
              'schools': School.objects.all().order_by('name'),
              'announcements': Announcement.objects.filter(is_public = True)
            }
          )
        )
      
      return(
        render(
          request,
          'landing_page.html',
          {
            'MESSAGE': 'کد وارد شده صحیح نیست.',
            'cities': City.objects.all().order_by('name'),
            'schools': School.objects.all().order_by('name'),
            'announcements': Announcement.objects.filter(is_public = True)
          }
        )
      )

    
  return(
    render(
      request,
      'people_judge_page.html',
      {
      }
    )
  )

def forgot_password_page(request):
  if request.method == 'POST':
    if 'forgot_password_L1_form' in request.POST:
      user = User.objects.filter(username = request.POST['forgot_password_phone'], user_detail__nationalcode = request.POST['forgot_password_nationalcode']).first()
      if user:
        user = user.user_detail
        user.code = str(randint(10000, 100000))
        user.save()
        SMS(UserApiKey, SecretKey, user.code, '0' + request.POST['forgot_password_phone'])
        return(
          render(
            request,
            'forgot_password_L2_page.html',
            {
              'the_user': user
            }
          )
        )
      return(
        render(
          request,
          'landing_page.html',
          {
            'MESSAGE': 'شماره تلفن یا کد ملی اشتباه وارد شده است.',
            'cities': City.objects.all().order_by('name'),
            'schools': School.objects.all().order_by('name'),
            'announcements': Announcement.objects.filter(is_public = True)
          }
        )
      )
    if 'forgot_password_L2_form' in request.POST:
      user = User.objects.filter(username = request.POST['forgot_password_phone']).first()
      if user and user.user_detail.code == request.POST['forgot_password_code']:
        user.set_password(request.POST['forgot_password_password'])
        user.save()
        return(
          render(
            request,
            'landing_page.html',
            {
              'MESSAGE': 'رمز عبور با موفقیت تغییر کرد.',
              'cities': City.objects.all().order_by('name'),
              'schools': School.objects.all().order_by('name'),
              'announcements': Announcement.objects.filter(is_public = True)
            }
          )
        )
      return(
        render(
          request,
          'landing_page.html',
          {
            'MESSAGE': 'کد وارد شده صحیح نیست.',
            'cities': City.objects.all().order_by('name'),
            'schools': School.objects.all().order_by('name'),
            'announcements': Announcement.objects.filter(is_public = True)
          }
        )
      )
  return(
    render(
      request,
      'forgot_password_L1_page.html',
      {
        
      }
    )
  )

def home_page(request):
  user = select_user(request.user)
  if not user:
    return(redirect('landing_page_link'))
  if not user.groups.all().first() and user.accessibility == Accessibility.objects.get(title = 'دسترسی دانش‌آموزی'):
    return(
      render(
        request,
        'landing_page.html',
        {
          'MESSAGE': str(user)
                    + ' عزیز! مسابقه شروع شده است و ثبت نام شما با موفقیت انجام شده است ولی شما هنوز تیم ندارید. کد شما عبارت است از:'
                    + '<br>' + str(user.code) + '<br>'
                    + 'برای تشکیل تیم و شروع مسابقه به این کد نیاز خواهید داشت.'
                    + '<br> <br>' + 'چند نکته بسیار مهم:'
                    + '<ul>'
                    + '<li>' + 'برای شرکت در مسابقه حتما لازم است گروه‌های خود را در سایت ثبت کنید (یکی از افراد گروه، با در دست داشتن کد اعضای دیگر، وارد سایت شده و در بخش ثبت نام گروهی اقدام می کند).' + '</li>'
                    + '<li>' + 'مسابقه از هفته دوم ماه مبارک رمضان آغاز شده است.' + '</li>'
                    + '<li>' + 'حتما و حتما در یکی از کانالهای مسابقه عضو شوید تا اطلاعیه‌های بعدی را دریافت نمایید.' + '</li>'
                    + '</ul>',
          'cities': City.objects.all().order_by('name'),
          'schools': School.objects.all().order_by('name'),
          'announcements': Announcement.objects.filter(is_public = True)
        }
      )
    )
  
  if request.method == 'POST':
    if 'club_form' in request.POST:
      c = 0
      for u in user.groups.all().first().users.all():
        try:
          if request.POST['club_file_' + str(u.id)] != '':
            if u.club_level < 0:
              return(
                render(
                  request,
                  'home_page.html',
                  {
                    'manazel': Manzel.objects.filter(id__lte = user.groups.all().first().manzel).order_by('right'),
                    'announcements': Announcement.objects.filter(is_active = True).order_by('-id'),
                    'reports': Report.objects.filter(group = user.groups.all().first()).order_by('-id'),
                    'FAQ': FAQ.objects.filter(is_active = True),
                    'achivements': Achivement.objects.filter(manzel = None),
                    'templates': Activity_Template.objects.all(),
                    'exam': Exam.objects.filter(active = True).first(),
                    'MESSAGE': 'شما قبلا یک فایل در باشگاه ارسال کرده‌اید.'
                  }
                )
              )
            
            Report.objects.create(
              group = user.groups.all().first(),
              text = 'فایل «' + str(u.get_club_level()) + '» با موفقیت ارسال شد.'
            )
            
            Club_File.objects.create(
              user = u,
              link = request.POST['club_file_' + str(u.id)],
              title = CLUB_LEVELS[u.club_level]['page'],
              level = u.club_level
            )

            u.club_level = -1
            u.save()
          c = c + 1
        except:
          pass
      return(redirect('home_page_link'))
      
    if 'charity_form' in request.POST:
      if int(request.POST['charity_value']) > user.groups.all().first().get_food():
        return(
          render(
            request,
            'home_page.html',
            {
              'manazel': Manzel.objects.filter(id__lte = user.groups.all().first().manzel).order_by('right'),
              'announcements': Announcement.objects.filter(is_active = True).order_by('-id'),
              'reports': Report.objects.filter(group = user.groups.all().first()).order_by('-id'),
              'FAQ': FAQ.objects.filter(is_active = True),
              'achivements': Achivement.objects.filter(manzel = None),
              'templates': Activity_Template.objects.all(),
              'exam': Exam.objects.filter(active = True).first(),
              'MESSAGE': 'میزان صدقه از میزان آذوقه گروه بیشتر است.'
            }
          )
        )
      Charity.objects.create(
        group = user.groups.all().first(),
        value = int(request.POST['charity_value'])
      )

      tmp = 0
      for x in user.groups.all().first().charities.all():
        tmp = tmp + x.value
      if tmp >= 40:
        delete_masir_group_and_achivement_rel(
          user.groups.all().first(),
          [
            Achivement.objects.get(code = 'Sdq_5'),
            Achivement.objects.get(code = 'Sdq_4'),
            Achivement.objects.get(code = 'Sdq_3'),
            Achivement.objects.get(code = 'Sdq_2'),
            Achivement.objects.get(code = 'Sdq_1')
          ]
        )
        set_masir_group_and_achivement_rel(
          user.groups.all().first(),
          Achivement.objects.get(code = 'Sdq_5'),
          0
        )
      elif tmp >= 30:
        delete_masir_group_and_achivement_rel(
          user.groups.all().first(),
          [
            Achivement.objects.get(code = 'Sdq_5'),
            Achivement.objects.get(code = 'Sdq_4'),
            Achivement.objects.get(code = 'Sdq_3'),
            Achivement.objects.get(code = 'Sdq_2'),
            Achivement.objects.get(code = 'Sdq_1')
          ]
        )
        set_masir_group_and_achivement_rel(
          user.groups.all().first(),
          Achivement.objects.get(code = 'Sdq_4'),
          0
        )
      elif tmp >= 20:
        delete_masir_group_and_achivement_rel(
          user.groups.all().first(),
          [
            Achivement.objects.get(code = 'Sdq_5'),
            Achivement.objects.get(code = 'Sdq_4'),
            Achivement.objects.get(code = 'Sdq_3'),
            Achivement.objects.get(code = 'Sdq_2'),
            Achivement.objects.get(code = 'Sdq_1')
          ]
        )
        set_masir_group_and_achivement_rel(
          user.groups.all().first(),
          Achivement.objects.get(code = 'Sdq_3'),
          0
        )
      elif tmp >= 10:
        delete_masir_group_and_achivement_rel(
          user.groups.all().first(),
          [
            Achivement.objects.get(code = 'Sdq_5'),
            Achivement.objects.get(code = 'Sdq_4'),
            Achivement.objects.get(code = 'Sdq_3'),
            Achivement.objects.get(code = 'Sdq_2'),
            Achivement.objects.get(code = 'Sdq_1')
          ]
        )
        set_masir_group_and_achivement_rel(
          user.groups.all().first(),
          Achivement.objects.get(code = 'Sdq_2'),
          0
        )
      elif tmp > 0:
        delete_masir_group_and_achivement_rel(
          user.groups.all().first(),
          [
            Achivement.objects.get(code = 'Sdq_5'),
            Achivement.objects.get(code = 'Sdq_4'),
            Achivement.objects.get(code = 'Sdq_3'),
            Achivement.objects.get(code = 'Sdq_2'),
            Achivement.objects.get(code = 'Sdq_1')
          ]
        )
        set_masir_group_and_achivement_rel(
          user.groups.all().first(),
          Achivement.objects.get(code = 'Sdq_1'),
          0
        )
    

      Report.objects.create(
        group = user.groups.all().first(),
        text = 'صدقات شما به ارزش ' + request.POST['charity_value'] + ' واحد با موفقیت ثبت شد.'
      )

      return(redirect('home_page_link'))

    if 'university_form' in request.POST:
      exam = Exam.objects.filter(active = True).first()
      if Masir_Group_And_Exams_Rel.objects.filter(group = user.groups.all().first(), exam = exam).first():
        return(
          render(
            request,
            'home_page.html',
            {
              'manazel': Manzel.objects.filter(id__lte = user.groups.all().first().manzel).order_by('right'),
              'announcements': Announcement.objects.filter(is_active = True).order_by('-id'),
              'reports': Report.objects.filter(group = user.groups.all().first()).order_by('-id'),
              'FAQ': FAQ.objects.filter(is_active = True),
              'achivements': Achivement.objects.filter(manzel = None),
              'templates': Activity_Template.objects.all(),
              'exam': Exam.objects.filter(active = True).first(),
              'MESSAGE': 'گروه شما قبلا یکبار در این آزمون شرکت کرده است.'
            }
          )
        )
      
      score = 0
      answers = ''
      for q in exam.questions.all():
        a = request.POST['Q' + str(q.id)]
        if q.A == int(a):
          score = score + 1
        answers = answers + a
        
      Masir_Group_And_Exams_Rel.objects.create(
        group = user.groups.all().first(),
        exam = exam,
        score = score,
        answers = answers
      )

      Report.objects.create(
        group = user.groups.all().first(),
        text = 'پاسخ‌های شما به ' + str(exam) + ' با موفقیت ثبت شد.'
      )

      return(redirect('home_page_link'))

    if 'next_level_form' in request.POST:
      if user.groups.all().first().get_manzel().food_for_next_manzel and user.groups.all().first().get_manzel().power_for_next_manzel and user.groups.all().first().get_food() >= user.groups.all().first().get_manzel().food_for_next_manzel or user.groups.all().first().get_power() >= user.groups.all().first().get_manzel().power_for_next_manzel:
        trash = user.groups.all().first().get_food() - user.groups.all().first().get_manzel().food_for_next_manzel - user.groups.all().first().get_manzel().max_export_food
        text = 'شما با صرف ' + str(user.groups.all().first().get_manzel().food_for_next_manzel) + ' واحد از آذوقه ی خود توانستید به منزل بعد بروید'
        if trash > 0:
          Trash.objects.create(
            group = user.groups.all().first(),
            food = trash
          )
          text = text + '؛ ' + str((trash * 100)/100) + ' واحد آذوقه اضافه را در مسیر حرکت از دست دادید'

        g = user.groups.all().first()
        
        tmp = 0
        for x in g.activities.filter(topic__manzel = g.get_manzel()):
          tmp = tmp + (x.get_score() * (4 - int(x.template.type)))
        if tmp > 25:
          set_masir_group_and_achivement_rel(
            g,
            Achivement.objects.get(code = 'Mnz_' + str(g.manzel)),
            10
          )
        if g.manzel == 7:
          set_masir_group_and_achivement_rel(
            Achivement.objects.get(code = 'Lst_0'),
            40
          )
        
        g.manzel = g.manzel + 1
        g.save()

        text = text + ' و با ' + str(g.get_food()) + ' آذوقه به منزل بعد رسیدید.'

        Report.objects.create(
          group = user.groups.all().first(),
          text = text
        )

        return(redirect('home_page_link'))

    for x in user.groups.all().first().get_manzel().activity_topics.all():
      if 'activity_' + str(x.id) + '_form' in request.POST:
        if (Activity.objects.filter(topic = x, group = user.groups.all().first()).exclude(state = '6').first()):
          return(
            render(
              request,
              'home_page.html',
              {
                'manazel': Manzel.objects.filter(id__lte = user.groups.all().first().manzel).order_by('right'),
                'announcements': Announcement.objects.filter(is_active = True).order_by('-id'),
                'reports': Report.objects.filter(group = user.groups.all().first()).order_by('-id'),
                'FAQ': FAQ.objects.filter(is_active = True),
                'achivements': Achivement.objects.filter(manzel = None),
                'templates': Activity_Template.objects.all(),
                'exam': Exam.objects.filter(active = True).first(),
                'MESSAGE': 'گروه شما قبلا یکبار این فعالیت را انجام داده است.'
              }
            )
          )
        
        Activity.objects.create(
          topic = x,
          template = Activity_Template.objects.filter(id = int(request.POST['activity_' + str(x.id) + '_template'])).first(),
          group = user.groups.all().first(),
          link = request.POST['activity_' + str(x.id) + '_file'],
          state = '1'
        )
        Report.objects.create(
          group = user.groups.all().first(),
          text = 'فعالیت شما در بخش «' + str(x) + '» و با قالب «' + str(Activity_Template.objects.filter(id = int(request.POST['activity_' + str(x.id) + '_template'])).first()) + '» با موفقیت ثبت شد.'
        )
        return(redirect('home_page_link'))
    

    if 'university_show_scores_admin_form' in request.POST:
      for x in Masir_Group_And_Exams_Rel.objects.filter(show_public = False):
        x.show_public = True
        x.save()

        tmp = 0
        for e in x.group.exams.filter(show_public = True):
          tmp = tmp + e.score
        if tmp >= 160:
          delete_masir_group_and_achivement_rel(
            x.group,
            [
              Achivement.objects.get(code = 'Mqz_5'),
              Achivement.objects.get(code = 'Mqz_4'),
              Achivement.objects.get(code = 'Mqz_3'),
              Achivement.objects.get(code = 'Mqz_2'),
              Achivement.objects.get(code = 'Mqz_1')
            ]
          )
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Mqz_5'),
            0
          )
        elif tmp >= 120:
          delete_masir_group_and_achivement_rel(
            x.group,
            [
              Achivement.objects.get(code = 'Mqz_5'),
              Achivement.objects.get(code = 'Mqz_4'),
              Achivement.objects.get(code = 'Mqz_3'),
              Achivement.objects.get(code = 'Mqz_2'),
              Achivement.objects.get(code = 'Mqz_1')
            ]
          )
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Mqz_4'),
            0
          )
        elif tmp >= 80:
          delete_masir_group_and_achivement_rel(
            x.group,
            [
              Achivement.objects.get(code = 'Mqz_5'),
              Achivement.objects.get(code = 'Mqz_4'),
              Achivement.objects.get(code = 'Mqz_3'),
              Achivement.objects.get(code = 'Mqz_2'),
              Achivement.objects.get(code = 'Mqz_1')
            ]
          )
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Mqz_3'),
            0
          )
        elif tmp >= 40:
          delete_masir_group_and_achivement_rel(
            x.group,
            [
              Achivement.objects.get(code = 'Mqz_5'),
              Achivement.objects.get(code = 'Mqz_4'),
              Achivement.objects.get(code = 'Mqz_3'),
              Achivement.objects.get(code = 'Mqz_2'),
              Achivement.objects.get(code = 'Mqz_1')
            ]
          )
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Mqz_2'),
            0
          )
        elif tmp > 0:
          delete_masir_group_and_achivement_rel(
            x.group,
            [
              Achivement.objects.get(code = 'Mqz_5'),
              Achivement.objects.get(code = 'Mqz_4'),
              Achivement.objects.get(code = 'Mqz_3'),
              Achivement.objects.get(code = 'Mqz_2'),
              Achivement.objects.get(code = 'Mqz_1')
            ]
          )
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Mqz_1'),
            0
          )
        
        if len(x.group.exams.filter(show_public = True)) >= 1:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Uni_1'),
            5
          )
        if len(x.group.exams.filter(show_public = True)) >= 5:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Uni_5'),
            10
          )
        if len(x.group.exams.filter(show_public = True)) >= 10:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Uni_10'),
            15
          )
        if len(x.group.exams.filter(show_public = True)) >= 15:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Uni_15'),
            20
          )
        if len(x.group.exams.filter(show_public = True)) >= 19:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Uni_20'),
            25
          )
        
        tmp = 0
        for e in x.group.exams.filter(show_public = True):
          tmp = tmp + e.score
        if tmp >= 200:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Kml_0'),
            50
          )

        Report.objects.create(
          group = x.group,
          text = 'نتایج آزمون ' + str(x.exam.title) + ' منتشر شد و گروه شما در این آزمون ' + str(x.score) + ' پاسخ درست ثبت کرد.'
        )

      return(redirect('home_page_link'))

    if 'club_show_scores_admin_form' in request.POST:
      for x in Club_File.objects.filter(show_public = False, verified = True):
        x.show_public = True
        x.save()

        tmp = 0
        for u in x.user.groups.all().first().users.all():
          tmp = tmp + len(u.club_files.filter(show_public = True))
        if tmp >= 24:
          delete_masir_group_and_achivement_rel(
            x.user.groups.all().first(),
            [
              Achivement.objects.get(code = 'Qra_5'),
              Achivement.objects.get(code = 'Qra_4'),
              Achivement.objects.get(code = 'Qra_3'),
              Achivement.objects.get(code = 'Qra_2'),
              Achivement.objects.get(code = 'Qra_1')
            ]
          )
          set_masir_group_and_achivement_rel(
            x.user.groups.all().first(),
            Achivement.objects.get(code = 'Qra_5'),
            0
          )
        elif tmp >= 18:
          delete_masir_group_and_achivement_rel(
            x.user.groups.all().first(),
            [
              Achivement.objects.get(code = 'Qra_5'),
              Achivement.objects.get(code = 'Qra_4'),
              Achivement.objects.get(code = 'Qra_3'),
              Achivement.objects.get(code = 'Qra_2'),
              Achivement.objects.get(code = 'Qra_1')
            ]
          )
          set_masir_group_and_achivement_rel(
            x.user.groups.all().first(),
            Achivement.objects.get(code = 'Qra_4'),
            0
          )
        elif tmp >= 12:
          delete_masir_group_and_achivement_rel(
            x.user.groups.all().first(),
            [
              Achivement.objects.get(code = 'Qra_5'),
              Achivement.objects.get(code = 'Qra_4'),
              Achivement.objects.get(code = 'Qra_3'),
              Achivement.objects.get(code = 'Qra_2'),
              Achivement.objects.get(code = 'Qra_1')
            ]
          )
          set_masir_group_and_achivement_rel(
            x.user.groups.all().first(),
            Achivement.objects.get(code = 'Qra_3'),
            0
          )
        elif tmp >= 6:
          delete_masir_group_and_achivement_rel(
            x.user.groups.all().first(),
            [
              Achivement.objects.get(code = 'Qra_5'),
              Achivement.objects.get(code = 'Qra_4'),
              Achivement.objects.get(code = 'Qra_3'),
              Achivement.objects.get(code = 'Qra_2'),
              Achivement.objects.get(code = 'Qra_1')
            ]
          )
          set_masir_group_and_achivement_rel(
            x.user.groups.all().first(),
            Achivement.objects.get(code = 'Qra_2'),
            0
          )
        elif tmp > 0:
          delete_masir_group_and_achivement_rel(
            x.user.groups.all().first(),
            [
              Achivement.objects.get(code = 'Qra_5'),
              Achivement.objects.get(code = 'Qra_4'),
              Achivement.objects.get(code = 'Qra_3'),
              Achivement.objects.get(code = 'Qra_2'),
              Achivement.objects.get(code = 'Qra_1')
            ]
          )
          set_masir_group_and_achivement_rel(
            x.user.groups.all().first(),
            Achivement.objects.get(code = 'Qra_1'),
            0
          )
        if len(Club_File.objects.filter(show_public = True, user__in = x.user.groups.all().first().users.all()).values('level').annotate(count=Count('id', distinct=True))) >= 19 or len(Club_File.objects.filter(show_public = True, user__in = x.user.groups.all().first().users.all()).values('date__day').annotate(count=Count('id', distinct=True))) >= 19:
          set_masir_group_and_achivement_rel(
            x.user.groups.all().first(),
            Achivement.objects.get(code = 'Vrz_0'),
            30
          )
        
          
        Report.objects.create(
          group = x.user.groups.all().first(),
          text = 'فایل ارسال شده از طرف ' + str(x.user) + ' با عنوان «' + str(x.title) + '» تایید شد.'
        )

      return(redirect('home_page_link'))

    if 'activities_show_scores_admin_form' in request.POST:
      for x in Activity.objects.filter(state = '3'):
        x.state = '4'
        x.save()

        set_masir_group_and_achivement_rel(
          x.group,
          Achivement.objects.get(code = ACTIVITIES[x.topic.title] + '_' + str(int(x.template.type)) + str(round(x.get_score()))),
          (4 - int(x.template.type)) * x.get_score()
        )

        if len(x.group.activities.filter(state = '4')) >= 1:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Flg_1'),
            5
          )
        if len(x.group.activities.filter(state = '4')) >= 5:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Flg_5'),
            15
          )
        if len(x.group.activities.filter(state = '4')) >= 10:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Flg_10'),
            20
          )
        if len(x.group.activities.filter(state = '4')) >= 15:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Flg_15'),
            25
          )
        if len(x.group.activities.filter(state = '4')) >= 20:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Flg_20'),
            30
          )
        if len(x.group.activities.filter(state = '4')) >= 21:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Sun_0'),
            70
          )

        if len(x.group.activities.filter(state = '4').values('template').annotate(count=Count('id', distinct=True))) >= 20:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Tla_20'),
            20
          )
        elif len(x.group.activities.filter(state = '4').values('template').annotate(count=Count('id', distinct=True))) >= 15:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Tla_15'),
            15
          )
        elif len(x.group.activities.filter(state = '4').values('template').annotate(count=Count('id', distinct=True))) >= 10:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Tla_10'),
            10
          )
        elif len(x.group.activities.filter(state = '4').values('template').annotate(count=Count('id', distinct=True))) >= 5:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Tla_5'),
            5
          )

        tmp = 0
        for a in x.group.activities.filter(state = '4'):
          if a.get_score() >= 4.5:
            tmp = tmp + 1
        if tmp >= 7:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Nqs_20'),
            50
          )
        if tmp >= 5:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Nqs_15'),
            40
          )
        if tmp >= 3:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Nqs_10'),
            30
          )
        if tmp >= 1:
          set_masir_group_and_achivement_rel(
            x.group,
            Achivement.objects.get(code = 'Nqs_5'),
            20
          )

        Report.objects.create(
          group = x.group,
          text = 'فعالیت ' + str(x.topic) + ' داوری شد.'
        )
      
      for x in Activity.objects.filter(state = '5'):
        x.state = '6'
        x.save()

        Report.objects.create(
          group = x.group,
          text = 'فعالیت ' + str(x.topic) + ' در داوری رد شد.'
        )
      
      return(redirect('home_page_link'))

    if 'achivements_recalculate_admin_form' in request.POST:
      for x in Masir_Group.objects.all():
        x.recalculate_achivements()
      
      return(redirect('home_page_link'))

  if user.accessibility != Accessibility.objects.get(title = 'دسترسی دانش‌آموزی'):
    user_is_admin = False
    if user.accessibility == Accessibility.objects.get(title = 'دسترسی کامل'):
      user_is_admin = True
    
    SGT = [{'title': str(x), 'light': x.get_light(), 'users': x.users.all()} for x in Masir_Group.objects.all()]
    SGT.sort(key=lambda x: x.get('light'), reverse=True)
    

    return(
      render(
        request,
        'home_page_admin.html',
        {
          'user_is_admin': user_is_admin,
          'groups': SGT
        }
      )
    )

  return(
    render(
      request,
      'home_page.html',
      {
        'manazel': Manzel.objects.filter(id__lte = user.groups.all().first().manzel).order_by('right'),
        'announcements': Announcement.objects.filter(is_active = True).order_by('-id'),
        'reports': Report.objects.filter(group = user.groups.all().first()).order_by('-id'),
        'FAQ': FAQ.objects.filter(is_active = True),
        'achivements': Achivement.objects.filter(manzel = None),
        'templates': Activity_Template.objects.all(),
        'exam': Exam.objects.filter(active = True).first()
      }
    )
  )

def contact_admin_page(request):
  user = select_user(request.user)
  if not user:
    return(redirect('landing_page_link'))
  
  if user.accessibility != Accessibility.objects.get(title = 'دسترسی دانش‌آموزی'):
    if not user.accessibility.contact_admin_page:
      return(redirect('home_page_link'))
    return(
      render(
        request,
        'contact_admin_page_admin.html',
        {
          'messages': Message.objects.all().order_by('-id')
        }
      )
    )
  
  if not user.groups.all().first():
    return(
      render(
        request,
        'landing_page.html',
        {
          'MESSAGE': str(user)
                    + ' عزیز! مسابقه شروع شده است و ثبت نام شما با موفقیت انجام شده است ولی شما هنوز تیم ندارید. کد شما عبارت است از:'
                    + '<br>' + str(user.code) + '<br>'
                    + 'برای تشکیل تیم و شروع مسابقه به این کد نیاز خواهید داشت.'
                    + '<br> <br>' + 'چند نکته بسیار مهم:'
                    + '<ul>'
                    + '<li>' + 'برای شرکت در مسابقه حتما لازم است گروه‌های خود را در سایت ثبت کنید (یکی از افراد گروه، با در دست داشتن کد اعضای دیگر، وارد سایت شده و در بخش ثبت نام گروهی اقدام می کند).' + '</li>'
                    + '<li>' + 'مسابقه از هفته دوم ماه مبارک رمضان آغاز شده است.' + '</li>'
                    + '<li>' + 'حتما و حتما در یکی از کانالهای مسابقه عضو شوید تا اطلاعیه‌های بعدی را دریافت نمایید.' + '</li>'
                    + '</ul>',
          'cities': City.objects.all().order_by('name'),
          'schools': School.objects.all().order_by('name'),
          'announcements': Announcement.objects.filter(is_public = True)
        }
      )
    )
  
  if request.method == 'POST':
    if 'message_form' in request.POST:
      Message.objects.create(
        name = request.POST['contact_us_name'],
        phone = request.POST['contact_us_phone'],
        message = request.POST['contact_us_message']
      )

      return(redirect('contact_admin_page_link'))

  return(
    render(
      request,
      'contact_admin_page.html',
      {
        'messages': Message.objects.filter(phone = user.user.username).order_by('-id')
      }
    )
  )

def contact_admin_detail_page(request, id):
  user = select_user(request.user)
  if not user:
    return(redirect('landing_page_link'))
  if user.accessibility == Accessibility.objects.get(title = 'دسترسی دانش‌آموزی'):
    return(redirect('landing_page_link'))
  if not user.accessibility.contact_admin_page_edit:
    return(redirect('contact_admin_page_link'))
  
  the_message = Message.objects.filter(id = id).first()
  if not the_message:
    return(redirect('contact_admin_page_link'))
  
  if request.method == 'POST':
    if 'message_admin_form' in request.POST:
      the_message.answer = request.POST['message_admin_answer']
      the_message.save()

      return(redirect('contact_admin_page_link'))

  return(
    render(
      request,
      'contact_admin_page_admin.html',
      {
        'the_message': the_message,
        'messages': Message.objects.filter(phone = the_message.phone).exclude(id = the_message.id).order_by('-id')
      }
    )
  )

def club_page(request):
  user = select_user(request.user)
  if not user:
    return(redirect('landing_page_link'))
  if user.accessibility == Accessibility.objects.get(title = 'دسترسی دانش‌آموزی'):
    return(redirect('home_page_link'))
  if not user.accessibility.club_page:
    return(redirect('home_page_link'))
    
  return(
    render(
      request,
      'club_page_admin.html',
      {
        'club_files': Club_File.objects.all().order_by('verified','-id')
      }
    )
  )

def club_detail_page(request, id):
  user = select_user(request.user)
  if not user:
    return(redirect('landing_page_link'))
  if user.accessibility == Accessibility.objects.get(title = 'دسترسی دانش‌آموزی'):
    return(redirect('landing_page_link'))
  if not user.accessibility.club_page_edit:
    return(redirect('club_page_link'))
  
  the_file = Club_File.objects.filter(id = id).first()
  if not the_file:
    return(redirect('club_page_link'))
  
  if request.method == 'POST':
    if 'club_admin_form' in request.POST and not the_file.verified:
      the_file.verified = True
      the_file.save()

      u = the_file.user
      u.club_level = the_file.level + 1
      u.save()

    return(redirect('club_page_link'))

  return(
    render(
      request,
      'club_page_admin.html',
      {
        'the_file': the_file,
        'club_files': Club_File.objects.filter(user = the_file.user).exclude(id = the_file.id).order_by('-id')
      }
    )
  )

def judge_page(request):
  user = select_user(request.user)
  if not user:
    return(redirect('landing_page_link'))
  if user.accessibility == Accessibility.objects.get(title = 'دسترسی دانش‌آموزی'):
    return(redirect('home_page_link'))
  if not user.accessibility.judge_page:
    return(redirect('home_page_link'))
    
  user_is_admin = False
  if user.accessibility == Accessibility.objects.get(title = 'دسترسی کامل'):
    user_is_admin = True

  return(
    render(
      request,
      'judge_page_admin.html',
      {
        'activities': Activity.objects.filter(state = '1').order_by('-id'),
        'user_is_admin': user_is_admin,
        'activities_for_admin': Activity.objects.exclude(state = '1').order_by('state', '-id'),
      }
    )
  )

def judge_detail_page(request, id):
  user = select_user(request.user)
  if not user:
    return(redirect('landing_page_link'))
  if user.accessibility == Accessibility.objects.get(title = 'دسترسی دانش‌آموزی'):
    return(redirect('landing_page_link'))
  if not user.accessibility.judge_page_edit:
    return(redirect('judge_page_link'))
  
  the_file = Activity.objects.filter(id = id).first()
  if not the_file:
    return(redirect('judge_page_link'))
  
  the_file.state = '2'
  the_file.save()

  if request.method == 'POST':
    if 'judge_admin_form' in request.POST:
      the_file.referee = user

      the_file.score1 = int(request.POST['judge_admin_score1'])
      the_file.score2 = int(request.POST['judge_admin_score2'])
      the_file.score3 = int(request.POST['judge_admin_score3'])
      the_file.score4 = int(request.POST['judge_admin_score4'])
      the_file.score5 = int(request.POST['judge_admin_score5'])
      the_file.score6 = int(request.POST['judge_admin_score6'])

      the_file.state = '3'
      the_file.save()
    
    if 'judge_admin_deny_form' in request.POST:
      the_file.referee = user

      the_file.comment = request.POST['judge_admin_denied_message']

      the_file.state = '5'
      the_file.save()
    
    if 'judge_admin_cancel_form' in request.POST:
      the_file.state = '1'
      the_file.save()

    return(redirect('judge_page_link'))

  return(
    render(
      request,
      'judge_page_admin.html',
      {
        'the_file': the_file,
        'activities': None
      }
    )
  )

def statistics_page(request):
  user = select_user(request.user)
  if not user:
    return(redirect('landing_page_link'))
  if user.accessibility == Accessibility.objects.get(title = 'دسترسی دانش‌آموزی'):
    return(redirect('home_page_link'))
  if not user.accessibility.statistics_page:
    return(redirect('home_page_link'))
    
  groups_all = [len(Masir_Group.objects.all()), 0, 0]
  charities_all = [0, len(Charity.objects.all().values('group').annotate(count=Count('id', distinct=True)))]
  for x in Charity.objects.all():
    charities_all[0] = charities_all[0] + x.value
  exams_all = [len(Masir_Group_And_Exams_Rel.objects.all()), len(Masir_Group_And_Exams_Rel.objects.all().values('group').annotate(count=Count('id', distinct=True)))]
  club_files_all = [len(Club_File.objects.all()), len(Club_File.objects.all().values('user').annotate(count=Count('id', distinct=True)))]
  activitiy_templates_all = []
  for x in Activity_Template.objects.all():
    activitiy_templates_all.append({'template': x, 'count': len(x.activities.all())})
  activitiy_templates_all.sort(key=lambda x: x.get('count'), reverse=True)
  activitiy_templates_all = Activity.objects.all().values('template__title').annotate(count=Count('id', distinct=True)).order_by('count')
  for x in Masir_Group.objects.all():
    if x.get_light() > 64:
      groups_all[1] = groups_all[1] + 1
    if x.activities.all().first():
      groups_all[2] = groups_all[2] + 1
  
  votes = {
    'all': len(Vote.objects.all()),
    'all_valid': len(Vote.objects.filter(is_valid = True)),
    'image_1': [len(Vote.objects.filter(is_valid = True, vote_image_1 = True)), 50],
    'image_2': [len(Vote.objects.filter(is_valid = True, vote_image_2 = True)), 40],
    'image_3': [len(Vote.objects.filter(is_valid = True, vote_image_3 = True)), 10],
    'image_4': [len(Vote.objects.filter(is_valid = True, vote_image_4 = True)), 90],
    'image_5': [len(Vote.objects.filter(is_valid = True, vote_image_5 = True)), 30],
    'music_1': [len(Vote.objects.filter(is_valid = True, vote_music_1 = True)), 50],
    'music_2': [len(Vote.objects.filter(is_valid = True, vote_music_2 = True)), 50],
    'music_3': [len(Vote.objects.filter(is_valid = True, vote_music_3 = True)), 50],
    'music_4': [len(Vote.objects.filter(is_valid = True, vote_music_4 = True)), 50],
    'music_5': [len(Vote.objects.filter(is_valid = True, vote_music_5 = True)), 50],
    'video_1': [len(Vote.objects.filter(is_valid = True, vote_video_1 = True)), 50],
    'video_2': [len(Vote.objects.filter(is_valid = True, vote_video_2 = True)), 50],
    'video_3': [len(Vote.objects.filter(is_valid = True, vote_video_3 = True)), 50],
    'video_4': [len(Vote.objects.filter(is_valid = True, vote_video_4 = True)), 50],
    'video_5': [len(Vote.objects.filter(is_valid = True, vote_video_5 = True)), 50]
  }
  for x in votes:
    try:
      votes[x][1] = (votes[x][0] / votes['all_valid']) * 100
    except:
      pass

  return(
    render(
      request,
      'statistics_page_admin.html',
      {
        'votes': votes,
        'groups_all': groups_all,
        'charities_all': charities_all,
        'exams_all': exams_all,
        'club_files_all': club_files_all,
        'activitiy_templates_all': activitiy_templates_all,
        'groups': Masir_Group.objects.all().order_by('supergroup')
      }
    )
  )

def help_page(request):
  
  return(
    render(
      request,
      'help_page.html',
      {
      }
    )
  )