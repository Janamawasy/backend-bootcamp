import json
from user import User

class SocialMediaPlatform():
    def __init__(self):
        self.users = []

    def register_user(self, username):
        '''
        if username is not already exist -> add username
        '''
        if not self._is_username_taken(username):
            user = User(username)
            # self.users.append(user)
            for existing_user in self.users:
                user.follow(existing_user.username)
            self.users.append(user)



    def _is_username_taken(self, username) -> bool:
        '''
        function checks if username exist or not
        return: True-> username exist, False-> username do not exist
        '''
        for user in self.users:
            if user.username == username:
                return True
        return False

    def get_user_by_username(self, username):
        '''
        get user instance by username
        return: user instance if found, None otherwise
        '''
        for user in self.users:
            if user.username == username:
                return user
        return None

    def generate_timeline(self, username):
        '''
        get all post for the followers of username
        return timeline: array of posts
        '''
        user = self.get_user_by_username(username)
        if not user:
            return []

        posts = self.get_posts('posts.json')
        timeline = []
        print('user11', user.following)
        for followed_user in user.following:
            print('followed_user', followed_user)
            for post in posts:
                if post['username'] == followed_user:
                    timeline.append(post)
        return timeline

    def get_posts(self, filename):
        """

        """
        with open(filename, 'r') as file:
            posts_data = json.load(file)
        return posts_data




