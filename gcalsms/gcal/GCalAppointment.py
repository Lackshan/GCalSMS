class GCalAppointment:

    """
    A class that is a facade for Google Calender appointments
    """
    phone_number = ''
    region = ''
    start_time = ''
    end_time = ''
    message_text = ''

    def __init__(self, phone_number, region, start_time, end_time, message_text=''):
        """
        Initialises the class. All args are required except message_text
        :param phone_number: Any mobile number with or without a country code as a str
        :param region: ISO 3166-1 alpha-2 country code
        :param start_time:
        :param end_time:
        :param message_text: str, optional, defaults to ''
        """
        if region is '' or None:
            raise ValueError('region cannot be an empty string or None.')

        self.phone_number = self.__sanitise_phone_number(phone_number, region)
        self.region = region
        self.start_time = start_time
        self.end_time = end_time
        self.message_text = message_text

    @staticmethod
    def __sanitise_phone_number(phone_number, region):
        """
        Checks type of phone_number and if it's a string, sanitizes it.
        :param phone_number: A string that is a phone number.
        :param region: ISO 3166-1 alpha-2 country code.
        :return: phone number with country code as a str
        """
        if region is 'MY':
            if type(phone_number) is str:
                if phone_number[:2] is '01':
                    return '+6' + phone_number
                elif phone_number[:3] is '601':
                    return '+' + phone_number
                elif phone_number[:4] is '+601':
                    return phone_number
                else:
                    raise ValueError('Phone number is invalid. Please make sure it starts with 01, 601 or +601.')
            else:
                raise TypeError('Phone number is not a string')

        else:
            print('Warning! Phone number sanitization is only available for Malaysian phone numbers.')
            return phone_number

    @staticmethod
    def __sanitise_time(appointment_time):
        pass



####### BLUEPRINT

## Times check for correct type and format

#### Documentation Notes
## Mention phone no sanitisation is only for malaysia

