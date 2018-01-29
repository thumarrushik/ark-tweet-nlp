
tweets = ['this is a message', 'and a second message']

RUN_TAGGER_CMD = "java -XX:ParallelGCThreads=2 -Xmx500m -jar ark-tweet-nlp-0.3.2.jar"
import os
import subprocess
import shlex
os.chdir("/Users/rpt/Downloads/ark-tweet-nlp-0.3.2/")



def CMUTweetTagger(tweets, run_tagger_cmd = RUN_TAGGER_CMD):
    #tweets_cleaned = [tw for tw in tweets]
    message = "\n".join(tweets)
    message = message.encode('utf-8')
    args = shlex.split(run_tagger_cmd)
    args.append('--output-format')
    args.append('conll')
    po = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = po.communicate(message)
    pos_result = result[0].strip()
    pos_result = pos_result.split()
    #pos_results = [pr.split() for pr in pos_result]
    pos_results = []

    for a1 in range(0,len(pos_result),3):
        pos_results.append([pos_result[a1].decode(), pos_result[a1+1].decode(),pos_result[a1+2].decode()])
    
    return pos_results



CMUTweetTagger(tweets, run_tagger_cmd = RUN_TAGGER_CMD)
