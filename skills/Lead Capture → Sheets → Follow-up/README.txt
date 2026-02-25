Purpose:
This automation captures inbound leads via a webhook, stores them in Google Sheets, and sends automated follow-up notifications via email and optional WhatsApp.

Typical Use Cases / Target Clients
•	Website contact or inquiry forms
•	Real estate lead collection
•	Service businesses receiving client requests
•	Agencies handling inbound leads for clients


Required Credentials and Prerequisites
•	Google Sheets account
•	Gmail account
•	(Optional) WhatsApp provider credentials
The workflow is triggered by a webhook and expects incoming lead data that can be mapped to the following standard fields:
•	name
•	email
•	phone
•	message
If the lead source uses a different payload structure, field mapping can be adjusted in the normalization step.



Nodes That Must Be Edited When Reusing the Template
•	CONFIG - Normalize Lead
Map incoming webhook data into standard lead fields.
•	STORE - Google Sheets (Lead)
Select the spreadsheet and sheet where leads should be stored.
•	NOTIFY - Email (Lead Follow-up)
Customize sender, subject, and email message.
•	NOTIFY - WhatsApp (Lead Follow-up) [Optional]
Requires WhatsApp provider credentials to enable.


Estimated Setup Time
•	Basic setup and incoming data mapping (Google Sheets + Email): ~10–15 minutes
•	Full setup with Google Sheets, Email, and WhatsApp follow-up: ~20–30 minutes


Common Failure Points and Maintenance Notes
•	Webhook must be triggered using a POST request
•	Incoming payload must include required lead fields
•	Google Sheets column structure should not be changed
•	WhatsApp messages are skipped if phone number is missing or invalid
•	WhatsApp credentials may require periodic re-authentication

