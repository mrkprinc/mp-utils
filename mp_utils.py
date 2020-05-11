#!/usr/bin/env python3
import sys
import redux_constants

def mp_utils(cli_args):
  tool, args = cli_args[0], cli_args[1:]

  return {
    'redux-constants': redux_constants.default,
  }.get(tool, unknown_tool)(args)

def unknown_tool(_args):
  raise AssertionError('This tool is not in my box :(')

try:
  assert len(sys.argv) > 1, 'Which MP tool do you want?'
  mp_utils(sys.argv[1:])
except AssertionError as e:
  print('Whoops! {}'.format(e))
