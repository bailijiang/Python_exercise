#coding=utf-8
__author__ = 'Bryan'

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_info = build_profile('albert', 'einstein',
                          location='princeton',
                          field='physics')
print(user_info)
