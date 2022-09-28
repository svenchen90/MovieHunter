# -*- coding: utf-8 -*-
from datetime import datetime
import random
import re
import threading
import urllib2

from mongoengine.connection import connect

from shutter.models import Genre, Mongo_Genre, Mongo_Occupation, Occupation, \
    Mongo_User, User, Mongo_Movie, Movie


class data_generation():
    def genre_gen(self):
        genre_list = ['Action','Adventure','Animation','Children`s','Comedy','Crime','Documentary','Drama',
                      'Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western']
        file_genre_mysql = open('D:/data/mysql/genre.sql','a')
        file_genre_mongo = open('D:/data/mongo/genre.dat','a')
        
        file_genre_mysql.write('INSERT INTO shutter_genre (id,name) VALUES\n')
        
        for idx,genre in enumerate(genre_list):
            if idx != len(genre_list) -1:
                file_genre_mysql.write('('+ str(idx+1) + ',\'' + genre + '\'),\n')
                file_genre_mongo.write('{ \"name\" : \"' + genre + '\" }\n')
            else:
                file_genre_mysql.write('('+ str(idx+1) + ',\'' + genre + '\');')
                file_genre_mongo.write('{ \"name\" : \"' + genre + '\" }')
        
        file_genre_mysql.close()
        file_genre_mongo.close()
        
    def state_gen(self):
        state_tax_map = {'AL' : 0.04,
                            'AK' : 0,
                            'AZ' : 0.056,
                            'AR' : 0.065,
                            'CA' : 0.075,
                            'CO' : 0.029,
                            'CT' : 0.0635,
                            'D.C.' : 0.0575,
                            'DE' : 0,
                            'FL' : 0.06,
                            'GA' : 0.04,
                            'HI' : 0.04,
                            'ID' : 0.06,
                            'IL' : 0.0625,
                            'IN' : 0.07,
                            'IA' : 0.06,
                            'KS' : 0.0615,
                            'KY' : 0.06,
                            'LA' : 0.04,
                            'ME' : 0.055,
                            'MD' : 0.06,
                            'MA' : 0.0625,
                            'MI' : 0.06,
                            'MN' : 0.06875,
                            'MS' : 0.07,
                            'MO' : 0.04225,
                            'MT' : 0,
                            'NE' : 0.055,
                            'NV' : 0.0685,
                            'NH' : 0,
                            'NJ' : 0.07,
                            'NM' : 0.05125,
                            'NY' : 0.04,
                            'NC' : 0.0475,
                            'ND' : 0.05,
                            'OH' : 0.0575,
                            'OK' : 0.045,
                            'OR' : 0,
                            'PA' : 0.06,
                            'RI' : 0.07,
                            'SC' : 0.06,
                            'SD' : 0.04,
                            'TN' : 0.07,
                            'TX' : 0.0625,
                            'UT' : 0.0595,
                            'VT' : 0.06,
                            'VA' : 0.053,
                            'WA' : 0.065,
                            'WV' : 0.06,
                            'WI' : 0.05,
                            'WY' : 0.05}
        file_state_mysql = open('D:/data/mysql/state.sql','a')
        file_state_mongo = open('D:/data/mongo/state.dat','a')
        
        file_state_mysql.write('INSERT INTO shutter_state (id,name,tax_rate) VALUES\n')
        for idx,key in enumerate(state_tax_map):
            if idx == len(state_tax_map)-1:
                file_state_mysql.write('(' + str(idx+1) +',\''+ key + '\',' + str(state_tax_map[key]) + ');')
                file_state_mongo.write('{ \"name\" : \"' + key + '\", \"tax_rate\" : ' + str(state_tax_map[key]) +' }')
            else:
                file_state_mysql.write('(' + str(idx+1) +',\''+ key + '\',' + str(state_tax_map[key]) + '),\n')
                file_state_mongo.write('{ \"name\" : \"' + key + '\", \"tax_rate\" : ' + str(state_tax_map[key]) +' }\n')
        
        file_state_mysql.close()
        file_state_mongo.close()
    def occupation_gen(self):
        occupation_list = ["other",
                            "academic/educator",
                            "artist",
                            "clerical/admin",
                            "college/grad student",
                            "customer service",
                            "doctor/health care",
                            "executive/managerial",
                            "farmer",
                            "homemaker",
                            "K-12 student",
                            "lawyer",
                            "programmer",
                            "retired",
                            "sales/marketing",
                             "scientist",
                            "self-employed",
                            "technician/engineer",
                            "tradesman/craftsman",
                            "unemployed",
                            "writer"]
        file_occupation_mysql = open('D:/data/mysql/occupation.sql','a')
        file_occupation_mongo = open('D:/data/mongo/occupation.dat','a')
        
        file_occupation_mysql.write('INSERT INTO shutter_occupation (id,name) VALUES\n')
        for idx,occupation in enumerate(occupation_list):
            if idx != len(occupation_list)-1:
                file_occupation_mysql.write('('+ str(idx+1) + ',\'' + occupation + '\'),\n')
                file_occupation_mongo.write('{ \"name\" : \"' + occupation + '\" }\n')
            else:
                file_occupation_mysql.write('('+ str(idx+1) + ',\'' + occupation + '\');')
                file_occupation_mongo.write('{ \"name\" : \"' + occupation + '\" }')
        
        file_occupation_mysql.close()     
        file_occupation_mongo.close()
        
    def movie_local_gen(self):
        file_movie = open('D:/data/ml-1m/ml-1m/movies.dat')
        movie_list = file_movie.readlines()
        
        mysql_genre = Genre.objects.all()
        connect('Mongo_Shutter')
        mongo_genre = Mongo_Genre.objects.all()
        mysql_genre_map = {}
        mongo_genre_map = {}
        for g in mysql_genre:
            mysql_genre_map[g.name] = g.id
        for g in mongo_genre:
            mongo_genre_map[g.name] = str(g.id) 
        
        file_movie_mysql = open('D:/data/mysql/movie.sql','a')
        file_movie_genre_mysql = open('D:/data/mysql/movie_genre.sql','a')
        file_movie_mongo = open('D:/data/mongo/movie.dat','a')
        
        file_movie_mysql.write('INSERT INTO shutter_movie (id,title,year) VALUES\n')
        file_movie_genre_mysql.write('INSERT INTO shutter_movie_genre (movie_id,genre_id) VALUES\n')
        
        for idx,movie in enumerate(movie_list):
            movie = re.sub(r'[^\x00-\x7F]*\n*',r'',movie)
            movie = re.sub(r'\'',r'`',movie)

            id, title_year,genres = re.split(r'::', movie)
            title = re.sub(r'\(\d{4}\)$', r'', title_year)
            year = re.search(r'\d{4}', re.search(r'\(\d{4}\)$', title_year).group()).group()
            genres = re.split(r'\|', genres)
            genres_mysql = [mysql_genre_map[g] for g in genres]
            #genres_mongo = [mongo_genre_map[g] for g in genres]
            genres_mongo = [{ '$oid' :   mongo_genre_map[g] }  for g in genres]

            if idx != len(movie_list)-1:
                file_movie_mysql.write('('+ id + ',\'' + title + '\' , ' + year + '),\n')
                for g_idx,g in enumerate(genres_mysql):
                    file_movie_genre_mysql.write('('+ id + ', ' + str(g) +'),\n')
                file_movie_mongo.write('{\"title\" : \"' + title + '\", \"year\" : \"' + year + '\", "genre" : ' + str(genres_mongo) + '}\n')
            else:
                file_movie_mysql.write('('+ id + ',\'' + title + '\' , ' + year + ');')
                for g_idx,g in enumerate(genres_mysql):
                    if g_idx != len(genres_mysql)-1:
                        file_movie_genre_mysql.write('('+ id + ', ' + str(g) +'),\n')
                    else:
                        file_movie_genre_mysql.write('('+ id + ', ' + str(g) +');')
                file_movie_mongo.write('{\"title\" : \"' + title + '\", \"year\" : \"' + year + '\", "genre" : ' + str(genres_mongo) + '}')
    
        file_movie.close()
        file_movie_mysql.close()
        file_movie_genre_mysql.close()
        file_movie_mongo.close()
        
    def user_gen(self):
        file_random_name = open('D:/data/ml-1m/ml-1m/random_name.dat')
        name_list = file_random_name.readlines()
        first_list = [re.split(r'\s+' ,name)[0]  for name in name_list]
        last_list = [re.split(r'\s+' ,name)[1]  for name in name_list]
        #print random.choice(first_list)
        
        file_user = open('D:/data/ml-1m/ml-1m/users.dat')
        user_list = file_user.readlines()
        file_user_mysql = open('D:/data/mysql/user.sql','a')
        file_user_mongo = open('D:/data/mongo/user.dat','a')
        
        file_user_mysql.write('INSERT INTO shutter_user (id,account,password,user_type,first,last,gender,occupation_id,zip) VALUES\n')
        
        for idx,user in enumerate(user_list):
            user = re.sub(r'\n',r'',user)
            id, gender, age ,occupation, zip  =  re.split(r'::',user)
            connect('Mongo_Shutter')
            if idx != len(user_list)-1:
                file_user_mysql.write('('+ id + ',\'account_' + id + '\' , \'password\' , 1 , \'' + random.choice(first_list) +'\' , \'' + random.choice(last_list) + '\' , ' + str(0 if gender == 'M' else 1) + ' , ' + str(int(occupation)+1) + ' , \'' + zip +'\' ),\n')
                file_user_mongo.write('{"account" : "account_' + id + '", "password" : "password", "user_type" : 1, "first" : "' + random.choice(first_list) + '", "last" : "' + random.choice(last_list) + '", "gender" : ' + str(0 if gender == 'M' else 1) + ', "occupation" : { "$oid" : "' + str(Mongo_Occupation.objects.filter(name = Occupation.objects.filter(id = int(occupation)+1)[0].name)[0].id) + '" }, "zip" : "' + zip + '"}\n')
            else:
                file_user_mysql.write('('+ id + ',\'account_' + id + '\' , \'password\' , 1 , \'' + random.choice(first_list) +'\' , \'' + random.choice(last_list) + '\' , ' + str(0 if gender == 'M' else 1) + ' , ' + str(int(occupation)+1) + ' , \'' + zip +'\' );')
                file_user_mongo.write('{"account" : "account_' + id + '", "password" : "password", "user_type" : 1, "first" : "' + random.choice(first_list) + '", "last" : "' + random.choice(last_list) + '", "gender" : ' + str(0 if gender == 'M' else 1) + ', "occupation" : { "$oid" : "' + str(Mongo_Occupation.objects.filter(name = Occupation.objects.filter(id = int(occupation)+1)[0].name)[0].id) + '" }, "zip" : "' + zip + '"}')
        
        file_random_name.close()
        file_user.close()
        file_user_mysql.close()
        file_user_mongo.close()
        
    def rating_gen(self):
        #print datetime.utcfromtimestamp(978300760)
        file_rating = open('D:/data/ml-1m/ml-1m/ratings.dat')
        file_user_dictionary = open('D:/data/dump_20140614/user_dictionary.dat')
        file_movie_dictionary = open('D:/data/dump_20140614/movie_dictionary.dat')
        file_rating_mysql = open('D:/data/mysql/rating.sql','a')
        file_rating_mongo = open('D:/data/mongo/rating.dat','a')
        rating_list = file_rating.readlines()
        user_dictionary_list = file_user_dictionary.readlines()
        movie_dictionary_list = file_movie_dictionary.readlines()
        user_dictionary = {}
        movie_dictionary = {}
        for user_d in user_dictionary_list:
            user_d = re.sub(r'\n',r'',user_d)
            mysql_id, mongo_id = re.split(r'::',user_d)
            user_dictionary[mysql_id] = mongo_id
        
        for movie_d in movie_dictionary_list:
            movie_d = re.sub(r'\n',r'',movie_d)
            mysql_id, mongo_id = re.split(r'::',movie_d)
            movie_dictionary[mysql_id] = mongo_id
        
        #file_rating_mysql.write('INSERT INTO shutter_rating (movie_id,user_id,rates,time) VALUES\n')
        for idx,rating in enumerate(rating_list):
            rating = re.sub(r'\n',r'',rating)
            user_id,movie_id,rating,timestamp = re.split(r'::',rating)
            time = datetime.utcfromtimestamp(float(timestamp))
            
            if idx != len(rating_list)-1:
                #file_rating_mysql.write('('+ movie_id + ' , ' + user_id + ',\'' + rating + '\' , \'' + str(time) +'\'),\n')
                file_rating_mongo.write('{"movie" : { "$oid" : "' + movie_dictionary[movie_id] + '" }, "user" : { "$oid" : "' + user_dictionary[user_id] + '" }, "rates" : ' + rating + ', "time" : { "$date" : "' + re.sub(r' ',r'T' ,str(time)) + 'Z" } }\n')
            else:
                #file_rating_mysql.write('('+ movie_id + ' , ' + user_id + ',\'' + rating + '\' , \'' + str(time) +'\');')
                file_rating_mongo.write('{"movie" : { "$oid" : "' + movie_dictionary[movie_id] + '" }, "user" : { "$oid" : "' + user_dictionary[user_id] + '" }, "rates" : ' + rating + ', "time" : { "$date" : "' + re.sub(r' ',r'T' ,str(time)) + 'Z" } }')
            
        file_rating.close()
        file_user_dictionary.close()
        file_movie_dictionary.close()
        file_rating_mysql.close()
        file_rating_mongo.close()
    
    def mongo_rating_divide(self):
        file_rating = open('D:/data/mongo/rating.dat')
        rating_list = file_rating.readlines()
        
        for idx,rating in enumerate(rating_list):
            if idx%100000 == 0:
                file = open('D:/data/mongo/rating/rating_' + str(idx/100000) + '.dat','a')
            
            file.write(rating)
            
            if idx%100000 == 99999 or idx == len(rating_list)-1:
                file.close()
        file_rating.close()
    
    def user_dictionary(self):
        file_user_dictionary = open('D:/data/dump_20140614/user_dictionary.dat','a')
        connect('Mongo_Shutter')
        mongo_user = Mongo_User.objects.all()
        for user in mongo_user:
            id = User.objects.filter(account = user.account)[0].id
            file_user_dictionary.write(str(id) + '::' + str(user.id) +'\n')
        file_user_dictionary.close()
        
    def movie_dictionary(self):
        file_movie_dictionary = open('D:/data/dump_20140614/movie_dictionary.dat','a')
        connect('Mongo_Shutter')
        mongo_movie = Mongo_Movie.objects.all()
        for movie in mongo_movie:
            id = Movie.objects.filter(title = movie.title, year = movie.year)[0].id
            file_movie_dictionary.write(str(id) + '::' + str(movie.id) +'\n')
        file_movie_dictionary.close()
        
    def movie_dictionary_title_year(self):
        '''
        connect('Mongo_Shutter')
        mongo_movie = Mongo_Movie.objects.all()
        for movie in mongo_movie:
            Mongo_Movie.objects.filter(id = movie.id).update(set__title = re.sub(r'\s+$',r'',movie.title))
        
        mysql_movie = Movie.objects.all()
        for movie in mysql_movie:
            Movie.objects.filter(id = movie.id).update(title = re.sub(r'\s+$',r'',movie.title))
        

        
        
        connect('Mongo_Shutter')
        mongo_movie = Mongo_Movie.objects.all()
        for movie in mongo_movie:
            title = 'The ' + re.sub(r', The', r'', movie.title) if re.match(r'.*, The,*', movie.title) else movie.title
            title = re.sub(r'\s*\(.*\)\s*$', r'', title)
            if title != movie.title:
                Mongo_Movie.objects.filter(id = movie.id).update(set__title = title)
        
        mysql_movie = Movie.objects.all()
        for movie in mysql_movie:
            title = 'The ' + re.sub(r', The', r'', movie.title) if re.match(r'.*, The,*', movie.title) else movie.title
            title = re.sub(r'\s*\(.*\)\s*$', r'', title)
            if title != movie.title:
                Movie.objects.filter(id = movie.id).update(title = title)
        '''
        
        
        
        
        '''
        string  = 'Eye of Vichy, The (Oeil de Vichy, L`)'
        print string
        print True if re.match(r'.*, The,*', string) else False
        
        string = 'The ' + re.sub(r', The', r'', string)
        print string
        string = re.sub(r'\s*\(.*\)\s*$', r'', string)
        print string
        '''
        '''
        connect('Mongo_Shutter')
        mongo_movie = Mongo_Movie.objects.all()
        for movie in mongo_movie:
            title = re.sub(r'`',r"'",movie.title)
            if title != movie.title:
                Mongo_Movie.objects.filter(id = movie.id).update(set__title = title)
        
        mysql_movie = Movie.objects.all()
        for movie in mysql_movie:
            title = re.sub(r'`',r"'",movie.title)
            if title != movie.title:
                Movie.objects.filter(id = movie.id).update(title = title)        
        '''
        
        connect('Mongo_Shutter')
        mongo_movie = Mongo_Movie.objects.all()
        file_movie_dictionary = open('D:/shutter/movie_dictionary.dat','a')
        for movie in mongo_movie:
            id = Movie.objects.filter(title = movie.title, year = movie.year)[0].id
            file_movie_dictionary.write(str(id) + '::' + str(movie.id) + '::' + movie.title + " " + movie.year +'\n')
        file_movie_dictionary.close()
    
    def spider_picture(self):
        file_spider_data = open('D:/data/dump_20140614/id_imdb_data.dat')
        data_list = file_spider_data.readlines()
        file_spider_data.close()
        targetlist = {}
        for data in data_list:     
            mysql,mongo,title_year,director,actors,description,img = re.split(r'::',data)
            if eval(re.sub(r'\n',r'',img)) != []:
                targetlist[mysql] = eval(re.sub(r'\n',r'',img))[0]
        self.downjpgmutithread(targetlist)
            
    def downjpg(self,url,filepath,filename):
        socket = urllib2.urlopen(url)
        img = socket.read()
        File = open(filepath+filename+'.jpg',"wb" )
        File.write(img)
        File.close()
        
    def downjpgmutithread(self,targetlist ):
        print("There are %d images wating to be downloaded"%len(targetlist)) 
        print("Start download")
        task_threads=[]
        count=1
        for id in targetlist:
            t= threading.Thread( target=self.downjpg,args=(targetlist[id],'D:/data/dump_20140614/img/',id) )
            count=count+1
            task_threads.append(t)
        for task in task_threads:
            task.start()
        for task in task_threads:
            task.join() 
        print("Mission Complete")
        
    def load_spider_data(self):
        file_spider_data = open('D:/data/dump_20140614/id_imdb_data.dat')
        data_list = file_spider_data.readlines()
        file_spider_data.close()
        targetlist = {}
        connect('Mongo_Shutter')
        for idx, data in enumerate(data_list):
            print str(idx) + '//' + str(len(data_list))
            mysql,mongo,title_year,director,actors,description,img = re.split(r'::',data)
            Movie.objects.filter(id = mysql).update(director = eval(director)[0] if eval(director) != [] else '',\
                                                    actor = ','.join(eval(actors)),\
                                                    description = eval(description)[0] if eval(director) != [] else '',\
                                                    picture = mysql+'.jpg')
            Mongo_Movie.objects.filter(id = mongo).update(set__director = eval(director)[0] if eval(director) != [] else '',\
                                                            set__actor = ','.join(eval(actors)),\
                                                            set__description = eval(description)[0] if eval(director) != [] else '',\
                                                            set__picture = mysql+'.jpg')
'''
file_movies = open('D:/data\ml-1m\ml-1m\\movies.dat')
file_ratings = open('D:\data\ml-1m\ml-1m\\ratings.dat')
file_users = open('D:\data\ml-1m\ml-1m\\users.dat')
print file_movies.readline()
print file_ratings.readline()
print file_users.readline()
'''
data = data_generation()