# -*- coding: utf-8 -*-
from copy import deepcopy

from dialogue_system.dialogue_management.state import DialogueState
from dialogue_system.backend.apis.hotpepper import HotPepperGourmetAPI
#from dialogue_system.backend.apis.docomo_dialogue import DocomoDialogAPI


class DialogueManager(object):

    def __init__(self):
        self.dialogue_state = DialogueState()

    def update_dialogue_state(self, dialogue_act):
        self.dialogue_state.update(dialogue_act)

    def select_action(self, dialogue_act):
        sys_act = deepcopy(dialogue_act)
        if dialogue_act['user_act_type'] == 'OTHER':
#            api = DocomoDialogAPI()
#            reply = api.reply(dialogue_act['utt'])
            reply = "もう一度お願いします"
            sys_act['sys_act_type'] = 'CHAT'
            sys_act['utt'] = reply
        elif not self.dialogue_state.has('SUBJECT'):
            sys_act['sys_act_type'] = 'REQUEST_SUBJECT'
        elif not self.dialogue_state.has('TEACHER'):
            sys_act['sys_act_type'] = 'REQUEST_TEACHER'
        elif not self.dialogue_state.has('REPLY'):
            sys_act['sys_act_type'] = 'REQUEST_REPLY'
        elif not self.dialogue_state.has('PICTURE'):
            sys_act['sys_act_type'] = 'REQUEST_PICTURE'
        else:
            api = HotPepperGourmetAPI()
            area = self.dialogue_state.get_area()
            food = self.dialogue_state.get_food()
            budget = self.dialogue_state.get_budget()
            restaurant = api.search_restaurant(area=area, food=food,budget=budget)
            sys_act['sys_act_type'] = 'INFORM_RESTAURANT'
            sys_act['restaurant'] = restaurant
            self.dialogue_state.clear()

        return sys_act