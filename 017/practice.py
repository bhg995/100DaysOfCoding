
#class User:
#    def __init__(self, city):
#        self.city = city
#        print("New user ...")
#
#user_1 = User("Anchiano")
#user_1.id = "0001"
#user_1.username = "leonardo".capitalize()
#
#print(user_1.username +": "+user_1.id, "Hailing from", user_1.city)
#
#user_2 = User("Caprese Michelangelo")
#user_2.id = "0002"
#user_2.username = "michelangelo".capitalize()
#
#print(user_2.username +": "+user_2.id, "Hailing from", user_2.city)
#
#user_3 = User("Pisa")
#user_3.id = "0002"
#user_3.username = "galileo".capitalize()
#
#print(user_3.username +": "+user_3.id, "Hailing from", user_3.city)

class User:
    def __init__(self, user_id, username, city):
        self.id = user_id
        self.username = username
        self.city = city
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User(user_id="0001", username="leonardo".capitalize(), city="Anchiano")
user_2 = User(user_id="0002", username="Michelangelo".capitalize(), city="Caprese Michelangelo")
user_3 = User(user_id="0003", username="Galileo".capitalize(), city="Pisa")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)