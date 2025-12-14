FastAPI stands for Fast Application Programming Interface. API facilitates access and control of data, it acts as a backend server that handles all data operations - creating,reading,updating,deleting

URL: Domain/PathOrEndpoint?QueryParameters

USER <--Send Request and Receive Response--> Frontend Client/Website <----> Backend Server or API Server 
Request Components: Type/Method,Path,Body(Additional data to be send),Headers(Authentication,meta data)
Response Components: Status Code(Status of request sent),Body(Additional Data),Headers(Authentication,meta data)


Tools Used:
- Uvicorn: It is a lightweight ASGI web server implementation which helps in network communication like HTTP Requests and WebSockets between clients and Python web frameworks like FastAPI. 
    -- ASGI: Asynchronous Server Gateway Interface, it acts as a standard interface between web servers and asynchronous web applications which enables it to handle websockets and efficient parallel processing.
    -- WebSocket: It is a communication protocol that enables full duplex connection between client and a server, allowing real time, low latency data exchange. Ideal for live chat, online gaming, financial tickers.

- Pydantic: Python library that uses type hints to validate, parse and manage data. Makes sure that data coming in are in correct format, convert data types or throw error if validation fails.