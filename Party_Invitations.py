class Friend:
    def __init__(self, name):
        self.name = name
        self.party_detail = "No party..."

    def set_party_detail(self, party_name, detail):
        self.party_detail = party_name + ": " + detail

    def show_invite(self):
        return self.party_detail


class Party:
    def __init__(self, name):
        self.name = name
        self.participants_list = []

    def add_friend(self, friend_obj):
        self.participants_list.append(friend_obj)

    def del_friend(self, friend_obj):
        self.participants_list.remove(friend_obj)

    def send_invites(self, detail):
        for friend_obj in self.participants_list:
            friend_obj.set_party_detail(self.name, detail)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    party = Party("Midnight Pub")
    nick = Friend("Nick")
    john = Friend("John")
    lucy = Friend("Lucy")
    chuck = Friend("Chuck")

    party.add_friend(nick)
    party.add_friend(john)
    party.add_friend(lucy)
    party.send_invites("Friday, 9:00 PM")
    party.del_friend(nick)
    party.send_invites("Saturday, 10:00 AM")
    party.add_friend(chuck)

    assert john.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert lucy.show_invite() == "Midnight Pub: Saturday, 10:00 AM"
    assert nick.show_invite() == "Midnight Pub: Friday, 9:00 PM"
    assert chuck.show_invite() == "No party..."
    print("Coding complete? Let's try tests!")
