__author__ = 'Bryan'
#coding=utf-8

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['Bryan'] = 'C/C++'
favorite_languages['Heero'] = 'Python'
favorite_languages['Blues'] = 'Java'
favorite_languages['Bai'] = 'Golang'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is: " + language.title() + ".")


# favorite_languages = {
#     'bob': 'Python',
#     'john': 'Java',
#     'leon': 'C',
#     'heero': 'Golang',
#     'bryan': 'C++'
# }
#
# print("bryan's favorite language is: " +
#       str(favorite_languages['bryan']).title() +
#       ".")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
#
# friends = ['phil', 'sarah']
#
# for name in favorite_languages.keys():
#     print(name.title())
#     if name in friends:
#         print(" Hi " + name.title() +
#               ", I see your favorite language is " +
#               favorite_languages[name].title() + "!")
#
# for name in sorted(favorite_languages.keys()):
#     print(name)
#
# for language in favorite_languages.values():
#     print(language.title())
#
# print("set--------------------------------------")
# for language in set(favorite_languages.values()):
#     print(language)

# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }
#
# for name, languages in favorite_languages.items():
#     print("\n" + name.title() + "'s favorite languages are: ")
#     for language in languages:
#         print("\t" + language)