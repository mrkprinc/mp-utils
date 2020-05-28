import sys
import os
import argparse

def functional_component(passed_args):
  p = argparse.ArgumentParser()
  p.add_argument('name')
  p.add_argument('--scss', action="store_true")
  p.add_argument('--path', default='.')
  args = p.parse_args(passed_args)

  name = args.name.capitalize()
  # normalize path
  path = args.path
  if path[-1] == '/':
    path = path[:-1]

  imports = [f"import styles from './{name}.module.scss'"]

  try:
    with open(os.path.join(sys.path[0], 'templates/FunctionComponent.txt')) as template_file, \
      open(f'{path}/{name}.tsx', 'x') as component_file, \
      open(f'{path}/{name}.module.scss', 'x'):

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
