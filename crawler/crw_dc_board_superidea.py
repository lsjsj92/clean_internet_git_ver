import crw_dc_handler, crw_dc_handler_selenium
import json, sys

url = url_list_data['superidea']
if len(sys.argv) <= 2 :
    print("please enter start page, end page\n ex ) python crw.py 1 10")
else :
    start_page = sys.argv[1]
    end_page = sys.argv[2]
crawler = crw_dc_handler_selenium.CrMain(url, 'superidea', start_page, end_page)
crawler.start()