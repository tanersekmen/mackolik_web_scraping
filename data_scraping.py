from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time 
from bs4 import BeautifulSoup

#my_url = 'http://arsiv.mackolik.com/Iddaa-Programi'
#93.0.4577.63

class Scraping:
    def __init__(self, driver_path, option):
        """
            Parameters:
                driver_path: the driver that I used in my local area.
                option: determined how looks like my website that I opened in new window. 

        """
        options = Options()
        options.add_argument(option)
        self.website = 'http://arsiv.mackolik.com/Iddaa-Programi'
        self.driver = webdriver.Chrome(options=options, executable_path=driver_path)
        
        
    def teams(self):
        """
            Grabing all teams that has match the day that I pulled.
        """
        self.driver.get(self.website)
        self.page_source = self.driver.page_source
        time.sleep(2)
        soup = BeautifulSoup(self.page_source, 'html.parser')
        for team in soup.find_all('a', {'class':'iddaa-rows-style'}):
            with open('teams.txt', 'a', encoding = 'UTF-8') as f:
                f.write(team.text + '\n')


    def full_time_home(self):
        """
            Gets us the odds of the winning home team
        """
        self.driver.get(self.website)
        self.page_source = self.driver.page_source
        time.sleep(2)
        soup = BeautifulSoup(self.page_source, 'html.parser')
        for ft1 in soup.find_all('a', {'class':'iddaa-rate MS1'}):
            with open('ft1.txt', 'a', encoding = 'UTF-8') as f:
                f.write(ft1.text + '\n')


    def full_time_zero(self):
        """
            If match ends as an equal, taking what is the odds of it.
        """
        self.driver.get(self.website)
        self.page_source = self.driver.page_source
        time.sleep(2)
        soup = BeautifulSoup(self.page_source, 'html.parser')
        for eq in soup.find_all('a', {'class':'iddaa-rate MSX'}):
            with open('equal.txt', 'a', encoding = 'UTF-8') as f:
                f.write(eq.text + '\n')


    def full_time_away(self):
        
        """
            Gets us the odds of the winning away team
        """
        self.driver.get(self.website)
        self.page_source = self.driver.page_source
        time.sleep(2)
        soup = BeautifulSoup(self.page_source, 'html.parser')
        for ft2 in soup.find_all('a', {'class':'iddaa-rate MSX'}):
            with open('ft2.txt', 'a', encoding = 'UTF-8') as f:
                f.write(ft2.text + '\n')


    def under(self):
        """
            If the match finishes like under > 2.5 goals, this take of under of odds
        """        
        self.driver.get(self.website)
        self.page_source = self.driver.page_source
        time.sleep(2)
        soup = BeautifulSoup(self.page_source, 'html.parser')
        for und in soup.find_all('a', {'class':'iddaa-rate AU1'}):
            with open('under.txt', 'a', encoding = 'UTF-8') as f:
                f.write(und.text + '\n')


    def over(self):
        """
            If the match finishes like over > 2.5 goals, this take of over of odds
        """
        self.driver.get(self.website)
        self.page_source = self.driver.page_source
        time.sleep(2)
        soup = BeautifulSoup(self.page_source, 'html.parser')
        for ov in soup.find_all('a', {'class':'iddaa-rate AU2'}):
            with open('over.txt', 'a', encoding = 'UTF-8') as f:
                f.write(ov.text + '\n')


    def zero_or_one(self):
        """
            If thinking match ends equal or home team will win, it gets what is the odds of that.
        """
        self.driver.get(self.website)
        self.page_source = self.driver.page_source
        time.sleep(2)
        soup = BeautifulSoup(self.page_source, 'html.parser')
        for z_o_o in soup.find_all('a', {'class':'iddaa-rate CS1-X'}):
            with open('zero_or_one.txt', 'a', encoding = 'UTF-8') as f:
                f.write(z_o_o.text + '\n')


    def one_or_two(self):
        """
            If thinking match ends away or home team will win, it gets what is the odds of that.
        """
        self.driver.get(self.website)
        self.page_source = self.driver.page_source
        time.sleep(2)
        soup = BeautifulSoup(self.page_source, 'html.parser')
        for o_o_t in soup.find_all('a', {'class':'iddaa-rate CS1-2'}):
            with open('one_or_two.txt', 'a', encoding = 'UTF-8') as f:
                f.write(o_o_t.text + '\n')



    def zero_or_two(self):
        """
            If thinking match ends equal or away team will win, it gets what is the odds of that.
        """
        self.driver.get(self.website)
        self.page_source = self.driver.page_source
        time.sleep(2)
        soup = BeautifulSoup(self.page_source, 'html.parser')
        for z_o_t in soup.find_all('a', {'class':'iddaa-rate CSX-2'}):
            with open('zero_or_two.txt', 'a', encoding = 'UTF-8') as f:
                f.write(z_o_t.text + '\n')


    def both_teams_to_score(self):
        """
            If two team score then this odds can be used.
        """
        self.driver.get(self.website)
        self.page_source = self.driver.page_source
        time.sleep(4)
        choose_situation = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/table/tbody/tr[2]/td/div[1]/select')
        choose_situation.click()
        time.sleep(5)
        both_teams_score = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/table/tbody/tr[2]/td/div[1]/select/option[2]')
        both_teams_score.click()
        time.sleep(5)       
        self.page_source = self.driver.page_source
        soup = BeautifulSoup(self.page_source, 'html.parser')
        for score in soup.find_all('a', {'class':'iddaa-rate KG1'}):
            with open('both_teams_to_score.txt', 'a', encoding = 'UTF-8') as f:
                f.write(score.text + '\n')

    
    def both_teams_no_score(self):
        """
            If two team do not score then this odds can be used.
        """
        self.driver.get(self.website)
        self.page_source = self.driver.page_source
        time.sleep(4)
        choose_situation = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/table/tbody/tr[2]/td/div[1]/select')
        choose_situation.click()
        time.sleep(5)
        both_teams_score = self.driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[1]/div/table/tbody/tr[2]/td/div[1]/select/option[2]')
        both_teams_score.click()
        time.sleep(5)
        self.page_source = self.driver.page_source
        soup = BeautifulSoup(self.page_source, 'html.parser')
        for no_score in soup.find_all('a', {'class':'iddaa-rate KG0'}):
            with open('both_teams_no_score.txt', 'a', encoding = 'UTF-8') as f:
                f.write(no_score.text + '\n')

