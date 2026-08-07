#!/usr/bin/env python3
"""Generate product detail pages in service-details style."""

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PRODUCTS = [
    {
        "slug": "product-erp",
        "title": "ERP",
        "subtitle": "Enterprise Resource Planning System",
        "icon": "bi-building",
        "meta": "Enterprise Application",
        "description": "AIBizs ERP unifies finance, operations, supply chain, HR, and customer management in one intelligent platform built for enterprises in Oman and the GCC.",
        "lead": "Comprehensive enterprise resource planning with integrated modules for finance, inventory, manufacturing, CRM, projects, and human resources — all with AI-ready workflows and multi-company support.",
        "overview_title": "Unified Enterprise Operations",
        "overview_p1": "AIBizs ERP connects every core business function into a single source of truth. From general ledger and treasury to procurement, manufacturing, and project delivery, teams work from consistent data with role-based access and real-time visibility.",
        "overview_p2": "Each module is designed for scalability across multiple companies and entities, with consolidation, audit trails, and AI integration built in from day one.",
        "image": "assets/img/finance/im2.png",
        "image_alt": "Oman Finance ERP dashboard",
        "sidebar_title": "Ready to Modernize Your ERP?",
        "sidebar_text": "Speak with our team about ERP implementation, module rollout, and integration with your existing systems.",
        "sidebar_cta": "Request Consultation",
        "sidebar_cta_href": "index.html#contact",
        "sidebar_guarantee": "ISO Certified Delivery",
        "sidebar_items": [
            ("bi-cash-stack", "Finance & Accounting", "GL, AP, AR, treasury, and reporting"),
            ("bi-box-seam", "Operations & Inventory", "Stock, manufacturing, and workflows"),
            ("bi-people-fill", "HR & Self Service", "Employee lifecycle and payroll integration"),
        ],
        "modules": [
            ("bi-cash-stack", "Finance", "Comprehensive financial management and accounting operations"),
            ("bi-arrow-down-circle", "Accounts Payable", "Manage vendor invoices, payments, and outstanding liabilities"),
            ("bi-arrow-up-circle", "Accounts Receivable", "Track customer invoices, payments, and receivables management"),
            ("bi-journal-text", "General Ledger", "Central accounting ledger with complete financial transaction records"),
            ("bi-bank", "Treasury", "Cash management, banking operations, and financial planning"),
            ("bi-box-seam", "Inventory Management", "Real-time inventory tracking, stock control, and warehouse management"),
            ("bi-gear", "Operation Management", "Streamline day-to-day business operations and workflows"),
            ("bi-person-heart", "Customer Relationship Management", "Manage customer interactions, sales pipeline, and customer service"),
            ("bi-truck", "Supplier Relation Management", "Manage supplier relationships, contracts, and procurement processes"),
            ("bi-door-open", "Vendor Portal", "Self-service portal for vendors to manage orders and invoices"),
            ("bi-receipt", "E-Invoicing", "Electronic invoice generation, submission, and compliance management"),
            ("bi-people-fill", "Human Resource Management", "Complete HR operations including employee data and HR processes"),
            ("bi-cpu", "Manufacturing", "Production planning, bill of materials, and manufacturing execution"),
            ("bi-kanban", "Project Management", "Plan, track, and manage projects with resources and timelines"),
            ("bi-person-badge", "Employee Self Service", "Employee portal for accessing personal information and services"),
        ],
        "platform": [
            ("bi-robot", "AI Integration", "All modules come with AI integration capabilities"),
            ("bi-shield-lock", "Role Based Access", "Granular permissions across companies and departments"),
            ("bi-building", "Multi Company", "Manage multiple legal entities from one platform"),
            ("bi-diagram-3", "Consolidation", "Group-level financial and operational consolidation"),
        ],
    },
    {
        "slug": "product-qhse",
        "title": "QHSE",
        "subtitle": "Quality, Health, Safety & Environment",
        "icon": "bi-shield-check",
        "meta": "Enterprise Application",
        "description": "Manage workplace safety, quality compliance, and environmental performance with real-time dashboards, incident tracking, and audit-ready records.",
        "lead": "A complete QHSE platform for risk identification, incident management, inspections, quality assurance, and environmental monitoring — integrated with IVMS for journey safety.",
        "overview_title": "Safety & Compliance at Scale",
        "overview_p1": "AIBizs QHSE helps industrial and corporate organizations identify risks, report incidents, conduct inspections, and close actions with full traceability. Dashboards give HSE managers real-time visibility into performance indicators and open actions.",
        "overview_p2": "Built for multi-site operations in Oman and the GCC, with role-based access, multi-company support, and AI-assisted analysis across every module.",
        "image": "assets/img/hse/hse1.png",
        "image_alt": "QHSE safety and environment dashboard",
        "sidebar_title": "Strengthen Your HSE Program",
        "sidebar_text": "Talk to us about QHSE deployment, IVMS integration, and compliance reporting for your organization.",
        "sidebar_cta": "Request Consultation",
        "sidebar_cta_href": "index.html#contact",
        "sidebar_guarantee": "Audit-Ready Records",
        "sidebar_items": [
            ("bi-exclamation-triangle", "Risk & Incidents", "Identify, report, and resolve safety events"),
            ("bi-search", "Inspections", "Schedule and document field inspections"),
            ("bi-award", "Quality & Vendors", "Quality management and vendor evaluation"),
        ],
        "modules": [
            ("bi-exclamation-triangle", "Risk Identification & Loss Reporting", "Identify potential risks, assess impact, and track loss incidents systematically"),
            ("bi-clipboard-x", "Incident Management", "Report, track, and manage workplace incidents and near-misses effectively"),
            ("bi-search", "Inspection", "Schedule, conduct, and document safety and quality inspections"),
            ("bi-geo-alt", "Journey Plan with IVMS Integration", "Plan and monitor vehicle journeys with integrated vehicle tracking"),
            ("bi-arrow-repeat", "Management of Change", "Control and manage organizational changes with risk assessment"),
            ("bi-award", "Quality Management", "Ensure quality standards through quality control and assurance processes"),
            ("bi-star", "Vendor Evaluation", "Assess and evaluate vendor performance and compliance standards"),
            ("bi-calendar-event", "Meeting", "Schedule and manage safety meetings, agendas, and action items"),
            ("bi-check-circle", "Fit to Work", "Assess employee fitness for work and manage medical clearances"),
        ],
        "platform": [
            ("bi-robot", "AI Integration", "All modules come with AI integration capabilities"),
            ("bi-shield-lock", "Role Based Access", "Granular permissions for HSE teams and site managers"),
            ("bi-building", "Multi Company", "Manage multiple sites and entities centrally"),
        ],
    },
    {
        "slug": "product-hrms",
        "title": "AIVizion HRMS",
        "subtitle": "Human Resource Management System",
        "icon": "bi-people",
        "meta": "Enterprise Application",
        "description": "Streamline the full employee lifecycle from recruitment and onboarding to payroll, leave, performance, and self-service.",
        "lead": "AIVizion HRMS centralizes people operations with payroll automation, leave management, recruitment pipelines, appraisals, and employee self-service — tailored for Omani organizations.",
        "overview_title": "People Operations, Simplified",
        "overview_p1": "Manage hiring, onboarding, compensation, attendance, and offboarding in one HR platform. HR teams gain dashboards for workforce analytics while employees access self-service tools for leave, documents, and personal records.",
        "overview_p2": "Integrated with ERP and payroll compliance requirements, with AI-assisted workflows and multi-company support for growing organizations.",
        "image": "assets/img/hrimage/payroll-hero.png",
        "image_alt": "AIVizion HRMS dashboard for Oman workforce",
        "sidebar_title": "Explore the AIVizion Brochure",
        "sidebar_text": "Browse a presentable, shareable overview of every AIVizion HRMS module — ideal for internal reviews and client presentations.",
        "sidebar_cta": "View Brochure",
        "sidebar_cta_href": "hrms-brochure.html",
        "sidebar_guarantee": "Omani Workforce Ready",
        "sidebar_items": [
            ("bi-wallet2", "Payroll", "Automated payroll with tax compliance"),
            ("bi-calendar-check", "Leave Management", "Requests, approvals, and balances"),
            ("bi-briefcase", "Recruitment", "End-to-end hiring workflows"),
        ],
        "modules": [
            ("bi-wallet2", "Payroll", "Automated payroll processing with tax calculations and compliance", "hrms-payroll.html"),
            ("bi-person-badge", "Employee Self Service", "Employee portal for accessing personal information and HR services", "hrms-employee-self-service.html"),
            ("bi-calendar-check", "Leave Management", "Manage employee leave requests, approvals, and balance tracking", "hrms-leave-management.html"),
            ("bi-person-plus", "Employee Onboarding", "Streamline new employee onboarding process and documentation", "hrms-employee-onboarding.html"),
            ("bi-person-dash", "Employee Offboarding", "Manage employee exit process, asset return, and final settlements", "hrms-employee-offboarding.html"),
            ("bi-graph-up", "Appraisal", "Performance evaluation, goal setting, and career development tracking", "hrms-appraisal.html"),
            ("bi-briefcase", "Recruitment", "Manage job postings, applications, interviews, and hiring workflow", "hrms-recruitment.html"),
            ("bi-phone", "Mobile Application", "iOS and Android app with self-service, geo-fenced clocking, approvals, and AI chat", "hrms-mobile-application.html"),
        ],
        "platform": [
            ("bi-robot", "AI Integration", "All modules come with AI integration capabilities"),
            ("bi-shield-lock", "Role Based Access", "HR, manager, and employee permission levels"),
            ("bi-building", "Multi Company", "Support for multiple legal entities and branches"),
        ],
    },
    {
        "slug": "product-business-intelligence",
        "title": "Business Intelligence",
        "subtitle": "AI-Enabled Analytics Platform",
        "icon": "bi-graph-up-arrow",
        "meta": "Enterprise Application",
        "description": "Connect any data source, build interactive dashboards, and unlock AI-powered insights without heavy custom development.",
        "lead": "AIBizs Business Intelligence delivers Power BI–class analytics with universal database connectivity, data lakes, no-code APIs, and AI-driven natural language queries.",
        "overview_title": "Intelligent Analytics for Every Team",
        "overview_p1": "Bring together structured and unstructured data from databases, APIs, files, and cloud services. Build interactive dashboards, automate reports, and expose secure APIs to downstream applications without writing code.",
        "overview_p2": "AI capabilities help users ask questions in natural language, detect trends, and generate insights — making enterprise data accessible to finance, operations, and leadership teams.",
        "image": "assets/img/bigdata/bd1.png",
        "image_alt": "Big data analytics dashboard",
        "sidebar_title": "Unlock Your Data",
        "sidebar_text": "Get a consultation on BI implementation, data lake design, and dashboard development for your organization.",
        "sidebar_cta": "Request Consultation",
        "sidebar_cta_href": "index.html#contact",
        "sidebar_guarantee": "Secure Data Access",
        "sidebar_items": [
            ("bi-database", "Data Connectivity", "SQL, NoSQL, and cloud sources"),
            ("bi-graph-up", "Dashboards", "Interactive visual analytics"),
            ("bi-robot", "AI Analytics", "Predictions and NL queries"),
        ],
        "modules": [
            ("bi-database", "Universal Database Connectivity", "Connect with any popular database including SQL, NoSQL, and cloud databases"),
            ("bi-cloud-arrow-down", "Data Lake Creation", "Build comprehensive data lakes to consolidate and store data from multiple sources"),
            ("bi-code-slash", "No-Code API Builder", "Build secure APIs without coding to expose data to external applications"),
            ("bi-robot", "AI-Powered Analytics", "Leverage advanced AI for intelligent insights, predictions, and automated analysis"),
            ("bi-graph-up", "Interactive Dashboards", "Create dynamic, interactive dashboards with drag-and-drop visualization builder"),
            ("bi-file-earmark-text", "Advanced Reporting", "Generate comprehensive reports with customizable templates and scheduling"),
            ("bi-bar-chart", "Data Visualization", "Rich visualization library with charts, graphs, maps, and custom visualizations"),
            ("bi-funnel", "Data Transformation", "Transform and prepare data with powerful ETL capabilities and data modeling"),
            ("bi-lightning", "Real-Time Analytics", "Perform real-time data analysis and stream processing for instant insights"),
            ("bi-shield-check", "Enterprise Security", "Secure data access with role-based permissions, encryption, and compliance"),
            ("bi-share", "Data Sharing & Collaboration", "Share insights, dashboards, and reports securely with team members"),
            ("bi-arrow-repeat", "Automated Refresh", "Schedule automatic data refreshes and keep dashboards up-to-date"),
            ("bi-mobile", "Mobile BI", "Access dashboards and reports on mobile devices with responsive design"),
            ("bi-search", "Natural Language Query", "Ask questions in natural language and get instant answers from your data"),
            ("bi-diagram-3", "Data Integration", "Integrate data from multiple sources including APIs, files, and cloud services"),
        ],
        "platform": [
            ("bi-robot", "Fully AI-Enabled", "AI-driven insights across the analytics stack"),
            ("bi-database", "Universal Database Support", "Connect to any major database or warehouse"),
            ("bi-code-slash", "No-Code API Builder", "Expose data securely without custom development"),
            ("bi-graph-up-arrow", "PowerBI-like Features", "Enterprise dashboards and self-service BI"),
            ("bi-cloud-arrow-down", "Data Lake Creation", "Consolidate data at scale"),
            ("bi-shield-lock", "Secure Data Exposure", "Role-based access and encrypted connections"),
        ],
    },
    {
        "slug": "product-cloud-infrastructure",
        "title": "DevOps as a Service",
        "subtitle": "Local Cloud, AWS, Azure & More",
        "icon": "bi-gear-wide-connected",
        "meta": "Managed Platform",
        "description": "Managed DevOps across local private cloud, AWS, Azure, and hybrid environments — including on-premises server migration, CI/CD, and integrated security.",
        "lead": "AIBizs delivers end-to-end DevOps as a Service — from local and private cloud to AWS, Azure, and multi-cloud setups, with seamless migration from on-premises servers and security built into every layer.",
        "overview_title": "End-to-End DevOps & Cloud Operations",
        "overview_p1": "We design, build, and operate infrastructure across local private cloud, AWS, Azure, and other platforms. Whether you are launching a new environment or moving workloads from on-premises servers, our team handles architecture, automation, and day-to-day operations so your teams can focus on the business.",
        "overview_p2": "Security is integrated at every stage — access controls, encryption, network hardening, and compliance-ready practices. From migration planning and CI/CD pipelines to backup, monitoring, and incident response, we keep your systems secure, scalable, and always available.",
        "image": "presentation/clouud_intr_imag.png",
        "image_alt": "DevOps and multi-cloud infrastructure architecture",
        "sidebar_title": "Start Your DevOps Journey",
        "sidebar_text": "Discuss cloud strategy, migration from local servers, or managed DevOps across AWS, Azure, and private cloud with our team.",
        "sidebar_cta": "Request Consultation",
        "sidebar_cta_href": "index.html#contact",
        "sidebar_guarantee": "Security-First Operations",
        "sidebar_items": [
            ("bi-hdd-network", "Multi-Cloud & Local Cloud", "Private cloud, AWS, Azure, and hybrid"),
            ("bi-arrow-left-right", "Server Migration", "On-premises to cloud migration"),
            ("bi-shield-check", "Security & Compliance", "Hardening, access control, and monitoring"),
        ],
        "modules": [
            ("bi-hdd-network", "Local & Private Cloud", "Design and operate on-premises and private cloud environments tailored to your requirements"),
            ("bi-cloud", "AWS & Azure Cloud", "Deploy and manage workloads on AWS, Azure, and other leading cloud platforms"),
            ("bi-arrow-left-right", "On-Premises to Cloud Migration", "Plan and execute migration from local servers to cloud with minimal downtime"),
            ("bi-git", "CI/CD & Automation", "Automated build, test, and deployment pipelines with zero-touch production releases"),
            ("bi-code-square", "Infrastructure as Code", "Repeatable, version-controlled infrastructure using modern IaC practices"),
            ("bi-shield-lock", "Security Hardening", "Network segmentation, encryption, secrets management, and vulnerability remediation"),
            ("bi-person-lock", "Access Control & Identity", "Role-based access, MFA, VPN-secured connections, and least-privilege policies"),
            ("bi-hdd-stack", "Backup & Disaster Recovery", "Scheduled backups, replication, and tested recovery procedures for VMs and databases"),
            ("bi-activity", "Monitoring & Alerting", "URL, resource, and performance monitoring with proactive alerting"),
            ("bi-headset", "Incident Management with SLA", "Rapid response with defined service level commitments and stakeholder communication"),
        ],
        "platform": [
            ("bi-gear-wide-connected", "DevOps as a Service", "Fully managed operations across your cloud and on-premises estate"),
            ("bi-clouds", "Multi-Platform Support", "Local cloud, AWS, Azure, and hybrid environments"),
            ("bi-arrow-left-right", "Migration Expertise", "Proven path from local servers to secure cloud infrastructure"),
            ("bi-shield-check", "Security Built In", "Compliance-ready controls at every layer of the stack"),
        ],
    },
    {
        "slug": "product-ivms",
        "title": "IVMS",
        "subtitle": "Integrated Vehicle Management System",
        "icon": "bi-geo-alt-fill",
        "meta": "Enterprise Application",
        "description": "Monitor fleets in real time, plan journeys, manage drivers, and integrate with HSE systems for transport operations in Oman.",
        "lead": "AIBizs IVMS delivers live GPS tracking, journey planning, driver management, fines configuration, and advanced reporting — with HSE system integration for safer fleet operations.",
        "overview_title": "Fleet Visibility & Control",
        "overview_p1": "Track vehicles in real time on live maps, plan routes with area-based alerts, and manage driver profiles, licenses, and performance. Operations teams get dashboards for fleet utilization, incidents, and compliance.",
        "overview_p2": "IVMS integrates with QHSE for journey planning and safety workflows, making it ideal for logistics, oil & gas, construction, and government transport fleets across Oman.",
        "image": "assets/img/hse/he33.png",
        "image_alt": "Fleet management dashboard",
        "sidebar_title": "Optimize Your Fleet",
        "sidebar_text": "Learn how IVMS can improve fleet safety, reduce costs, and integrate with your HSE program.",
        "sidebar_cta": "Request Consultation",
        "sidebar_cta_href": "index.html#contact",
        "sidebar_guarantee": "HSE Integration Ready",
        "sidebar_items": [
            ("bi-geo-alt", "Live Tracking", "Real-time GPS fleet visibility"),
            ("bi-map", "Journey Planning", "Route optimization and area alerts"),
            ("bi-truck", "Fleet Management", "Vehicles, drivers, and maintenance"),
        ],
        "modules": [
            ("bi-truck", "Manage Vehicles", "Comprehensive vehicle registration, maintenance tracking, and fleet management"),
            ("bi-person-badge", "Manage Drivers", "Driver profile management, license tracking, and performance monitoring"),
            ("bi-map", "Journey Plan", "Plan and optimize routes with real-time traffic and route alternatives"),
            ("bi-geo-alt", "Live Tracking", "Real-time GPS tracking of vehicles with location history and movement alerts"),
            ("bi-geo-fill", "Road and Area Mapping", "Detailed mapping of roads, restricted zones, and area-based alerts"),
            ("bi-cash-coin", "Fine Setting", "Configure and manage traffic violations, fines, and penalty rules"),
            ("bi-share", "Data Sharing", "Secure data sharing and integration with external systems and stakeholders"),
            ("bi-file-earmark-text", "Advance Reports", "Comprehensive reporting with customizable analytics and export options"),
            ("bi-speedometer2", "Dashboards", "Interactive dashboards with real-time metrics and visual analytics"),
            ("bi-list-check", "Action Tracker", "Track and manage actions, incidents, and follow-up tasks efficiently"),
            ("bi-shield-check", "HSE Integration", "Seamless integration with Health, Safety, and Environment management systems"),
        ],
        "platform": [
            ("bi-geo-alt-fill", "Real-Time GPS", "Live vehicle location and history"),
            ("bi-shield-check", "HSE Connected", "Integrated journey safety workflows"),
            ("bi-graph-up", "Advanced Analytics", "Fleet performance dashboards and reports"),
            ("bi-share", "Open Integration", "API-ready data sharing with stakeholders"),
        ],
    },
    {
        "slug": "product-agentic-agent",
        "title": "Agentic Agent (AI)",
        "subtitle": "Intelligent AI Agent Platform",
        "icon": "bi-robot",
        "meta": "AI Platform",
        "description": "Build unlimited AI agents that connect to enterprise applications, automate workflows, and respond to voice commands.",
        "lead": "Deploy intelligent AI agents locally or in the cloud. Connect multiple applications, build visual workflows, and control operations through voice-driven reports and dashboards.",
        "overview_title": "AI Agents for Enterprise Automation",
        "overview_p1": "AIBizs Agentic Agent platform lets organizations create unlimited AI agents tailored to specific business processes. Agents connect directly to ERP, HRMS, BI, and custom systems through flexible API integration.",
        "overview_p2": "With visual workflow builders, voice-based actions, and adaptive learning, teams automate repetitive tasks while maintaining security through local hosting options and role-based access control.",
        "image": "assets/img/ai_adoption/ai1.png",
        "image_alt": "Corporate AI adoption dashboard",
        "sidebar_title": "Deploy Intelligent Agents",
        "sidebar_text": "Explore how AI agents can automate workflows and connect your enterprise applications.",
        "sidebar_cta": "Request Consultation",
        "sidebar_cta_href": "index.html#contact",
        "sidebar_guarantee": "Local Hosting Available",
        "sidebar_items": [
            ("bi-diagram-3", "Multi-App Integration", "Connect all enterprise systems"),
            ("bi-mic", "Voice Control", "Voice-driven reports and actions"),
            ("bi-infinity", "Unlimited Agents", "Build agents for every use case"),
        ],
        "modules": [
            ("bi-diagram-3", "Multi-Application Integration", "Connect directly to multiple organizational applications seamlessly"),
            ("bi-server", "Local Hosting", "Deploy and host the AI agent locally for enhanced security and control"),
            ("bi-infinity", "Unlimited Agent Building", "Create unlimited AI agents tailored to your specific business needs"),
            ("bi-diagram-2", "Workflow Management", "Advanced workflow automation with visual workflow builder"),
            ("bi-mic", "Voice-Based Actions", "Execute actions and commands using natural voice interactions"),
            ("bi-graph-up", "Voice-Driven Reports", "Generate comprehensive reports and dashboards through voice commands"),
            ("bi-speedometer2", "Voice-Driven Dashboards", "Build and customize interactive dashboards using voice instructions"),
            ("bi-plug", "Universal Connectivity", "Connect to any application or system with flexible API integration"),
            ("bi-cpu", "Intelligent Automation", "AI-powered decision making and autonomous task execution"),
            ("bi-shield-lock", "Enterprise Security", "Advanced security protocols with role-based access control"),
            ("bi-arrow-repeat", "Real-Time Processing", "Process requests and execute workflows in real-time"),
            ("bi-brain", "Adaptive Learning", "Machine learning capabilities that improve performance over time"),
        ],
        "platform": [
            ("bi-link-45deg", "Multi-App Integration", "Connect ERP, HRMS, BI, and custom apps"),
            ("bi-mic-fill", "Voice Command Interface", "Natural language control and reporting"),
            ("bi-infinity", "Unlimited Agents", "No cap on agent creation"),
            ("bi-diagram-2-fill", "Visual Workflow Builder", "N8N-style automation design"),
            ("bi-server", "Local Deployment", "On-premise hosting for sensitive workloads"),
            ("bi-plug-fill", "Universal API Support", "Flexible integration with any system"),
        ],
    },
    {
        "slug": "product-e-invoicing",
        "title": "e-Invoicing",
        "subtitle": "PEPPOL Standard Compliant Electronic Invoicing",
        "icon": "bi-receipt",
        "meta": "Enterprise Application",
        "description": "OTA-approved Accredited Service Provider for Oman Fawtara e-invoicing with PEPPOL BIS 3.0 compliance and ERP integration.",
        "lead": "ConvergeX by AIBizs enables organizations to create, validate, and submit electronic invoices to the Oman Tax Authority through Fawtara, with PEPPOL network exchange and ERP connectivity.",
        "overview_title": "Compliant E-Invoicing for Oman",
        "overview_p1": "Meet Oman Tax Authority requirements with an OTA-approved ASP platform. Generate UBL 2.1 compliant invoices, validate data before submission, and track status from draft to acknowledgement with full audit trails.",
        "overview_p2": "Integrate with SAP, Oracle, Microsoft Dynamics, or custom systems via REST API. Exchange invoices domestically and internationally through PEPPOL standards.",
        "image": "assets/img/einvoice/im1.jpeg",
        "image_alt": "Oman e-invoicing compliance dashboard",
        "sidebar_title": "Ready for Compliant E-Invoicing?",
        "sidebar_text": "Speak with our team about OTA ASP onboarding, PEPPOL connectivity, and ERP-integrated electronic invoicing.",
        "sidebar_cta": "Visit Website",
        "sidebar_cta_href": "https://convergex.biz/",
        "sidebar_cta_external": True,
        "sidebar_guarantee": "OTA Approved ASP · PEPPOL Approved",
        "sidebar_items": [
            ("bi-shield-check", "OTA ASP", "Oman Tax Authority compliant submissions"),
            ("bi-globe", "PEPPOL Network", "Standardized invoice exchange"),
            ("bi-diagram-3", "ERP Integration", "Automated invoice sync from ERP"),
        ],
        "modules": [
            ("bi-shield-check", "PEPPOL Standard Compliance", "Full compliance with PEPPOL network standards for seamless cross-border invoicing"),
            ("bi-file-earmark-text", "Invoice Generation", "Automated invoice creation with customizable templates, line items, and tax calculations"),
            ("bi-check-circle", "Invoice Validation", "Real-time validation against PEPPOL BIS 3.0 specifications and business rules"),
            ("bi-lock", "Digital Signatures", "Advanced digital signature support with XAdES and PAdES standards"),
            ("bi-filetype-xml", "Multi-Format Support", "Support for UBL 2.1, XML, PDF, and other standard formats"),
            ("bi-send", "Invoice Delivery", "Secure automated delivery through PEPPOL network with confirmation"),
            ("bi-inbox", "Invoice Receiving", "Automated receipt and processing of incoming supplier invoices"),
            ("bi-clipboard-check", "Compliance Reporting", "Comprehensive compliance reports and audit trails"),
            ("bi-diagram-3", "ERP Integration", "Seamless integration with ERP systems for automated processing"),
            ("bi-activity", "Real-Time Status Tracking", "Track invoice status from creation to delivery and payment"),
            ("bi-gear", "Automated Workflows", "Configurable approval workflows and processing rules"),
            ("bi-calculator", "Tax Compliance", "Automatic tax calculation aligned with VAT and local regulations"),
            ("bi-globe", "Multi-Country Support", "Multiple countries and currencies with localized rules"),
            ("bi-archive", "Invoice Archiving", "Secure long-term archiving with searchable metadata"),
            ("bi-file-earmark-check", "Audit Trail", "Complete timestamped logs of all invoice activities"),
        ],
        "platform": [
            ("bi-shield-check", "PEPPOL Compliant", "BIS 3.0 and UBL 2.1 standards"),
            ("bi-lock-fill", "Secure & Encrypted", "Enterprise-grade data protection"),
            ("bi-lightning-charge", "Real-Time Processing", "Instant validation and submission"),
            ("bi-patch-check", "OTA Approved ASP", "Accredited Service Provider for Oman"),
        ],
    },
    {
        "slug": "product-mobile-application",
        "title": "Mobile Application",
        "subtitle": "AI-Powered Mobile Platform",
        "icon": "bi-phone",
        "meta": "Enterprise Application",
        "description": "A unified mobile experience that connects to any enterprise application with AI assistance, real-time sync, and offline capability.",
        "lead": "AIBizs Mobile Application provides a single AI-powered interface to connect ERP, HRMS, QHSE, BI, and custom systems — with real-time synchronization and offline support.",
        "overview_title": "Enterprise Mobility, Unified",
        "overview_p1": "Give field teams and executives one mobile app to access data and workflows from every connected enterprise system. Bi-directional sync keeps information current across platforms without duplicate entry.",
        "overview_p2": "An built-in AI assistant helps users navigate applications, receive smart notifications, and automate cross-app workflows — with bank-level encryption and role-based security.",
        "image": "assets/img/ai_adoption/ai2.png",
        "image_alt": "Mobile enterprise application platform",
        "sidebar_title": "Connect Your Workforce",
        "sidebar_text": "Learn how our mobile platform unifies your enterprise applications with AI-powered mobility.",
        "sidebar_cta": "Request Consultation",
        "sidebar_cta_href": "index.html#contact",
        "sidebar_guarantee": "Offline Mode Supported",
        "sidebar_items": [
            ("bi-plug", "Universal Connectivity", "Connect any enterprise application"),
            ("bi-robot", "AI Assistant", "Intelligent mobile automation"),
            ("bi-phone", "Unified Dashboard", "One app for all systems"),
        ],
        "modules": [
            ("bi-plug", "Universal Application Connectivity", "Seamlessly connect with any application in your enterprise ecosystem"),
            ("bi-brain", "AI-Powered Intelligence", "Advanced AI for intelligent automation and decision-making"),
            ("bi-diagram-3", "Multi-Application Integration", "Connect and manage multiple applications from one mobile interface"),
            ("bi-arrow-left-right", "Real-Time Synchronization", "Bi-directional data sync across all connected applications"),
            ("bi-shield-check", "Enterprise Security", "Bank-level encryption and secure authentication"),
            ("bi-lightning-charge", "Offline Capability", "Work offline and sync automatically when connection is restored"),
            ("bi-robot", "AI Assistant", "Intelligent assistant to navigate and interact with connected applications"),
            ("bi-bell", "Smart Notifications", "AI-driven notifications from all connected applications"),
            ("bi-graph-up", "Unified Dashboard", "Consolidated view of data and insights from all applications"),
            ("bi-cpu", "Intelligent Automation", "AI-powered workflow automation across connected applications"),
        ],
        "platform": [
            ("bi-plug-fill", "Connect Any App", "ERP, HRMS, QHSE, BI, and custom systems"),
            ("bi-brain", "AI Powered", "Intelligent automation on mobile"),
            ("bi-arrow-left-right", "Real-Time Sync", "Always-current data across systems"),
            ("bi-lightning-charge", "Offline Ready", "Work anywhere, sync when online"),
        ],
    },
]


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def module_cards(modules):
    rows = []
    for item in modules:
        if len(item) == 4:
            icon, title, desc, href = item
        else:
            icon, title, desc = item
            href = None

        go = (
            '<span class="product-module-go" aria-hidden="true"><i class="bi bi-arrow-up-right"></i></span>'
            if href
            else ""
        )
        body = f"""              <div class="product-module-icon"><i class="bi {esc(icon)}"></i></div>
              <div class="product-module-body">
                <h4>{esc(title)}</h4>
                <p>{esc(desc)}</p>
              </div>
              {go}"""

        if href:
            card = f"""            <a href="{esc(href)}" class="product-module-card product-module-card-link" aria-label="View {esc(title)} module details">
{body}
            </a>"""
        else:
            card = f"""            <div class="product-module-card">
{body}
            </div>"""

        rows.append(
            f"""          <div class="col-md-6">
{card}
          </div>"""
        )
    return "\n".join(rows)


def benefit_cards(items):
    rows = []
    for icon, title, desc in items:
        rows.append(
            f"""          <div class="col-md-6">
            <div class="benefit-card">
              <div class="benefit-icon"><i class="bi {esc(icon)}"></i></div>
              <h4>{esc(title)}</h4>
              <p>{esc(desc)}</p>
            </div>
          </div>"""
        )
    return "\n".join(rows)


def sidebar_items(items):
    rows = []
    for icon, title, desc in items:
        rows.append(
            f"""                  <li>
                    <i class="bi {esc(icon)}"></i>
                    <div>
                      <h5>{esc(title)}</h5>
                      <p>{esc(desc)}</p>
                    </div>
                  </li>"""
        )
    return "\n".join(rows)


def render_product(p):
    slug = p["slug"]
    filename = f"{slug}.html"
    external = p.get("sidebar_cta_external", False)
    cta_attrs = ' target="_blank" rel="noopener noreferrer"' if external else ""

    return f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>{esc(p['title'])} | AIBizs Enterprise Application</title>
  <meta name="description" content="{esc(p['description'])}">
  <meta name="author" content="AIBizs">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://aibizs.com/{esc(filename)}">

  <link href="assets/img/favicon.png" rel="icon">
  <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
  <link href="https://fonts.googleapis.com" rel="preconnect">
  <link href="https://fonts.gstatic.com" rel="preconnect" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&family=Raleway:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&family=Nunito+Sans:ital,wght@0,200;0,300;0,400;0,600;0,700;0,800;0,900;1,200;1,300;1,400;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet">
  <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="assets/vendor/aos/aos.css" rel="stylesheet">
  <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">
  <link href="assets/css/main.css" rel="stylesheet">
</head>

<body class="service-details-page">

  <header id="header" class="header d-flex align-items-center fixed-top">
    <div class="header-container container-fluid container-xl position-relative d-flex align-items-center justify-content-between">
      <a href="index.html" class="logo d-flex align-items-center me-auto me-xl-0">
        <h1 class="sitename">AIBizs</h1>
      </a>
      <nav id="navmenu" class="navmenu">
        <ul>
          <li><a href="index.html#hero">Home</a></li>
          <li><a href="index.html#about">About</a></li>
          <li><a href="index.html#services">Our Solutions</a></li>
          <li><a href="index.html#products">Our Products</a></li>
          <li><a href="index.html#contact">Contact</a></li>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>
      <a class="btn-getstarted" href="index.html#contact">Get Started</a>
    </div>
  </header>

  <main class="main">

    <div class="page-title dark-background" data-aos="fade">
      <div class="container position-relative">
        <h1>{esc(p['title'])}</h1>
        <p>{esc(p['subtitle'])}</p>
        <nav class="breadcrumbs">
          <ol>
            <li><a href="index.html">Home</a></li>
            <li><a href="index.html#products">Our Products</a></li>
            <li class="current">{esc(p['title'])}</li>
          </ol>
        </nav>
      </div>
    </div>

    <section id="product-details" class="service-details section">
      <div class="container" data-aos="fade-up" data-aos-delay="100">
        <div class="row gy-5">
          <div class="col-lg-8 order-lg-1 order-2">
            <div class="service-main-content">
              <div class="service-header" data-aos="fade-up">
                <h1>{esc(p['title'])}</h1>
                <div class="service-meta">
                  <span><i class="bi {esc(p['icon'])}"></i> {esc(p['meta'])}</span>
                  <span><i class="bi bi-geo-alt"></i> Oman &amp; GCC</span>
                  <span><i class="bi bi-patch-check"></i> AIBizs Product</span>
                </div>
                <p class="lead">{esc(p['lead'])}</p>
              </div>

              <div class="service-tabs" data-aos="fade-up" data-aos-delay="200">
                <ul class="nav nav-tabs" role="tablist">
                  <li class="nav-item" role="presentation">
                    <button class="nav-link active" data-bs-toggle="tab" data-bs-target="#product-tab-overview" type="button" role="tab" aria-selected="true">
                      <i class="bi bi-info-circle"></i> Overview
                    </button>
                  </li>
                  <li class="nav-item" role="presentation">
                    <button class="nav-link" data-bs-toggle="tab" data-bs-target="#product-tab-modules" type="button" role="tab" aria-selected="false">
                      <i class="bi bi-grid-3x3-gap"></i> Modules &amp; Features
                    </button>
                  </li>
                  <li class="nav-item" role="presentation">
                    <button class="nav-link" data-bs-toggle="tab" data-bs-target="#product-tab-platform" type="button" role="tab" aria-selected="false">
                      <i class="bi bi-stars"></i> Platform Capabilities
                    </button>
                  </li>
                </ul>

                <div class="tab-content">
                  <div class="tab-pane fade show active" id="product-tab-overview" role="tabpanel">
                    <div class="row">
                      <div class="col-md-6">
                        <div class="content-block">
                          <h3>{esc(p['overview_title'])}</h3>
                          <p>{esc(p['overview_p1'])}</p>
                          <p>{esc(p['overview_p2'])}</p>
                        </div>
                      </div>
                      <div class="col-md-6">
                        <img src="{esc(p['image'])}" alt="{esc(p['image_alt'])}" class="img-fluid rounded" loading="lazy">
                      </div>
                    </div>
                  </div>

                  <div class="tab-pane fade" id="product-tab-modules" role="tabpanel">
                    <div class="row g-4">
{module_cards(p['modules'])}
                    </div>
                  </div>

                  <div class="tab-pane fade" id="product-tab-platform" role="tabpanel">
                    <div class="row g-4">
{benefit_cards(p['platform'])}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="col-lg-4 order-lg-2 order-1">
            <div class="service-sidebar" data-aos="fade-left">
              <div class="action-card" data-aos="zoom-in" data-aos-delay="100">
                <h3>{esc(p['sidebar_title'])}</h3>
                <p>{esc(p['sidebar_text'])}</p>
                <a href="{esc(p['sidebar_cta_href'])}" class="btn-primary"{cta_attrs}>{esc(p['sidebar_cta'])}</a>
                <span class="guarantee"><i class="bi bi-shield-check"></i> {esc(p['sidebar_guarantee'])}</span>
              </div>

              <div class="service-features-list" data-aos="fade-up" data-aos-delay="200">
                <h4>Highlights</h4>
                <ul>
{sidebar_items(p['sidebar_items'])}
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

  </main>

  <footer id="footer" class="footer">
    <div class="container footer-top">
      <div class="row gy-4">
        <div class="col-lg-5 col-md-12 footer-about">
          <a href="index.html" class="logo d-flex align-items-center"><span class="sitename">AIBizs</span></a>
          <p>Artificial Intelligence Business Solutions LLC delivers innovative, future-ready solutions that empower businesses to thrive in a rapidly evolving digital world.</p>
        </div>
        <div class="col-lg-2 col-6 footer-links">
          <h4>Useful Links</h4>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="index.html#about">About us</a></li>
            <li><a href="index.html#services">Our Solutions</a></li>
            <li><a href="index.html#products">Our Products</a></li>
            <li><a href="index.html#contact">Contact</a></li>
          </ul>
        </div>
        <div class="col-lg-2 col-6 footer-links">
          <h4>Our Products</h4>
          <ul>
            <li><a href="product-erp.html">ERP</a></li>
            <li><a href="product-qhse.html">QHSE</a></li>
            <li><a href="product-hrms.html">HRMS</a></li>
            <li><a href="product-e-invoicing.html">e-Invoicing</a></li>
          </ul>
        </div>
        <div class="col-lg-3 col-md-12 footer-contact text-center text-md-start">
          <h4>Contact Us</h4>
          <p>Super Plaza, Building #340, Way #480, Azaiba</p>
          <p>Muscat, Oman</p>
          <p class="mt-4"><strong>Phone:</strong> <span>+968 24 506181</span></p>
          <p><strong>Email:</strong> <span>info@aibizs.com</span></p>
        </div>
      </div>
    </div>
    <div class="container copyright text-center mt-4">
      <p>© <span>Copyright</span> <strong class="px-1 sitename">AIBizs</strong> <span>All Rights Reserved</span></p>
    </div>
  </footer>

  <a href="#" id="scroll-top" class="scroll-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>
  <div id="preloader"></div>

  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/aos/aos.js"></script>
  <script src="assets/vendor/swiper/swiper-bundle.min.js"></script>
  <script src="assets/js/main.js"></script>
</body>
</html>
"""


def main():
    for product in PRODUCTS:
        path = ROOT / f"{product['slug']}.html"
        path.write_text(render_product(product), encoding="utf-8")
        print(f"Wrote {path.name}")
    (ROOT / "scripts" / "products-manifest.json").write_text(
        json.dumps([{"slug": p["slug"], "title": p["title"]} for p in PRODUCTS], indent=2),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
