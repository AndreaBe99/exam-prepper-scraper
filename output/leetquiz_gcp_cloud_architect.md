# Exam Dump Export

**Total Questions:** 279
**Generated:** 2025-12-24 12:26:59

---

### Question 1

Your company operates nationally and plans to migrate multiple batch workloads to Google Cloud Platform (GCP). These workloads include some non time-critical tasks. You are also required to ensure compliance with HIPAA regulations and manage the service costs effectively. Based on Google's best practices, how should you design your solution on GCP?

A) Provision preemptible VMs to reduce cost. Discontinue use of all GCP services and APIs that are not HIPAA-compliant.
B) Provision preemptible VMs to reduce cost. Disable and then discontinue use of all GCP services and APIs that are not HIPAA-compliant.
C) Provision standard VMs in the same region to reduce cost. Discontinue use of all GCP services and APIs that are not HIPAA-compliant.
D) Provision standard VMs to the same region to reduce cost. Disable and then discontinue use of all GCP services and APIs that are not HIPAA-compliant.

**Answer:** [B]

Explanation: The correct answer is B. Provision preemptible VMs to reduce cost and disable, then discontinue use of all GCP services and APIs that are not HIPAA-compliant. Preemptible VMs can significantly cut costs for non time-critical workloads, fitting the requirements outlined. Disabling non-HIPAA-compliant services before discontinuing them allows you to verify the impact on your operations and ensure a smooth transition to compliant services.

---

### Question 2: https://www.leetquiz.com/quiz/cly2nv3yh000tnykpnkwmxibp/practice?status=UNANSWERED

You are designing a Data Warehouse on Google Cloud and want to store sensitive data in BigQuery. Due to stringent security policies, your company requires you to generate the encryption keys outside of Google Cloud. This ensures that the encryption keys are managed and controlled internally before being utilized within Google Cloud services. You need to implement a solution that adheres to these requirements. What should you do?

A) Generate a new key in Cloud Key Management Service (Cloud KMS). Store all data in Cloud Storage using the customer-managed key option and select the created key. Set up a Dataflow pipeline to decrypt the data and to store it in a new BigQuery dataset.
B) Generate a new key in Cloud KMS. Create a dataset in BigQuery using the customer-managed key option and select the created key.
C) Import a key in Cloud KMS. Store all data in Cloud Storage using the customer-managed key option and select the created key. Set up a Dataflow pipeline to decrypt the data and to store it in a new BigQuery dataset.
D) Import a key in Cloud KMS. Create a dataset in BigQuery using the customer-managed encryption key (CMEK) option and select the imported key.

**Answer:** [D]

Explanation: The requirement specifies that keys must be generated outside of Google Cloud. This is achieved by using the **Key Import** feature of Cloud KMS, which allows you to bring your own key (BYOK) into the Google ecosystem. Once the key is imported into Cloud KMS, it is managed as a **Customer-Managed Encryption Key (CMEK)**. BigQuery natively supports CMEK to encrypt data at rest at the dataset or table level. Option B is incorrect because it involves generating the key within Cloud KMS, and Option C is unnecessarily complex by involving Cloud Storage and Dataflow for a requirement that BigQuery handles natively. Note: While the original prompt text mentioned "customer-supplied" in option D, the standard GCP terminology for keys managed via Cloud KMS (even if imported) is **Customer-Managed Encryption Keys (CMEK)**.

---

### Question 3: https://www.leetquiz.com/quiz/cly2o3l9m0000ifkp0rkhydkx/practice?status=UNANSWERED

Your company, which focuses on data-centric business practices, is developing a new architecture to support these initiatives. You have been tasked with setting up the network infrastructure. The company plans to deploy mobile and web-facing applications on-premises while conducting all data analytics in Google Cloud Platform (GCP). The data strategy includes processing and loading 7 years' worth of archived .csv files totaling 900 TB, followed by the daily upload of an additional 10 TB of data. Currently, the company operates with a 100-MB internet connection. What steps should you take to meet your company's data transfer and processing needs?

A) Compress and upload both archived files and files uploaded daily using the gsutil 'm option.
B) Lease a Transfer Appliance, upload archived files to it, and send it to Google to transfer archived data to Cloud Storage. Establish a connection with Google using a Dedicated Interconnect or Direct Peering connection and use it to upload files daily.
C) Lease a Transfer Appliance, upload archived files to it, and send it to Google to transfer archived data to Cloud Storage. Establish one Cloud VPN Tunnel to VPC networks over the public internet, and compress and upload files daily using the gsutil 'm option.
D) Lease a Transfer Appliance, upload archived files to it, and send it to Google to transfer archived data to Cloud Storage. Establish a Cloud VPN Tunnel to VPC networks over the public internet, and compress and upload files daily.

**Answer:** [B]

Explanation: The solution addresses two distinct data transfer challenges. First, moving 900 TB of legacy data over a 100-Mbps connection is mathematically impractical (it would take years); therefore, using a **Transfer Appliance** is the best practice for high-volume initial migrations. Second, the daily requirement of 10 TB exceeds the capacity of a standard 100-Mbps internet connection and even many VPN configurations. A **Dedicated Interconnect** or **Direct Peering** provides the necessary high-bandwidth, consistent throughput (typically 10 Gbps or 100 Gbps) required to reliably ingest 10 TB every single day. Options C and D are incorrect because a standard Cloud VPN over a 100-Mbps line cannot support a 10 TB daily payload.

---

### Question 4: https://www.leetquiz.com/quiz/cly2o4ymp0003ifkpowse7k8e/practice?status=UNANSWERED

Your company has an application running on Google Cloud's Compute Engine that allows users to stream their favorite music. Currently, there are a fixed number of instances handling the workload. Music files are stored in Google Cloud Storage, and the data is streamed directly to users from these storage locations. Recently, users have reported that when trying to play popular songs, they often need to attempt multiple times before succeeding. You need to improve the performance and reliability of the application to ensure a smoother user experience. What should you do?

A) Mount the Cloud Storage bucket using gcsfuse on all backend Compute Engine instances. Serve music files directly from the backend Compute Engine instance.
B) Create a Cloud Filestore NFS volume and attach it to the backend Compute Engine instances. Download popular songs in Cloud Filestore. Serve music files directly from the backend Compute Engine instance.
C) Copy popular songs into CloudSQL as a blob. Update application code to retrieve data from CloudSQL when Cloud Storage is overloaded.
D) Create a managed instance group with Compute Engine instances. Create a global load balancer and configure it with two backends: Managed instance group, Cloud Storage bucket. Enable Cloud CDN on the bucket backend.

**Answer:** [D]

Explanation: The scenario describes a classic "hot object" problem where popular content (hit songs) causes high latency or request failures due to concentrated demand on specific Cloud Storage shards. To resolve this, **Cloud CDN (Content Delivery Network)** is the best practice. By using a **Global External HTTP(S) Load Balancer** with a Cloud Storage bucket as a backend, you can cache popular files at Google's edge locations closer to the users. This reduces the load on the origin (Cloud Storage) and significantly improves streaming performance and reliability. Using Managed Instance Groups (MIGs) ensures the application layer itself can scale to handle varying user traffic.

---

### Question 5: https://www.leetquiz.com/quiz/cly2o5b550004ifkpwipw3vtd/practice?status=UNANSWERED

Dress4Win, a web-based company that helps users organize their personal wardrobe, is planning to migrate their on-premises MySQL deployment to the cloud to handle rapid growth and infrastructure capacity issues. They aim to minimize downtime and performance impact during the migration. Which approach should you recommend?

A) Create a dump of the on-premises MySQL master server, and then shut it down, upload it to the cloud environment, and load into a new MySQL cluster.
B) Setup a MySQL replica server/slave in the cloud environment, and configure it for asynchronous replication from the MySQL master server on-premises until cutover.
C) Create a new MySQL cluster in the cloud, configure applications to begin writing to both on-premises and cloud MySQL masters, and destroy the original cluster at cutover.
D) Create a dump of the MySQL replica server into the cloud environment, load it into Google Cloud Datastore, and configure applications to read/write to Cloud Datastore at cutover.

**Answer:** [B]

Explanation: To minimize downtime and performance impact, the best practice is to use **asynchronous replication**. By setting up a replica (slave) in Google Cloud that synchronizes with the on-premises master, the data stays up-to-date in real-time without interrupting the live application. During the "cutover" window, you simply stop the application briefly, ensure the last transactions are replicated, promote the cloud replica to master, and point your applications to the new endpoint. Option A causes significant downtime during the upload/load process. Option C (dual-writing) is complex to implement and risks data inconsistency. Option D is incorrect because Cloud Datastore is a NoSQL database, and migrating from a relational MySQL schema to NoSQL would require a complete application rewrite.

---

### Question 6: https://www.leetquiz.com/quiz/cly2o5j0m0005ifkpm1u980z4/practice?status=UNANSWERED

Your organization has several departments, each needing its own set of IAM policies. However, you also want to manage these policies centrally to maintain consistency and control. Which approach should you take to best achieve this objective?

A) Multiple Organizations with multiple Folders
B) Multiple Organizations, one for each department
C) A single Organization with Folders for each department
D) A single Organization with multiple projects, each with a central owner

**Answer:** [C]

Explanation: The **Organization** resource is the root node of the Google Cloud resource hierarchy. By using a single Organization, you establish a central point of control where high-level security policies (Cloud IAM) and Organization Policy Constraints can be applied to every resource in the company. **Folders** allow you to group resources (projects) by department, team, or environment. IAM policies are inherited down the hierarchy, meaning you can grant permissions at the Organization level for central IT/Security teams while granting department-specific permissions at the Folder level. This structure perfectly balances central governance with departmental autonomy.

---

### Question 7: https://www.leetquiz.com/quiz/cly2o7beq0007ifkpy2np7b0f/practice?status=UNANSWERED

You are using Google Cloud SQL as the database backend for a large Customer Relationship Management (CRM) deployment. As your user base grows, you need to ensure scalability and availability. Specifically, you want to achieve three main goals: 1) Avoid running out of storage, 2) Maintain CPU usage below 75%, and 3) Ensure replication lag remains under 60 seconds. Considering these requirements, what are the correct steps to meet your objectives?

A) Enable automatic storage increase for the instance. 2. Create a Cloud Monitoring (formerly Stackdriver) alert when CPU usage exceeds 75%, and change the instance type to reduce CPU usage. 3. Create a Cloud Monitoring alert for replication lag, and shard the database to reduce replication time.
B) Enable automatic storage increase for the instance. 2. Change the instance type to a 32-core machine type to keep CPU usage below 75%. 3. Create a Cloud Monitoring alert for replication lag, and deploy memcache to reduce load on the master.
C) Create a Stackdriver alert when storage exceeds 75%, and increase the available storage on the instance to create more space. 2. Deploy memcached to reduce CPU load. 3. Change the instance type to a 32-core machine type to reduce replication lag.
D) Create a Stackdriver alert when storage exceeds 75%, and increase the available storage on the instance to create more space. 2. Deploy memcached to reduce CPU load. 3. Create a Stackdriver alert for replication lag, and change the instance type to a 32-core machine type to reduce replication lag.

**Answer:** [A]

Explanation: The correct approach involves utilizing Google Cloud's native automation and monitoring tools. 1) **Automatic storage increase** is a built-in Cloud SQL feature that prevents "out of space" errors by adding storage as needed. 2) Using **Cloud Monitoring alerts** for CPU usage allows you to proactively resize the instance (vertical scaling) when it hits the 75% threshold. 3) **Replication lag** is often caused by the volume of writes being too high for a single instance to handle or propagate; **sharding** (horizontal scaling) is a standard architectural pattern to distribute the write load and minimize the time it takes for replicas to stay in sync. Option B is less efficient as it suggests a fixed 32-core machine regardless of actual need, and Option C/D suggest manual storage management which is less reliable than automation.

---

### Question 8: https://www.leetquiz.com/quiz/cly2o7pkm0008ifkpfs6u147t/practice?status=UNANSWERED

Your company has a Google Cloud project that utilizes BigQuery for its data warehousing needs. To ensure secure communication, a VPN tunnel is established between the on-premises environment and Google Cloud using Cloud VPN. Given recent security audits, the security team has raised concerns regarding potential data exfiltration by malicious insiders, compromised code, or accidental oversharing of sensitive information. What measures should the security team implement to address these concerns?

A) Configure Private Google Access for on-premises only.
B) Perform the following tasks: 1. Create a service account. 2. Give the BigQuery JobUser role and Storage Reader role to the service account. 3. Remove all other IAM access from the project.
C) Configure VPC Service Controls and configure Private Google Access.
D) Configure Private Google Access.

**Answer:** [C]

Explanation: To prevent data exfiltration, standard IAM roles are not enough because a user with legitimate access could still move data to a resource outside the company's control (e.g., an external BigQuery dataset or Cloud Storage bucket). **VPC Service Controls** allows you to define a security perimeter around your Google Cloud resources. This ensures that data cannot be moved across the perimeter boundary, even by authorized users. Combining this with **Private Google Access** (specifically for On-Premises hosts via the VPN) allows your local machines to reach Google APIs using internal IP addresses, further reducing exposure to the public internet and ensuring traffic stays within the managed environment.

---

### Question 9: https://www.leetquiz.com/quiz/cly2o8gob000aifkp1v17q9yo/practice?status=UNANSWERED

You are transitioning a legacy game to a new game project in Google Cloud. You need to ensure that a service account (SA) can access both the legacy game's and the new game's Google Cloud resources with the required Firebase Admin permissions. What steps should you take to achieve this?

A) Create a new service account in the legacy game's Google Cloud project, add it to the new game's IAM page, and give it the Firebase Admin role in both projects.
B) Create a new service account in the new game's Google Cloud project, and give necessary permissions in both projects.
C) Create a service account (SA) in the legacy game's Google Cloud project, add this SA in the new game's IAM page, and then give it the Firebase Admin role in both projects.
D) Create a service account in both projects independently and manage their roles separately.

**Answer:** [C]

Explanation: In Google Cloud, a **Service Account** resides in a specific "home" project but can be granted IAM roles in any other project within the same organization (or even across organizations if permitted). To allow a single identity to manage resources across both the legacy and new projects, you should create the SA in one project (e.g., the legacy project) and then navigate to the IAM section of the second project to add that SA's email address as a member. Once added to both, you assign the **Firebase Admin** role to that specific SA in both locations. This centralizes management and avoids the overhead of managing two separate sets of credentials.

---

### Question 10: https://www.leetquiz.com/quiz/cly2o9d3x000cifkpwk1je82s/practice?status=UNANSWERED

Your company captures all web traffic data in Google Analytics 360 and stores it in BigQuery, with each country having its own dataset containing multiple tables. To maintain data security and privacy, it is crucial that analysts from each country can only see and query the data specific to their own country. Given this requirement, how should you configure the access rights in BigQuery?

A) Create a group per country. Add analysts to their respective country-groups. Create a single group 'all_analysts,' and add all country-groups as members. Grant the 'all_analysts' group the IAM role of BigQuery jobUser. Share the appropriate dataset with view access with each respective analyst country-group.
B) Create a group per country. Add analysts to their respective country-groups. Create a single group 'all_analysts,' and add all country-groups as members. Grant the 'all_analysts' group the IAM role of BigQuery jobUser. Share the appropriate tables with view access with each respective analyst country-group.
C) Create a group per country. Add analysts to their respective country-groups. Create a single group 'all_analysts,' and add all country-groups as members. Grant the 'all_analysts' group the IAM role of BigQuery dataViewer. Share the appropriate dataset with view access with each respective analyst country-group.
D) Create a group per country. Add analysts to their respective country-groups. Create a single group 'all_analysts,' and add all country-groups as members. Grant the 'all_analysts' group the IAM role of BigQuery dataViewer. Share the appropriate table with view access with each respective analyst country-group.

**Answer:** [A]

Explanation: In BigQuery, to run a query, a user needs two distinct sets of permissions: the ability to run a job (billing) and the ability to read the data. The **BigQuery JobUser** role granted at the project level (via the 'all_analysts' group) allows users to initiate query jobs and consume the project's resources. However, this role does not grant access to the data itself. To enforce data isolation by country, you grant access at the **Dataset level** to the specific country groups. Sharing at the dataset level is more manageable than sharing individual tables (Option B/D) and follows the principle of least privilege. Option C is incorrect because granting `dataViewer` at the project level to 'all_analysts' would allow every analyst to see every country's dataset, violating the privacy requirement.

---

### Question 11: https://www.leetquiz.com/quiz/cly2o9py7000difkphjzafzju/practice?status=UNANSWERED

An application development team has come to you for advice regarding their new project. They need to write and deploy an HTTP(S) API using Go 1.12. The API is expected to have an unpredictable workload, which means that it must be able to handle sudden spikes in traffic reliably. The team also prefers to minimize the operational overhead for this application to focus more on development rather than infrastructure management. Given these requirements, which approach should you recommend?

A) Develop the application with containers, and deploy to Google Kubernetes Engine.
B) Develop the application for App Engine standard environment.
C) Use a Managed Instance Group when deploying to Compute Engine.
D) Develop the application for App Engine flexible environment, using a custom runtime.

**Answer:** [B]

Explanation: The **App Engine standard environment** is the ideal choice for this scenario. It is a fully managed Platform-as-a-Service (PaaS) that minimizes operational overhead by handling all infrastructure management, including scaling and patching. One of its key strengths is its ability to scale rapidly and even scale down to zero when there is no traffic, making it highly effective for handling **unpredictable workloads and sudden spikes**. Go 1.12 is a supported runtime in the standard environment. In contrast, Option A (GKE) and Option C (Compute Engine) involve significantly more operational overhead (managing clusters, nodes, or OS images). Option D (App Engine flexible) has slower scaling times compared to the standard environment because it relies on Compute Engine virtual machines and Docker containers that take longer to spin up, making it less responsive to sudden traffic spikes.

---

### Question 12: https://www.leetquiz.com/quiz/cly2oaqv0000fifkp9oameqtv/practice?status=UNANSWERED

You are a cloud architect working for a sports association that caters to members aged 8 to 30. The association collects extensive health data on its members, including information on sustained injuries, which is stored in BigQuery. Current data protection legislation mandates that any personal health data must be deleted upon request by the individual. You need to design a solution that meets this requirement while ensuring that the process is efficient and compliant. What should you do?

A) Use a unique identifier for each individual. Upon a deletion request, delete all rows from BigQuery with this identifier.
B) When ingesting new data in BigQuery, run the data through the Data Loss Prevention (DLP) API to identify any personal information. As part of the DLP scan, save the result to Data Catalog. Upon a deletion request, query Data Catalog to find the column with personal information.
C) Create a BigQuery view over the table that contains all data. Upon a deletion request, exclude the rows that affect the subject's data from this view. Use this view instead of the source table for all analysis tasks.
D) Use a unique identifier for each individual. Upon a deletion request, overwrite the column with the unique identifier with a salted SHA256 of its value.

**Answer:** [A]

Explanation: Under data protection laws like GDPR or HIPAA, the "right to be forgotten" or specific deletion mandates require the actual removal of the data subjects' records. **BigQuery supports DML (Data Manipulation Language)**, specifically the `DELETE` statement, which allows you to target and remove specific rows based on a unique identifier (like a Member ID). This is the most direct and compliant way to ensure the data is no longer stored. Option C (Views) only hides the data but leaves it physically stored in the underlying table, which fails audit compliance. Option D (Pseudonymization/Hashing) is a security measure but does not constitute "deletion" if the underlying health data (the "what") remains linked to a identifiable (even if hashed) "who."

---

### Question 13: https://www.leetquiz.com/quiz/cly2obrhs000iifkpxf6x6jrf/practice?status=UNANSWERED

You are tasked with choosing a Google Cloud Storage class for a project. The data will need to be stored for a long duration of 10 years and will be accessed infrequently. Cost optimization is your top priority. Which Google Cloud Storage class should you choose?

A) Coldline Storage
B) Archive Storage
C) Nearline Storage
D) Regional Storage

**Answer:** [B]

Explanation: **Archive Storage** is specifically designed for data that is accessed very rarely (less than once a year) and needs to be retained for long periods, such as for regulatory compliance or historical archives. It offers the **lowest monthly cost** for data at rest (starting at **$0.0012 per GB/month**) compared to Coldline, Nearline, or Standard storage. While it has the highest retrieval costs and a minimum storage duration of 365 days, these trade-offs are ideal for a 10-year storage plan where cost optimization is the primary goal. Unlike similar "cold" tiers in other clouds, Google Cloud's Archive Storage still provides millisecond access latency when you do need to retrieve the data.

---

### Question 14: https://www.leetquiz.com/quiz/cly2occ1o000jifkpqiv9ulyq/practice?status=UNANSWERED

Your operations team is facing a performance issue with a production application running on Google Compute Engine. Under heavy load, the application is dropping incoming requests. The process list for affected instances shows that a single application process is consuming all available CPU resources, and the autoscaling has already reached its maximum limit of instances. Other related systems, including the database, are not experiencing any abnormal load. To ensure that production traffic can be served again as quickly as possible, which action should you recommend?

A) Change the autoscaling metric to [agent.googleapis.com/memory/percent_used](https://www.google.com/search?q=https://agent.googleapis.com/memory/percent_used).
B) Restart the affected instances on a staggered schedule.
C) SSH to each instance and restart the application process.
D) Increase the maximum number of instances in the autoscaling group.

**Answer:** [D]

Explanation: The core issue is that the current capacity (the maximum limit of the Managed Instance Group) has been exhausted while the demand (CPU-intensive application processes) continues to exceed what the existing fleet can handle. Since the database and other systems are healthy, the bottleneck is purely the compute layer. **Increasing the maximum number of instances** allows the autoscaler to provision more VMs immediately to distribute the load, which is the fastest way to resume serving traffic. Option A is incorrect because the bottleneck is CPU, not memory. Options B and C are temporary "band-aids" that don't solve the underlying capacity issue and could lead to further downtime as instances stop serving traffic during the restart.

---

### Question 15: https://www.leetquiz.com/quiz/cly2odj5b000lifkpj01z91q8/practice?status=UNANSWERED

You are tasked with migrating files from your on-premises environment to Google Cloud Storage. To ensure the highest level of security, you need the files to be encrypted using customer-supplied encryption keys (CSEK). What specific steps should you take to achieve this during the upload process?

A) Supply the encryption key in a .boto configuration file. Use gsutil to upload the files.
B) Supply the encryption key using gcloud config. Use gsutil to upload the files to that bucket.
C) Use gsutil to upload the files, and use the flag --encryption-key to supply the encryption key.
D) Use gsutil to create a bucket, and use the flag --encryption-key to supply the encryption key. Use gsutil to upload the files to that bucket.

**Answer:** [A]

Explanation: When using **Customer-Supplied Encryption Keys (CSEK)** with the `gsutil` tool, the standard and most secure way to provide the keys is through the **.boto configuration file**. Within this file, you define the `encryption_key` (and optionally `decryption_key` for existing objects). This allows `gsutil` to automatically encrypt the data locally before it is transmitted to Google Cloud. Unlike Cloud KMS (CMEK), Google does not store or manage CSEK; if you lose the key defined in your .boto file, the data is unrecoverable. Option C and D are incorrect because `gsutil` does not use a `--encryption-key` flag for these operations; it relies on the configuration file settings.

---

### Question 15: https://www.leetquiz.com/quiz/cly2odu3k000mifkpiogz7477/practice?status=UNANSWERED

Mountkirk Games wants to limit the physical location of resources to their operating Google Cloud regions as part of their effort to manage costs and maintain latency. They are currently deploying their new multiplayer game's backend on Google Kubernetes Engine and using Google's global load balancer. What should you do?

A) Configure an organizational policy which constrains where resources can be deployed.
B) Configure IAM conditions to limit what resources can be configured.
C) Configure the quotas for resources in the regions not being used to 0.
D) Configure a custom alert in Cloud Monitoring so you can disable resources as they are created in other regions.

**Answer:** [A]

Explanation: The **Organization Policy Service** provides centralized and programmatic control over your organization's cloud resources. Specifically, the **Resource Location Restriction** (`gcp.resourceLocations`) constraint is the best practice for ensuring that resources (like GKE clusters, Compute Engine instances, or storage buckets) are only created in approved geographical locations. This acts as a "guardrail" that prevents developers from accidentally or intentionally deploying infrastructure in regions that don't meet latency or cost requirements. Option B is incorrect because IAM manages *who* can do what, but not *where* they can do it. Option C (Quotas) is a reactive and manual workaround that is difficult to maintain at scale. Option D is a reactive approach that doesn't prevent the resource creation in the first place.

---

### Question 16: https://www.leetquiz.com/quiz/cly2oengb000nifkpvlt9zx99/practice?status=UNANSWERED

You have developed an application using Google Cloud Machine Learning (ML) Engine that recognizes famous paintings from images uploaded by users. To ensure quality and functionality, you want to conduct a test where a selected group of users can upload images for the next 24 hours. However, not all of these users have Google Accounts. Given these constraints, how should you allow these users to upload images during the testing period?

A) Have users upload the images to Cloud Storage. Protect the bucket with a password that expires after 24 hours.
B) Have users upload the images to Cloud Storage using a signed URL that expires after 24 hours.
C) Create an App Engine web application where users can upload images. Configure App Engine to disable the application after 24 hours. Authenticate users via Cloud Identity.
D) Create an App Engine web application where users can upload images for the next 24 hours. Authenticate users via Cloud Identity.

**Answer:** [B]

Explanation: The correct answer is B. Signed URLs are the best mechanism to allow users without Google Accounts to perform specific actions (like uploading an object) to a Cloud Storage bucket for a limited time. Cloud Storage does not support "password protection" for buckets in the traditional sense (Option A), and Cloud Identity (Options C and D) requires users to have managed identities, which contradicts the constraint that not all users have Google Accounts. Signed URLs provide a time-limited cryptographic key that grants temporary access to anyone in possession of the URL.

---

### Question 17: https://www.leetquiz.com/quiz/cly2ofwx5000pifkp48w7ma2a/practice?status=UNANSWERED

You are developing an application using different microservices on Google Kubernetes Engine (GKE). These microservices should remain internal to the cluster for security and performance reasons. Each microservice needs to be configured with a specific number of replicas to ensure availability and scalability. Additionally, it is essential that one microservice can address any other microservice in a uniform manner, regardless of how many replicas the target microservice has scaled to. How should you configure your microservices to meet these requirements?

A) Deploy each microservice as a Deployment. Expose the Deployment in the cluster using a Service, and use the Service DNS name to address it from other microservices within the cluster.
B) Deploy each microservice as a Deployment. Expose the Deployment in the cluster using an Ingress, and use the Ingress IP address to address the Deployment from other microservices within the cluster.
C) Deploy each microservice as a Pod. Expose the Pod in the cluster using a Service, and use the Service DNS name to address the microservice from other microservices within the cluster.
D) Deploy each microservice as a Pod. Expose the Pod in the cluster using an Ingress, and use the Ingress IP address name to address the Pod from other microservices within the cluster.

**Answer:** [A]

Explanation: The correct answer is A. In GKE, a **Deployment** is the standard way to manage a group of identical **Pods** (replicas), providing declarative updates and scaling. To allow microservices to communicate with each other internally using a consistent name, you must use a **Service** (specifically a ClusterIP service by default). The Service provides a stable virtual IP and a DNS name that remains constant even as the underlying Pod replicas are created or destroyed. Using an Ingress (Options B and D) is typically for exposing services to external traffic (HTTP/S), and deploying as individual Pods (Options C and D) does not provide the automated management or scaling capabilities of a Deployment.

---

### Question 18:  https://www.leetquiz.com/quiz/cly2ohdyy000sifkpwjtjnmqe/practice?status=UNANSWERED

As a Google Cloud architect, you are responsible for developing and testing a disaster recovery plan for a mission-critical application hosted on Google Cloud Platform (GCP). The plan must adhere to Google-recommended practices and leverage native GCP capabilities. What should you do?

A) Use Deployment Manager to automate service provisioning. Use Activity Logs to monitor and debug your tests.
B) Use Deployment Manager to automate service provisioning. Use Stackdriver to monitor and debug your tests.
C) Use gcloud scripts to automate service provisioning. Use Activity Logs to monitor and debug your tests.
D) Use gcloud scripts to automate service provisioning. Use Stackdriver to monitor and debug your tests.

**Answer:** [B]

Explanation: The correct answer is B. For disaster recovery (DR), Google Cloud best practices emphasize Infrastructure as Code (IaC) to ensure environment consistency and rapid recovery. **Deployment Manager** (now often superseded by Terraform, but still the native GCP IaC tool in this context) allows for automated, repeatable service provisioning. To monitor the health of the recovery process and debug issues during testing, **Stackdriver** (now integrated into the **Google Cloud Operations Suite**) provides the comprehensive logging and monitoring necessary for mission-critical applications. While `gcloud` scripts (Options C and D) can automate tasks, they are more imperative and harder to manage at scale compared to the declarative approach of Deployment Manager. Activity Logs (Options A and C) are more limited in scope compared to the full observability suite offered by Stackdriver.

---

### Question 19: https://www.leetquiz.com/quiz/cly2oimq8000tifkp9cwzo7n0/practice?status=UNANSWERED

Your company stores highly sensitive data in Google Cloud Storage buckets, and data analysts have Identity Access Management (IAM) permissions to read from these buckets. To ensure security, you want to prevent data analysts from accessing the data in these buckets when they are not connected to the company's office network. How should you configure your Google Cloud environment to meet this requirement?

A) Create a VPC Service Controls perimeter that includes the projects with the buckets. 2. Create an access level with the CIDR of the office network.
B) Create a firewall rule for all instances in the Virtual Private Cloud (VPC) network for source range. 2. Use the Classless Inter-domain Routing (CIDR) of the office network.
C) Create a Cloud Function to remove IAM permissions from the buckets, and another Cloud Function to add IAM permissions to the buckets. 2. Schedule the Cloud Functions with Cloud Scheduler to add permissions at the start of business and remove permissions at the end of business.
D) Create a Cloud VPN to the office network. 2. Configure Private Google Access for on-premises hosts.

**Answer:** [A]

Explanation: The correct answer is A. **VPC Service Controls** (VPC SC) allows you to define a security perimeter around Google-managed services like Cloud Storage. While IAM controls *who* has access, VPC SC controls *from where* that access is allowed. By creating an **Access Level** using **Access Context Manager**, you can restrict access based on the source IP address (the office network's CIDR). If an analyst attempts to access the bucket from outside this perimeter (e.g., from home), the request will be blocked even if their IAM permissions are valid. Firewall rules (Option B) only apply to VPC network traffic (VMs), not to global SaaS services like Cloud Storage. Cloud Functions (Option C) are a complex and brittle workaround for a problem VPC SC is specifically designed to solve. Private Google Access (Option D) enables internal IPs to reach Google APIs but does not provide the restriction mechanism required here.

---

### Question 20: https://www.leetquiz.com/quiz/cly2oj54l000uifkp6oio8cwm/practice?status=UNANSWERED

The Director of Engineering requires all developers to move their development infrastructure resources from on-premises virtual machines (VMs) to Google Cloud Platform (GCP) to reduce costs. These development resources often start and stop throughout the day and need to maintain their state across these cycles. Additionally, the finance department needs visibility into the associated costs. You are asked to design a process for running a development environment in GCP that ensures cost visibility while maintaining the state across start/stop cycles. Which two steps should you take? (Choose two.)

A) Use the --no-auto-delete flag on all persistent disks and stop the VM
B) Use the --auto-delete flag on all persistent disks and terminate the VM
C) Apply VM CPU utilization label and include it in the BigQuery billing export
D) Use Google BigQuery billing export and labels to associate cost to groups
E) Store all state in Google Cloud Storage, snapshot the persistent disks, and terminate the VM

**Answer:** [A, D]

Explanation: The correct answers are A and D. To maintain the state of development resources across start/stop cycles, you should stop the VM instead of deleting (terminating) it. Using the `--no-auto-delete` flag on persistent disks (Option A) ensures that the data remains intact even if the VM instance is accidentally deleted, though simply stopping the VM is the primary way to retain state while ceasing Compute Engine charges. For cost visibility, Google Cloud best practices recommend using **Labels** to tag resources (e.g., by department, project, or environment) and enabling the **BigQuery billing export** (Option D) to perform detailed cost analysis and provide the finance department with the required transparency. Option B and E involve terminating the VM, which is inefficient for frequent daily cycles compared to stopping. Option C is incorrect because "CPU utilization" is a performance metric, not a standard metadata label used for billing attribution.

---

### Question 21: https://www.leetquiz.com/quiz/cly2oje9j000vifkpcijgdjty/practice?status=UNANSWERED

In a scenario where your customer support tool logs all email and chat conversations to Cloud Bigtable for long-term retention and subsequent analysis, it is crucial to sanitize the data to remove any personally identifiable information (PII) or payment card information (PCI) before storing it. What is the recommended approach for performing this sanitization to ensure compliance with data protection regulations?

A) Hash all data using SHA256
B) Encrypt all data using elliptic curve cryptography
C) De-identify the data with the Cloud Data Loss Prevention API
D) Use regular expressions to find and redact phone numbers, email addresses, and credit card numbers

**Answer:** [C]

Explanation: The correct answer is C. The **Cloud Data Loss Prevention (DLP) API** is the native Google Cloud service specifically designed to inspect, identify, and redact sensitive information like PII and PCI. It uses a combination of built-in infoType detectors, machine learning, and pattern matching that is far more robust than simple regular expressions (Option D), which often miss edge cases or complex formats. Hashing (Option A) or Encrypting (Option B) the entire dataset would make subsequent analysis of the non-sensitive text impossible, whereas the DLP API allows for targeted de-identification (redaction, masking, or tokenization) while preserving the utility of the remaining data.

---

### Question 22: https://www.leetquiz.com/quiz/cly2ojzb3000wifkpe2etjnwd/practice?status=UNANSWERED

TerramEarth manufactures heavy equipment for the mining and agricultural industries. They have 20 million vehicles in operation, collecting 120 fields of data per second, with about 200,000 vehicles connected to a cellular network. Data is currently stored locally on the vehicles and transferred to a single U.S. west coast-based data center when serviced. The current system results in data that is 3 weeks old, and they want to reduce the unplanned vehicle downtime to less than 1 week and minimize file storage costs. TerramEarth has decided to store data files in Cloud Storage. You need to configure Cloud Storage lifecycle rules to retain data for 1 year and minimize the storage cost. Which two actions should you take?

A) Create a Cloud Storage lifecycle rule with Age: '30', Storage Class: 'Standard', and Action: 'Set to Coldline', and create a second GCS life-cycle rule with Age: '365', Storage Class: 'Coldline', and Action: 'Delete'.
B) Create a Cloud Storage lifecycle rule with Age: '30', Storage Class: 'Coldline', and Action: 'Set to Nearline', and create a second GCS life-cycle rule with Age: '91', Storage Class: 'Coldline', and Action: 'Set to Nearline'.
C) Create a Cloud Storage lifecycle rule with Age: '90', Storage Class: 'Standard', and Action: 'Set to Nearline', and create a second GCS life-cycle rule with Age: '91', Storage Class: 'Nearline', and Action: 'Set to Coldline'.
D) Create a Cloud Storage lifecycle rule with Age: '30', Storage Class: 'Standard', and Action: 'Set to Coldline', and create a second GCS life-cycle rule with Age: '365', Storage Class: 'Nearline', and Action: 'Delete'.

**Answer:** [A]

Explanation: The correct answer is A. To balance the need for data retention (1 year) with the goal of minimizing costs, Google Cloud Storage Lifecycle Management is the ideal tool. Moving data from **Standard** to **Coldline** after 30 days (when the data is no longer "hot" and unlikely to be accessed frequently for immediate downtime analysis) significantly reduces storage costs. The second rule ensures the data is automatically deleted after 365 days (1 year) to meet the retention requirement without incurring unnecessary long-term storage fees. Option C and D contain logical errors in storage class transitions (e.g., trying to move Nearline to Coldline at nearly the same time or deleting from the wrong class), and Option B incorrectly moves data from a cheaper class (Coldline) to a more expensive one (Nearline).

---

### Question 23: https://www.leetquiz.com/quiz/cly2ok7tb000xifkpt7aptm9i/practice?status=UNANSWERED

Your web application uses Google Kubernetes Engine (GKE) to manage several workloads. One of these workloads is a stateful application that requires a consistent set of hostnames for each pod, even after scaling operations or pod restarts. Which feature of Kubernetes should you use to accomplish this?

A) StatefulSets
B) Role-based access control
C) Container environment variables
D) Persistent Volumes

**Answer:** [A]

Explanation: The correct answer is A. **StatefulSets** are designed specifically for applications that require stable, unique network identifiers (like hostnames) and persistent storage. Unlike a Deployment, where Pods are interchangeable and receive random names, a StatefulSet assigns a sticky identity (e.g., `web-0`, `web-1`) to each Pod. This identity is maintained even if the Pod is rescheduled to a different node. While Persistent Volumes (Option D) provide stable storage, they do not manage the network identity or hostnames of the Pods. RBAC (Option B) handles security permissions, and environment variables (Option C) are for configuration but do not provide persistent hostnames across restarts.

---

### Question 24: https://www.leetquiz.com/quiz/cly2oklzd000yifkp6ka79m9b/practice?status=UNANSWERED

Refer to the Dress4Win case study: Dress4Win is a web-based company specializing in personal wardrobe management via a web app and mobile application. They also maintain a social network connecting users with designers and retailers. With rapid application growth, Dress4Win is migrating to a public cloud due to current infrastructure limitations. You are responsible for the security of data stored in Cloud Storage for Dress4Win. You have already created a set of Google Groups and assigned the appropriate users to those groups. Considering Dress4Win's business and technical requirements, what should you do to ensure security using Google best practices and implementing the simplest design?

A) Assign custom IAM roles to the Google Groups you created in order to enforce security requirements. Encrypt data with a customer-supplied encryption key when storing files in Cloud Storage.
B) Assign custom IAM roles to the Google Groups you created in order to enforce security requirements. Enable default storage encryption before storing files in Cloud Storage.
C) Assign predefined IAM roles to the Google Groups you created in order to enforce security requirements. Utilize Google's default encryption at rest when storing files in Cloud Storage.
D) Assign predefined IAM roles to the Google Groups you created in order to enforce security requirements. Ensure that the default Cloud KMS key is set before storing files in Cloud Storage.

**Answer:** [C]

Explanation: The correct answer is C. Google Cloud best practices for a "simplest design" recommend using **predefined IAM roles** whenever they meet the business requirements, as they are maintained by Google and reduce administrative overhead compared to custom roles (Options A and B). Regarding encryption, Google Cloud **automatically encrypts all data at rest** by default using Google-managed keys. Unless there is a specific regulatory requirement for Customer-Supplied (CSEK) or Customer-Managed (CMEK) keys, relying on the default encryption is the simplest and most efficient approach. Option D is unnecessary because default encryption is active by default and does not require setting a Cloud KMS key manually.

---

### Question 25: https://www.leetquiz.com/quiz/cly2okzjr000zifkpzwajj9vz/practice?status=UNANSWERED

You are planning to deploy a business-critical application on Google Compute Engine. Given the importance of maintaining uptime, you need to design an architecture that includes a disaster recovery plan. This plan should ensure that if one region suffers an outage, the application can automatically fail over to resources in another region, minimizing downtime. What should you do?

A) Deploy the application on two Compute Engine instances in the same project but in a different region. Use the first instance to serve traffic, and use the HTTP load balancing service to fail over to the standby instance in case of a disaster.
B) Deploy the application on a Compute Engine instance. Use the instance to serve traffic, and use the HTTP load balancing service to fail over to an instance on your premises in case of a disaster.
C) Deploy the application on two Compute Engine instance groups, each in the same project but in a different region. Use the first instance group to serve traffic, and use the HTTP load balancing service to fail over to the standby instance group in case of a disaster.
D) Deploy the application on two Compute Engine instance groups, each in a separate project and a different region. Use the first instance group to serve traffic, and use the HTTP load balancing service to fail over to the standby instance group in case of a disaster.

**Answer:** [C]

Explanation: The correct answer is C. For business-critical applications, Google Cloud best practices recommend using **Managed Instance Groups (MIGs)** because they provide automated scaling, healing, and multi-zone/region availability. By deploying two MIGs in different regions within the same project and placing them behind a **Global HTTP(S) Load Balancer**, you create a robust failover mechanism. The Load Balancer automatically detects if a regional backend becomes unhealthy or unreachable and redirects traffic to the available standby region. Option A uses single instances, which lacks high availability within the region itself. Option B involves on-premises failover, which is more complex and less "native" than a multi-region cloud setup. Option D suggests separate projects, which adds unnecessary administrative and networking complexity for a standard regional failover setup.

---

### Question 26: https://www.leetquiz.com/quiz/cly2olcmk0010ifkpd77d6i76/practice?status=UNANSWERED

In your Google Cloud Platform (GCP) environment, you need a solution for the centralized collection of all administrative activity and VM system logs within your project. Given the requirement that logs need to be collected from both VMs and services, which approach should you take?

A) All admin and VM system logs are automatically collected by Stackdriver.
B) Stackdriver automatically collects admin activity logs for most services. The Stackdriver Logging agent must be installed on each instance to collect system logs.
C) Launch a custom syslogd compute instance and configure your GCP project and VMs to forward all logs to it.
D) Install the Stackdriver Logging agent on a single compute instance and let it collect all audit and access logs for your environment.

**Answer:** [B]

Explanation: The correct answer is B. In Google Cloud, **Cloud Audit Logs** (formerly part of Stackdriver) automatically captures administrative activities for most GCP services without any additional configuration. However, to capture **system logs** from inside a Compute Engine VM (such as syslog, auth.log, or third-party application logs), you must install the **Logging agent** (based on fluentd) on each specific instance. Option A is incorrect because system-level logs inside a VM are not captured by default. Option C is a manual, non-native approach that increases operational overhead. Option D is technically impossible; the agent must run on the local instance it is monitoring to access its internal log files.

---

### Question 27: https://www.leetquiz.com/quiz/cly2olu8w0011ifkp8n0wj615/practice?status=UNANSWERED

You have an application that makes HTTP requests to Cloud Storage for storing and retrieving data. Occasionally, the requests fail with HTTP status codes of 5xx and 429, indicating server errors and too many requests, respectively. How should you handle these types of errors to ensure reliability and performance of your application?

A) Use gRPC instead of HTTP for better performance.
B) Implement retry logic using a truncated exponential backoff strategy.
C) Make sure the Cloud Storage bucket is multi-regional for geo-redundancy.
D) Monitor [https://status.cloud.google.com/feed.atom](https://status.cloud.google.com/feed.atom) and only make requests if Cloud Storage is not reporting an incident.

**Answer:** [B]

Explanation: The correct answer is B. According to Google Cloud best practices, transient errors (5xx) and rate-limiting errors (429) should be handled using **truncated exponential backoff**. This strategy involves retrying the request after a short delay, then progressively increasing the wait time between subsequent retries up to a maximum (the "truncation"). This approach prevents "thundering herd" problems and allows the system time to recover. While multi-regional buckets (Option C) provide redundancy, they do not resolve 429 rate-limiting issues. Using gRPC (Option A) is a protocol choice that doesn't inherently fix error handling, and monitoring the status feed (Option D) is too slow and coarse-grained for handling individual request failures.

---

### Question 28: https://www.leetquiz.com/quiz/cly2ompj30012ifkp823lwbqz/practice?status=UNANSWERED

One of the developers on your team deployed their application in Google Container Engine (GKE) using a Dockerfile. They report that their application deployments are taking too long. The Dockerfile includes installing Python and dependencies from a requirements.txt file. You want to optimize this Dockerfile for faster deployment times without adversely affecting the application's functionality. Which two actions should you take? (Choose two.)

A) Remove Python after running pip
B) Remove dependencies from requirements.txt
C) Use a slimmed-down base image like Alpine Linux
D) Use larger machine types for your Google Container Engine node pools
E) Copy the source after the package dependencies (Python and pip) are installed

**Answer:** [C, E]

Explanation: The correct answers are C and E. To optimize Docker build and deployment times, you should leverage **layer caching** and **minimal base images**. Using a slimmed-down base image like **Alpine Linux** (Option C) significantly reduces the image size, leading to faster pulls and lower storage costs. Additionally, by copying the application source code *after* installing dependencies (Option E), you ensure that the expensive dependency installation layer is only rebuilt when `requirements.txt` changes, rather than every time a line of source code is modified. Removing Python (Option A) would break the application, and removing dependencies (Option B) would affect functionality. Larger machine types (Option D) might speed up the build process slightly but don't address the root cause of inefficient image layering or size.

---

### Question 29: https://www.leetquiz.com/quiz/cly2on1x10013ifkpmqg0tqv9/practice?status=UNANSWERED

Your web application is hosted on Google Cloud Platform and must comply with the requirements of the European Union's General Data Protection Regulation (GDPR). As the architect responsible for the technical architecture, you need to ensure that the application handles personal data appropriately and meets GDPR standards. What should you do?

A) Ensure that your web application only uses native features and services of Google Cloud Platform, because Google already has various certifications and provides pass-on compliance when you use native features.
B) Enable the relevant GDPR compliance setting within the GCP Console for each of the services in use within your application.
C) Ensure that Cloud Security Scanner is part of your test planning strategy in order to pick up any compliance gaps.
D) Define a design for the security of data in your web application that meets GDPR requirements.

**Answer:** [D]

Explanation: The correct answer is D. Compliance is a **shared responsibility**. While Google Cloud provides a secure infrastructure and is GDPR-compliant at the platform level, the customer is responsible for ensuring that the applications they build and the data they manage are handled according to GDPR requirements (e.g., data minimization, encryption, and right to erasure). There is no single "GDPR switch" in the console (Option B), and using native features alone does not guarantee compliance if your application logic mishandles data (Option A). Cloud Security Scanner (Option C) is a tool for finding web vulnerabilities like XSS, but it cannot verify legal or regulatory data privacy compliance.

---

### Question 30: https://www.leetquiz.com/quiz/cly2onjli0014ifkpm14kxg0b/practice?status=UNANSWERED

Your company has developed an application running on Google App Engine that allows users to upload music files and share them with others. To improve the user experience and reduce backend load, you want to allow users to upload files directly from their browser sessions into Google Cloud Storage, without the payload passing through your backend servers. What configuration should you implement to achieve this?

A) Set a CORS configuration in the target Cloud Storage bucket where the base URL of the App Engine application is an allowed origin. Use the Cloud Storage Signed URL feature to generate a POST URL.
B) Set a CORS configuration in the target Cloud Storage bucket where the base URL of the App Engine application is an allowed origin. Assign the Cloud Storage WRITER role to users who upload files.
C) Use the Cloud Storage Signed URL feature to generate a POST URL. Use App Engine default credentials to sign requests against Cloud Storage.
D) Assign the Cloud Storage WRITER role to users who upload files. Use App Engine default credentials to sign requests against Cloud Storage.

**Answer:** [A]

Explanation: The correct answer is A. To allow a browser-based application to upload directly to a different domain (Cloud Storage), you must configure **Cross-Origin Resource Sharing (CORS)** on the destination bucket to permit requests from the App Engine origin. Furthermore, to authorize the upload without requiring the user to have their own Google Account or IAM permissions, you should use **Signed URLs**. A Signed URL provides temporary, limited-time permission to perform a specific action (like an HTTP POST) using the credentials of a service account. Options B and D are incorrect because assigning IAM roles (WRITER) to end-users is neither secure nor practical for general web users. Option C misses the critical CORS configuration required for browser-to-bucket communication.

---

### Question 31: https://www.leetquiz.com/quiz/cly2onygj0015ifkpc3s28pu8/practice?status=UNANSWERED

TerramEarth manufactures heavy equipment for the mining and agricultural industries. They currently have over 500 dealers and service centers in 100 countries. TerramEarth has about 1 petabyte (PB) of vehicle testing data in a private data center. Their goal is to move this data to Cloud Storage for the machine learning team to use. Currently, a 1-Gbps interconnect link is available. The machine learning team wants to start using the data in a month. What should you do?

A) Request Transfer Appliances from Google Cloud, export the data to appliances, and return the appliances to Google Cloud.
B) Configure the Storage Transfer service from Google Cloud to send the data from your data center to Cloud Storage.
C) Make sure there are no other users consuming the 1Gbps link, and use multi-thread transfer to upload the data to Cloud Storage.
D) Export files to an encrypted USB device, send the device to Google Cloud, and request an import of the data to Cloud Storage.

**Answer:** [A]

Explanation: The correct answer is A. The primary constraint here is the **timeframe** (1 month) relative to the **data volume** (1 PB) and **bandwidth** (1 Gbps). 1. **Math Check:** At a sustained speed of 1 Gbps, transferring 1 PB would take approximately **92-124 days** (depending on network overhead and protocol efficiency), which far exceeds the 30-day requirement. 2. **Solution:** **Transfer Appliance** is a high-capacity storage server that you lease from Google. You load your data onto it locally and ship it back to a Google data center, where it is uploaded directly to Cloud Storage. For 1 PB, you would use multiple appliances (e.g., several TA300 units) in parallel to meet the one-month deadline. 3. **Why others fail:** Storage Transfer Service (Option B) and multi-threaded uploads (Option C) are "online" methods limited by the physical speed of the 1 Gbps link. Exporting to a standard USB device (Option D) is not a supported enterprise-scale ingestion method for Petabyte-scale data in GCP.

