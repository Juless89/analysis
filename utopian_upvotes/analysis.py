from steem.blockchain import Blockchain
from steem import Steem

import threading
import sys
import database


class myThread (threading.Thread):
    def __init__(self, thread_id, start_block, end_block, n, blockchain):
        threading.Thread.__init__(self)
        self.db = database.Database()
        self.thread_id = thread_id
        self.start_block = start_block
        self.end_block = end_block
        self.n = n
        self.blockchain = blockchain
        self.current_block = self.start_block

        print(self.thread_id, self.start_block, self.end_block)

    def process_block(self, block):
        timestamp = block['timestamp']

        # Count each transaction inside the block
        for operation in block['transactions']:
            if operation['operations'][0][0] == 'vote':
                vote = operation['operations'][0][1]

                voter = vote['voter']
                author = vote['author']
                permlink = vote['permlink']
                weight = vote['weight']

                if vote['voter'] == 'utopian-io':
                    print(timestamp, self.current_block, voter, author,
                          permlink, weight)
                    self.db.insert_vote_into_db(timestamp, voter, author,
                                                permlink, weight)

    def run(self):
        run = 0

        while run == 0:
            stream = self.blockchain.stream_from(start_block=self.start_block,
                                                 end_block=self.end_block,
                                                 full_blocks=True)
            try:
                for block in stream:
                    self.process_block(block)
                    percentage = ((self.start_block-self.current_block) /
                                  self.n*100)
                    print(f"Thread {self.thread_id}: block {self.start_block}/"
                          f"{self.end_block} {percentage:.2f}%", end='\r')
                    self.start_block += 1

                    run = 1
            except Exception as e:
                print('Error:', e)

        self.dump_data()


def run():
    # Global variables for creating threads
    steem = Steem(['https://api.steemit.com'])
    blockchain = Blockchain(steem)
    head_block = blockchain.get_current_block_num()
    block_count = int(sys.argv[1])
    amount_of_threads = int(sys.argv[2])
    blocks_per_thread = int(block_count/amount_of_threads)
    start_block = head_block-block_count
    threads = []

    # Calculate start_block and end_block for each thread
    for thread_id in range(0, amount_of_threads):
        thread = myThread(thread_id, start_block,
                          start_block + blocks_per_thread-1, blocks_per_thread,
                          blockchain)
        thread.start()
        threads.append(thread)
        start_block = start_block + blocks_per_thread

    # Wait for all the threads to finish
    for t in threads:
        t.join()


if __name__ == '__main__':
    run()
