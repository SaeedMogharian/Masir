from django.test.testcases import TestCase
from django.test import TestCase
from base.models import Activity_Topic
from base.models import Masir_Group


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
        self.a = Masir_Group.objects.all()[0]

    def getDiscovered(self):
        c = list(self.a.discovered.all())
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
