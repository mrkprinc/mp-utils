import sys
import os
import argparse
from contextlib import ExitStack

def functional_component(passed_args):
  p = argparse.ArgumentParser()
  p.add_argument('name', nargs='*')
  p.add_argument('--scss', action="store_true")
  p.add_argument('--index', action="store_true")
  p.add_argument('--path', default='.')
  args = p.parse_args(passed_args)
  print(args)

  name = ''.join(map(lambda s:s.capitalize(), args.name))
  # normalize path
  path = args.path
  if path[-1] == '/':
    path = path[:-1]

  imports = []

  try:
    with ExitStack() as stack:
      template_file = stack.enter_context(open(os.path.join(sys.path[0], 'templates/FunctionComponent.txt')))
      component_file = stack.enter_context(open(f'{path}/{name}.tsx', 'x'))

      if args.scss:
        stack.enter_context(open(f'{path}/{name}.module.scss', 'x'))
        imports.append(f"import styles from './{name}.module.scss'")
      if args.index:
        index_file = stack.enter_context(open(f'{path}/index.ts', 'x'))
        index_file.write(f'import {name} from \'./{name}\'\n\nexport default {name}\n')

      component = template_file.read().format(
        name = name,
        imports = '\n'.join(imports)
      )
      component_file.write(component)
  except FileNotFoundError:
    print('I\'m lost - that path doesn\'t exist :(')
  except FileExistsError:
    print('This component file already exists.')

default = functional_component
