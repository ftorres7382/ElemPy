import sys
import argparse
import json
import typing as tp
import platform

from backend import index


settings_path = "settings.json"


def main() -> None:
    parser = argparse.ArgumentParser(description="Runs a Visual python scripting software")

    # Add arguments
    parser.add_argument("--validate_types", help="Validates the types of the functions using mypy in strict mode", action="store_true")

    # Parse the arguments
    args = parser.parse_args()

    # Show index html
    index.run()


def show_warning_error(message: str, error: bool = False, error_type: tp.Union[tp.Type[Exception]] = Exception) -> None:
    if error:
        raise error_type(message)
    else:
        print("WARNING! " + message)

    


if __name__ == "__main__":


    # Do required setup

    ## Import settings
    with open(settings_path, "r") as settings_file:
        settings = json.load(settings_file)

    ## Do required checks

    ### Check supported OS
    if platform.system() not in settings["supported_os"]:
        message = f"Unsupported OS: {platform.system()}. Supported OSs are {settings['supported_os']}"
        show_warning_error(message, error=settings["strict_os"], error_type=Exception)
    
    ### Check supported python version
    python_version = sys.version.split(" ")[0]
    if python_version not in settings["supported_python_versions"]:
        message = f"Unsupported Python version: {python_version}. Supported Python versions are {settings['supported_python_versions']}"
        show_warning_error(message, error=settings["strict_python_version"], error_type=Exception)
    



    
    # Run main
    main()
