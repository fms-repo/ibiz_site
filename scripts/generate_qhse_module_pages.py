#!/usr/bin/env python3
"""Generate QHSE module product pages — reuse HRMS product layout classes in AIBizs theme."""

from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MODULES = [
    {
        "slug": "qhse-risk-identification",
        "title": "Risk Identification & Loss Reporting",
        "eyebrow": "AIBizs QHSE",
        "hero_title": "Identify Risks Before They Become Losses",
        "hero_text": "Capture hazards, assess risk matrices, and report losses from one HSE workspace — built for oil & gas, industrial, and construction sites across Oman and the GCC that need audit-ready risk registers.",
        "description": "AIBizs QHSE Risk Identification & Loss Reporting helps industrial and corporate teams in Oman and the GCC log hazards, score risk, and track loss events with full traceability.",
        "icon": "bi-exclamation-triangle",
        "image": "assets/img/qhseimage/risk-hero.png",
        "image_alt": "AIBizs QHSE risk identification dashboard",
        "trust_line": "Clearer hazard registers. Faster risk scoring. Traceable loss reporting.",
        "solutions": [
            {
                "title": "Hazard & Risk Register",
                "text": "Log workplace hazards by site, activity, and asset class — then score likelihood and severity so HSE teams prioritize the risks that matter most.",
                "bullets": [
                    "Site and activity-based hazard capture",
                    "Likelihood and severity risk matrix",
                    "Ownership and residual risk tracking",
                    "Multi-site risk register views",
                ],
                "image": "assets/img/qhseimage/risk-hero.png",
                "image_alt": "Hazard and risk register dashboard",
            },
            {
                "title": "Risk Matrix & Controls",
                "text": "Apply consistent risk matrices across operations and link controls, PTW requirements, and mitigating actions so residual risk stays visible to supervisors.",
                "bullets": [
                    "Configurable risk matrices by company",
                    "Control and barrier linking",
                    "PTW and permit-related risk flags",
                    "Action plans with due dates",
                ],
                "image": "assets/img/qhseimage/risk-matrix.png",
                "image_alt": "Risk matrix scoring and controls",
                "reverse": True,
            },
            {
                "title": "Loss & Near-Miss Reporting",
                "text": "Report losses, damage, and near misses with structured categories — feeding investigation workflows and leadership dashboards without spreadsheet gaps.",
                "bullets": [
                    "Loss and near-miss classification",
                    "Photo and evidence attachments",
                    "Cost and impact capture",
                    "HSE KPI dashboards for leadership",
                ],
                "image": "assets/img/qhseimage/risk-loss.png",
                "image_alt": "Loss and near-miss reporting",
            },
        ],
        "process": [
            ("Identify", "Capture hazards and potential loss scenarios at site level."),
            ("Assess", "Score risk using standard matrices and assign owners."),
            ("Control", "Link barriers, PTW rules, and corrective actions."),
            ("Report", "Track losses, residual risk, and leadership KPIs."),
        ],
        "capabilities": [
            ("bi-exclamation-triangle", "Hazard capture"),
            ("bi-grid-3x3", "Risk matrix scoring"),
            ("bi-shield-check", "Control linking"),
            ("bi-clipboard-data", "Loss reporting"),
            ("bi-eye", "Near-miss tracking"),
            ("bi-geo-alt", "Multi-site registers"),
            ("bi-paperclip", "Evidence attachments"),
            ("bi-graph-up", "HSE risk KPIs"),
        ],
        "faqs": [
            ("Who is Risk Identification for?", "HSE teams in oil & gas, industrial, and construction organizations across Oman and the GCC that need consistent hazard registers and loss reporting."),
            ("Can we use our own risk matrix?", "Yes. Configure likelihood and severity scales by company so scoring matches your HSE standards."),
            ("Does it support near-miss reporting?", "Yes. Near misses and losses are captured with categories, evidence, and follow-up actions."),
            ("Is it suitable for multi-site operations?", "Yes. Maintain site-level registers with company-wide visibility for corporate HSE."),
        ],
    },
    {
        "slug": "qhse-incident-management",
        "title": "Incident Management",
        "eyebrow": "AIBizs QHSE",
        "hero_title": "Close Incidents with Full Traceability",
        "hero_text": "Report workplace incidents and near misses, run investigations, and drive corrective actions to closure — designed for industrial HSE teams in Oman and the GCC who need audit-ready incident records.",
        "description": "AIBizs QHSE Incident Management handles incident reporting, investigation, and corrective actions for industrial and corporate organizations in Oman and the GCC.",
        "icon": "bi-clipboard-x",
        "image": "assets/img/qhseimage/incident-hero.png",
        "image_alt": "AIBizs QHSE incident management dashboard",
        "trust_line": "Faster reporting. Clearer investigations. Actions that actually close.",
        "solutions": [
            {
                "title": "Incident & Near-Miss Capture",
                "text": "Enable field teams to report incidents and near misses quickly with structured forms, severity levels, and site context — so nothing waits for end-of-shift paperwork.",
                "bullets": [
                    "Mobile-friendly incident reporting",
                    "Severity and classification controls",
                    "Witness and evidence capture",
                    "Immediate notification to HSE owners",
                ],
                "image": "assets/img/qhseimage/incident-hero.png",
                "image_alt": "Incident and near-miss capture",
            },
            {
                "title": "Investigation Workflows",
                "text": "Assign investigators, document root causes, and record findings against company HSE procedures — keeping every step ready for internal and external audit.",
                "bullets": [
                    "Investigation assignment and SLA tracking",
                    "Root cause and contributing factors",
                    "Timeline and evidence packages",
                    "Regulatory and client reporting support",
                ],
                "image": "assets/img/qhseimage/incident-report.png",
                "image_alt": "Incident investigation and reporting",
                "reverse": True,
            },
            {
                "title": "Corrective & Preventive Actions",
                "text": "Convert findings into owned CAPA items with due dates and verification — so leadership can see open actions and overdue closures in real time.",
                "bullets": [
                    "CAPA creation from investigation findings",
                    "Owner, due date, and priority tracking",
                    "Verification and effectiveness checks",
                    "Open-action dashboards for HSE managers",
                ],
                "image": "assets/img/qhseimage/incident-actions.png",
                "image_alt": "Corrective action tracking",
            },
        ],
        "process": [
            ("Report", "Log the incident or near miss with evidence and severity."),
            ("Investigate", "Assign investigators and document root causes."),
            ("Act", "Create CAPA items with owners and due dates."),
            ("Close", "Verify effectiveness and archive audit-ready records."),
        ],
        "capabilities": [
            ("bi-clipboard-x", "Incident reporting"),
            ("bi-eye", "Near-miss tracking"),
            ("bi-search", "Investigation workflows"),
            ("bi-diagram-3", "Root cause analysis"),
            ("bi-check2-square", "CAPA management"),
            ("bi-bell", "HSE notifications"),
            ("bi-paperclip", "Evidence packages"),
            ("bi-shield-check", "Audit-ready closure"),
        ],
        "faqs": [
            ("Can field workers report incidents on site?", "Yes. Structured reporting is designed for rapid capture with photos and severity so HSE teams are notified quickly."),
            ("Does it cover near misses?", "Yes. Near misses follow the same workflow path with classification suited to proactive HSE programs."),
            ("How are corrective actions tracked?", "Findings generate CAPA items with owners, due dates, and verification before formal closure."),
            ("Is the record audit-ready?", "Yes. Investigation timelines, evidence, and closures remain fully traceable for client and regulatory reviews."),
        ],
    },
    {
        "slug": "qhse-inspection",
        "title": "Inspection",
        "eyebrow": "AIBizs QHSE",
        "hero_title": "Inspect Sites with Checklists That Stick",
        "hero_text": "Schedule safety and quality inspections, execute checklist-driven audits in the field, and close findings with owners — built for multi-site HSE programs across Oman and the GCC.",
        "description": "AIBizs QHSE Inspection helps organizations schedule, conduct, and document safety and quality inspections with findings and corrective actions.",
        "icon": "bi-search",
        "image": "assets/img/qhseimage/inspection-hero.png",
        "image_alt": "AIBizs QHSE inspection management dashboard",
        "trust_line": "Scheduled inspections. Checklist discipline. Findings that get closed.",
        "solutions": [
            {
                "title": "Inspection Planning",
                "text": "Plan routine and ad-hoc inspections by site, asset, and HSE topic — so supervisors know what must be audited this week and who owns it.",
                "bullets": [
                    "Scheduled and ad-hoc inspection plans",
                    "Site, asset, and checklist assignment",
                    "Inspector and contractor coverage",
                    "Calendar and overdue visibility",
                ],
                "image": "assets/img/qhseimage/inspection-hero.png",
                "image_alt": "Inspection planning calendar",
            },
            {
                "title": "Checklist Execution",
                "text": "Run standardized checklists in the field with pass/fail scoring, photos, and notes — reducing paperwork and inconsistent audit quality.",
                "bullets": [
                    "Configurable HSE and quality checklists",
                    "Pass, fail, and N/A scoring",
                    "Photo evidence per checklist item",
                    "Offline-friendly field capture patterns",
                ],
                "image": "assets/img/qhseimage/inspection-checklist.png",
                "image_alt": "Field inspection checklist execution",
                "reverse": True,
            },
            {
                "title": "Findings & Follow-Up",
                "text": "Turn failed items into owned findings with priorities and verification — so inspection programs drive real improvement, not just reports.",
                "bullets": [
                    "Automatic finding creation from fails",
                    "Priority and owner assignment",
                    "Corrective action linkage",
                    "Inspection compliance dashboards",
                ],
                "image": "assets/img/qhseimage/inspection-findings.png",
                "image_alt": "Inspection findings and follow-up",
            },
        ],
        "process": [
            ("Plan", "Schedule inspections and assign checklists by site."),
            ("Execute", "Complete checklist items with scores and evidence."),
            ("Find", "Raise findings from failed or observation items."),
            ("Verify", "Close actions and confirm inspection compliance."),
        ],
        "capabilities": [
            ("bi-calendar-check", "Inspection scheduling"),
            ("bi-list-check", "Digital checklists"),
            ("bi-camera", "Photo evidence"),
            ("bi-flag", "Finding management"),
            ("bi-person-check", "Inspector assignment"),
            ("bi-building", "Multi-site coverage"),
            ("bi-graph-up", "Compliance dashboards"),
            ("bi-shield-check", "Audit trail"),
        ],
        "faqs": [
            ("Can we use company-specific checklists?", "Yes. Configure checklists by inspection type, site, or asset class to match your HSE procedures."),
            ("How are findings managed?", "Failed items can generate findings with owners, priorities, and linked corrective actions."),
            ("Does it support contractor inspections?", "Yes. Assign inspections to internal or contractor inspectors with the same checklist discipline."),
            ("Can leadership see compliance rates?", "Yes. Dashboards show completed inspections, open findings, and overdue follow-ups."),
        ],
    },
    {
        "slug": "qhse-journey-plan",
        "title": "Journey Plan with IVMS Integration",
        "eyebrow": "AIBizs QHSE",
        "hero_title": "Plan Journeys. Monitor Vehicles. Reduce Road Risk.",
        "hero_text": "Create journey management plans, approve high-risk trips, and monitor vehicles through IVMS integration — essential for remote and industrial operations across Oman and the GCC.",
        "description": "AIBizs QHSE Journey Plan with IVMS Integration manages journey approvals and vehicle monitoring for safer road travel in Oman and the GCC.",
        "icon": "bi-geo-alt",
        "image": "assets/img/qhseimage/journey-hero.png",
        "image_alt": "AIBizs QHSE journey plan and IVMS dashboard",
        "trust_line": "Approved journeys. Live IVMS visibility. Safer road operations.",
        "solutions": [
            {
                "title": "Journey Management Plans",
                "text": "Raise journey plans with route, driver, vehicle, and risk controls — so night drives, remote sites, and high-risk corridors get the right approvals before departure.",
                "bullets": [
                    "Driver, vehicle, and route capture",
                    "Risk-based journey categories",
                    "Manager and HSE approval workflows",
                    "Night and remote-travel controls",
                ],
                "image": "assets/img/qhseimage/journey-hero.png",
                "image_alt": "Journey management planning",
            },
            {
                "title": "Plan Compliance & Controls",
                "text": "Enforce rest rules, companion requirements, and check-call schedules so journey plans stay aligned with company road-safety standards.",
                "bullets": [
                    "Check-call and ETA tracking",
                    "Rest and fatigue rule prompts",
                    "Companion and convoy requirements",
                    "Deviation and overdue alerts",
                ],
                "image": "assets/img/qhseimage/journey-plan.png",
                "image_alt": "Journey plan compliance controls",
                "reverse": True,
            },
            {
                "title": "IVMS Integration",
                "text": "Connect approved journeys to IVMS tracking so speeding, harsh events, and live location feed HSE visibility without separate trip paperwork.",
                "bullets": [
                    "IVMS vehicle location linkage",
                    "Speeding and harsh-event alerts",
                    "Journey vs actual route comparison",
                    "Driver behavior visibility for HSE",
                ],
                "image": "assets/img/qhseimage/journey-ivms.png",
                "image_alt": "IVMS integrated journey monitoring",
            },
        ],
        "process": [
            ("Request", "Create a journey plan with route, driver, and risk level."),
            ("Approve", "Route high-risk trips through manager and HSE approvals."),
            ("Monitor", "Track check-calls and IVMS events during the journey."),
            ("Close", "Confirm arrival and capture exceptions for review."),
        ],
        "capabilities": [
            ("bi-geo-alt", "Journey planning"),
            ("bi-truck", "Vehicle assignment"),
            ("bi-person-badge", "Driver controls"),
            ("bi-check2-circle", "Approval workflows"),
            ("bi-broadcast", "IVMS integration"),
            ("bi-speedometer2", "Speeding alerts"),
            ("bi-telephone", "Check-call tracking"),
            ("bi-shield-exclamation", "Road-risk controls"),
        ],
        "faqs": [
            ("What is journey management used for?", "It controls road risk for remote, night, and high-hazard travel common in oil & gas and industrial operations across Oman and the GCC."),
            ("How does IVMS integration help?", "Approved journeys link to vehicle tracking so HSE teams see location, speeding, and harsh events against the plan."),
            ("Can high-risk trips require dual approval?", "Yes. Configure approval rules by risk category, distance, or night travel."),
            ("Does it replace IVMS?", "No. It complements IVMS by connecting formal journey plans with live vehicle monitoring."),
        ],
    },
    {
        "slug": "qhse-management-of-change",
        "title": "Management of Change",
        "eyebrow": "AIBizs QHSE",
        "hero_title": "Control Change Without Losing Safety",
        "hero_text": "Govern process, equipment, and organizational changes with structured MOC workflows, risk assessment, and approvals — so temporary and permanent changes stay controlled on Oman and GCC industrial sites.",
        "description": "AIBizs QHSE Management of Change controls organizational and operational changes with risk assessment and approval workflows for industrial HSE programs.",
        "icon": "bi-arrow-repeat",
        "image": "assets/img/qhseimage/moc-hero.png",
        "image_alt": "AIBizs QHSE management of change dashboard",
        "trust_line": "Structured MOC. Assessed risk. Approved change before go-live.",
        "solutions": [
            {
                "title": "MOC Request & Classification",
                "text": "Raise temporary or permanent change requests with clear scope, affected systems, and urgency — so HSE and operations know what is changing before work starts.",
                "bullets": [
                    "Temporary and permanent MOC types",
                    "Scope and affected-area capture",
                    "Priority and initiator tracking",
                    "Document and drawing attachments",
                ],
                "image": "assets/img/qhseimage/moc-hero.png",
                "image_alt": "MOC request and classification",
            },
            {
                "title": "Workflow & Approvals",
                "text": "Route MOCs through technical, operations, and HSE reviewers with stage gates — preventing informal changes that bypass permit and risk controls.",
                "bullets": [
                    "Multi-stage approval workflows",
                    "Technical and HSE review gates",
                    "PTW and isolation linkage",
                    "Rejection and revision history",
                ],
                "image": "assets/img/qhseimage/moc-workflow.png",
                "image_alt": "MOC approval workflow",
                "reverse": True,
            },
            {
                "title": "Change Risk Assessment",
                "text": "Assess hazards introduced by the change, define mitigating controls, and verify close-out so residual risk is understood before implementation.",
                "bullets": [
                    "Change-specific risk assessment",
                    "Mitigation and control definition",
                    "Implementation and verification steps",
                    "MOC close-out with audit trail",
                ],
                "image": "assets/img/qhseimage/moc-risk.png",
                "image_alt": "MOC risk assessment and close-out",
            },
        ],
        "process": [
            ("Request", "Submit the change with scope, impact, and attachments."),
            ("Assess", "Complete risk assessment and required reviews."),
            ("Approve", "Pass technical, operations, and HSE stage gates."),
            ("Implement", "Execute, verify controls, and close the MOC."),
        ],
        "capabilities": [
            ("bi-arrow-repeat", "MOC requests"),
            ("bi-diagram-3", "Approval workflows"),
            ("bi-exclamation-triangle", "Change risk assessment"),
            ("bi-file-earmark-text", "Document attachments"),
            ("bi-clock-history", "Temporary change control"),
            ("bi-link-45deg", "PTW linkage"),
            ("bi-check2-square", "Verification close-out"),
            ("bi-shield-check", "Full audit trail"),
        ],
        "faqs": [
            ("What types of change does MOC cover?", "Process, equipment, procedural, and organizational changes — temporary or permanent — that can affect HSE risk."),
            ("Can MOC link to PTW?", "Yes. Link change requests to permit requirements and isolation controls where needed."),
            ("Who approves MOCs?", "Configure multi-stage reviewers spanning technical, operations, and HSE roles."),
            ("Is close-out tracked?", "Yes. Implementation and verification steps must complete before the MOC is closed."),
        ],
    },
    {
        "slug": "qhse-quality-management",
        "title": "Quality Management",
        "eyebrow": "AIBizs QHSE",
        "hero_title": "Hold Quality Standards Across Every Site",
        "hero_text": "Manage quality control, non-conformances, and corrective actions in one QHSE platform — so industrial and corporate teams in Oman and the GCC keep product and process quality visible and auditable.",
        "description": "AIBizs QHSE Quality Management supports quality control, NCR handling, and assurance processes for organizations in Oman and the GCC.",
        "icon": "bi-award",
        "image": "assets/img/qhseimage/quality-hero.png",
        "image_alt": "AIBizs QHSE quality management dashboard",
        "trust_line": "Stronger QC. Clear NCRs. Assurance that stands up to audit.",
        "solutions": [
            {
                "title": "Quality Control Processes",
                "text": "Define QC checkpoints, inspection criteria, and acceptance standards so teams catch deviations early in production, construction, or service delivery.",
                "bullets": [
                    "QC checkpoint definition",
                    "Acceptance criteria and sampling",
                    "In-process and final inspections",
                    "Quality record retention",
                ],
                "image": "assets/img/qhseimage/quality-hero.png",
                "image_alt": "Quality control process dashboard",
            },
            {
                "title": "Quality Assurance Oversight",
                "text": "Give quality and HSE leadership visibility into open issues, audit findings, and assurance status across sites and contractors.",
                "bullets": [
                    "QA audit and review tracking",
                    "Site and contractor quality views",
                    "Trend analysis on recurring issues",
                    "Leadership quality KPIs",
                ],
                "image": "assets/img/qhseimage/quality-control.png",
                "image_alt": "Quality assurance oversight",
                "reverse": True,
            },
            {
                "title": "NCR & Corrective Action",
                "text": "Raise non-conformance reports, assign disposition, and drive CAPA to verified closure — keeping quality evidence ready for clients and ISO audits.",
                "bullets": [
                    "NCR creation and classification",
                    "Disposition and containment actions",
                    "CAPA ownership and verification",
                    "Client and audit-ready NCR history",
                ],
                "image": "assets/img/qhseimage/quality-ncr.png",
                "image_alt": "NCR and corrective action tracking",
            },
        ],
        "process": [
            ("Define", "Set QC criteria and assurance checkpoints."),
            ("Inspect", "Execute quality checks and record results."),
            ("Raise", "Create NCRs for non-conformances."),
            ("Close", "Complete CAPA and verify effectiveness."),
        ],
        "capabilities": [
            ("bi-award", "Quality control"),
            ("bi-clipboard-check", "QA oversight"),
            ("bi-x-octagon", "NCR management"),
            ("bi-check2-square", "CAPA workflows"),
            ("bi-bar-chart", "Quality KPIs"),
            ("bi-people", "Contractor quality views"),
            ("bi-folder2-open", "Quality records"),
            ("bi-shield-check", "Audit readiness"),
        ],
        "faqs": [
            ("Does Quality Management handle NCRs?", "Yes. Raise, classify, and close non-conformances with disposition and CAPA tracking."),
            ("Can it support ISO-style audits?", "Yes. Quality records, NCRs, and corrective actions remain traceable for internal and external audits."),
            ("Is it useful for construction and industrial sites?", "Yes. QC checkpoints and NCR workflows fit fabrication, construction, and process operations common in Oman and the GCC."),
            ("How does it connect to inspections?", "Inspection findings can feed quality issues and NCR workflows for a single action trail."),
        ],
    },
    {
        "slug": "qhse-vendor-evaluation",
        "title": "Vendor Evaluation",
        "eyebrow": "AIBizs QHSE",
        "hero_title": "Score Vendor HSE Before They Enter Site",
        "hero_text": "Evaluate contractor and vendor HSE performance, compliance documents, and site behavior — so procurement and HSE in Oman and the GCC award work to partners who meet your standards.",
        "description": "AIBizs QHSE Vendor Evaluation assesses contractor and vendor HSE performance and compliance for industrial organizations in Oman and the GCC.",
        "icon": "bi-star",
        "image": "assets/img/qhseimage/vendor-hero.png",
        "image_alt": "AIBizs QHSE vendor evaluation dashboard",
        "trust_line": "Scored vendors. Documented compliance. Safer contractor control.",
        "solutions": [
            {
                "title": "Vendor HSE Pre-Qualification",
                "text": "Collect HSE questionnaires, certificates, and method statements before mobilization — reducing onboarding risk for high-hazard contractor work.",
                "bullets": [
                    "HSE pre-qualification questionnaires",
                    "Certificate and insurance tracking",
                    "Method statement review status",
                    "Approved vendor lists by risk category",
                ],
                "image": "assets/img/qhseimage/vendor-hero.png",
                "image_alt": "Vendor HSE pre-qualification",
            },
            {
                "title": "Performance Scoring",
                "text": "Score vendors on incident rates, inspection findings, and site compliance so commercial decisions reflect real HSE performance, not just price.",
                "bullets": [
                    "Weighted HSE performance scores",
                    "Incident and finding linkage",
                    "Periodic re-evaluation cycles",
                    "Scorecards for procurement reviews",
                ],
                "image": "assets/img/qhseimage/vendor-score.png",
                "image_alt": "Vendor HSE performance scoring",
                "reverse": True,
            },
            {
                "title": "Compliance Monitoring",
                "text": "Track expiring documents, open actions, and site bans so non-compliant vendors are blocked before they create exposure.",
                "bullets": [
                    "Document expiry alerts",
                    "Open HSE action tracking by vendor",
                    "Site access and restriction flags",
                    "Compliance history for audits",
                ],
                "image": "assets/img/qhseimage/vendor-compliance.png",
                "image_alt": "Vendor compliance monitoring",
            },
        ],
        "process": [
            ("Qualify", "Collect HSE documents and pre-qualification data."),
            ("Score", "Evaluate performance against weighted criteria."),
            ("Monitor", "Track compliance, findings, and document expiry."),
            ("Decide", "Approve, restrict, or re-evaluate vendor status."),
        ],
        "capabilities": [
            ("bi-star", "HSE scoring"),
            ("bi-file-earmark-check", "Document compliance"),
            ("bi-clipboard-data", "Pre-qualification"),
            ("bi-graph-up", "Performance scorecards"),
            ("bi-bell", "Expiry alerts"),
            ("bi-slash-circle", "Access restrictions"),
            ("bi-people", "Contractor oversight"),
            ("bi-shield-check", "Audit history"),
        ],
        "faqs": [
            ("Who uses Vendor Evaluation?", "HSE and procurement teams that need contractor pre-qualification and ongoing HSE scoring for industrial sites."),
            ("Can scores influence approved vendor lists?", "Yes. Performance and compliance status can drive approval, restriction, or re-evaluation decisions."),
            ("Does it track certificate expiry?", "Yes. Document expiry alerts help prevent non-compliant mobilization."),
            ("Can incident history affect scores?", "Yes. Link incidents and inspection findings into vendor performance scorecards."),
        ],
    },
    {
        "slug": "qhse-meeting",
        "title": "Meeting",
        "eyebrow": "AIBizs QHSE",
        "hero_title": "Run Safety Meetings That Drive Action",
        "hero_text": "Schedule toolbox talks, HSE committee meetings, and safety briefings with agendas, attendance, and action items — keeping frontline communication disciplined across Oman and GCC operations.",
        "description": "AIBizs QHSE Meeting manages safety meetings, agendas, attendance, and action items for industrial and corporate HSE programs.",
        "icon": "bi-calendar-event",
        "image": "assets/img/qhseimage/meeting-hero.png",
        "image_alt": "AIBizs QHSE safety meeting dashboard",
        "trust_line": "Planned meetings. Clear agendas. Actions that do not get lost.",
        "solutions": [
            {
                "title": "Safety Meeting Scheduling",
                "text": "Plan toolbox talks, pre-job briefs, and HSE committee sessions by site and crew — so communication cadence stays consistent even across multi-site operations.",
                "bullets": [
                    "Toolbox talk and committee scheduling",
                    "Site and crew assignment",
                    "Recurring meeting templates",
                    "Attendance planning and invites",
                ],
                "image": "assets/img/qhseimage/meeting-hero.png",
                "image_alt": "Safety meeting scheduling",
            },
            {
                "title": "Agendas & Records",
                "text": "Capture agendas, discussion notes, and attendance so every safety conversation leaves an auditable record for clients and regulators.",
                "bullets": [
                    "Structured agenda templates",
                    "Attendance and sign-off capture",
                    "Discussion and decision notes",
                    "Meeting minutes archive",
                ],
                "image": "assets/img/qhseimage/meeting-agenda.png",
                "image_alt": "Meeting agenda and attendance records",
                "reverse": True,
            },
            {
                "title": "Action Item Follow-Up",
                "text": "Convert meeting decisions into owned actions with due dates — closing the gap between toolbox talk commitments and verified follow-through.",
                "bullets": [
                    "Action items from meeting decisions",
                    "Owner and due-date tracking",
                    "Overdue action reminders",
                    "HSE communication KPIs",
                ],
                "image": "assets/img/qhseimage/meeting-actions.png",
                "image_alt": "Meeting action item follow-up",
            },
        ],
        "process": [
            ("Schedule", "Plan toolbox talks and HSE meetings by site."),
            ("Agenda", "Set topics, owners, and required attendees."),
            ("Record", "Capture attendance, notes, and decisions."),
            ("Follow up", "Track action items to verified closure."),
        ],
        "capabilities": [
            ("bi-calendar-event", "Meeting scheduling"),
            ("bi-list-ul", "Agenda templates"),
            ("bi-people", "Attendance tracking"),
            ("bi-chat-left-text", "Minutes & notes"),
            ("bi-check2-square", "Action items"),
            ("bi-bell", "Overdue reminders"),
            ("bi-geo-alt", "Multi-site meetings"),
            ("bi-folder2-open", "Meeting archive"),
        ],
        "faqs": [
            ("Does it support toolbox talks?", "Yes. Schedule and record toolbox talks with attendance and follow-up actions."),
            ("Can we keep meeting minutes for audits?", "Yes. Agendas, attendance, notes, and actions remain archived for client and regulatory review."),
            ("How are actions tracked?", "Meeting decisions create owned action items with due dates and reminders."),
            ("Is it useful for multi-crew sites?", "Yes. Assign meetings by site and crew so frontline HSE communication stays consistent."),
        ],
    },
    {
        "slug": "qhse-fit-to-work",
        "title": "Fit to Work",
        "eyebrow": "AIBizs QHSE",
        "hero_title": "Confirm Fitness Before High-Risk Work",
        "hero_text": "Manage medical clearances, fitness assessments, and work restrictions — so only fit personnel enter high-risk roles and sites across oil & gas, industrial, and construction operations in Oman and the GCC.",
        "description": "AIBizs QHSE Fit to Work assesses employee fitness for work and manages medical clearances for industrial organizations in Oman and the GCC.",
        "icon": "bi-check-circle",
        "image": "assets/img/qhseimage/fit-hero.png",
        "image_alt": "AIBizs QHSE fit to work dashboard",
        "trust_line": "Medical clarity. Role-based fitness. Safer mobilization.",
        "solutions": [
            {
                "title": "Fitness Assessment Workflows",
                "text": "Assess fitness against role and site requirements before mobilization — reducing the chance that unfit personnel enter high-risk tasks or confined spaces.",
                "bullets": [
                    "Role and site fitness criteria",
                    "Pre-mobilization assessment workflows",
                    "Temporary and permanent restrictions",
                    "Supervisor fitness visibility",
                ],
                "image": "assets/img/qhseimage/fit-hero.png",
                "image_alt": "Fitness assessment workflows",
            },
            {
                "title": "Medical Clearance Records",
                "text": "Track medical certificates, expiry dates, and clinic results so HSE and HR share one view of clearance status without paper chasing.",
                "bullets": [
                    "Medical certificate tracking",
                    "Expiry and renewal alerts",
                    "Clinic and occupational health records",
                    "Confidential access controls",
                ],
                "image": "assets/img/qhseimage/fit-medical.png",
                "image_alt": "Medical clearance records",
                "reverse": True,
            },
            {
                "title": "Clearance & Site Access Control",
                "text": "Link fit-to-work status to site access and high-risk task eligibility so PTW and gate processes respect current medical clearance.",
                "bullets": [
                    "Fit / unfit / restricted status flags",
                    "High-risk task eligibility checks",
                    "Site access clearance linkage",
                    "Audit history for medical fitness decisions",
                ],
                "image": "assets/img/qhseimage/fit-clearance.png",
                "image_alt": "Fit-to-work clearance and site access",
            },
        ],
        "process": [
            ("Assess", "Evaluate fitness against role and site requirements."),
            ("Record", "Capture medical results and clearance status."),
            ("Control", "Apply restrictions and site access eligibility."),
            ("Renew", "Alert on expiry and re-clear personnel."),
        ],
        "capabilities": [
            ("bi-check-circle", "Fitness assessments"),
            ("bi-heart-pulse", "Medical clearances"),
            ("bi-calendar-x", "Expiry alerts"),
            ("bi-slash-circle", "Work restrictions"),
            ("bi-door-open", "Site access linkage"),
            ("bi-person-badge", "Role-based criteria"),
            ("bi-lock", "Confidential access"),
            ("bi-shield-check", "Audit history"),
        ],
        "faqs": [
            ("Who needs Fit to Work?", "Organizations with high-risk roles — oil & gas, industrial, and construction — that must confirm medical fitness before mobilization."),
            ("Can restrictions be temporary?", "Yes. Apply temporary or permanent restrictions with clear status for supervisors."),
            ("Does it track medical certificate expiry?", "Yes. Expiry alerts help renew clearances before site access is blocked."),
            ("Can it link to site access or PTW?", "Yes. Fit-to-work status can inform site access and high-risk task eligibility."),
        ],
    },
    {
        "slug": "qhse-document-management",
        "title": "Document Management",
        "eyebrow": "AIBizs QHSE",
        "hero_title": "Controlled Documents for Audit-Ready HSE",
        "hero_text": "Centralize policies, procedures, permits, forms, and safety manuals with version control, approvals, and role-based access — so every site works from the latest controlled documents.",
        "description": "AIBizs QHSE Document Management controls HSE documents, policies, procedures, and versioned controlled records for industrial organizations in Oman and the GCC.",
        "icon": "bi-folder2-open",
        "image": "assets/img/qhseimage/document-hero.png",
        "image_alt": "AIBizs QHSE document management dashboard",
        "trust_line": "One library. Controlled versions. Always audit-ready.",
        "solutions": [
            {
                "title": "Controlled Document Library",
                "text": "Organize HSE policies, SOPs, permits, forms, and manuals in a structured library so teams find the right document fast — and always the approved revision.",
                "bullets": [
                    "Policies, procedures, permits, and forms",
                    "Folders and categories by site or department",
                    "Fast search across the document library",
                    "Multi-company and multi-site libraries",
                ],
                "image": "assets/img/qhseimage/document-hero.png",
                "image_alt": "Controlled HSE document library",
            },
            {
                "title": "Version Control & Approvals",
                "text": "Publish only approved revisions. Track draft → review → approve → release with clear ownership so obsolete documents are never used in the field.",
                "bullets": [
                    "Version history with change notes",
                    "Review and approval workflows",
                    "Obsolete document control",
                    "Read-and-acknowledge for critical procedures",
                ],
                "image": "assets/img/qhseimage/document-versions.png",
                "image_alt": "Document version control and approvals",
                "reverse": True,
            },
            {
                "title": "Access, Distribution & Audit Trail",
                "text": "Control who can view, edit, or approve documents, distribute updates to sites, and keep a full audit trail for clients, ISO, and regulatory reviews.",
                "bullets": [
                    "Role-based document permissions",
                    "Site and contractor distribution",
                    "Download and access history",
                    "Audit-ready controlled records",
                ],
                "image": "assets/img/qhseimage/document-access.png",
                "image_alt": "Document access control and audit trail",
            },
        ],
        "process": [
            ("Upload & Classify", "Add documents into the controlled library with category and owners."),
            ("Review & Approve", "Route drafts through review and approval workflows."),
            ("Publish & Notify", "Release the approved version and notify affected sites."),
            ("Control & Audit", "Retire obsolete versions and retain full access history."),
        ],
        "capabilities": [
            ("bi-folder2-open", "Document library"),
            ("bi-files", "Version control"),
            ("bi-check2-square", "Approval workflows"),
            ("bi-eye-slash", "Obsolete control"),
            ("bi-shield-lock", "Role-based access"),
            ("bi-bell", "Update notifications"),
            ("bi-search", "Full-text search"),
            ("bi-journal-check", "Audit trail"),
        ],
        "faqs": [
            ("What documents can we manage?", "HSE policies, SOPs, permits, forms, manuals, and other controlled safety or quality documents."),
            ("Does it support version control?", "Yes. Every revision is tracked with history, and only approved versions are published for use."),
            ("Can we require read acknowledgment?", "Yes. Critical procedures can require employees to read and acknowledge the latest version."),
            ("Is it audit-ready for ISO and clients?", "Yes. Access history, approvals, and obsolete control support ISO and client audits."),
        ],
    },
]

RELATED = [(m["slug"], m["title"], m["icon"]) for m in MODULES]


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def solution_blocks(solutions):
    blocks = []
    for i, s in enumerate(solutions):
        reverse = s.get("reverse", False) or i % 2 == 1
        img_col = f"""          <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
            <div class="hrms-product-media">
              <img src="{esc(s['image'])}" alt="{esc(s['image_alt'])}" loading="lazy">
            </div>
          </div>"""
        bullets = "\n".join(
            f'                <li><i class="bi bi-check2-circle"></i><span>{esc(b)}</span></li>'
            for b in s["bullets"]
        )
        text_col = f"""          <div class="col-lg-6" data-aos="fade-up" data-aos-delay="150">
            <div class="hrms-product-copy">
              <h2>{esc(s['title'])}</h2>
              <p>{esc(s['text'])}</p>
              <ul class="hrms-check-list">
{bullets}
              </ul>
            </div>
          </div>"""
        if reverse:
            row = f'        <div class="row gy-4 align-items-center hrms-solution-row">\n{text_col}\n{img_col}\n        </div>'
        else:
            row = f'        <div class="row gy-4 align-items-center hrms-solution-row">\n{img_col}\n{text_col}\n        </div>'
        blocks.append(row)
    return "\n\n".join(blocks)


def process_steps(steps):
    items = []
    for i, (title, desc) in enumerate(steps, start=1):
        items.append(
            f"""          <div class="col-md-6 col-xl-3" data-aos="fade-up" data-aos-delay="{i * 50}">
            <div class="hrms-process-card">
              <span class="hrms-process-num">{i:02d}</span>
              <h3>{esc(title)}</h3>
              <p>{esc(desc)}</p>
            </div>
          </div>"""
        )
    return "\n".join(items)


def capability_cards(items):
    rows = []
    for icon, label in items:
        rows.append(
            f"""          <div class="col-6 col-md-4 col-lg-3" data-aos="fade-up">
            <div class="hrms-capability-item">
              <i class="bi {esc(icon)}"></i>
              <span>{esc(label)}</span>
            </div>
          </div>"""
        )
    return "\n".join(rows)


def faq_items(faqs):
    rows = []
    for i, (q, a) in enumerate(faqs):
        show = " show" if i == 0 else ""
        collapsed = "" if i == 0 else " collapsed"
        expanded = "true" if i == 0 else "false"
        rows.append(
            f"""            <div class="accordion-item">
              <h2 class="accordion-header">
                <button class="accordion-button{collapsed}" type="button" data-bs-toggle="collapse" data-bs-target="#faq-{i}" aria-expanded="{expanded}" aria-controls="faq-{i}">
                  {esc(q)}
                </button>
              </h2>
              <div id="faq-{i}" class="accordion-collapse collapse{show}" data-bs-parent="#qhseFaq">
                <div class="accordion-body">{esc(a)}</div>
              </div>
            </div>"""
        )
    return "\n".join(rows)


def related_cards(current_slug):
    cards = []
    for slug, title, icon in RELATED:
        if slug == current_slug:
            continue
        cards.append(
            f"""          <div class="col-6 col-md-4 col-lg-2">
            <a href="{esc(slug)}.html" class="hrms-related-card">
              <i class="bi {esc(icon)}"></i>
              <span>{esc(title)}</span>
            </a>
          </div>"""
        )
    return "\n".join(cards)


def render_module(m):
    filename = f"{m['slug']}.html"
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>{esc(m['title'])} | AIBizs QHSE</title>
  <meta name="description" content="{esc(m['description'])}">
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
  <link href="assets/css/main.css" rel="stylesheet">
</head>

<body class="hrms-product-page">

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
          <li><a href="index.html#products" class="active">Our Products</a></li>
          <li><a href="index.html#contact">Contact</a></li>
        </ul>
        <i class="mobile-nav-toggle d-xl-none bi bi-list"></i>
      </nav>
      <a class="btn-getstarted" href="index.html#contact">Get Started</a>
    </div>
  </header>

  <main class="main">

    <section class="hrms-product-hero section">
      <div class="container">
        <nav class="hrms-product-breadcrumbs" aria-label="Breadcrumb">
          <a href="index.html">Home</a>
          <span>/</span>
          <a href="product-qhse.html">QHSE</a>
          <span>/</span>
          <span>{esc(m['title'])}</span>
        </nav>

        <div class="row gy-5 align-items-center">
          <div class="col-lg-6" data-aos="fade-up">
            <p class="hrms-product-eyebrow"><i class="bi {esc(m['icon'])}"></i> {esc(m['eyebrow'])}</p>
            <h1>{esc(m['hero_title'])}</h1>
            <p class="hrms-product-lead">{esc(m['hero_text'])}</p>
            <div class="hrms-product-cta-group">
              <a href="index.html#contact" class="btn-primary">Request a Demo</a>
              <a href="product-qhse.html" class="hrms-btn-ghost">Explore QHSE</a>
            </div>
          </div>
          <div class="col-lg-6" data-aos="fade-left" data-aos-delay="100">
            <div class="hrms-product-hero-media">
              <img src="{esc(m['image'])}" alt="{esc(m['image_alt'])}" loading="eager">
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="hrms-product-trust">
      <div class="container">
        <p data-aos="fade-up">{esc(m['trust_line'])}</p>
      </div>
    </section>

    <section class="hrms-product-solutions section">
      <div class="container">
{solution_blocks(m['solutions'])}
      </div>
    </section>

    <section class="hrms-product-capabilities section light-background">
      <div class="container">
        <div class="section-title text-center" data-aos="fade-up">
          <h2>Platform Capabilities</h2>
          <p>Everything you need to run {esc(m['title']).lower()} with control and clarity</p>
        </div>
        <div class="row g-3">
{capability_cards(m['capabilities'])}
        </div>
      </div>
    </section>

    <section class="hrms-product-process section">
      <div class="container">
        <div class="section-title text-center" data-aos="fade-up">
          <h2>End-to-End Process</h2>
          <p>A clear operating flow from setup to outcomes</p>
        </div>
        <div class="row g-4">
{process_steps(m['process'])}
        </div>
      </div>
    </section>

    <section class="hrms-product-faq section light-background">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-8">
            <div class="section-title text-center" data-aos="fade-up">
              <h2>Frequently Asked Questions</h2>
            </div>
            <div class="accordion hrms-faq-accordion" id="qhseFaq" data-aos="fade-up" data-aos-delay="100">
{faq_items(m['faqs'])}
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="hrms-product-cta-band section">
      <div class="container" data-aos="zoom-in">
        <div class="hrms-cta-panel">
          <div>
            <h2>Ready to see {esc(m['title'])} in action?</h2>
            <p>Speak with our team about configuring AIBizs QHSE for your organization in Oman and the GCC.</p>
          </div>
          <div class="hrms-product-cta-group">
            <a href="index.html#contact" class="btn-primary">Book a Discovery Call</a>
            <a href="product-qhse.html" class="hrms-btn-ghost">Back to QHSE</a>
          </div>
        </div>
      </div>
    </section>

    <section class="hrms-product-related section">
      <div class="container">
        <div class="section-title text-center" data-aos="fade-up">
          <h2>More QHSE Modules</h2>
        </div>
        <div class="row g-3 justify-content-center">
{related_cards(m['slug'])}
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
            <li><a href="product-qhse.html">QHSE</a></li>
            <li><a href="index.html#products">Our Products</a></li>
            <li><a href="index.html#contact">Contact</a></li>
          </ul>
        </div>
        <div class="col-lg-2 col-6 footer-links">
          <h4>QHSE Modules</h4>
          <ul>
            <li><a href="qhse-incident-management.html">Incident Management</a></li>
            <li><a href="qhse-inspection.html">Inspection</a></li>
            <li><a href="qhse-journey-plan.html">Journey Plan</a></li>
            <li><a href="qhse-quality-management.html">Quality Management</a></li>
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
  <script src="assets/js/main.js"></script>
</body>

</html>
"""


def main():
    for module in MODULES:
        path = ROOT / f"{module['slug']}.html"
        path.write_text(render_module(module), encoding="utf-8")
        print(f"Wrote {path.name}")


if __name__ == "__main__":
    main()
