# Y13Project
AQA NEA Computer Science Project


### Brief
A website which provides a GUI to interact with graph creation and traversal software. The website will be powered by python backend and frontend graphics powered by WebGL, and basic framework using html5, JS, CSS.\
Graphs which would be available:
- Digraphs (weighted + non-weighted)
- Directed (weighted + non-weighted)

### How I would do it:
#### Web framework
Python-flask: A module which supplies a web server framework using Jinja and WSGI.\
Python-sockets (socket-io): A module providing TCP/IP communication\
Use for communication between client and server.

#### Graphics
WebGL: advanced graphics renderer (can be used for 3D).\
Used to render the graphs rather than using JS Canvas.\
Python Math: standard included library for maths (duh).\
Graph all in the same plane, but rotational (optimistic).

#### User Authentication
SQLite: A module supplying databases.\
User Accounts\
Saved graphs\
Hashlib: A module which can hash and return hashed strings used for passwords\
smtplib + email: latter is the standard library to send emails. smtplib is a dependency. \
Registration verification and 2FA

#### Backend
I’ll be writing the backend in python (rather than java) as I believe this will be beneficial for scripting.\
I am debating using node.js, but I am not acquainted with it at all, so I have no clue how to use node.js