# this script was developed by Shashika Hiripitiyalage

from flask import Flask
from flask import jsonify
from flask import request
from datetime import datetime

app = Flask(__name__)

# sample conversation messages
conversationList = [
    {
        "conversation_id": "1234",
        "messages": [
            {
                "created": "2018-01-17T04:50:14.883Z",
                "message": "I love python",
                "sender": "shashika"
            },
            {
                "created": "2018-01-17T04:52:17.201Z",
                "message": "Python is great",
                "sender": "sandaruwan"
            }
        ]
    },
    {
        "conversation_id": "1235",
        "messages": [
            {
                "created": "2020-11-16T06:52:17.101Z",
                "message": "Hello Python",
                "sender": "Kenneth"
            }
        ]
    }
]

# function accepts HTTP POST actions to create new messages in the conversation
@app.route("/messages/",methods=['POST'])
def addConversations() :
    creatmsg = {
            "message": request.json['message'],
            "sender": request.json['sender'],
            "created": datetime.utcnow().isoformat()[:-3] + 'Z'
        }

    conversation = [convstn for convstn in conversationList if (convstn['conversation_id'] == request.json['conversation_id'])]

    if bool(conversation) and conversation[0]['conversation_id'] == request.json['conversation_id']:
        conversation[0]['messages'].append(creatmsg)
        return jsonify({"New Message added to the conversation": conversation})
    else:
        newconversation = {
            'conversation_id': request.json['conversation_id'],
            "messages": [creatmsg]
        }
        conversationList.append(newconversation)
        return jsonify({"Created a new Conversation ": newconversation})

# function returns a list of all conversation messages persisting in the conversationList
@app.route("/conversations/",methods=['GET'])
def getAlltheConversations():
    return jsonify({"All the conversations": conversationList})

# function returns a list of conversation messages for a given conversation_id
@app.route("/conversations/<conversation_id>",methods=['GET'])
def getASpecicConversation(conversation_id):
    conversation = [convstn for convstn in conversationList if (convstn['conversation_id'] == conversation_id)]
    if bool(conversation):
        return jsonify({f"Conversation for the conversation ID : {conversation_id} ":conversation})
    else:
        return jsonify(f'There is no conversation for this conversation ID : {conversation_id} ')

#landing page, shows the welcome message
@app.route("/",methods=['GET'])
def welcome():
    return "Welcome to the Ada Support Backend Coding Challenge - webservice.!"

if (__name__=="__main__"):
    app.run()
    #app.run(debug=True)

    # This line can be used if you need to run the webservice on a particular port
    #app.run(host='127.0.0.1', port=5001)