from dotenv import load_dotenv

from irctc.config import load_settings
from irctc.flows.booking_flow import BookingFlow


def main() -> None:
    load_dotenv()
    print("IRCTC booking helper")
    settings = load_settings()
    BookingFlow(settings).run()


if __name__ == "__main__":
    main()
