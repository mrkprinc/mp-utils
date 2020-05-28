#!/usr/bin/env python3
import sys
import argparse
import redux_constants
import functional_component

tools = {
  'redux-const': redux_constants.default,
  'component': functional_component.default
}

def unknown_tool(_args):
  raise AssertionError('This tool is not in my box :(')

p = argparse.ArgumentParser()
p.add_argument('tool')
p.add_argument('--scss', action="store_true")
options, pass_args = p.parse_known_args()

try:
  tools.get(options.tool, unknown_tool)(pass_args, options)
except AssertionError as e:
  print('Whoops! {}'.format(e))
