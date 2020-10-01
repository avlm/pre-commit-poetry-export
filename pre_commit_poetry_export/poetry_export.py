import hashlib
import os


def main(argv=None):
    os.system('cp requirements.txt old.requirements.txt')
    os.system('poetry export -f requirements.txt > requirements.txt')

    with open('requirements.txt', 'r') as new,\
            open('old.requirements.txt', 'r') as old:
        new_content = new.read()
        new.close()
        new_md5 = hashlib.md5()
        new_md5.update(new_content.encode('utf-8'))

        old_content = old.read()
        old.close()
        old_md5 = hashlib.md5()
        old_md5.update(old_content.encode('utf-8'))

    if new_md5.hexdigest() == old_md5.hexdigest():
        os.system('rm old.requirements.txt')
        return 0

    print('requirements.txt updated!')
    return 1


if __name__ == '__name__':
    exit(main())
