from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--disable-images")
options.add_argument("--disable-popup-blocking")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
