from django.test.testcases import TestCase
from django.test import TestCase
from base.models import Activity_Topic
from base.models import Masir_Group
from base.models import Manzel

# Create your tests here.

# class testTopic(TestCase):
#     def __init__(self):
#         self.a = Activity_Topic.objects.all()
#
#     def __str__(self):
#         s = ''
#         for x in self.a:
#             s += str(x) + '  '
#         return s
#
#     def noManzel(self):
#         l = self.a.filter(manzel=None).first().title
#         return l


class testDiscoverd(TestCase):
    def __init__(self):
        self.a = Manzel.objects.all()

    def getDiscovered(self):
        c=[]
        for x in self.a:
            c.append(str(x.back_image)[4:])
        return c

    def __str__(self):
        s = ''
        for x in self.getDiscovered():
            s += str(x) + '  '
        return s

# A = testTopic()
# l=A.noManzel()
# print(str(l))

T = testDiscoverd()
print(str(T))
