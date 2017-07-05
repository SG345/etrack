# EventTracking API Assignment - Problem Statement

 The features of the tracking system are as listed below:
 
● The stream comes with a  unique device id  and a list of events performed along with the attributes for those events. Each device corresponds to a  user_id  in the system. (Note: A mapping from unique device id to user_id can be assumed to be present in the system)

● Some particular events can be blocked at the backend and should be filtered out (not saved) by the API

● Any blocked event should be logged and a counter has to be maintained against any blocked event to count the number of such events blocked (a blocked count per event name)

● The system should allow blocking any event in realtime (as simple as adding another database entry to block a particular event).

● If the unique device identifier is not found in the system, the api should return appropriate status back to the caller (Missing device id etc).

● If all checks are passed, the event should be saved in a database, along with the event attributes, against the  user_id  that the event corresponds to. The api should return success in such a case.

● The API should have appropriate error handling in place to handle scenarios like infrastructure failures (database unavailable etc) and any other failures points you can foresee.

API 1 - Consume the event stream as described above
API 2 - List the events corresponding to a particular device id
***




## Endpoints

#### Brief Summary of API Endpoints 

- **[<code>POST</code> api/adduser/]()**
- **[<code>POST</code> api/events/]()**
- **[<code>GET</code> api/event/get/UserDevice/]()**
- **[<code>POST</code> api/event/block/add/]()**
- **[<code>POST</code> api/event/block/delete/]()**

# Add user and assign a DeviceID into system

    POST api/adduser/

## Description
Each UniqueDevice is mapped to a username.
## Parameters
- **UserName** _(required)_ 
- **UserDevice** _(required)_ 

**Example of adding user/device**

    curl -X POST http://localhost:8000/api/adduser/ -d "UserName=Sushrut&UserDevice=MacbookAir4"

**Return** 
``` json
{'Success': 'Username/Device mapped successfully'}```


# Record event activity from the stream

    POST api/events/

## Description
Event details are recorded and stored in the database. If the EventName matches the name in **BlockedEventList** it will not be stored in the database.


## Parameters
- **EventName** _(required)_ — Name of the event

- **EventLabel** _(required)_ — Label for the event:

- **EventAction** _(required)_ — Action for the event:

- **UserDevice** _(required)_ — UserDevice where this event was recorded:

## Return format
If successful, a JSON-response indicating success will be returned to the caller. If not successful, appropriate error messages such as missing parameters/info will be returned to the caller in JSON format.


## Examples
**Event record**

    curl -X POST http://localhost:8000/api/events/ -d "EventName=DieHard&EventLabel=Movie&EventAction=Downloaded&UserDevice=MacbookPro" 

**Return** 
``` json
[{"Success":"Event recorded"}]
``` 

**Event record when UserDeviceID is not present in system**

    curl -X POST http://localhost:8000/api/events/ -d "EventName=Serendpity&EventLabel=Movie&EventAction=Downloaded&UserDevice=Lenovo442" 


**Return** 
``` json
[{"Error":"UserDevice does not exist in the system"}] ```


**Event record with missing parameter**

    curl -X POST http://localhost:8000/api/events/ -d "EventName=DieHard&EventLabel=Movie"

**Return** 
``` json
{"UserDevice":["This field is required."],"EventAction":["This field is required."]}```


**Event record with blocked event**

    curl -X POST http://localhost:8000/api/events/ -d "EventName=Golmaal&EventLabel=Movie&EventAction=Downloaded&UserDevice=MacbookAir"

**Return** 
``` json
{'Error': 'Event was blocked as per existing rules'}```

# Manage BlockedEventList

    POST api/event/block/add/
    POST api/event/block/delete/

## Description
Event details are added/deleted from the BlockedEventList.

## Parameters
- **EventName** _(required)_ — Name of the event to be added/deleted


## Return format
If successful, a JSON-response indicating success will be returned to the caller. If not successful, appropriate error messages such as missing parameters/info will be returned to the caller in JSON format.


**Add Event into BlockedEventList**

    curl -X POST http://localhost:8000/api/event/block/delete/Golmaal/

**Return** 
``` json
{'Success': 'Event has been removed from Block List'```

**Remove Event from BlockedEventList**

    curl -X POST http://localhost:8000/api/event/block/delete/Golmaal/

**Return** 
``` json
{'Success': 'Event has been removed from Block List'```






