# This will show how to use command-line arguments.
def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Ola",
        "German": "Hallo"
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description= "Provides a personal greeting."
    )

    parser.add_argument(
        "-n", "--name", metavar="Name",
        required=True, help="The name of the person to greet."
    )
    
    parser.add_argument(
        "-l", "--lang", metavar="Language",
        required=True, choices=["English","Spanish","German"], help="The language of the person to greet."
    )

    args = parser.parse_args()

    hello(args.name, args.lang)