from data_scraping import Scraping


driver_path = 'Your chrome path'  
option = "--window-size=1920,1200"
mackolik = scraping(driver_path = driver_path, option = option)
mackolik.teams()
mackolik.full_time_home()
mackolik.full_time_zero()
mackolik.full_time_away()
mackolik.under()
mackolik.over()
mackolik.zero_or_one()
mackolik.zero_or_two()
mackolik.one_or_two()
mackolik.both_teams_to_score()
mackolik.both_teams_no_score()
