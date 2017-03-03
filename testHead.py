import sys

if sys.platform.startswith('win32'):
    print('window')
elif sys.platform.startswith('linux'):
    print('linux')
elif sys.platform.startswith('darwin'):
    print('mac')


