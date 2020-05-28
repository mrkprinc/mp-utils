def redux_constants(args, _options):
  assert args, 'This tool needs args.'

  base = '_'.join(args).upper()
  constants = """{0} = '{0}',
  {0}{1} = '{0}{1}',
  {0}{2} = '{0}{2}',
  {0}{3} = '{0}{3}',
""".format(base, '_PENDING', '_FULFILLED', '_REJECTED')
  print(constants)

default = redux_constants
