join.stuykc.org
==========

A website for logging signups onto a Google Form by sending a form response from the backend. It also sends a confirmation email upon submission.

Installation
----------

1. Deploy onto Google App Engine
2. Then visit `/admin/settings` to modify the settings for the Google Form that the form responses should go to. Make sure that the identifiers are the `name` identifier for each input on the Google Form and that the form response url corresponds to the location that is pointed to on the Google Form.
3. Submit a test response to make sure everything is working properly.
