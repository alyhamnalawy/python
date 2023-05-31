import requests
import sys
import getopt
def send_salck_message(message):
    payload='{"text":"%s"}' % message
    response = requests.post('https://hooks.slack.com/services/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',data=payload)
    print(response.text)
#send slack message
def main(argv):
    message=' '
    try: opts, args=getopt.getopt(argv,"hm:",["message="])
    except getopt.GetoptErr:
        print('slack message.py -m <message>')
        sys.exit(2)
    if len(opts)==0:
        message="Hello, world"
    for opt,arg in opts:
        if opt=='-h':
            print('slack message.py -m <message>')
            sys.exit()
        elif opt in ("-m","message"):
            message=arg
    send_slack_message(message)
if __name__=="__main__":
    main(sys.argv[1:])