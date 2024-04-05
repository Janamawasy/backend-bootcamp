import json

class User:
    def __init__(self, username):
        '''
        Intelize user
        following: array of usernames
        params: username
        '''
        self.username = username
        self.following = []

    def follow(self, other_username):
        '''
        add follower to following array
        '''
        if other_username not in self.following:
            self.following.append(other_username)
            print(f'{self.username} follow {other_username}')

    def post_message(self, message):
        '''
        add post to posts.json
        '''
        print('following', self.following)
        post = {'username': self.username, 'message': message}
        self.append_json('posts.json', post)

    def append_json(self, filename, post):
        with open(filename, 'r+') as file:
            data = json.load(file)
            data.append(post)
            # Move the file pointer to the beginning to overwrite the existing data
            file.seek(0)
            # Write the updated data back to the file
            json.dump(data, file, indent=4)
            # Truncate the remaining content in case the new data is shorter than the previous content
            file.truncate()


# Assume posts are stored in a global list
