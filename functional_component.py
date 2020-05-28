import sys
import os

def functional_component(args):
  assert args, 'This tool needs args.'

  name = args[0].capitalize()
  path = '.' if len(args) == 1 else args[1]

  # normalize path
  if path[-1] == '/':
    path = path[:-1]

  try:
    with open(os.path.join(sys.path[0], 'templates/FunctionComponent.txt')) as template_file, \
      open(f'{path}/{name}.tsx', 'x') as component_file, \
      open(f'{path}/{name}.module.scss', 'x'):

      component = template_file.read().format(name = name)
      component_file.write(component)
      pass
  except FileNotFoundError:
    print('I\'m lost - that path doesn\'t exist :(')
  except FileExistsError:
    print('This component file already exists.')

default = functional_component
