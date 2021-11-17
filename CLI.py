import sys
import core

args = sys.argv
for i in range(0, len(args)):
    arg = args[i]
    if arg == '-i':
        path = args[i + 1]
        images = core.get_images(path)
        if args[i + 2] == '-o':
            output = args[i + 3]
            print(output)
            core.apply_filters(images, output)
