def process_command(command):
    command = command.lower()

    if "open chrome" in command or "launch chrome" in command or "start chrome" in command:
        return "open_chrome"

    if "search youtube" in command or "youtube search" in command:
        return "search_youtube"

    return "unknown"