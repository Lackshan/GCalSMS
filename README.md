# GCalSMS
GCalSMS is a Python SMS Server that is triggered by Google Calendar events. More specifically, it checks a Google account's calendar for patient appointments and sends them reminders. It can work with either Celcom's Omni messaging service or a Raspberry Pi with a Waveshare GSM HAT.

## Getting Started
### Prerequisites
GCalSMS needs Python 3.7 (64-bit). Venv is recommended to manage dependencies.

### Installing Dependencies
Navigate to the root directory.
```bash
cd GCalSMS
```

Install the dependencies in requirements.txt with:
```bash
pip install -r requirements.txt
```
Depending on your system installation of Python you may need to use ```pip3``` instead of ```pip```.

## Usage
### main.py
You should use main.py if you want to run this module from the commandline. You can run it with:
```bash
python3 main.py 'CelcomOmni' '[1 day, 3 days, 1 week]'
```
or
```bash
python3 main.py 'WaveshareGSM' '[1 day, 3 days, 1 week]'
```

### gcalsms module
Coming soon!

## Tests
Coming soon!

## Deployment
### Crontab
Coming soon!

### Docker
Coming soon!