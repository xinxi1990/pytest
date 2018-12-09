#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
pytest插件，让你播放描述一些动作和断言的json文件.
'''
import pytest,json



@pytest.fixture
def play_json():
    return json.loads(open('./test_login.json', 'r').read())

def test_login(play_json):
    print play_json
    # data = play_json.get_file_contents(
    #     'my', 'path', 'etc', 'test_login.json')
    play_json.execute(play_json, extra_variables={})


