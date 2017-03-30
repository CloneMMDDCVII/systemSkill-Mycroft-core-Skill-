# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.
#
# This is a simple skill based on the HelloWorld Skill that shuts down the computer when asking for it. 
# It does not require root.
from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import os
import time
__author__ = 'eward'
__author__ = 'BrokenClock'

LOGGER = getLogger(__name__)


class systemSkill(MycroftSkill):

    def __init__(self):
        super(systemSkill, self).__init__(name="systemSkill")

    def initialize(self):
        shutdown_intent = IntentBuilder("shutdownIntent").\
            require("shutdownKeyword").build()
        self.register_intent(shutdown_intent, self.handle_shutdown_intent)

        restart_intent = IntentBuilder("restartIntent").\
            require("restartKeyword").build()
        self.register_intent(restart_intent,
                             self.handle_restart_intent)


    def handle_shutdown_intent(self, message):
        self.speak_dialog("shuttingDown")
        time.sleep(30)
        os.system("systemctl poweroff")

    def handle_restart_intent(self, message):
        self.speak_dialog("restart")
        time.sleep(30)
        os.system("systemctl reboot")

    def stop(self):
        pass


def create_skill():
    return systemSkill()