from selenium import webdriver

from logging import config
config.fileConfig('dev.logger.conf')
from RetailLoyalty import RetailLoyalty

driver = webdriver.Chrome()

parser = RetailLoyalty(driver)
docs = parser.content()


print(*docs, sep='\n\r\n')