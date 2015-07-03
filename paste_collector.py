#!/usr/bin/env python

import requests;
from bs4 import BeautifulSoup;

class pastebin(object):
    """ Paste Collector bot """


    def __init__(self):
        """ booting it all up... """
        self.session = requests.Session();
        self.base_address = 'http://pastebin.com';

    def check(self):
        ''' Search Pastebin archive for new pastes '''
        raw_html = None;
        while not raw_html:
            try:
                raw_html = self.session.get(self.base_address + '/archive').text;
                results = BeautifulSoup(raw_html, 'lxml');
                for row in results.find_all('td'):
                    if(row.a and '/archive' not in row.a['href']):
                        print(self.base_address + row.a['href'] + " - " + row.a.string);
            except:
                print("error!");
                #raw_html = 'error';


if __name__ == "__main__":
    bot = pastebin();
    bot.check();
