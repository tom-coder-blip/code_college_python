def build_profile(first, last, **user_info):

    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile) 



def make_person_profile(the_name, the_age, **person_1):

    person_1['name'] = the_name
    person_1['age'] = the_age
    return person_1

the_profile = make_person_profile('Jack', 90, gender='male', status='Married')

print(the_profile)