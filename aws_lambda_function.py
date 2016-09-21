## This script is a sample function that you can plug in AWS Lambda Function
## to trigger the build of your project on CircleCI

import json
import urllib2


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    try:
        request = urllib2.Request(
            'https://circleci.com/api/v1/project/{project}/tree/{branch}?circle-token={circle_token}'.format(
                project='woosmap/circleci-continuous-import',
                branch='master',
                circle_token='Fake_Token_a16I98h7b756b87dsgbb0f73c6b9fe435f1024'), data={})
        response = urllib2.urlopen(request)
        return json.dumps(response.read(), indent=2)
    except Exception as e:
        print(e)
        raise e
