from pandas import DataFrame as DF
from pandas import options
import vk

SERVICE_TOKEN = 'd7298aa8d7298aa8d7298aa850d75d6bc6dd729d7298aa8b74dc74788cf206b20fd1058'
USER_TOKEN = '2048775f54b164078be15df3074bfd8eba4ded95ced92de68155048c3ed6010185f1b73408db939f625d7'

all_varieties = []

options.display.max_columns = 100
options.display.max_rows = 100


class Group:
    def __init__(self, string):
        session = vk.Session(access_token=USER_TOKEN)
        self.vk = vk.API(session)  # авторизация

    def searching(self, string):
        all_varieties.clear()
        varieties = self.vk.users.search(q=string, v=5.21, count=600)['items']
        for i in range(0, len(varieties)):
            all_vk_varieties = varieties[i]['id']
            interests_vk = 'http://vk.com/id' + str(all_vk_varieties)
            all_varieties.append(interests_vk)
            return all_varieties

    def get_information1(self, string):
        information_key, information_value = [], []
        information1 = self.vk.users.get(
            user_ids=string[16:],
            v=5.21,
            fields='verified, online, '
            'domain, has_mobile, contacts, site, education, universities, '
            'status, last_seen, followers_count, '
            ' nickname, relatives, relation,connections, '
            'exports, activities, interests, music, movies, tv, books, games, '
            'about, quotes, is_favorite, '
            'timezone, maiden_name, '
            ' career, military')

        for key in information1[0].keys():
            if information1[0][key] != 0 or '' or []:
                information_key.append(str(key))
                information_value.append(str(information1[0][key]))
                information = {
                    'keys': information_key,
                    'values': information_value
                }
        information = DF(data=information)
        print(information)
        return str(information)

    def get_information2(self, string):
        information1 = self.vk.users.get(
            user_ids=string[16:],
            v=5.21,
            fields='occupation, personal, schools')
        print(information1)
        return str(information1)

    def get_photos(self, string):
        information2 = self.vk.users.get(user_ids=string[16:],
                                         v=5.21,
                                         fields='photo_400_orig')
        return information2[0].get('photo_400_orig')


a = Group('')

# https://oauth.vk.com/authorize?client_id=7659886&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends&response_type=token&v=5.130&state=123456
