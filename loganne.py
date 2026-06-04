import os, sys, requests
from datetime import datetime

try:
	SYSTEM = os.environ["SYSTEM"]
except KeyError:
	sys.exit("\033[91mSYSTEM environment variable not set\033[0m")
try:
	LOGANNE_ENDPOINT = os.environ["LOGANNE_ENDPOINT"]
except KeyError:
	sys.exit("\033[91mLOGANNE_ENDPOINT environment variable not set - needs to be the URL of a running lucos_loganne instance\033[0m")

session = requests.Session()
session.headers.update({
	"User-Agent": SYSTEM,
	"Content-Type": "application/json",
})

VALID_LEVELS = {"detail", "routine", "notable", "headline"}

def updateLoganne(type: str, humanReadable: str, level: str, url: str = None, **extra_data):
	if level not in VALID_LEVELS:
		raise ValueError(f"Invalid level '{level}'. Must be one of: {', '.join(sorted(VALID_LEVELS))}")
	payload = {
		"type": type,
		"source": SYSTEM,
		"humanReadable": humanReadable,
		"level": level,
	}
	if url:
		payload["url"] = url
	payload.update(extra_data)
	try:
		loganne_response = session.post(LOGANNE_ENDPOINT, json=payload)
		loganne_response.raise_for_status()
	except Exception as error:
		print("\033[91m [{}] ** Error calling Loganne: {}\033[0m".format(datetime.now().isoformat(), error), flush=True)