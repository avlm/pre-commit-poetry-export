import hashlib
import os


def get_content_md5(file_path):
    with open(file_path, 'r') as file_handler:
        content = file_handler.read()
        content_md5 = hashlib.md5()
        content_md5.update(content.encode('utf-8'))
        return content_md5.hexdigest()


def main(argv=None):
    old_requirements_path = 'old.requirements.txt'
    requirements_path = 'requirements.txt'

    if not os.path.exists(requirements_path):
        os.system(f'poetry export -f requirements.txt > {requirements_path}')
        print('requirements.txt created')
        return 1

    if os.path.exists(old_requirements_path):
        os.remove(old_requirements_path)

    os.system('mv requirements.txt old.requirements.txt')
    os.system(f'poetry export --dev -f requirements.txt > {requirements_path}')
    requirements_hash = get_content_md5(requirements_path)
    old_requirements_hash = get_content_md5(old_requirements_path)
    os.remove(old_requirements_path)

    if requirements_hash == old_requirements_hash:
        return 0

    print('requirements.txt updated!')
    return 1


if __name__ == '__name__':
    exit(main())
