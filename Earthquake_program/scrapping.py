from selenium import webdriver
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By


class ScrappingClass:
    def __init__(self):
        pass

    def returnerf(self,mode):

        mcdo = ChromeOptions()
        
        if mode == 'görünür':
            pass

        elif mode == 'görünmez':
            mcdo.add_argument("--window-position=-32000,-32000")

        driver = Chrome(options=mcdo)


        driver.get('https://deprem.afad.gov.tr/last-earthquakes.html')

        i1 = 0
        i0 = 1

        while True:
            try:
                xpath = f'/html/body/div[2]/table/tbody/tr[{i0}]/td[1]'
                driver.find_element(By.XPATH,xpath)

                i0 += 1
            except:
                i1 = i0
                print('2f')
                break
            
        for ij in range(1,i1):
            timecode_xpath = f'/html/body/div[2]/table/tbody/tr[{ij}]/td[1]'
            lat_xpath = f'/html/body/div[2]/table/tbody/tr[{ij}]/td[2]'
            lon_xpath = f'/html/body/div[2]/table/tbody/tr[{ij}]/td[3]'
            depth_xpath = f'/html/body/div[2]/table/tbody/tr[{ij}]/td[4]'
            type_xpath = f'/html/body/div[2]/table/tbody/tr[{ij}]/td[5]'
            magnitude_xpath = f'/html/body/div[2]/table/tbody/tr[{ij}]/td[6]'                
            loc_xpath = f'/html/body/div[2]/table/tbody/tr[{ij}]/td[7]'

            tcode_xpath = driver.find_element(By.XPATH,timecode_xpath).text
            lat_xpath = driver.find_element(By.XPATH,lat_xpath).text
            lon_xpath = driver.find_element(By.XPATH,lon_xpath).text
            depth_xpath = driver.find_element(By.XPATH,depth_xpath).text
            type_xpath = driver.find_element(By.XPATH,type_xpath).text
            magnitude_xpath = driver.find_element(By.XPATH,magnitude_xpath).text
            loc_xpath = driver.find_element(By.XPATH,loc_xpath).text

            yield [tcode_xpath,lat_xpath,lon_xpath,depth_xpath,type_xpath,magnitude_xpath,loc_xpath]
