-	Run the script WebService.py locally 
    Based on the OS you might need to give execution permission for this script. 
    python3 WebService.py
-	By default, application will be running on the localhost(127.0.0.1), port number: 5000
    http://127.0.0.1:5000/
    
    Landing page 
        URL : http://127.0.0.1:5000/


->  Create New Messages 
	URL : http://127.0.0.1:5000/messages/

        cat <<EOF | curl -X POST -H "Content-Type: application/json" --data-binary @- "http://127.0.0.1:5000/messages/"
        {
            "sender": "shashika",
            "conversation_id": "12346",
            "message": "I'm a Developer"
        }
        EOF
    
    
->  Get the list of messages per “conversation_id”
        URL: http://127.0.0.1:5000/conversations/<conversation_id>
    
-> Get the list of all the messages 
        URL: http://127.0.0.1:5000/conversations/

