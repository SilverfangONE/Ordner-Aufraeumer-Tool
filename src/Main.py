"""
CMD-Applications entry-point/ main-function
"""

# local-lib
import src.cli_commands as cli_com


def main():
    """
    entry point for cli application
    """
    cli_com.lunch()


if __name__ == "__main__":
    main()
