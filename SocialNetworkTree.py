from User import User


class SocialNetworkTree:
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name)
        else:
            print(f"User {user_id} already exists.")

    def add_relationship(self, user_id1, user_id2):
        if user_id1 in self.users and user_id2 in self.users:
            self.users[user_id1].relationships.append(self.users[user_id2])
            self.users[user_id2].relationships.append(self.users[user_id1])
        else:
            print(f"One or both users not found: {user_id1}, {user_id2}")

    def remove_user(self, user_id):
        if user_id in self.users:
            for friend in self.users[user_id].relationships:
                friend.relationships.remove(self.users[user_id])
            del self.users[user_id]
        else:
            print(f"User {user_id} not found.")

    def display_tree(self):
        for user in self.users.values():
            print(f"{user.name} ({
                  user.user_id}) -> {[friend.name for friend in user.relationships]}")

    def find_user(self, user_id):
        if user_id in self.users:
            user = self.users[user_id]
            return user
        else:
            print(f"User {user_id} not found.")
            return None

    def find_communities(self):
        visited = set()
        communities = []

        def dfs(user, community):
            visited.add(user.user_id)
            community.append(user)
            for friend in user.relationships:
                if friend.user_id not in visited:
                    dfs(friend, community)

        for user in self.users.values():
            if user.user_id not in visited:
                community = []
                dfs(user, community)
                communities.append(community)

        return communities
