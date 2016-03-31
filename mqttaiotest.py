# Import Adafruit IO MQTT client
from Adafruit_IO import MQTTClient
import time
#create the empty configuration file for AIO
config = {}

#fill the config files with the secure AIO details
execfile("aio_config.py", config)

#create the AIO_KEY and AIO_USER data
AIO_KEY = config["app_key"]
AIO_USER = config["user"]

FEED_TWEET_TEXT = "test"
FEED_SNAP = "button"

def connected(client):
	print 'Connected to Adafruit IO! Listening for changes...'
	client.subscribe(FEED_TWEET_TEXT)
	client.subscribe(FEED_SNAP)

check1 = ""
check2 = ""

def disconnected(client):
	print 'Disconnected from Adafruit IO!'
	sys.exit(1)

def message(client, feed_id, payload):
	#print 'Feed {0} received new value: {1}'.format(feed_id, payload)
	if feed_id == FEED_TWEET_TEXT:
		check1 = payload
		print payload
	else:
		check2 = payload
		print payload
client = MQTTClient(AIO_USER, AIO_KEY)

client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

client.connect()


print "Client is running in the background"

while True:
	client.loop()
	print check1
	time.sleep(5)
