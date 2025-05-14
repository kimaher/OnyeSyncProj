# OnyeSyncProj

---

The writing in part 1 and all of part three is in this md file. For the part 2 I used regular javascript because my classes are still in session and I am in the middle of my athletic season so I did not have time to learn React.js and submit this project by Thursday. With more time I would have learned how to use these tools and would have linked my python file as backend to my website to do the natural language processing. I would have also implemented a less brute force method of detecting meaning in inputted sentences in my python program. GitHub pages web link: [FHIR Query Interface](https://kimaher.github.io/OnyeSyncProj/).

---

You can run the `.py` file and input any string to get a FHIR API query.  
You can continue entering strings to get FHIR API queries until you type `exit`, which ends the program.

---

### 💡 Example Input/Output:
Request a patient query or type 'exit' to quit: hello
FHIR Request: GET /Patient

Request a patient query or type 'exit' to quit: Show all men with diabetes
FHIR Request: GET /Patient?gender=male&condition=diabetes

Request a patient query or type 'exit' to quit: show all women with diabetic
FHIR Request: GET /Patient?gender=female&condition=diabetes

Request a patient query or type 'exit' to quit: show everyone under 25 with a heart disease
FHIR Request: GET /Patient?age=lt25&condition=heart-disease

Request a patient query or type 'exit' to quit: exit
### Security and Compliance

To ensure the system is HIPAA-compliant and securely handles FHIR data, the following mechanisms will be implemented:

#### Authentication and Authorization Mechanisms
1. **OAuth 2.0**: I would implement OAuth 2.0 for secure authorization, where each API request requires a valid access token. This guarantees that only authorized users and systems can access sensitive health data.
   
2. **SMART on FHIR**: This builds on OAuth and is specifically designed for healthcare systems. It ensures secure, role-based access to FHIR data for third-party applications and healthcare providers.

3. **Token Expiry and Refresh**: Tokens are temporary and refresh to minimize the risk of unauthorized access if a token is stolen.

#### Data Privacy and Audit Logging Strategy
1. **Data Encryption**: 
   - **In Transit**: Data will be encrypted using HTTPS (TLS/SSL) to ensure that data transmitted between clients and servers remains private.
   - **At Rest**: All sensitive data, including patient records, will be encrypted using AES-256 or similar algorithms when stored on the server.

2. **Audit Logging**: All access to sensitive data will be logged. Logs will capture user identity, time of access, and type of action (read, write or delete). These logs will be stored securly and can be reviewed regularly.

3. **Data Minimization**: I will only save the minimum necessary patient data to fulfill specific queries, reducing the risk of data exposure.

#### Role-Based Access Control (RBAC)
1. **Defining Roles**:
   - **Patient**: Can only access and modify their own health data.
   - **Healthcare Provider**: Has access to only the health data of patients under their care.
   - **Admin**: Has full access for administrative tasks.

2. **Granular Permissions**: Permissions will be restricted to ensure users can only access the data they need for their role. For example, healthcare providers can view patient records but not delete them.

3. **Periodic Audits**: Regular audits of user roles and access rights will ensure that all users have the least amount of access necessary for their job functions.

By employing these measures, the system will ensure compliance with HIPAA, safeguarding patient health data and maintaining the privacy and security required for healthcare systems.