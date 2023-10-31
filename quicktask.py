import os
import configparser

def load_config():
    config_file = os.path.expanduser('~/.config/quicktask/config.ini')
    vault = ''
    newly_created_config = False
    if os.path.exists(config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        vault = config.get('DEFAULT', 'obsidian_vault')
    else:
        # create directory if not exists
        if not os.path.exists(os.path.expanduser('~/.config/quicktask')):
            os.makedirs(os.path.expanduser('~/.config/quicktask'))

        # create config file
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'obsidian_vault': os.path.expanduser('~/obsidian')}
        with open(config_file, 'w') as configfile:
            config.write(configfile)
        vault = os.path.expanduser('~/obsidian')
        newly_created_config = True

    # for each folder in vault, find folder containing name 'inbox'
    for root, dirs, files in os.walk(vault):
        for name in dirs:
            # if name lower contains inbox
            if 'inbox' in name.lower():
                vault = os.path.join(root, name)
                break

    if newly_created_config:
        print(f'Using inbox folder: {vault}')
        print(f'Change this by editing {config_file}')

    return vault


def create_markdown(vault, title, contents):
    # create file vault
    file_name = f'{title}.md'
    file_path = os.path.join(vault, file_name)

    # if file already exists, ask user if want to replace
    # if replace delete, if not exit
    if os.path.exists(file_path):
        print(f'File already exists: {file_path}')
        replace = input("Replace? (y/n): ")
        if replace.lower() == 'y':
            os.remove(file_path)
        else:
            print('Exiting...')
            exit()

    # create file
    with open(file_path, 'w') as f:
        f.write(f'{contents}\n')
        # f.write(f'\n')
        # f.write(f'---\n')
        # f.write(f'Created by quicktask\n')

    print(f'Created file: {file_path}')

    # print out full file contents
    with open(file_path, 'r') as f:
        print(f.read())


def capture(vault):
    title = input("Title: ")
    contents = input("Note: ")

    create_markdown(vault, title, contents)

def main():

    vault = load_config()

    capture(vault)

if __name__ == '__main__':
    main()