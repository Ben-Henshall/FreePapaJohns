from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

user_agent = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " + "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36")

NUM_OF_POINTS_TO_STOP_ON = ["8", "12", "25"] # Number of points that you won't to stop trying on. 8, 12 or 25.

URL = "http://www.papajohns.co.uk/paparewards/"

WINNING_URLS = []

for points in NUM_OF_POINTS_TO_STOP_ON:
	winningurl = "http://www.papajohns.co.uk/paparewards/images/reveal-%s-points.gif" %points
	WINNING_URLS.append(winningurl)

EMAILNAME = "ilikespam"
EMAILPROVIDER = "@hotmail.co.uk"

NUM_TO_START_AT = 70
i = NUM_TO_START_AT

won = False
while not won:
	
	#while not won:
	driver = webdriver.Chrome()
	driver.set_window_size(600, 600)

	emailstring = "%s+%i%s" %(EMAILNAME, i, EMAILPROVIDER)

	print("Attempting to enter contest with %s." % emailstring)

	driver.get(URL)
	elem = driver.find_element_by_name("ctl00$cphBody$txtEmailAddressEnter")
	elem.send_keys(emailstring)

	elem = driver.find_element_by_id("ctl00_cphBody_btnNext")
	elem.click()

	loaded = False
	while not loaded:
		newurl = str(driver.current_url).split("?")
		if newurl[0] == "http://www.papajohns.co.uk/paparewards/play.aspx":
			loaded = True
			print "loaded page, waiting for wheel to spin"
			time.sleep(10)
		else:
			print "trying to load page"
			time.sleep(2)

	elem = driver.find_element_by_id("wheel")

	if elem.get_attribute('src') in WINNING_URLS:
		won = True
		print "YOU WON! FILL OUT YOUR DETAILS TO COLLECT!"
	else:
		print "Didn't win, rerolling"
		i += 1
		driver.close()
		