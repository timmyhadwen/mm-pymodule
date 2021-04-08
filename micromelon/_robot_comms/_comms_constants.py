from enum import Enum

DEFAULT_SPAM_INTERVAL_MS = 150
MIN_SPAM_INTERVAL_MS = 5


class CONNECTION_STATUS(Enum):
    NOT_CONNECTED = 0
    SEARCHING = 1
    CONNECTING = 2
    INTERROGATING = 3
    CONNECTED = 4
    DISCONNECTED = 5
    UPDATING = 6


class RUNNING_STATES(Enum):
    RUNNING = 5
    FINISHED = 1
    CLOSED = 0


class BUTTON_NOTIFICATION_CODES(Enum):
    START_STOP = 0
    COLOUR_CAL_COMPLETE = 8
    SLEEPING = 9


class MicromelonOpCode(Enum):
    READ = 0
    WRITE = 1
    ACK = 2
    NOTIFY = 3
    ERROR_INVALID_OP_CODE = 4
    ERROR_INVALID_PAYLOAD_SIZE = 5
    ERROR_INVALID_CHECKSUM = 6
    ERROR_NOT_IMPLEMENTED = 7


class MicromelonType(Enum):
    # Actuators
    MOTOR_SET = 0
    MOTOR_ENCODERS = 1
    TURN_DEGREES = 2
    RGBS = 3
    SERVO_MOTORS = 4
    BUZZER_TUNE = 5
    BUZZER_FREQ = 6

    # Sensors
    ACCL = 7
    GYRO = 8
    COLOUR_RGBW = 9
    COLOUR_HUE = 10
    COLOUR_ALL = 11
    TIME_OF_FLIGHT = 12
    ULTRASONIC = 13
    ROBOT_NAME = 14
    I2C_HEADER = 15

    # Versions
    HW_VERSION = 16
    FW_VERSION = 17

    # Util
    BUTTON_PRESS = 18
    BATTERY_VOLTAGE = 19
    STATE_OF_CHARGE = 20
    CURRENT_SENSOR = 21
    USB_VOLTAGE = 22

    # Advanced Util
    SENSOR_ERRORS = 23
    ENTER_OTA = 24
    CONFIG = 25
    CONTROL_MODE = 26

    ALL_SENSORS = 27
    MIN_SW_VERSION = 28

    MOTOR_TACHO = 29

    SPAM_MODE = 30
    SPAM_RATE = 31

    BOTID = 32
    GYRO_ACCUM = 33

    CALIBRATE_IMU = 34
    IDLE_LED_COLOUR = 35

    SIMULATOR_INFO = 36

    DISPLAY_TEXT = 37

    RPI_IMAGE = 150
    NETWORK_KEEP_ALIVE = 151
