# -*- coding: utf-8 -*-
"""
Created on Mon May 28 13:20:19 2018

@author: SilverDoe
"""

'''
Personally I would recommend lxml over BeautifulSoup. lxml can be a pain to install
 because of it's dependencies, but it is a newer, higher performance library which 
 implements the ElementTree API and which features lend to more reliable code, for 
 example lxml does not use 'magic attributes'. lxml also supports css selectors which
 is basically awesome. (I love to talk about the merits of lxml but this is not the 
 place to enumerate them, suffice to say it's a great library and you will profit from
 having it in your skillset)
 
'''

import time
import queue
from threading import Thread
import lxml.html

def process_queue(url_queue, seen, domain):
    while True:
        try:
            url = None
            url = url_queue.get_nowait()
            print('Processing {}'.format(url))
            # Download and parse url
            root = lxml.html.parse(url).getroot()
            # Rewrite relative urls to absolute urls
            root.make_links_absolute(url)
            # Select all elements with href element.
            for e in root.cssselect('[href]'):
                # Discard bookmarks
                href = e.get('href').split('#')[0]
                # Filter external links, and already added links
                if href.startswith(domain) and href not in seen:
                   seen.add(href)
                   url_queue.put(href)
                   # There is a miniscule chance of href being added to queue 
                   # twice. It will just be processed twice. That's all.
            for e in root.iter('p'):
                p_text = e.text_content()
                # ... do something with text of paragraph
        except queue.Empty:
            # Nothing left to do
            return

        finally:
            if url is not None:
                # If we popped a task, mark as complete.
                url_queue.task_done()

def crawl(domain, num_threads=4):
    url_queue = queue.Queue()
    url_queue.put(domain)
    seen = set()
    for i in range(0, num_threads):
        t = Thread(target=process_queue, kwargs={"url_queue": url_queue, "seen": seen, "domain": domain})
        t.start()
        time.sleep(1) # Stagger thread start.
    # Wait for the queue to become empty.
    url_queue.join()
    print('All done!')

if __name__ == '__main__':
    crawl('http://www.wccftech.com', 4)