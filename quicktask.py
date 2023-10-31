import os
import configparser

def load_config():
    """
    Load config file from ~/.config/quicktask/config.ini
    """

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

        vault = os.path.expanduser('~/obsidian')

        # for each folder in vault, find folder containing name 'inbox'
        for root, dirs, files in os.walk(vault):
            for name in dirs:
                # if name lower contains inbox
                if 'inbox' in name.lower():
                    vault = os.path.join(root, name)
                    break

        # create config file
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'obsidian_vault': vault}
        with open(config_file, 'w') as configfile:
            config.write(configfile)
        vault = os.path.expanduser('~/obsidian')
        newly_created_config = True

    print(f'Using inbox folder: {vault}')

    if newly_created_config:
        print(f'Change this by editing {config_file}')

    return vault

def create_markdown(vault, title, contents):
    """
    Create markdown file in vault with title and contents
    """
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
        for line in contents:
            f.write(f'{line}\n')

    print(f'Created file: {file_path}')

    # print out full file contents
    # with open(file_path, 'r') as f:
        # print(f.read())

def capture(vault):
    """
    Capture user input and create markdown file
    """
    title = input("Title: ")

    contents = []
    print("Press enter (empty line) to save:")
    while True:
        line = input()
        if line == '':
            break
        contents.append(line)

    create_markdown(vault, title, contents)

def main():
    """
    Main function
    """
    # load vault path from config file
    vault = load_config()

    # capture user input
    try:
        capture(vault)
    except KeyboardInterrupt:
        print()
        pass

if __name__ == '__main__':
    main()