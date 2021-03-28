# Client Module

This module is responsible for communication with external APIs.\
The only responsibility is to fetch and parse data.

### Why marshmallow not DRF serializers and django related stuff?
It should be a standalone module without any coupling to the eycars project. Thanks to that we can also 
reuse it in not django projects.

### If I have more time I would make this separate project / app
