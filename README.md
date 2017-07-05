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

#### Brief Summary of Endpoints 

- **[<code>POST</code> api/events/]()**
- **[<code>POST</code> api/adduser/]()**
- **[<code>GET</code> api/event/get/USERDEVICE/]()**
- **[<code>GET</code> api/event/block/add/EventName/]()**
- **[<code>GET</code> api/event/block/delete/EventName/]()**


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
If successful, a JSON-serialized list with all the input parameters will be returned. If not successful, appropriate error messages such as missing parameter/info will be returned to the caller in JSON format.

***

## Errors
None

***

## Example
**Request**

    curl -X POST http://localhost:8000/api/events/ -d "EventName=Serendpity&EventLabel=Movie&EventAction=Downloaded&UserDevice=MacbookPro" 

**Return** __shortened for example purpose__
``` json
[{"Success":"Event recorded"}]

