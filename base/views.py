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
    if not group.achivements.filter(group=group, achivement=achivement).first():
        Masir_Group_And_Achivement_Rel.objects.create(
            group=group,
            achivement=achivement,
            score=score
        )


def delete_masir_group_and_achivement_rel(group, achivements):
    for x in achivements:
        if Masir_Group_And_Achivement_Rel.objects.filter(group=group, achivement=x).first():
            Masir_Group_And_Achivement_Rel.objects.filter(group=group, achivement=x).first().delete()


def select_user(username):
    user = User.objects.filter(username=username).first()
    if not user:
        return (None)
    return (user.user_detail)


def get_message_public(name, phone, message):
    return (None)


def get_city(name):
    if City.objects.filter(name=name).first():
        return (City.objects.filter(name=name).first())
    return (
        City.objects.create(
            name=name
        )
    )


def get_school(name):
    if School.objects.filter(name=name).first():
        return (School.objects.filter(name=name).first())
    return (
        School.objects.create(
            name=name
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
    if request.method == 'POST':
        if 'message_form' in request.POST:
            Message.objects.create(
                name=request.POST['contact_us_name'],
                phone=request.POST['contact_us_phone'],
                message=request.POST['contact_us_message']
            )
            return (
                render(
                    request,
                    'landing_page.html',
                    {
                        'MESSAGE': 'پیام شما با موفقیت ثبت شد.',
                        'cities': City.objects.all().order_by('name'),
                        'schools': School.objects.all().order_by('name'),
                        'announcements': Announcement.objects.filter(is_public=True)
                    }
                )
            )
        if 'login_form' in request.POST:
            user = authenticate(
                username=request.POST['login_phone'],
                password=request.POST['login_password']
            )
            if user and user.is_active:
                login(request, user)
                if user.user_detail.groups.all().first() or user.user_detail.accessibility != Accessibility.objects.get(
                        title='دسترسی دانش‌آموزی'):
                    return (redirect('home_page_link'))
                return (
                    render(
                        request,
                        'landing_page.html',
                        {
                            'MESSAGE': str(user.user_detail)
                                       + ' عزیز! ثبت نام شما با موفقیت انجام شد.'
                                       + ' کد ورود شما:'
                                       + '<br>' + str(user.user_detail.code) + '<br>'
                                       + 'برای تشکیل تیم و شروع مسابقه به این کد نیاز خواهید داشت.'
                                       + '<br> <br>' + 'چند نکته بسیار مهم:'
                                       + '<ul>'
                                       + '<li>' + 'ثبت نام گروهی از دهه دوم ماه مبارک رمضان آعاز خواهد شد.' + '</li>'
                                       + '<li>' + 'مسابقه گروهی است و بصورت فردی نمی‌توانید در آن شرکت کنید.' + '</li>'
                                       + '<li>' + 'برای ساخت گروه باید یکی از افراد با داشتن کد اعضای دیگر، از بخش ثبت نام گروهی اقدام نماید.' + '</li>'
                                       + '<li>' + 'مسابقه از <u>نیمه دوم ماه مبارک رمضان</u> آغاز می‌شود.' + '</li>'
                                       + '<li>' + 'حتما و حتما در یکی از <a href="https://zil.ink/masir1402">کانالهای مسابقه </a> عضو شوید تا اطلاعیه‌های بعدی را دریافت نمایید.' + '</li>'
                                       + '</ul>',
                            'cities': City.objects.all().order_by('name'),
                            'schools': School.objects.all().order_by('name'),
                            'announcements': Announcement.objects.filter(is_public=True)
                        }
                    )
                )
            return (
                render(
                    request,
                    'landing_page.html',
                    {
                        'MESSAGE': 'شماره تلفن یا رمز عبور اشتباه وارد شده است.',
                        'cities': City.objects.all().order_by('name'),
                        'schools': School.objects.all().order_by('name'),
                        'announcements': Announcement.objects.filter(is_public=True)
                    }
                )
            )
        if 'register_form' in request.POST:
            user = User.objects.filter(username=request.POST['register_phone']).first()
            if user:
                if user.is_active:
                    return (
                        render(
                            request,
                            'landing_page.html',
                            {
                                'MESSAGE': 'شماره تلفن ' + request.POST['register_phone'] + ' قبلا ثبت شده است.',
                                'cities': City.objects.all().order_by('name'),
                                'schools': School.objects.all().order_by('name'),
                                'announcements': Announcement.objects.filter(is_public=True)
                            }
                        )
                    )
                user.delete()

            if User.objects.filter(user_detail__nationalcode=request.POST['register_nationalcode']).first():
                return (
                    render(
                        request,
                        'landing_page.html',
                        {
                            'MESSAGE': 'کد ملی ' + request.POST['register_nationalcode'] + ' قبلا ثبت شده است.',
                            'cities': City.objects.all().order_by('name'),
                            'schools': School.objects.all().order_by('name'),
                            'announcements': Announcement.objects.filter(is_public=True)
                        }
                    )
                )

            user = User.objects.create_user(
                first_name=request.POST['register_firstname'],
                last_name=request.POST['register_lastname'],
                username=request.POST['register_phone'],
                password=request.POST['register_password']
            )
            user.is_active = False
            user.save()

            User_Detail.objects.create(
                user=user,
                accessibility=Accessibility.objects.get(title='دسترسی دانش‌آموزی'),
                nationalcode=request.POST['register_nationalcode'],
                level=int(request.POST['register_level']),
                city=get_city(request.POST['register_city']),
                school=get_school(request.POST['register_school']),
                code=str(randint(10000, 100000))
            )

            SMS(UserApiKey, SecretKey, user.user_detail.code, '0' + user.username)

            return (
                render(
                    request,
                    'verification_page.html',
                    {
                        'phone': user.username
                    }
                )
            )
        if 'verification_form' in request.POST:
            user = User.objects.filter(username=request.POST['verification_phone']).first()
            if user and user.user_detail.code == request.POST['verification_code']:
                user.is_active = True
                user.save()
                return (
                    render(
                        request,
                        'landing_page.html',
                        {
                            'MESSAGE': str(user.user_detail)
                                       + ' عزیز! ثبت نام شما با موفقیت انجام شد.'
                                       + ' کد ورود شما:'
                                       + '<br>' + str(user.user_detail.code) + '<br>'
                                       + 'برای تشکیل تیم و شروع مسابقه به این کد نیاز خواهید داشت.'
                                       + '<br> <br>' + 'چند نکته بسیار مهم:'
                                       + '<ul>'
                                       + '<li>' + 'ثبت نام گروهی از دهه دوم ماه مبارک رمضان آعاز خواهد شد.' + '</li>'
                                       + '<li>' + 'مسابقه گروهی است و بصورت فردی نمی‌توانید در آن شرکت کنید.' + '</li>'
                                       + '<li>' + 'برای ساخت گروه باید یکی از افراد با داشتن کد اعضای دیگر، از بخش ثبت نام گروهی اقدام نماید.' + '</li>'
                                       + '<li>' + 'مسابقه از <u>نیمه دوم ماه مبارک رمضان</u> آغاز می‌شود.' + '</li>'
                                       + '<li>' + 'حتما و حتما در یکی از <a href="https://zil.ink/masir1402">کانالهای مسابقه </a> عضو شوید تا اطلاعیه‌های بعدی را دریافت نمایید.' + '</li>'
                                       + '</ul>',
                            'cities': City.objects.all().order_by('name'),
                            'schools': School.objects.all().order_by('name'),
                            'announcements': Announcement.objects.filter(is_public=True)
                        }
                    )
                )
            return (
                render(
                    request,
                    'landing_page.html',
                    {
                        'MESSAGE': 'کد وارد شده صحیح نیست!',
                        'cities': City.objects.all().order_by('name'),
                        'schools': School.objects.all().order_by('name'),
                        'announcements': Announcement.objects.filter(is_public=True)
                    }
                )
            )
        if 'group_register_form' in request.POST:
            user1 = User_Detail.objects.filter(user__username=request.POST['group_register_phone_1'],
                                               code=request.POST['group_register_code_1']).first()
            user2 = User_Detail.objects.filter(user__username=request.POST['group_register_phone_2'],
                                               code=request.POST['group_register_code_2']).first()
            user3 = User_Detail.objects.filter(user__username=request.POST['group_register_phone_3'],
                                               code=request.POST['group_register_code_3']).first()

            if user1 and user2 and user3 and user1 != user2 and user2 != user3 and user3 != user1:
                if not user1.groups.all() and not user2.groups.all() and not user3.groups.all():
                    g = Masir_Group.objects.create(
                        title=request.POST['group_register_title']
                    )
                    g.users.add(user1)
                    g.users.add(user2)
                    g.users.add(user3)
                    g.add_mains()
                    g.goto_supergroup()
                    g.save()

                    Report.objects.create(
                        group=g,
                        text='گروه شما با عنوان «' + str(g.title) + '» ثبت شد.'
                    )

                    return (
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
                                           + g.get_users()
                                           + '<br> <br>'
                                           + 'چند نکته مهم:'
                                           + '<ul>'
                                           + '<li>' + 'مسابقه از نیمه دوم ماه مبارک رمضان آغاز خواهد شد.' + '</li>'
                                           + '<li>' + 'حتما و حتما در یکی از کانالهای مسابقه عضو شوید تا اطلاعیه‌های بعدی را دریافت نمایید.' + '</li>'
                                           + '<li>' + "<a data-bs-toggle='modal' href='#login_modal' role='button' > ورود </a>" + '</li>'
                                           + '</ul>',
                                'cities': City.objects.all().order_by('name'),
                                'schools': School.objects.all().order_by('name'),
                                'announcements': Announcement.objects.filter(is_public=True)
                            }
                        )
                    )
                return (
                    render(
                        request,
                        'landing_page.html',
                        {
                            'MESSAGE': 'اعضای گروه نباید در گروه دیگری عضو باشند.'
                                       + '<br>'
                                       + 'اگر از صحت اطلاعات خود مطمئن هستید اقدام به '
                                       + "<a data-bs-toggle='modal' href='#login_modal' role='button' > ورود </a>"
                                       + 'کنید.',

                            'cities': City.objects.all().order_by('name'),
                            'schools': School.objects.all().order_by('name'),
                            'announcements': Announcement.objects.filter(is_public=True)
                        }
                    )
                )
            return (
                render(
                    request,
                    'landing_page.html',
                    {
                        'MESSAGE': 'اطلاعات وارد شده صحیح نیست.',
                        'cities': City.objects.all().order_by('name'),
                        'schools': School.objects.all().order_by('name'),
                        'announcements': Announcement.objects.filter(is_public=True)
                    }
                )
            )

    user = select_user(request.user)
    if user:
        if user.groups.all().first() or user.accessibility != Accessibility.objects.get(title='دسترسی دانش‌آموزی'):
            return (redirect('home_page_link'))
        return (
            render(
                request,
                'landing_page.html',
                {
                    'MESSAGE': str(user.user_detail)
                               + ' عزیز! ثبت نام شما با موفقیت انجام شد.'
                               + ' کد ورود شما:'
                               + '<br>' + str(user.user_detail.code) + '<br>'
                               + 'برای تشکیل تیم و شروع مسابقه به این کد نیاز خواهید داشت.'
                               + '<br> <br>' + 'چند نکته بسیار مهم:'
                               + '<ul>'
                               + '<li>' + 'ثبت نام گروهی از دهه دوم ماه مبارک رمضان آعاز خواهد شد.' + '</li>'
                               + '<li>' + 'مسابقه گروهی است و بصورت فردی نمی‌توانید در آن شرکت کنید.' + '</li>'
                               + '<li>' + 'برای ساخت گروه باید یکی از افراد با داشتن کد اعضای دیگر، از بخش ثبت نام گروهی اقدام نماید.' + '</li>'
                               + '<li>' + 'مسابقه از <u>نیمه دوم ماه مبارک رمضان</u> آغاز می‌شود.' + '</li>'
                               + '<li>' + 'حتما و حتما در یکی از <a href="https://zil.ink/masir1402">کانالهای مسابقه </a> عضو شوید تا اطلاعیه‌های بعدی را دریافت نمایید.' + '</li>'
                               + '</ul>',
                    'cities': City.objects.all().order_by('name'),
                    'schools': School.objects.all().order_by('name'),
                    'announcements': Announcement.objects.filter(is_public=True)
                }
            )
        )

    return (
        render(
            request,
            'landing_page.html',
            {
                'MESSAGE': None,
                'cities': City.objects.all().order_by('name'),
                'schools': School.objects.all().order_by('name'),
                'announcements': Announcement.objects.filter(is_public=True)
            }
        )
    )


# def full_map_page(request):
#   return(
#     render(
#       request,
#       'full_map_page.html',
#       {
#         'MESSAGE': 'صفحه نهایی بازی برای یک گروه فرضی!',
#         'manazel': Manzel.objects.all().order_by('right')[0:7],
#         'manzel_achievements': Achivement.objects.exclude(manzel = None).order_by('manzel__id'),
#         'none_manzel_achievements': Achivement.objects.filter(manzel = None),
#         'exam': Exam.objects.all().last(),
#         'announcements': Announcement.objects.filter(is_public = True),
#         'FAQ': FAQ.objects.filter(is_active = True)
#       }
#     )
#   )

def people_judge_page(request):
    user = select_user(request.user)
    topworks = [list(Top_Work.objects.filter(type='1')),
                list(Top_Work.objects.filter(type='2')),
                list(Top_Work.objects.filter(type='3'))]
    if request.method == 'POST':
        # if 'people_judge_form' in request.POST:
        #
        #     try:
        #         if request.POST['people_judge_image_1'] == 'on':
        #             v.vote_image_1 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_image_2'] == 'on':
        #             v.vote_image_2 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_image_3'] == 'on':
        #             v.vote_image_3 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_image_4'] == 'on':
        #             v.vote_image_4 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_image_5'] == 'on':
        #             v.vote_image_5 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_music_1'] == 'on':
        #             v.vote_music_1 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_music_2'] == 'on':
        #             v.vote_music_2 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_music_3'] == 'on':
        #             v.vote_music_3 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_music_4'] == 'on':
        #             v.vote_music_4 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_music_5'] == 'on':
        #             v.vote_music_5 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_video_1'] == 'on':
        #             v.vote_video_1 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_video_2'] == 'on':
        #             v.vote_video_2 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_video_3'] == 'on':
        #             v.vote_video_3 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_video_4'] == 'on':
        #             v.vote_video_4 = True
        #             v.save()
        #     except:
        #         pass
        #     try:
        #         if request.POST['people_judge_video_5'] == 'on':
        #             v.vote_video_5 = True
        #             v.save()
        #     except:
        #         pass
        #
        #
        #     return (
        #         render(
        #             request,
        #             'verification_page.html',
        #             {
        #                 'phone': v.phone
        #             }
        #         )
        #     )

        if 'send_phone_vote_form' in request.POST:
            if Vote.objects.filter(phone__contains=request.POST['phone_vote'], is_voted=True).first():
                return (
                    render(
                        request,
                        'people_judge_page.html',
                        {
                            'MESSAGE': 'شماره ' + request.POST['phone_vote'] + ' قبلا در نظرسنجی شرکت کرده است.',
                            'phone': str(request.POST['phone_vote']),
                            'voted': True,
                            'verified': True,
                            'topworks': topworks
                        }
                    )
                )
            if Vote.objects.filter(phone__contains=request.POST['phone_vote'], is_valid=True).first():
                v = Vote.objects.filter(phone__contains=request.POST['phone_vote'], is_valid=True).first()
                if v.vote.all():
                    for x in v.vote.all():
                        v.vote.remove(x)
                        v.save()
                return (
                    render(
                        request,
                        'people_judge_page.html',
                        {
                            'phone': v.phone,
                            'verified': True,
                            'voted': False,
                            'topworks': topworks
                        }
                    )
                )
            if Vote.objects.filter(phone__contains=request.POST['phone_vote'], is_valid=False).first():
                Vote.objects.filter(phone__contains=request.POST['phone_vote'], is_valid=False).delete()

            phone = int(str(request.POST['phone_vote'])),
            code = randint(10000, 100000)
            v = Vote.objects.create(
                phone=str(phone)[1:-2],
                code=code,
            )
            v.save()

            SMS(UserApiKey, SecretKey, code, '0' + request.POST['phone_vote'])
            return (
                render(
                    request,
                    'people_judge_page.html',
                    {
                        'phone': str(v.phone),
                        'verified': False,
                        'voted': False,
                        'topworks': topworks
                    }
                )
            )
        if 'send_code_vote_form' in request.POST:
            v = Vote.objects.filter(phone__contains=request.POST['phone_vote_code']).last()

            if str(v.code) == request.POST['code_vote']:
                v.is_valid = True
                v.save()

                return (
                    render(
                        request,
                        'people_judge_page.html',
                        {
                            'verified': True,
                            'voted': False,
                            'phone': str(v.phone),
                            'topworks': topworks
                        }
                    )
                )
            return (
                render(
                    request,
                    'people_judge_page.html',
                    {
                        'MESSAGE': 'کد وارد شده صحیح نمی‌باشد',
                        'verified': False,
                        'voted': False,
                        'phone': str(v.phone),
                        'topworks': topworks
                    }
                )
            )
        if 'public_vote_form' in request.POST:
            v = Vote.objects.filter(phone__contains=request.POST['phone_vote_final']).last()

            if v.is_valid:
                audio = request.POST['audio_vote']
                video = request.POST['video_vote']
                picture = request.POST['picture_vote']

                if audio == video == picture == 'None':
                    return (
                        render(
                            request,
                            'people_judge_page.html',
                            {
                                'MESSAGE': 'شما در هیچ بخشی رای ثبت شده ندارید. لطفا دوباره تلاش کنید.',
                                'verified': True,
                                'voted': False,
                                'phone': str(v.phone),
                                'topworks': topworks
                            }
                        )
                    )

                i = 1
                for x in str(audio):
                    if x == '1':
                        t = Top_Work.objects.get(number=int(i), type='1')
                        v.vote.add(t)
                    i += 1

                i = 1
                for x in str(video):
                    if x == '1':
                        t = Top_Work.objects.get(number=int(i), type='2')
                        v.vote.add(t)
                    i += 1

                i = 1
                for x in str(picture):
                    if x == '1':
                        t = Top_Work.objects.get(number=int(i), type='3')
                        v.vote.add(t)
                    i += 1

                v.is_voted = True
                v.save()
                link = "https://masir1402.ir/public_poll"
                text = '<a href = ' + link + '>' + 'بازگشت به صفحه نظرسنجی' + '</a>'
                return (
                    render(
                        request,
                        'landing_page.html',
                        {
                            'MESSAGE': 'نظر شما با موفقیت ثبت شد.'
                                       + '<br>' + text,
                            'announcements': Announcement.objects.filter(is_public=True),
                        }
                    )
                )

            return (
                render(
                    request,
                    'people_judge_page.html',
                    {
                        'MESSAGE': 'مشکلی در ثبت نظر شما پیش آمده است. مجددا تلاش کنید.',
                        'voted': False,
                        'verified': False,
                        'phone': str(v.phone),
                        'topworks': topworks
                    }
                )
            )

    if (type(user) == User and user.is_active) or (type(user) == User_Detail):
        phone = user.user
        code = user.code if type(user) == User_Detail else user.user_detail.code
        voted = False
        if not Vote.objects.filter(phone__contains=phone).first():
            Vote.objects.create(
                phone=phone,
                code=code,
                is_valid=True,
            )
        elif Vote.objects.filter(phone__contains=phone, is_voted=True):
            voted = True

        return (
            render(
                request,
                'people_judge_page.html',
                {
                    'voted': voted,
                    'verified': True,
                    'phone': phone,
                    'topworks': topworks
                }
            )
        )

    return (
        render(
            request,
            'people_judge_page.html',
            {
                'voted': False,
                'verified': False,
                'phone': None,
                'topworks': topworks
            }
        )
    )


def on_masir(request):
    return (
        render(
            request,
            'on_masir.html',
            {
            }
        )
    )


def forgot_password_page(request):
    if request.method == 'POST':
        if 'forgot_password_L1_form' in request.POST:
            user = User.objects.filter(username=request.POST['forgot_password_phone'],
                                       user_detail__nationalcode=request.POST['forgot_password_nationalcode']).first()
            if user:
                user = user.user_detail
                user.code = str(randint(10000, 100000))
                user.save()
                SMS(UserApiKey, SecretKey, user.code, '0' + request.POST['forgot_password_phone'])
                return (
                    render(
                        request,
                        'forgot_password_L2_page.html',
                        {
                            'the_user': user
                        }
                    )
                )
            return (
                render(
                    request,
                    'landing_page.html',
                    {
                        'MESSAGE': 'شماره تلفن یا کد ملی اشتباه وارد شده است.',
                        'cities': City.objects.all().order_by('name'),
                        'schools': School.objects.all().order_by('name'),
                        'announcements': Announcement.objects.filter(is_public=True)
                    }
                )
            )
        if 'forgot_password_L2_form' in request.POST:
            user = User.objects.filter(username=request.POST['forgot_password_phone']).first()
            if user and user.user_detail.code == request.POST['forgot_password_code']:
                user.set_password(request.POST['forgot_password_password'])
                user.save()
                return (
                    render(
                        request,
                        'landing_page.html',
                        {
                            'MESSAGE': 'رمز عبور با موفقیت تغییر کرد.',
                            'cities': City.objects.all().order_by('name'),
                            'schools': School.objects.all().order_by('name'),
                            'announcements': Announcement.objects.filter(is_public=True)
                        }
                    )
                )
            return (
                render(
                    request,
                    'landing_page.html',
                    {
                        'MESSAGE': 'کد وارد شده صحیح نیست.',
                        'cities': City.objects.all().order_by('name'),
                        'schools': School.objects.all().order_by('name'),
                        'announcements': Announcement.objects.filter(is_public=True)
                    }
                )
            )
    return (
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
        return (redirect('landing_page_link'))
    if not user.groups.all().first() and user.accessibility == Accessibility.objects.get(title='دسترسی دانش‌آموزی'):
        return (
            render(
                request,
                'landing_page.html',
                {
                    'MESSAGE': str(user)
                               + ' عزیز! ثبت نام شما با موفقیت انجام شد.'
                               + ' کد ورود شما:'
                               + '<br>' + str(user.code) + '<br>'
                               + 'برای تشکیل تیم و شروع مسابقه به این کد نیاز خواهید داشت.'
                               + '<br> <br>' + 'چند نکته بسیار مهم:'
                               + '<ul>'
                               + '<li>' + 'ثبت نام گروهی از دهه دوم ماه مبارک رمضان آعاز خواهد شد.' + '</li>'
                               + '<li>' + 'مسابقه گروهی است و بصورت فردی نمی‌توانید در آن شرکت کنید.' + '</li>'
                               + '<li>' + 'برای ساخت گروه باید یکی از افراد با داشتن کد اعضای دیگر، از بخش ثبت نام گروهی اقدام نماید.' + '</li>'
                               + '<li>' + 'مسابقه از <u>نیمه دوم ماه مبارک رمضان</u> آغاز می‌شود.' + '</li>'
                               + '<li>' + 'حتما و حتما در یکی از <a href="https://zil.ink/masir1402">کانالهای مسابقه </a> عضو شوید تا اطلاعیه‌های بعدی را دریافت نمایید.' + '</li>'
                               + '</ul>',
                    'cities': City.objects.all().order_by('name'),
                    'schools': School.objects.all().order_by('name'),
                    'announcements': Announcement.objects.filter(is_public=True)
                }
            )
        )

    if request.method == 'POST':
        # ثبت باشگاه
        if 'club_form' in request.POST:
            c = 0
            for u in user.groups.all().first().users.all():
                try:
                    if request.POST['club_file_' + str(u.id)] != '':
                        if u.club_level < 0:
                            return (
                                render(
                                    request,
                                    'home_page.html',
                                    {
                                        'manazel': Manzel.objects.filter(
                                            id__lte=user.groups.all().first().manzel).order_by('-id'),
                                        'announcements': Announcement.objects.filter(is_active=True).order_by('-id'),
                                        'reports': Report.objects.filter(group=user.groups.all().first()).order_by(
                                            '-id'),
                                        'FAQ': FAQ.objects.filter(is_active=True),
                                        'achivements': Achivement.objects.filter(
                                            manzel=None) | Achivement.objects.filter(code__contains='Mnz'),
                                        'exam': Exam.objects.filter(active=True).first(),
                                        'event': Event.objects.filter(active=True).first(),
                                        'MESSAGE': 'شما قبلا یک فایل در باشگاه ارسال کرده‌اید.'
                                    }
                                )
                            )

                        Report.objects.create(
                            group=user.groups.all().first(),
                            text='فایل «' + str(u.get_club_level()) + '» با موفقیت ارسال شد.'
                        )

                        Club_File.objects.create(
                            user=u,
                            link=request.POST['club_file_' + str(u.id)],
                            title=CLUB_LEVELS[u.club_level]['page'],
                            level=u.club_level
                        )

                        u.club_level = -1
                        u.save()
                    c = c + 1
                except:
                    pass
            return (redirect('home_page_link'))
        # ثبت صدقه
        if 'charity_form' in request.POST:
            if int(request.POST['charity_value']) > user.groups.all().first().get_food():
                return (
                    render(
                        request,
                        'home_page.html',
                        {
                            'manazel': Manzel.objects.filter(id__lte=user.groups.all().first().manzel).order_by(
                                '-id'),
                            'announcements': Announcement.objects.filter(is_active=True).order_by('-id'),
                            'reports': Report.objects.filter(group=user.groups.all().first()).order_by('-id'),
                            'FAQ': FAQ.objects.filter(is_active=True),
                            'achivements': Achivement.objects.filter(manzel=None) | Achivement.objects.filter(
                                code__contains='Mnz'),
                            'exam': Exam.objects.filter(active=True).first(),
                            'event': Event.objects.filter(active=True).first(),
                            'MESSAGE': 'میزان صدقه از میزان آذوقه گروه بیشتر است.'
                        }
                    )
                )
            Charity.objects.create(
                group=user.groups.all().first(),
                value=int(request.POST['charity_value'])
            )

            # دست رحمت
            user.groups.all().first().ach_sdq()

            Report.objects.create(
                group=user.groups.all().first(),
                text='صدقات شما به ارزش ' + request.POST['charity_value'] + ' واحد با موفقیت ثبت شد.'
            )

            return (redirect('home_page_link'))

        # ثبت دانشگاه
        if 'university_form' in request.POST:
            exam = Exam.objects.filter(active=True).first()
            if Masir_Group_And_Exams_Rel.objects.filter(group=user.groups.all().first(), exam=exam).first():
                return (
                    render(
                        request,
                        'home_page.html',
                        {
                            'manazel': Manzel.objects.filter(id__lte=user.groups.all().first().manzel).order_by(
                                '-id'),
                            'announcements': Announcement.objects.filter(is_active=True).order_by('-id'),
                            'reports': Report.objects.filter(group=user.groups.all().first()).order_by('-id'),
                            'FAQ': FAQ.objects.filter(is_active=True),
                            'achivements': Achivement.objects.filter(manzel=None) | Achivement.objects.filter(
                                code__contains='Mnz'),
                            'exam': Exam.objects.filter(active=True).first(),
                            'event': Event.objects.filter(active=True).first(),
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
                group=user.groups.all().first(),
                exam=exam,
                score=score,
                answers=answers
            )

            Report.objects.create(
                group=user.groups.all().first(),
                text='پاسخ‌های شما به آزمون' + str(exam) + ' با موفقیت ثبت شد.'
            )

            return (redirect('home_page_link'))

        if 'event_form' in request.POST:
            event = Event.objects.filter(active=True).first()
            if Masir_Group_And_Event_Rel.objects.filter(group=user.groups.all().first(), event=event).first():
                return (
                    render(
                        request,
                        'home_page.html',
                        {
                            'manazel': Manzel.objects.filter(id__lte=user.groups.all().first().manzel).order_by(
                                '-id'),
                            'announcements': Announcement.objects.filter(is_active=True).order_by('-id'),
                            'reports': Report.objects.filter(group=user.groups.all().first()).order_by('-id'),
                            'FAQ': FAQ.objects.filter(is_active=True),
                            'achivements': Achivement.objects.filter(manzel=None) | Achivement.objects.filter(
                                code__contains='Mnz'),
                            'exam': Exam.objects.filter(active=True).first(),
                            'event': Event.objects.filter(active=True).first(),
                            'MESSAGE': 'گروه شما قبلا یکبار در این فراخوان شرکت کرده است.'
                        }
                    )
                )
            score = 0
            answers = ''
            a = request.POST['Q']
            if event.A == int(a):
                score = 1
            answers = a

            Masir_Group_And_Event_Rel.objects.create(
                group=user.groups.all().first(),
                event=event,
                score=score,
                answers=answers
            )

            Report.objects.create(
                group=user.groups.all().first(),
                text='پاسخ‌های شما به فراخوان' + str(event) + ' با موفقیت ثبت شد.'
            )

            return redirect('home_page_link')

        # رفتن به منزل بعد
        if 'next_level_form' in request.POST:
            if user.groups.all().first().get_manzel().food_for_next_manzel and user.groups.all().first().get_manzel().power_for_next_manzel and user.groups.all().first().get_food() >= user.groups.all().first().get_manzel().food_for_next_manzel or user.groups.all().first().get_power() >= user.groups.all().first().get_manzel().power_for_next_manzel:
                trash = user.groups.all().first().get_food() - user.groups.all().first().get_manzel().food_for_next_manzel - user.groups.all().first().get_manzel().max_export_food
                text = 'شما با صرف ' + str(
                    user.groups.all().first().get_manzel().food_for_next_manzel) + ' واحد از آذوقه ی خود توانستید به منزل بعد بروید'
                if trash > 0:
                    Trash.objects.create(
                        group=user.groups.all().first(),
                        food=trash
                    )
                    text = text + '؛ ' + str(
                        float(round((trash * 100) / 100))) + ' واحد آذوقه اضافه را در مسیر حرکت از دست دادید'

                g = user.groups.all().first()

                # نشان منزل

                g.ach_manzel(g.manzel)

                g.manzel = g.manzel + 1
                g.save()

                g.ach_last()

                text = text + ' و با ' + str(g.get_food()) + ' آذوقه به منزل بعد رسیدید.'

                Report.objects.create(
                    group=user.groups.all().first(),
                    text=text
                )
                if user.groups.all().first().has_unjudged_activity():
                    for x in user.groups.all().first().activities.exclude(state='4').exclude(state='6').all():
                        x.cheated = True
                        x.save()

                return (redirect('home_page_link'))

        # اکتشاف
        if 'discover_form' in request.POST:
            for x in user.groups.all().first().get_manzel().activity_topics.all():
                if request.POST['discover_code'] == x.code and not x.main:
                    if x not in user.groups.all().first().discovered.all():
                        user.groups.all().first().discovered.add(x)
                        user.save()
                        # نشان ذره بین
                        user.groups.all().first().ach_mng()

                        Report.objects.create(
                            group=user.groups.all().first(),
                            text='شما در یک اکتشاف موفقیت آمیز ماموریت مخفی «' + str(x) + '» را پیدا کردید'
                        )
                        return (
                            render(
                                request,
                                'home_page.html',
                                {
                                    'manazel': Manzel.objects.filter(id__lte=user.groups.all().first().manzel).order_by(
                                        '-id'),
                                    'announcements': Announcement.objects.filter(is_active=True).order_by('-id'),
                                    'reports': Report.objects.filter(group=user.groups.all().first()).order_by('-id'),
                                    'FAQ': FAQ.objects.filter(is_active=True),
                                    'achivements': Achivement.objects.filter(manzel=None) | Achivement.objects.filter(
                                        code__contains='Mnz'),
                                    'exam': Exam.objects.filter(active=True).first(),
                                    'event': Event.objects.filter(active=True).first(),
                                    'MESSAGE': 'آفرین! اکتشاف شما موفق بود! <br> ماموریت مخفی «' + x.title + '» به گروه شما اضافه شد'
                                }
                            )
                        )
                    else:
                        return (
                            render(
                                request,
                                'home_page.html',
                                {
                                    'manazel': Manzel.objects.filter(id__lte=user.groups.all().first().manzel).order_by(
                                        '-id'),
                                    'announcements': Announcement.objects.filter(is_active=True).order_by('-id'),
                                    'reports': Report.objects.filter(group=user.groups.all().first()).order_by('-id'),
                                    'FAQ': FAQ.objects.filter(is_active=True),
                                    'achivements': Achivement.objects.filter(manzel=None) | Achivement.objects.filter(
                                        code__contains='Mnz'),

                                    'exam': Exam.objects.filter(active=True).first(),
                                    'event': Event.objects.filter(active=True).first(),
                                    'MESSAGE': 'این ماموریت مخفی را قبلا پیدا کرده اید. دوباره تلاش کنید! '
                                }
                            )
                        )
            return (
                render(
                    request,
                    'home_page.html',
                    {
                        'manazel': Manzel.objects.filter(id__lte=user.groups.all().first().manzel).order_by(
                            '-id'),
                        'announcements': Announcement.objects.filter(is_active=True).order_by('-id'),
                        'reports': Report.objects.filter(group=user.groups.all().first()).order_by('-id'),
                        'FAQ': FAQ.objects.filter(is_active=True),
                        'achivements': Achivement.objects.filter(manzel=None) | Achivement.objects.filter(
                            code__contains='Mnz'),
                        'exam': Exam.objects.filter(active=True).first(),
                        'event': Event.objects.filter(active=True).first(),
                        'MESSAGE': 'متاسفانه اکتشاف موفق نبود!<br> بیشتر تلاش کنید '
                    }
                )
            )

        if 'unlock_form' in request.POST:
            i = request.POST['unlock_value']
            t = Activity_Template.objects.filter(id=i).first()
            y = 0
            for x in user.groups.all().first().get_side_activities():
                for a in x.template.all():
                    if t == a:
                        y = x
                        break
            if y in user.groups.all().first().unlocked.all():
                return (
                    render(
                        request,
                        'home_page.html',
                        {
                            'manazel': Manzel.objects.filter(id__lte=user.groups.all().first().manzel).order_by(
                                '-id'),
                            'announcements': Announcement.objects.filter(is_active=True).order_by('-id'),
                            'reports': Report.objects.filter(group=user.groups.all().first()).order_by('-id'),
                            'FAQ': FAQ.objects.filter(is_active=True),
                            'achivements': Achivement.objects.filter(manzel=None) | Achivement.objects.filter(
                                code__contains='Mnz'),
                            'exam': Exam.objects.filter(active=True).first(),
                            'event': Event.objects.filter(active=True).first(),
                            'MESSAGE': 'شما قبلا این سطح را بازگشایی کرده اید.'
                        }
                    )
                )
            f = 0
            if y.id in user.groups.all().first().is_acted():
                f = 1
            if f and user.groups.all().first().get_food() < 5:
                return (
                    render(
                        request,
                        'home_page.html',
                        {
                            'manazel': Manzel.objects.filter(id__lte=user.groups.all().first().manzel).order_by(
                                '-id'),
                            'announcements': Announcement.objects.filter(is_active=True).order_by('-id'),
                            'reports': Report.objects.filter(group=user.groups.all().first()).order_by('-id'),
                            'FAQ': FAQ.objects.filter(is_active=True),
                            'achivements': Achivement.objects.filter(manzel=None) | Achivement.objects.filter(
                                code__contains='Mnz'),
                            'exam': Exam.objects.filter(active=True).first(),
                            'event': Event.objects.filter(active=True).first(),
                            'MESSAGE': 'میزان آذوقه شما کافی نمی باشد'
                        }
                    )
                )
            user.groups.all().first().unlocked.add(t)
            user.save()
            display = t.get_title()
            m = 'شما با موفقیت سطح «' + display + '» از ماموریت «' + str(y) + '» را بازگشایی کردید. '
            if f:
                m += 'و به این دلیل 5 واحد آذوقه از دست دادید'
            Report.objects.create(
                group=user.groups.all().first(),
                text=m
            )
            return redirect('home_page_link')

        if 'introduction_form' in request.POST:
            if user.groups.all().first().introduced:
                return (
                    render(
                        request,
                        'home_page.html',
                        {
                            'manazel': Manzel.objects.filter(id__lte=user.groups.all().first().manzel).order_by(
                                '-id'),
                            'announcements': Announcement.objects.filter(is_active=True).order_by('-id'),
                            'reports': Report.objects.filter(group=user.groups.all().first()).order_by('-id'),
                            'FAQ': FAQ.objects.filter(is_active=True),
                            'achivements': Achivement.objects.filter(manzel=None) | Achivement.objects.filter(
                                code__contains='Mnz'),
                            'exam': Exam.objects.filter(active=True).first(),
                            'event': Event.objects.filter(active=True).first(),
                            'MESSAGE': 'شما قبلا این مرحله را گذرانده اید'
                        }
                    )
                )
            g = user.groups.all().first()
            g.introduced = True
            g.save()
            Report.objects.create(
                group=user.groups.all().first(),
                text='شما با موفقیت منزل بانگ رحیل را پشت سر گذاشتید'
            )
            return redirect('home_page_link')

        # ثبت فعالیت
        for x in Activity_Topic.objects.all():
            if 'activity_' + str(x.id) + '_form' in request.POST:
                if (Activity.objects.filter(topic=x, group=user.groups.all().first()).exclude(state='6').first()):
                    return (
                        render(
                            request,
                            'home_page.html',
                            {
                                'manazel': Manzel.objects.filter(id__lte=user.groups.all().first().manzel).order_by(
                                    '-id'),
                                'announcements': Announcement.objects.filter(is_active=True).order_by('-id'),
                                'reports': Report.objects.filter(group=user.groups.all().first()).order_by('-id'),
                                'FAQ': FAQ.objects.filter(is_active=True),
                                'achivements': Achivement.objects.filter(manzel=None) | Achivement.objects.filter(
                                    code__contains='Mnz'),
                                'exam': Exam.objects.filter(active=True).first(),
                                'event': Event.objects.filter(active=True).first(),
                                'MESSAGE': 'گروه شما قبلا یکبار این ماموریت را انجام داده است.'
                            }
                        )
                    )
                if x in user.groups.all().first().get_side_activities():
                    template = Activity_Template.objects.filter(
                        id=int(request.POST['activity_' + str(x.id) + '_template'])).first()
                    if template not in user.groups.all().first().unlocked.all():
                        return (
                            render(
                                request,
                                'home_page.html',
                                {
                                    'manazel': Manzel.objects.filter(id__lte=user.groups.all().first().manzel).order_by(
                                        '-id'),
                                    'announcements': Announcement.objects.filter(is_active=True).order_by('-id'),
                                    'reports': Report.objects.filter(group=user.groups.all().first()).order_by('-id'),
                                    'FAQ': FAQ.objects.filter(is_active=True),
                                    'achivements': Achivement.objects.filter(manzel=None) | Achivement.objects.filter(
                                        code__contains='Mnz'),
                                    'exam': Exam.objects.filter(active=True).first(),
                                    'event': Event.objects.filter(active=True).first(),
                                    'MESSAGE': 'شما به این فعالیت دسترسی ندارید'
                                }
                            )
                        )
                if 'activity_' + str(x.id) + '_template' in request.POST:
                    Activity.objects.create(
                        topic=x,
                        template=Activity_Template.objects.filter(
                            id=int(request.POST['activity_' + str(x.id) + '_template'])).first(),
                        group=user.groups.all().first(),
                        link=request.POST['activity_' + str(x.id) + '_file'],
                        state='1'
                    )
                    Report.objects.create(
                        group=user.groups.all().first(),
                        text='ماموریت شما در بخش «' + str(x) + '» و با قالب «' + str(Activity_Template.objects.filter(
                            id=int(
                                request.POST['activity_' + str(x.id) + '_template'])).first()) + '» با موفقیت ثبت شد.'
                    )
                else:
                    Activity.objects.create(
                        topic=x,
                        group=user.groups.all().first(),
                        link=request.POST['activity_' + str(x.id) + '_file'],
                        state='1'
                    )
                    Report.objects.create(
                        group=user.groups.all().first(),
                        text='ماموریت بلند مدت شما با موفقیت ثبت شد'
                    )
                return (redirect('home_page_link'))

        if 'university_show_scores_admin_form' in request.POST:
            for x in Masir_Group_And_Exams_Rel.objects.filter(show_public=False):
                x.show_public = True
                x.save()
                g = x.group
                g: Masir_Group

                # مغز متفکر
                # قلم
                # کمال
                g.ach_mqz_qlm_kml()

                Report.objects.create(
                    group=g,
                    text='نتایج آزمون ' + str(x.exam.title) + ' منتشر شد و گروه شما در این آزمون ' + str(
                        x.score) + ' پاسخ درست ثبت کرد.'
                )

            return (redirect('home_page_link'))

        if 'event_show_scores_admin_form' in request.POST:
            for x in Masir_Group_And_Event_Rel.objects.filter(show_public=False):
                x.show_public = True
                x.save()
                a = 'اشتباه'
                if x.score == 1:
                    a = 'درست'

                Report.objects.create(
                    group=x.group,
                    text='نتایج فراخوان ' + str(x.event.title) + ' منتشر شد و پاسخ گروه شما در این فراخوان ' + str(
                        a) + ' بود.'
                )

            return redirect('home_page_link')

        if 'club_show_scores_admin_form' in request.POST:
            for x in Club_File.objects.filter(show_public=False, verified=True, denied=False):
                x.show_public = True
                x.save()
                g = x.user.groups.all().first()
                g: Masir_Group
                # قاری
                # ورزیده

                g.ach_qra_vrz()

                Report.objects.create(
                    group=g,
                    text='فایل ارسال شده از طرف ' + str(x.user) + ' با عنوان «' + str(x.title) + '» تایید شد.'
                )

            for x in Club_File.objects.filter(show_public=False, verified=False, denied=True):
                x.show_public = True
                x.save()

                Report.objects.create(
                    group=x.user.groups.all().first(),
                    text='فایل ارسال شده از طرف ' + str(x.user) + ' با عنوان «' + str(x.title) + '» به دلیل «' + str(
                        x.comment) + '» در بررسی رد شد.'
                )
            return (redirect('home_page_link'))

        if 'activities_show_scores_admin_form' in request.POST:
            for x in Activity.objects.filter(state='3').exclude(topic__manzel=None):
                x.state = '4'
                x.save()
                g = x.group
                g: Masir_Group

                # دستاورد ماموریت ها
                g.ach_mission(x)

                # پرچم
                # بی نقص
                g.ach_flg_nqs

                code = ACTIVITIES[x.topic.co_title] + '0' + str(int(x.template.type)) + '0' + str(
                    round(x.get_score()))
                ati = Achivement.objects.filter(code=code).first().title
                ate = Achivement.objects.filter(code=code).first().text
                main_score = 2 if x.topic.main else 1
                text = 'احسنت به شما! به ازای «' + str(ate) + '» نشان «' + str(ati) + '» رو به دست آوردید و ' + str(
                    (4 - int(x.template.type)) * round(
                        x.get_score()) * main_score) + ' واحد امتیاز حیات به گروه شما اضافه شد.'

                if x.cheated:
                    text += ' اما به دلیل حرکت شما پیش از اعلام نتایج داوری، آذوقه ای دریافت نکردید.'

                Report.objects.create(
                    group=x.group,
                    text=text
                )

            for x in Activity.objects.filter(state='5').exclude(topic__manzel=None):
                x.state = '6'
                x.save()

                Report.objects.create(
                    group=x.group,
                    text='متاسفانه ماموریت ' + str(x.topic) + ' به دلیل «' + str(x.comment) + '» در داوری رد شد.'
                )

            return (redirect('home_page_link'))

        if 'achivements_recalculate_admin_form' in request.POST:
            for x in Masir_Group.objects.all():
                x.recalculate_achivements()

            return (redirect('home_page_link'))

        if 'longterm_activities_show_scores_admin_form' in request.POST:
            for x in Activity.objects.filter(state='3').filter(topic__manzel=None):
                x.state = '4'
                x.save()
                g = x.group
                g: Masir_Group

                g.ach_lng(x)

                main_score = 2 if x.topic.main else 1
                text = 'احسنت به شما! به ازای انجام ماموریت تحول، نشان «تحول خواه» رو به دست آوردید و ' + str(
                    round(120 * x.get_score() / 5)) + ' واحد امتیاز حیات به گروه شما اضافه شد.'

                Report.objects.create(
                    group=x.group,
                    text=text
                )

            return (redirect('home_page_link'))

        if 'longterm_activities_deny_show_scores_admin_form' in request.POST:
            for x in Activity.objects.filter(state='5').filter(topic__manzel=None):
                x.state = '6'
                x.save()

                Report.objects.create(
                    group=x.group,
                    text='متاسفانه ماموریت تحول شمابه دلیل «' + str(x.comment) + '» در داوری رد شد.'
                )

            return (redirect('home_page_link'))

    if user.accessibility != Accessibility.objects.get(title='دسترسی دانش‌آموزی'):
        user_is_admin = False
        if user.accessibility == Accessibility.objects.get(title='دسترسی کامل'):
            user_is_admin = True

        return (
            render(
                request,
                'home_page_admin.html',
                {
                    'user_is_admin': user_is_admin,
                }
            )
        )

    return (
        render(
            request,
            'home_page.html',
            {
                'manazel': Manzel.objects.filter(id__lte=user.groups.all().first().manzel).order_by('-id'),
                'announcements': Announcement.objects.filter(is_active=True).order_by('-id'),
                'reports': Report.objects.filter(group=user.groups.all().first()).order_by('-id'),
                'FAQ': FAQ.objects.filter(is_active=True),
                'achivements': Achivement.objects.filter(manzel=None) | Achivement.objects.filter(code__contains='Mnz'),
                'exam': Exam.objects.filter(active=True).first(),
                'event': Event.objects.filter(active=True).first(),
            }
        )
    )


def leaderboard_page(request):
    user = select_user(request.user)
    if not user:
        return (redirect('landing_page_link'))
    if user.accessibility == Accessibility.objects.get(title='دسترسی دانش‌آموزی'):
        return (redirect('home_page_link'))
    if not user.accessibility == Accessibility.objects.get(title='دسترسی کامل'):
        return (redirect('home_page_link'))
    user_is_admin = True

    SGT = [{'title': str(x), 'light': x.get_light(), 'power': x.get_power(), 'food': x.get_food(),
            'manzel': int(x.manzel - 1), 'users': x.users.all(), 'supergroup': x.supergroup} for x in
           Masir_Group.objects.all()]
    return (
        render(
            request,
            'leaderboard_page_admin.html',
            {
                'user_is_admin': user_is_admin,
                'groups': SGT
            }
        )
    )


def contact_admin_page(request):
    user = select_user(request.user)
    if not user:
        return (redirect('landing_page_link'))

    if user.accessibility != Accessibility.objects.get(title='دسترسی دانش‌آموزی'):
        if not user.accessibility.contact_admin_page:
            return (redirect('home_page_link'))
        return (
            render(
                request,
                'contact_admin_page_admin.html',
                {
                    'FAQ': FAQ.objects.filter(is_active=True),
                    'messages': Message.objects.all().order_by('-id')
                }
            )
        )

    if not user.groups.all().first():
        return (
            render(
                request,
                'landing_page.html',
                {
                    'MESSAGE': str(user)
                               + ' عزیز! ثبت نام شما با موفقیت انجام شد.'
                               + ' کد ورود شما:'
                               + '<br>' + str(user.code) + '<br>'
                               + 'برای تشکیل تیم و شروع مسابقه به این کد نیاز خواهید داشت.'
                               + '<br> <br>' + 'چند نکته بسیار مهم:'
                               + '<ul>'
                               + '<li>' + 'ثبت نام گروهی از دهه دوم ماه مبارک رمضان آعاز خواهد شد.' + '</li>'
                               + '<li>' + 'مسابقه گروهی است و بصورت فردی نمی‌توانید در آن شرکت کنید.' + '</li>'
                               + '<li>' + 'برای ساخت گروه باید یکی از افراد با داشتن کد اعضای دیگر، از بخش ثبت نام گروهی اقدام نماید.' + '</li>'
                               + '<li>' + 'مسابقه از <u>نیمه دوم ماه مبارک رمضان</u> آغاز می‌شود.' + '</li>'
                               + '<li>' + 'حتما و حتما در یکی از <a href="https://zil.ink/masir1402">کانالهای مسابقه </a> عضو شوید تا اطلاعیه‌های بعدی را دریافت نمایید.' + '</li>'
                               + '</ul>',
                    'cities': City.objects.all().order_by('name'),
                    'schools': School.objects.all().order_by('name'),
                    'announcements': Announcement.objects.filter(is_public=True)
                }
            )
        )

    if request.method == 'POST':
        if 'message_form' in request.POST:
            Message.objects.create(
                name=request.POST['contact_us_name'],
                phone=request.POST['contact_us_phone'],
                message=request.POST['contact_us_message']
            )

            return (redirect('contact_admin_page_link'))

    return (
        render(
            request,
            'contact_admin_page.html',
            {
                'FAQ': FAQ.objects.filter(is_active=True),
                'messages': Message.objects.filter(phone=user.user.username).order_by('-id')
            }
        )
    )


def contact_admin_detail_page(request, id):
    user = select_user(request.user)
    if not user:
        return (redirect('landing_page_link'))
    if user.accessibility == Accessibility.objects.get(title='دسترسی دانش‌آموزی'):
        return (redirect('landing_page_link'))
    if not user.accessibility.contact_admin_page_edit:
        return (redirect('contact_admin_page_link'))

    the_message = Message.objects.filter(id=id).first()
    if not the_message:
        return (redirect('contact_admin_page_link'))

    if request.method == 'POST':
        if 'message_admin_form' in request.POST:
            the_message.answer = request.POST['message_admin_answer']
            the_message.support = user
            the_message.save()

            return (redirect('contact_admin_page_link'))

    return (
        render(
            request,
            'contact_admin_page_admin.html',
            {
                'the_message': the_message,
                'messages': Message.objects.filter(phone=the_message.phone).exclude(id=the_message.id).order_by('-id')
            }
        )
    )


def club_page(request):
    user = select_user(request.user)
    if not user:
        return (redirect('landing_page_link'))
    if user.accessibility == Accessibility.objects.get(title='دسترسی دانش‌آموزی'):
        return (redirect('home_page_link'))
    if not user.accessibility.club_page:
        return (redirect('home_page_link'))

    return (
        render(
            request,
            'club_page_admin.html',
            {
                'club_files': Club_File.objects.all().order_by('show_public', 'verified', 'denied', '-id', )
            }
        )
    )


def club_detail_page(request, id):
    user = select_user(request.user)
    if not user:
        return (redirect('landing_page_link'))
    if user.accessibility == Accessibility.objects.get(title='دسترسی دانش‌آموزی'):
        return (redirect('landing_page_link'))
    if not user.accessibility.club_page_edit:
        return (redirect('club_page_link'))

    the_file = Club_File.objects.filter(id=id).first()
    if not the_file:
        return (redirect('club_page_link'))

    if request.method == 'POST':
        the_file.show_public = False
        the_file.referee = user
        if 'club_admin_form' in request.POST and not the_file.verified:
            the_file.verified = True
            the_file.denied = False
            the_file.comment = None
            the_file.save()

            u = the_file.user
            u.club_level = the_file.level + 1
            u.save()
        if 'club_admin_deny_form' in request.POST:
            the_file.denied = True
            the_file.verified = False
            the_file.comment = request.POST['club_admin_denied_message']
            the_file.save()

            u = the_file.user
            u.club_level = the_file.level
            u.save()

        return (redirect('club_page_link'))

    return (
        render(
            request,
            'club_page_admin.html',
            {
                'the_file': the_file,
                'club_files': Club_File.objects.filter(user=the_file.user).exclude(id=the_file.id).order_by('-id')
            }
        )
    )


def judge_page(request):
    user = select_user(request.user)
    if not user:
        return (redirect('landing_page_link'))
    if user.accessibility == Accessibility.objects.get(title='دسترسی دانش‌آموزی'):
        return (redirect('home_page_link'))
    if not user.accessibility.judge_page:
        return (redirect('home_page_link'))

    user_is_admin = False
    if user.accessibility == Accessibility.objects.get(title='دسترسی کامل'):
        user_is_admin = True

    return (
        render(
            request,
            'judge_page_admin.html',
            {
                'activities': Activity.objects.filter(state='1').exclude(topic__manzel=None).order_by('-id'),
                'user_is_admin': user_is_admin,
                'activities_for_admin': Activity.objects.exclude(state='1').exclude(topic__manzel=None).order_by(
                    'state', '-id'),
            }
        )
    )


def judge_detail_page(request, id):
    user = select_user(request.user)
    if not user:
        return (redirect('landing_page_link'))
    if user.accessibility == Accessibility.objects.get(title='دسترسی دانش‌آموزی'):
        return (redirect('landing_page_link'))
    if not user.accessibility.judge_page_edit:
        return (redirect('judge_page_link'))

    the_file = Activity.objects.filter(id=id).first()
    if not the_file:
        return (redirect('judge_page_link'))

    the_file.state = '2'
    the_file.referee = user
    the_file.save()

    if request.method == 'POST':
        if 'judge_admin_form' in request.POST:
            the_file.referee = user

            the_file.score1 = int(request.POST['judge_admin_score1'])
            the_file.score2 = int(request.POST['judge_admin_score2'])
            the_file.score3 = int(request.POST['judge_admin_score3'])
            the_file.score4 = int(request.POST['judge_admin_score4'])
            the_file.score5 = int(request.POST['judge_admin_score5'])

            the_file.state = '3'
            the_file.save()

        if 'judge_admin_deny_form' in request.POST:
            the_file.referee = user

            the_file.comment = request.POST['judge_admin_denied_message']

            the_file.state = '5'
            the_file.save()

        if 'judge_admin_cancel_form' in request.POST:
            the_file.state = '1'
            the_file.referee = None
            the_file.save()

        return (redirect('judge_page_link'))

    return (
        render(
            request,
            'judge_page_admin.html',
            {
                'the_file': the_file,
                'activities': None
            }
        )
    )


def longterm_judge_page(request):
    user = select_user(request.user)
    if not user:
        return (redirect('landing_page_link'))
    if not user.accessibility == Accessibility.objects.get(title='دسترسی کامل'):
        return (redirect('home_page_link'))

    return (
        render(
            request,
            'longterm_judge_page_admin.html',
            {
                'longterms': Activity.objects.filter(topic__manzel=None).order_by('state', '-id'),
            }
        )
    )


def longterm_judge_detail_page(request, id):
    user = select_user(request.user)
    if not user:
        return (redirect('landing_page_link'))
    if user.accessibility == Accessibility.objects.get(title='دسترسی دانش‌آموزی'):
        return (redirect('landing_page_link'))
    if not user.accessibility == Accessibility.objects.get(title='دسترسی کامل'):
        return (redirect('longterm_judge_page_link'))

    the_file = Activity.objects.filter(id=id).first()
    if not the_file:
        return (redirect('longterm_judge_page_link'))

    the_file.state = '2'
    the_file.referee = user
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
            the_file.score7 = int(request.POST['judge_admin_score7'])

            the_file.state = '3'
            the_file.save()

        if 'judge_admin_deny_form' in request.POST:
            the_file.referee = user

            the_file.comment = request.POST['judge_admin_denied_message']

            the_file.state = '5'
            the_file.save()

        if 'judge_admin_cancel_form' in request.POST:
            the_file.state = '1'
            the_file.referee = None
            the_file.save()

        return (redirect('longterm_judge_page_link'))

    return (
        render(
            request,
            'longterm_judge_page_admin.html',
            {
                'the_file': the_file,
                'longterms': None
            }
        )
    )


def statistics_page(request):
    user = select_user(request.user)
    if not user:
        return (redirect('landing_page_link'))
    if not user.user.is_staff:
        return (redirect('home_page_link'))

    groups_all = [len(Masir_Group.objects.all()), 0, 0, 0]
    discover_all = [0, 0]
    for x in Masir_Group.objects.all():
        if x.get_light() > 14:
            groups_all[1] = groups_all[1] + 1
        if x.activities.all().first():
            groups_all[2] = groups_all[2] + 1
        if x.introduced:
            groups_all[3] += 1
        if len(x.discovered.all()) > 5:
            discover_all[0] += 1
            discover_all[1] += len(x.discovered.all()) - 5

    charities_all = [0, len(Charity.objects.all().values('group').annotate(count=Count('id', distinct=True)))]
    for x in Charity.objects.all():
        charities_all[0] = charities_all[0] + x.value
    exams_all = [len(Masir_Group_And_Exams_Rel.objects.all()),
                 len(Masir_Group_And_Exams_Rel.objects.all().values('group').annotate(
                     count=Count('id', distinct=True)))]
    club_files_all = [len(Club_File.objects.all()),
                      len(Club_File.objects.all().values('user').annotate(count=Count('id', distinct=True)))]
    events_all = [len(Masir_Group_And_Event_Rel.objects.all()),
                  len(Masir_Group_And_Event_Rel.objects.all().values('group').annotate(
                      count=Count('id', distinct=True)))]

    activity_topic_all = Activity.objects.all().exclude(topic__manzel=None).exclude(state='6').values('topic__title',
                                                                                                      'topic__manzel__number').annotate(
        count=Count('id', distinct=True)).order_by('-count')

    return (
        render(
            request,
            'statistics_page_admin.html',
            {
                'groups_all': groups_all,
                'charities_all': charities_all,
                'exams_all': exams_all,
                'club_files_all': club_files_all,
                'groups': Masir_Group.objects.all().order_by('supergroup'),
                'activity_topic_all': activity_topic_all,
                'discover_all': discover_all,
                'events_all': events_all,
            }
        )
    )


def poll_statistics_page(request):
    user = select_user(request.user)
    if not user:
        return redirect('landing_page_link')
    if not user.user.is_staff:
        return redirect('home_page_link')

    votes_all = {
        'all': len(Vote.objects.all()),
        'valid': len(Vote.objects.filter(is_valid=True)),
        'voted': len(Vote.objects.filter(is_voted=True)),
    }
    topworks = [list(Top_Work.objects.filter(type='1')),
                list(Top_Work.objects.filter(type='2')),
                list(Top_Work.objects.filter(type='3'))]

    return (
        render(
            request,
            'poll_page_admin.html',
            {
                'votes_all': votes_all,
                'topworks' : topworks
            }
        )
    )


def help_page(request):
    return (
        render(
            request,
            'help_page.html',
            {
            }
        )
    )
