from user import User
from social_media import SocialMediaPlatform

posts = []
user1 = User('user1')
user2 = User('user2')
user3 = User('user3')

user1.follow('user2')
user1.follow('user3')

user2.post_message('whatsup guys?')
user3.post_message('hiiiii')
user1.post_message('dd')

SM =SocialMediaPlatform()
SM.register_user('user1')
SM.register_user('user2')
SM.register_user('user3')
print(SM.generate_timeline('user1'))


