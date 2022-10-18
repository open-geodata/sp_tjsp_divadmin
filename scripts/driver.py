"""


"""

import os
import time
import requests

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.options import Options

from webdriver_manager.firefox import GeckoDriverManager

from paths import *


# Credencials
from dotenv import dotenv_values, find_dotenv
#config = dotenv_values(find_dotenv(usecwd=False))
#os.environ['GH_TOKEN'] = config['GH_TOKEN']


# Set Options
options = Options()
options.headless = False


# By default, all driver binaries are saved to user.home/.wdm folder. (0)
# You can override this setting and save binaries to project.root/.wdm. (1)
os.environ['WDM_LOCAL'] = '0'
print(os.getenv('WDM_LOCAL'))


# Download Driver
driver_binary = GeckoDriverManager(
    # path=project_path,
    # path=None,
    cache_valid_range=30
).install()
print(f'>>>>>> {driver_binary}')


# Create Driver
driver = webdriver.Firefox(
    service=Service(
        executable_path=driver_binary,
        log_path=logs_path / 'geckodriver.log'
    ),
    options=options,
)


# Add-ons Xpath
xpath_path = adds_path / 'xpath.xpi'
xpath_path = xpath_path.absolute().resolve()
if not xpath_path.is_file():
    r = requests.get(
        'https://addons.mozilla.org/firefox/downloads/file/3588871/xpath_finder-1.0.2-fx.xpi')

    with open(xpath_path, 'wb') as f:
        f.write(r.content)

driver.install_addon(str(xpath_path), temporary=True)


if __name__ == '__main__':
    # Get Url
    driver.get('https://github.com/SergeyPirogov/webdriver_manager')

    # Close Connection
    time.sleep(4)
    driver.quit()

    # Message
    print('Driver close!!')
