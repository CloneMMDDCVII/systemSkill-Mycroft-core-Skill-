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
import os


class System(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    # Get the user's confirmation before proceeding with the given task
    def userValidation(self, action):
        # Keyworks translated in the user's language
        ASSERTION = self.translate_namedvalues('assertion')

        dialogData = {'action' : action}
        validation = self.get_response('validation', dialogData)

        if ASSERTION['yes'] in validation:
            return True

    @intent_file_handler('reboot.intent')
    def handle_reboot(self, message):
        # 'action' words translated in the user's language
        ACTIONS = self.translate_namedvalues('actions')

        if self.userValidation(ACTIONS['reboot']):
            os.system("systemctl reboot")

    @intent_file_handler('powerOff.intent')
    def handle_powerOff(self, message):
        # 'action' words translated in the user's language
        ACTIONS = self.translate_namedvalues('actions')

        if self.userValidation(ACTIONS['poweroff']):
            os.system("systemctl poweroff")


def create_skill():
    return System()

