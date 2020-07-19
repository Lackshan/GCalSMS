class GCalAppointment:

    phone_number = ''
    start_time = ''
    end_time = ''
    message_text = ''

    def __init__(self, phone_number, start_time, end_time, message_text):
        self.phone_number = self.__sanitise_phone_number(phone_number)
        self.start_time = start_time
        self.end_time = end_time
        self.message_text = message_text

    @staticmethod
    def __sanitise_phone_number(phone_number):
        if type(phone_number) is str:
            if phone_number[:2] is '01':
                return '+6' + phone_number
            elif phone_number[:2] is '60':
                return '+' + phone_number
            elif phone_number[:2] is '+6':
                return phone_number
            else:
                raise ValueError('Phone number is invalid. Please make sure it starts with ')
        else:
            raise TypeError('Phone number is not a string')



####### BLUEPRINT
## Phone number accepts 012...., 6012..... and +6012...
## Output +6012....

## Times check for correct type and format

#### Documentation Notes
## Mention phone no sanitisation is only for malaysia

