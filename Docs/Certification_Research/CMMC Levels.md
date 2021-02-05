# CMMC Level 3 Checklist 

![index](/home/dave/Capstone/index.jpeg)



### CMMC Level 1

48 CFR 52.204-21 (“Basic Safeguarding of Covered Contractor Information Systems”) 

### CMMC Level 2

NIST SP 800-171 

#### CMMC Level 3

DFARS   clause   252.204-7012   (“Safeguarding   of   Covered   Defense   Information   and   Cyber   Incident   Reporting”) 

### ACCESS CONTROL

- [ ] ##### Level 1
- [ ] AC.1.001: Limit information system access to authorized users, processes acting on behalf of authorized users, or devices (including other information systems).
- [ ] AC.1.002: Limit information system access to the types of transactions and functions that authorized users are permitted to execute.
- [ ] AC.1.003: Verify and control/limit connections to and use of external information systems.
- [ ] AC.1.004: Control information posted or processed on publicly accessible information systems.
- [ ] ##### Level 2
- [ ] AC.2.005: Provide privacy and security notices consistent with applicable CUI rules.
- [ ] AC.2.006: Limit use of portable storage devices on external systems.
- [ ] AC.2.007: Employ  the  principle  of  least  privilege,  including  for  specific  security  functions  and  privileged  accounts.AC.2.008Use non-privileged accounts or roles when accessing nonsecurity functions.
- [ ] AC.2.009: Limit unsuccessful logon attempts.
- [ ] AC.2.010: Use session lock with pattern-hiding displays to prevent access and viewing of data after a period of inactivity.
- [ ] AC.2.011: Authorize wireless access prior to allowing such connections.
- [ ] AC.2.013: Monitor and control remote access sessions.
- [ ] AC.2.015: Route remote access via managed access control points.
- [ ] AC.2.016: Control the flow of CUI in accordance with approved authorizations.
- [ ] ##### Level 3
- [ ] AC.3.017: Separate the duties of individuals to reduce the risk of malevolent activity without collusion.
- [ ] AC.3.018: Prevent non-privileged users from executing privileged functions and capture the execution of such functions in audit logs.
- [ ] AC.3.019: Terminate (automatically) user sessions after a defined condition.
- [ ] AC.3.012: Protect wireless access using authentication and encryption.
- [ ] AC.3.020: Control connection of mobile devices.
- [ ] AC.3.014: Employ cryptographic mechanisms to protect the confidentiality of remote access sessions.
- [ ] AC.3.021: Authorize  remote  execution  of  privileged  commands  and  remote  access  to  security-relevant information.
- [ ] AC.3.022: Encrypt CUI on mobile devices and mobile computing platforms
### AUDIT AND ACCOUNTABILITY (AU)
- [ ] ##### Level 2

- [ ] AU.2.041: Ensure that the actions of individual system users can be uniquely traced to those users so they can be held accountable for their actions.

- [ ] AU.2.042: Create and retain system audit logs and records to the extent needed to enable the monitoring, analysis, investigation, and reporting of unlawful or unauthorized system activity.

- [ ] AU.2.043: Provide  a  system  capability  that  compares  and  synchronizes  internal  system  clocks  with  an  authoritative source to generate time stamps for audit records.

- [ ] AU.2.044: Review audit logs.

- [ ] ##### Level 3

- [ ] AC.3.017: Separate the duties of individuals to reduce the risk of malevolent activity without collusion.

- [ ] AC.3.018: Prevent non-privileged users from executing privileged functions and capture the execution of such functions in audit logs.

- [ ] AC.3.019: Terminate (automatically) user sessions after a defined condition.

- [ ] AC.3.012: Protect wireless access using authentication and encryption.

- [ ] AC.3.020: Control connection of mobile devices.

- [ ] AC.3.014: Employ cryptographic mechanisms to protect the confidentiality of remote access sessions.

- [ ] AC.3.021: Authorize  remote  execution  of  privileged  commands  and  remote  access  to  security-relevant information.

- [ ] AC.3.022: Encrypt CUI on mobile devices and mobile computing platforms.

### AWARENESS AND TRAINING (AT)

- [ ] ##### Level 2

- [ ] AT.2.056: Ensure  that  managers,  system  administrators,  and  users  of  organizational  systems  are  made  aware of the security risks associated with their activities and of the applicable policies, standards, and procedures related to the security of those systems.

- [ ] AT.2.057: Ensure that personnel are trained to carry out their assigned information security-related duties and responsibilities.

- [ ] ##### Level 3

- [ ] AT.3.058: Provide  security  awareness  training  on  recognizing  and  reporting  potential  indicators  of  insider  threat.

### CONFIGURATION MANAGEMENT (CM)

- [ ] ##### Level 2

- [ ] CM.2.061: Establish   and   maintain   baseline   configurations   and   inventories   of   organizational   systems   (including hardware, software, firmware, and documentation) throughout the respective system development life cycles.

- [ ] CM.2.062: Employ the principle of least functionality by configuring organizational systems to provide only essential capabilities.

- [ ] CM.2.063: Control and monitor user-installed software.

- [ ] CM.2.064: Establish and   enforce   security   configuration   settings   for   information   technology   products   employed in organizational systems.

- [ ] CM.2.065: Track, review, approve, or disapprove, and log changes to organizational systems.

- [ ] CM.2.066: Analyze the security impact of changes prior to implementation.

- [ ] ##### Level 3

- [ ] CM.3.067: Define, document, approve, and enforce physical and logical access restrictions associated with changes to organizational systems.

- [ ] CM.3.068: Restrict,  disable,  or  prevent  the  use  of  nonessential  programs,  functions,  ports,  protocols,  and  services.

- [ ] CM.3.069: Apply deny-by-exception (blacklisting) policy to prevent the use of unauthorized software or deny-all, permit-by-exception (whitelisting) policy to allow the execution of authorized software.

### IDENTIFICATION AND AUTHENTICATION (IA)

- [ ] ##### Level 1

- [ ] IA.1.076: Identify information system users, processes acting on behalf of users, or devices.

- [ ] IA.1.077: Authenticate (or verify) the identities of those users, processes, or devices, as a prerequisite to allowing access to organizational information systems.

- [ ] ##### Level 2

- [ ] IA.2.078: Enforce  a  minimum  password  complexity  and  change  of  characters  when  new  passwords  are  created.

- [ ] IA.2.079: Prohibit password reuse for a specified number of generations.

- [ ] IA.2.080: Allow  temporary  password  use  for  system  logons  with  an  immediate  change  to  a  permanent  password.

- [ ] IA.2.081: Store and transmit only cryptographically-protected passwords.

- [ ] IA.2.082: Obscure feedback of authentication information.

- [ ] ##### Level 3

- [ ] IA.3.083: Use  multifactor  authentication  for  local  and  network  access  to  privileged  accounts  and  for  network access to non-privileged accounts.

- [ ] IA.3.084: Employ replay-resistant authentication mechanisms for network access to privileged and non-privileged accounts.

- [ ] IA.3.085: Prevent the reuse of identifiers for a defined period.

- [ ] IA.3.086: Disable identifiers after a defined period of inactivity.

### INCIDENT RESPONSE (IR)

- [ ] ##### Level 2

- [ ] IR.2.092: Establish  anoperational  incident-handling  capability  for  organizational  systems  that  includes  preparation, detection, analysis, containment, recovery, and user response activities.

- [ ] IR.2.093: Detect and report events.

- [ ] IR.2.094: Analyze and triage events to support event resolution and incident declaration.

- [ ] IR.2.096: Develop and implement responses to declared incidents according to pre-defined procedures.

- [ ] IR.2.097: Perform root cause analysis on incidents to determine underlying causes.

- [ ] ##### Level 3

- [ ] IR.3.098: Track, document, and report incidents to designated officials and/or authorities both internal and external to the organization.

- [ ] IR.3.099: Test the organizational incident response capability.

### MAINTENANCE (MA)

### Level 2

- [ ] MA.2.111: Perform maintenance on organizational systems.

- [ ] MA.2.112: Provide  controls  on  the  tools,  techniques,  mechanisms,  and  personnel  used  to  conduct  system  maintenance.

- [ ] MA.2.113: Require  multifactor  authentication  to  establish  nonlocal  maintenance  sessions  via  external  network connections and terminate such connections when nonlocal maintenance is complete.

- [ ] MA.2.114: Supervise the maintenance activities of personnel without required access authorization.

- [ ] ##### Level 3

- [ ] MA.3.115: Ensure equipment removed for off-site maintenance is sanitized of any CUI.

- [ ] MA.3.116: Check  media  containing  diagnostic  and  test  programs  for  malicious  code  before  the  media  are  used in organizational systems. 

### MEDIA PROTECTION (MP) 

- [ ] ##### Level 1

- [ ] MP.1.118: Sanitize  or  destroy  information  system  media  containing  Federal  Contract  Information  before  disposal or release for reuse.

- [ ] ##### Level 2

- [ ] MP.2.119: Protect (i.e., physically control and securely store) system media containing CUI, both paper and digital.

- [ ] MP.2.120: Limit access to CUI on system media to authorized users.

- [ ] MP.2.121: Control the use of removable media on system components.

- [ ] ##### Level 3

- [ ] MP.3.122: Mark media with necessary CUI markings and distribution limitations.

- [ ] MP.3.123: Prohibit the use of portable storage devices when such devices have no identifiable owner.

- [ ] MP.3.124: Control access to media containing CUI and maintain accountability for media during transport outside of controlled areas.

- [ ] MP.3.125: Implement  cryptographic  mechanisms  to  protect  the  confidentiality  of  CUI  stored  on  digital  media during transport unless otherwise protected by alternative physical safeguards.

### PERSONNEL SECURITY (PS)

- [ ] ##### Level 2

- [ ] PS.2.127: Screen individuals prior to authorizing access to organizational systems containing CUI.

- [ ] PS.2.128: Ensure that  organizational  systems  containing  CUI  are  protected  during  and  after  personnel  actions such as terminations and transfers.

### PHYSICAL PROTECTION (PE)

- [ ] ##### Level 1

- [ ] PE.1.131: Limit  physical  access  to  organizational  information  systems,  equipment,  and  the  respective operating environments to authorized individuals.

- [ ] PE.1.132: Escort visitors and monitor visitor activity.

- [ ] PE.1.133: Maintain audit logs of physical access.

- [ ] PE.1.134: Control and manage physical access devices.

- [ ] ##### Level 2

- [ ] PE.2.135: Protect and monitor the physical facility and support infrastructure for organizational systems.

- [ ] ##### Level 3

- [ ] PE.3.136Enforce safeguarding measures for CUI at alternate work sites.

### RECOVERY (RE) 

- [ ] ##### Level 2

- [ ] RE.2.137: Regularly perform and test data back-ups.

- [ ] RE.2.138Protect the confidentiality of backup CUI at storage locations.

- [ ] ##### Level 3

- [ ] RE.3.139: Regularly  perform  complete,  comprehensive,  and  resilient  data  back-ups  as  organizationally  defined.

### RISK MANAGEMENT (RM)

- [ ] ##### Level 2

- [ ] RM.2.141: Periodically  assess  the  risk  to  organizational  operations  (including  mission,  functions,  image,  or  reputation), organizational assets, and individuals, resulting from the operation of organizational systems and the associated processing, storage, or transmission of CUI.

- [ ] RM.2.142: Scan  for  vulnerabilities  in  organizational  systems  and  applications  periodically  and  when  new  vulnerabilities affecting those systems and applications are identified.

- [ ] RM.2.143: Remediate vulnerabilities in accordance with risk assessments.

- [ ] ##### Level 3

- [ ] RM.3.144: Periodically perform risk assessments to identify and prioritize risks according to the defined risk categories, risk sources, and risk measurement criteria.

- [ ] RM.3.146: Develop and implement risk mitigation plans.

- [ ] RM.3.147: Manage non-vendor-supported products (e.g., end of life) separately and restrict as necessary to reduce risk.

### SECURITY ASSESSMENT (CA)

- [ ] ##### Level 2

- [ ] CA.2.157: Develop,   document,   and   periodically   update   system   security   plans   that   describe   system   boundaries, system environments of operation, how security requirements are implemented, and the relationships with or connections to other systems.

- [ ] CA.2.158: Periodically assess the security controls in organizational systems to determine if the controls are effective in their application.

- [ ] CA.2.159: Develop and implement plans of action designed to correct deficiencies and reduce or eliminate vulnerabilities in organizational systems.

- [ ] ##### Level 3

- [ ] CA.3.161: Monitor  security  controls  on  an  ongoing  basis  to  ensure  the  continued  effectiveness  of  the  controls.

- [ ] CA.3.162: Employ  a  security  assessment  of  enterprise  software  that  has  been  developed  internally,  for  internal use, and that has been organizationally defined as an area of risk.

### SITUATIONAL AWARENESS (SA)

- [ ] ##### Level 3

- [ ] SA.3.169: Receive  and  respond  to  cyber  threat  intelligence  from  information  sharing  forums  and  sources  and communicate to stakeholders.

### SYSTEM AND COMMUNICATIONS PROTECTION (SC) 

- [ ] ##### Level 1

- [ ] SC.1.175: Monitor, control, and protect organizational communications (i.e., information transmitted or received  by  organizational  information  systems)  at  the  external  boundaries  and  key  internal  boundaries of the information systems.

- [ ] SC.1.176: Implement  subnetworks  for  publicly  accessible  system  components  that  are  physically  or  logically separated from internal networks.

- [ ] ##### Level 2

- [ ] SC.2.178: Prohibit remote activation of collaborative computing devices and provide indication of devices in use to users present at the device.

- [ ] SC.2.179: Use encrypted sessions for the management of network devices.

- [ ] ##### Level 3

- [ ] SC.3.177: Employ FIPS-validated cryptography when used to protect the confidentiality of CUI.

- [ ] SC.3.180: Employ  architectural  designs,  software  development  techniques,  and  systems  engineering  principles that promote effective information security within organizational systems.

- [ ] SC.3.181: Separate user functionality from system management functionality.

- [ ] SC.3.182: Prevent unauthorized and unintended information transfer via shared system resources.

- [ ] SC.3.183: Deny network communications traffic by default and allow network communications traffic by exception (i.e., deny all, permit by exception).

- [ ] SC.3.184: Prevent   remote   devices   from   simultaneously   establishing   non-remote   connections   with   organizational systems and communicating via some other connection to resources in external networks (i.e., split tunneling).

- [ ] SC.3.185: Implement  cryptographic  mechanisms  to  prevent  unauthorized  disclosure  of  CUI  during  transmission unless otherwise protected by alternative physical safeguards.

- [ ] SC.3.186: Terminate  network  connections  associated  with  communications  sessions  at  the  end  of  the  sessions or after a defined period of inactivity.

- [ ] SC.3.187: Establish and manage cryptographic keys for cryptography employed in organizational systems.

- [ ] SC.3.188: Control and monitor the use of mobile code.

- [ ] SC.3.189: Control and monitor the use of Voice over Internet Protocol (VoIP) technologies.

- [ ] SC.3.190: Protect the authenticity of communications sessions.

- [ ] SC.3.191: Protect the confidentiality of CUI at rest.

- [ ] SC.3.192: Implement Domain Name System (DNS) filtering services.

- [ ] SC.3.193: Implement  a  policy  restricting  the  publication  of  CUI  on  externally  owned,  publicly  accessible  websites (e.g., forums, LinkedIn, Facebook, Twitter).
