class DesconnectionError(Exception):
    def __init__(self):
        super().__init__(f"Detected Internet issues, cancelling operations")
