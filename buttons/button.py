import RPi.GPIO as GPIO

# Generic button base (event -> trigger())

class GenericButtonHandler:
    """Base class for button logic (GPIO event)"""
    def __init__(
        self, 
        input_pin, 
        output_pin, 
        event=GPIO.RISING, 
        bouncetime=200
    ):
        self.input_pin = input_pin
        self.output_pin = output_pin
        self.event = event
        self.bouncetime = bouncetime

    # Pin setup (input with pull-down + output LOW)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup(input_pin)
        GPIO.setup(self.input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.output_pin, GPIO.OUT, initial=GPIO.LOW)

    # Default event registration
        self.setup_event_detection()

        print("Button instantiated")

    def setup_event_detection(self):
        """Set up event detection (overridable)"""
        GPIO.add_event_detect(
            self.input_pin,
            self.event,
            callback=self.trigger,
            bouncetime=self.bouncetime
        )

    def trigger(self, pin):
        """Implemented by concrete button class"""
        pass
