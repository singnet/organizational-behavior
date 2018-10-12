# Tested on python2.7

import db_interface
from textblob import TextBlob
import logging
import re
import sys
import time



class SentimentAnalysis:



    bad_texts = ['has joined the channel','has left the channel']

    def __init__(self,db):


        self.db = db
        self.non_alpha_counter = 0
        self.bad_texts_counter = 0



    def create_sentiment(self):

        d = db_interface.DbInterface(self.db)

        sentiments = []

        try:
            q = """SELECT * from message"""
            d.cursor.execute((q))
            rows = d.cursor.fetchall()
            i = 0
            len_rows = len(rows)
            self.start_time = time.time()
            for row in rows:

                try:

                    if self.is_non_alpha_numeric(row['text']):
                        self.non_alpha_counter = self.non_alpha_counter + 1
                        continue
                    if self.contains_x(row['text']):
                        self.bad_texts_counter = self.bad_texts_counter + 1
                        continue

                    sentiments.append({"id":row['id'],"value":TextBlob(row['text'].decode("utf8")).sentiment.polarity})

                    self.print_progress(i, len_rows - 1, prefix='',
                                        suffix='of sentiment evaluations done in ' + str(
                                            int((time.time() - self.start_time))) + ' seconds', barLength=50)
                    i = i + 1


                except Exception as e:

                    logging.exception("message")

            self.print_progress(len_rows - 1, len_rows - 1, prefix='',
                                suffix='of sentiment evaluations done in ' + str(
                                    int((time.time() - self.start_time))) + ' seconds', barLength=50)

            sentiments_tuple = tuple(sentiments)

            d.cursor.executemany("""INSERT INTO sentiment(id,value) VALUES (%(id)s, %(value)s)""", sentiments_tuple)

            print('Sentiment values inserted into db.')



        except Exception as e:

            logging.exception("message")


        print('self.non_alpha_counter=',self.non_alpha_counter)
        print('self.bad_texts_counter=',self.bad_texts_counter)




    def is_non_alpha_numeric(self,text):

        text = re.sub('[^A-Za-z0-9]', '', text)
        return True if text == '' else False

    def contains_x(self,text):

        for bt in self.bad_texts:
            if bt in text:
                return True

        return False


    def print_progress (self,iteration, total, prefix = '', suffix = '', decimals = 0, barLength = 100):
        """
        Call in a loop to create terminal progress bar
        @params:
            iterations  - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
        """
        filledLength    = int(round(barLength * iteration / float(total)))
        percents        = round(100.00 * (iteration / float(total)), decimals)
        bar             = '#' * filledLength + '-' * (barLength - filledLength)
        sys.stdout.write('%s [%s] %s%s %s\r' % (prefix, bar, str(percents)[:-2], '%', suffix)),
        sys.stdout.flush()
        if iteration == total:
            print("\n")






def run_1():

    s = SentimentAnalysis('local')
    s.create_sentiment()











__end__ = '__end__'


if __name__ == '__main__':

    run_1()

    pass