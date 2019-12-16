# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one,
# 　　　　　　　　　　　　turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", if the channel N or
# 　　　　　　　　　　　　'name' exists in the list, or "No" - in the other case.
#


class VoiceCommand:
    def __init__(self, channels):
        self.channels = channels
        self.now = 1

    def first_channel(self):
        self.now = 1
        return self.channels[0]

    def last_channel(self):
        self.now = len(self.channels)
        return self.channels[-1]

    def turn_channel(self, num):
        if 1 <= num <= len(self.channels):
            self.now = num
            return self.channels[num - 1]
        else:
            pass

    def current_channel(self):
        return self.channels[self.now - 1]

    def next_channel(self):
        if self.now == len(self.channels):
            self.now = 1
            return self.channels[0]
        else:
            self.now = self.now + 1
            return self.channels[self.now - 1]

    def previous_channel(self):
        if self.now == 1:
            self.now = len(self.channels)
            return self.channels[-1]
        else:
            self.now = self.now - 1
            return self.channels[self.now - 1]

    def is_exist(self, val):
        if isinstance(val, str):
            if val in self.channels:
                return "Yes"
            else:
                return "No"
        elif isinstance(val, int):
            if 1 <= val <= len(self.channels):
                return "Yes"
            else:
                return "No"
        else:
            pass


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    CHANNELS = ["BBC", "Discovery", "TV1000"]

    controller = VoiceCommand(CHANNELS)

    assert controller.first_channel() == "BBC"
    assert controller.last_channel() == "TV1000"
    assert controller.turn_channel(1) == "BBC"
    assert controller.next_channel() == "Discovery"
    assert controller.previous_channel() == "BBC"
    assert controller.current_channel() == "BBC"
    assert controller.is_exist(4) == "No"
    assert controller.is_exist("TV1000") == "Yes"
