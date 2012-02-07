#!/usr/bin/env python2.7

import BeautifulSoup
import cookielib
import csv
import json
import os
import subprocess
import sys
import urllib
import urllib2

COOKIE_FILE = 'cookies.lwp'

cj = cookielib.LWPCookieJar()

if os.path.isfile(COOKIE_FILE):
    cj.load(COOKIE_FILE)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)

class HotOrNotScraper(object):
    def scrape(self, csrf_header, login, rate):
        url = 'http://hotornot.com'
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        values = {'name' : 'Lloyd Henning',
              'location' : 'Manchester',
              'language' : 'Python', 
              'gender' : '2',
              '_method' : 'put',
              'csrf_authentication_token' : '08c50b0a6a83a9e5a09604d170a4bf74',
              'age' : '1',
              'set_rate_filter' : '1' }
        headers = { 'User-Agent' : user_agent}

        if login:
            values['password'] = 'SeyQ9Q3sYpqEut7b'
            values['login'] = 'clivesinclair'
            values['login_submit'] = ''
        values['csrf_authentication_token'] = csrf_header
        data = urllib.urlencode(values)
        if login:
            req = urllib2.Request("https://hotornot.com/users/login", data, headers)
        else:
            req = urllib2.Request(url, data, headers)
        print "Fetching page..."
        response = urllib2.urlopen(req)
        print "Reading page..."
        the_page = response.read()
        response.close()
        soup = BeautifulSoup.BeautifulSoup(the_page)
        usr = soup.findAll('a', id='usernameLoggedIn')
        #print usr
        sel = soup.findAll('option', selected='selected')
        #print sel
        img = soup.findAll('img', id='currentPhoto')
        print img[0].attrs[1][1]
        csrf = soup.findAll('input', attrs={'name' : 'csrf_authentication_token'})
        cj.save(COOKIE_FILE)    
        voted_on = soup.findAll('input', attrs={'name' : 'rating[voted_on_id]'})[0].attrs[2][1]
        votee_id = soup.findAll('input', attrs={'name' : 'rating[votee_id]'})[0].attrs[2][1]
        return (csrf, voted_on, votee_id)

    def rate(self, vote_on, votee):
        values = {}
        headers = {}
        values['rating[origin]'] = 'W'
        values['_method'] = 'post'
        values['rating[rating]'] = '5'
        values['rating[voted_on_gender]'] = 'f'
        values['rating[voted_on_id]'] = vote_on
        values['rating[votee_id]'] =   votee
        headers['X-Requested-With'] = 'XMLHttpRequest'
        headers['Referer'] = 'http://hotornot.com/rate'
        headers['Accept'] =  'application/json, text/javascript, */*'
        headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        data = urllib.urlencode(values)
        req2 = urllib2.Request("http://hotornot.com/rate/votes", data, headers)
        res = urllib2.urlopen(req2)
        update = res.read() 
        return json.loads(update)

    def list(self, csrf_header):
        values = {}
        headers = {}
        values['_method'] = 'post'
        headers['X-Requested-With'] = 'XMLHttpRequest'
        headers['Referer'] = 'http://hotornot.com/rate'
        headers['Accept'] =  'application/json, text/javascript, */*'
        headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'
        headers['User-Agent'] = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        data = urllib.urlencode(values)
        req2 = urllib2.Request("http://hotornot.com/rate/next_rating", data, headers)
        res = urllib2.urlopen(req2)
        update = res.read()
        return json.loads(update)


if __name__ == '__main__':
    hot_or_not_scraper = HotOrNotScraper()
    state = (c_h, vote_on, votee) = ('lol', '', '')
    state = hot_or_not_scraper.scrape(c_h, False, False)
    state = hot_or_not_scraper.scrape(c_h, True, True)

    our_id = votee
    with open('hotornot.csv', 'ab') as f:
        csv_writer = csv.writer(f)

        for count in range(100):
            for person in hot_or_not_scraper.list(c_h):
                print person['display_name']
                print person['pic_url']
                print person['score']
                print person['description']
                csv_writer.writerow([person['user_id'], person['display_name'].encode('utf8'), person['pic_url'], person['score'], person['num_votes'], person['age'], person['description'].encode('utf8')])
                p_id =  person['profile_id']
                subprocess.check_call(['wget', 'http://asset3-cdn.hotornot.com%s' % person['pic_url'], '-O', 'data/raw/%s-%s.jpg' % (person['user_id'], person['score'])])
                our_id = hot_or_not_scraper.rate(p_id, our_id)['r'] 
