## Dave Fuller's Notes

###  08 Feb 21

 	Found a Linux distribution on www.distrowatch.com called Univention Corporate Server. The description reads in part (emphasis mine):
>   It features an integrated management system for central administration of servers, **Microsoft Active Directory-compatible domain services**, and functions for parallel operation of virtualised server and desktop operating systems.    
>
>   From: https://distrowatch.com/table.php?distribution=univention

I downloaded the operating system and spun up an instance on a virtual machine. Due to the propriety nature of Microsoft products, I was concerned that multiple VMs of Windows servers would become a problem. I found the Univention OS optimized for domain/enterprise use, the web-based server management is user friendly, and setting it up was a snap. I contacted the Team Leader about using Univention for testing scripts and as a substitute for Windows VMs. Chris informed me that his testing environment was working and it was <u>not</u> needed at this time. 

Although this avenue did not pan out, I have left the instance on my virtual machine, if licensing issues or if any other issue causes us to lose access to window servers for testing this will be ready as a backup, if needed.

![univention](./univention.png)

Additional link: https://www.univention.com/

