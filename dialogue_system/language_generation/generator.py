# -*- coding: utf-8 -*-
import sys


class LanguageGenerator(object):

    def __init__(self):
        pass

    def generate_sentence(self, dialogue_act):
        sent = ''
        if 'SUBJECT' in dialogue_act:
            sent += '質問の科目は{0}ですね。'.format(dialogue_act['SUBJECT'])
        if 'TEACHER' in dialogue_act:
            sent += '{0}先生ですね。'.format(dialogue_act['TEACHER'])
        if 'REPLY' in dialogue_act:
            judge = '{0}'.format(dialogue_act['REPLY'])
            if judge in "yes":
                sent += "ありがとう！"
            elif judge in "no":
                sent += "まとめてからまた持って来てね"
            else:
                sent += "質問内容がよくわからないな"
        if 'PICTURE' in dialogue_act:
            sent += '記憶したよ'


        sys_act_type = dialogue_act['sys_act_type']
        if sys_act_type == 'REQUEST_SUBJECT':
            sent += '質問の科目は何ですか？'
        elif sys_act_type == 'REQUEST_TEACHER':
            sent += '質問したい先生がいたら教えてください。'
        elif sys_act_type == 'REQUEST_REPLY':
            sent += '質問内容を専用の用紙にまとめてくれた？'
        elif sys_act_type == 'REQUEST_PICTURE':
            sent += '記憶するから僕に見せてくれるかな？頑張ってって応援してね'
        elif sys_act_type == 'CHAT':
            sent += dialogue_act['utt']
        elif sys_act_type == 'INFORM_RESTAURANT':
            sent += '予約したよ！これからもよろしくね！'
        else:
            print('Error')
            sys.exit(-1)

        return sent