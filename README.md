# QuickTask

QuickTask is a Python program that allows you to quickly create Markdown files in your Obsidian vault. It's designed to streamline the process of capturing thoughts, ideas, and notes by creating a simple text-based interface for creating new notes.

## Installation

Before you start using QuickTask, you need to make sure you have Python 3 installed on your system. You can download and install Python from the [official Python website](https://www.python.org/downloads/).

To use QuickTask, follow these steps:

1. Clone this repository to your local machine:

2. Change to the QuickTask directory:

   ```bash
   cd quicktask
   ```

3. Make the script executable:

   ```bash
   chmod +x quicktask.py
   ```

4. Run QuickTask:

   ```bash
   ./quicktask.py
   ```

## Command

Use create_exec.sh or create_symbolic_link.sh to create system wide `quicktask` command.

## Usage

QuickTask has a simple and intuitive interface for creating Markdown files in your Obsidian vault. When you run the program, you'll be prompted to provide a title and then enter the contents of the note. To create the note, simply press Enter on an empty line.

If a note with the same title already exists in your vault, QuickTask will ask if you want to replace it. You can confirm by typing 'y' or cancel by typing 'n'.

## Configuration

QuickTask uses a configuration file to determine the location of your Obsidian vault. By default, it looks for the configuration file at `~/.config/quicktask/config.ini`. If the configuration file does not exist, QuickTask will attempt to create it and set the vault location.

You can manually edit the configuration file to change the vault location if needed.

### Example Configuration

```ini
[DEFAULT]
obsidian_vault = /path/to/your/vault
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

This tool is created by [chrisbrasington](github.com/chrisbrasington).

Happy note-taking!
