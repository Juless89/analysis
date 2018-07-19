import MySQLdb
import json
from steem.post import Post
from steem import Steem


class Database():
    def __init__(self):
        self.db = None
        self.cur = None

    def connect_to_db(self):
        self.db = MySQLdb.connect(host="localhost",    # host location
                                  user="test",         # username
                                  passwd="Test!234#",  # password
                                  db="steem")          # database
        self.cur = self.db.cursor()

    def close_connection(self):
        self.cur.close()
        self.db.close()

    def get_utopian_90days(self):
        query = ("SELECT `timestamp`,`author`,`permlink`,`weight` FROM " +
                 "`utopian-io` WHERE `timestamp` BETWEEN '2018-04-16' AND " +
                 "'2018-07-15' ORDER BY `timestamp` ASC;")

        tags = json.load(open('tags.json'))

        try:
            self.connect_to_db()
            self.cur.execute(query)

            votes_per_user = {}
            weight_per_user = {}

            total_votes = 0
            total_weight = 0

            s = Steem(['https://api.steemit.com'])

            counter = 0
            for result in self.cur.fetchall():
                counter += 1
                author = result[1]
                permlink = result[2]
                weight = result[3]

                identifier = f'@{author}/{permlink}'

                print(f"Counter: {counter}", end='\r')

                try:
                    post = Post(identifier, s)
                    hashtags = post['json_metadata']['tags']
                    for tag in hashtags:
                        if tag in tags:
                            tags[tag]['weight'] += weight
                            tags[tag]['votes'] += 1
                except Exception as e:
                    continue

                if author in votes_per_user:
                    votes_per_user[author] += 1
                else:
                    votes_per_user[author] = 1

                if author in weight_per_user:
                    weight_per_user[author] += weight
                else:
                    weight_per_user[author] = weight

                total_votes += 1
                total_weight += weight

            # Distribution of weight per tag
            print(tags)

            sorted_by_value_votes = sorted(votes_per_user.items(),
                                           key=lambda kv: kv[1], reverse=True)
            sorted_by_value_weight = sorted(weight_per_user.items(),
                                            key=lambda kv: kv[1], reverse=True)

            # Top 20 by votes
            print("\nUser Votes")
            for (user, value) in sorted_by_value_votes[:20]:
                print(user, value)
            print(f'Total votes {total_votes}')

            # Top 20 by votes
            print("\nUser Weight")
            for (user, value) in sorted_by_value_weight[:20]:
                print(user, value)
            print(f'Total weight {total_weight}')

            # Distribution by weight top 20%
            n = len(sorted_by_value_weight)
            print("\nUser Weight")
            for (user, value) in sorted_by_value_weight[:int(n/5)]:
                print(user, value)
            print(f'Total weight {total_weight}')

            self.db.commit()

        except Exception as e:
            print('Error:', e)

        finally:
            # close connection afterwards
            self.close_connection()

    def get_utopian_all(self):
        query = ("SELECT `timestamp`,`author`,`permlink`,`weight` FROM " +
                 "`utopian-io` ORDER BY `timestamp` ASC;")

        try:
            self.connect_to_db()
            self.cur.execute(query)

            votes_per_day = {}
            unique_users = {}
            average_weight = {}
            users = []

            counter = 0
            for result in self.cur.fetchall():
                counter += 1
                timestamp = result[0]
                author = result[1]
                weight = result[3]

                print(f"Counter: {counter}", end='\r')

                date = timestamp.date()
                if timestamp.date() in votes_per_day:
                    votes_per_day[date] += 1
                else:
                    votes_per_day[date] = 1

                if timestamp.date() in average_weight:
                    list = average_weight[date]
                    list.append(weight)
                    average_weight[date] = list
                else:
                    average_weight[date] = [weight]

                if author not in users:
                    users.append(author)
                    if date in unique_users:
                        unique_users[date] = len(users)
                    else:
                        unique_users[date] = len(users)

            print("\nDate average_weight")
            for date, value in average_weight.items():
                print(date, sum(value) / len(value))

            # Unique users over time
            print("\nDate users")
            for date, value in unique_users.items():
                print(date, value)

            # Voter per day over time
            print("\nDate votes")
            for date, value in votes_per_day.items():
                print(date, value)

            self.db.commit()

        except Exception as e:
            print('Error:', e)

        finally:
            # close connection afterwards
            self.close_connection()

    def insert_vote_into_db(self, timestamp, voter, author, permlink, weight):
        query = ("INSERT INTO `utopian-io` (`timestamp`,`voter`, `author`, " +
                 f"`permlink`, `weight`) VALUES ({timestamp}', '{voter}', " +
                 f"'{author}', '{permlink}', '{weight}');")

        try:
            self.connect_to_db()

            # Lock table
            self.cur.execute(f"LOCK TABLES `utopian-io` WRITE;")

            self.cur.execute(query)

            # Release table
            self.cur.execute(f"UNLOCK TABLES;")

            # Commite changes made to the db
            self.db.commit()

        except Exception as e:
            print('Error:', e)

        finally:
            # Close connections
            self.close_connection()
