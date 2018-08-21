#~ Copyright (C) eward & BrokenClock
#~ Modified by backasswards, 2018

#~ This program is free software: you can redistribute it and/or modify
#~ it under the terms of the GNU General Public License as published by
#~ the Free Software Foundation, either version 3 of the License, or
#~ (at your option) any later version.

#~ This program is distributed in the hope that it will be useful,
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#~ GNU General Public License for more details.

#~ You should have received a copy of the GNU General Public License
#~ along with this program.  If not, see <http://www.gnu.org/licenses/>.

from mycroft import MycroftSkill, intent_file_handler
from mycroft.messagebus.message import Message


class System(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.tasks = self.translate_namedvalues('tasks')

    def getUserConfirmation(self, task):
        assert task

        data = {'task' : task}
        utter = self.ask_yesno('confirmation', data)

        if self.is_match(utter, 'yes'):
            return True

    @intent_file_handler('reboot.intent')
    def handle_reboot(self, message):
        if self.getUserConfirmation(self.tasks['reboot']):
            self.emitter.emit(Message('system.reboot'))

    @intent_file_handler('powerOff.intent')
    def handle_powerOff(self, message):
        if self.getUserConfirmation(self.tasks['poweroff']):
            self.emitter.emit(Message('system.shutdown'))


def create_skill():
    return System()

