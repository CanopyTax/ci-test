from source import crazy
import requests
from unittest.mock import patch, MagicMock
import pytest



# def test_use_normal_monkey_patching():
#     d = {'apple': 'pie'}
#
#     def my_func(val):
#         return d
#
#     crazy.do_some_crazy_stuff = my_func
#
#     assert crazy.use_some_crazy_stuff(1) == d
#
#
#
#
#
#
#
# def test_monkey_patch_requests():
#     d = {'something': 'deathstar'}
#
#     class MyResponse:
#         def json(self):
#             return d
#
#     def my_request(url):
#         return MyResponse()
#
#     requests.get = my_request
#     assert crazy.use_some_crazy_stuff(1) == d








@patch('source.crazy.do_some_crazy_stuff')
def test_use_crazy_stuff_1(mock):
    d = {'foo': 'bar'}
    mock.return_value = d

    assert crazy.use_some_crazy_stuff(1) == d





@patch('requests.get')
def test_mock_requests(mock_get):
    d = {'biz': 'baz'}
    response = MagicMock()
    response.json.return_value = d
    mock_get.return_value = response

    assert crazy.use_some_crazy_stuff(1) == d










@patch('source.crazy.do_some_crazy_stuff')
def test_side_effects(mock):
    mock.side_effect = lambda val: {val: 'a'}

    assert crazy.use_some_crazy_stuff(1) == {1: 'a'}
    assert crazy.use_some_crazy_stuff(2) == {2: 'a'}
    assert crazy.use_some_crazy_stuff('pie') == {'pie': 'a'}








@patch('source.crazy.do_some_crazy_stuff')
def test_side_effects_list(mock):
    mock.side_effect = [{1: 'a'}, {2: 'a'}, {3: 'a'}, {4: 'a'}]

    assert crazy.use_some_crazy_stuff(1) == {1: 'a'}
    assert crazy.use_some_crazy_stuff(1) == {2: 'a'}
    assert crazy.use_some_crazy_stuff(1) == {3: 'a'}
    assert crazy.use_some_crazy_stuff(1) == {4: 'a'}






def test_do_something_with_monkeypatch(monkeypatch):
    monkeypatch.setattr(crazy, 'do_some_crazy_stuff', lambda val: {val: 'a'})
    assert crazy.use_some_crazy_stuff(1) == {1: 'a'}
    assert crazy.use_some_crazy_stuff(2) == {2: 'a'}
    assert crazy.use_some_crazy_stuff(3) == {3: 'a'}







def test_monkeypatch_env(monkeypatch):
    import os
    monkeypatch.setenv('FOO', 'BAR')
    assert os.getenv('FOO') == 'BAR'


def test_monkeypatch_env_normal():
    import os
    assert os.getenv('FOO') is None