#!/usr/bin/env python3
"""Generate HRMS module product pages — HR platform marketing layout in AIBizs theme."""

from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MODULES = [
    {
        "slug": "hrms-payroll",
        "title": "Payroll",
        "eyebrow": "AIVizion HRMS",
        "hero_title": "Flexible Payroll Solutions",
        "hero_text": "Automate salary processing, statutory deductions, payslips, and bank disbursement — built for Omani and GCC organizations that need accuracy, control, and audit-ready payroll every cycle.",
        "description": "AIVizion HRMS Payroll automates salary calculations, allowances, deductions, social contributions, payslip generation, and bank disbursement for Omani and GCC workforces.",
        "icon": "bi-wallet2",
        "image": "assets/img/hrimage/payroll-hero.png",
        "image_alt": "AIBizs payroll cycle dashboard",
        "trust_line": "One payroll engine for multi-company workforces across Oman and the GCC",
        "solutions": [
            {
                "title": "Cloud Payroll Software",
                "text": "A simple, automated, and secure payroll module that puts HR and finance in control — without spreadsheet chaos. Configure pay elements once, then run accurate cycles every month.",
                "bullets": [
                    "Unlimited salary components, allowances, and deductions",
                    "Gross-to-net automation with exception checks",
                    "Payslips and bank transfer file generation",
                    "Role-based access for HR and finance teams",
                ],
                "image": "assets/img/hrimage/payroll-cloud.png",
                "image_alt": "Cloud payroll salary engine and pay elements",
            },
            {
                "title": "Integrated HR & Payroll",
                "text": "Say goodbye to disconnected systems. Payroll pulls leave, attendance, loans, and employee changes directly from AIVizion HRMS — one source of truth for people and pay.",
                "bullets": [
                    "Eliminate duplicate data entry between HR and payroll",
                    "Leave and overtime impact reflected automatically",
                    "Employee self-service payslip access",
                    "Finance-ready journals and cost-center reporting",
                ],
                "image": "assets/img/hrimage/payroll-integrated.png",
                "image_alt": "Integrated HR and payroll data sync",
                "reverse": True,
            },
            {
                "title": "Compliance-Ready Operations",
                "text": "Configure social insurance, labor-aligned rules, and company policies once. Every cycle runs with validation, approvals, and a full audit trail for leadership and auditors.",
                "bullets": [
                    "Statutory contribution and policy configuration",
                    "Multi-level payroll approval workflows",
                    "Retro pay and mid-cycle adjustments",
                    "Archived cycle history for audits",
                ],
                "image": "assets/img/hrimage/payroll-compliance.png",
                "image_alt": "Payroll compliance and audit controls",
            },
        ],
        "process": [
            ("Define Structures", "Set grades, pay elements, overtime rules, and deduction policies."),
            ("Capture Inputs", "Sync attendance, leave, loans, and one-time adjustments."),
            ("Calculate & Approve", "Run gross-to-net with exception flags and approvals."),
            ("Disburse & Report", "Issue payslips, bank files, journals, and statutory outputs."),
        ],
        "capabilities": [
            ("bi-calculator", "Automated salary engine"),
            ("bi-building", "Multi-company payroll"),
            ("bi-file-earmark-text", "Payslips & bank files"),
            ("bi-shield-check", "Compliance controls"),
            ("bi-journal-text", "ERP / GL export"),
            ("bi-graph-up", "Payroll analytics"),
            ("bi-person-badge", "Employee self-serve payslips"),
            ("bi-clock-history", "Retro & adjustments"),
        ],
        "faqs": [
            ("Who is AIVizion Payroll for?", "Organizations in Oman and the GCC that need reliable in-house payroll — from growing SMBs to multi-entity enterprises — with clear HR and finance collaboration."),
            ("Does it integrate with other HRMS modules?", "Yes. Payroll connects with Leave, Attendance, ESS, Onboarding, and Offboarding so pay reflects real workforce events without re-keying data."),
            ("Can we support multiple companies?", "Yes. Run separate or consolidated cycles across legal entities and branches with shared or company-specific pay rules."),
            ("How do employees access payslips?", "Through Employee Self Service — secure download of current and historical payslips with role-based privacy controls."),
        ],
    },
    {
        "slug": "hrms-employee-self-service",
        "title": "Employee Self Service",
        "eyebrow": "AIVizion HRMS",
        "hero_title": "Self-Service HR for Every Employee",
        "hero_text": "Give your workforce a modern portal to manage profiles, payslips, leave, and documents — cutting HR admin while improving everyday employee experience.",
        "description": "AIVizion Employee Self Service gives staff a secure portal for profiles, payslips, leave balances, documents, and requests.",
        "icon": "bi-person-badge",
        "image": "assets/img/hrimage/ess-hero.png",
        "image_alt": "Employee self-service workplace dashboard",
        "trust_line": "Fewer tickets. Faster answers. Better employee experience.",
        "solutions": [
            {
                "title": "Employee Portal",
                "text": "A clean, always-available workspace where employees handle routine HR tasks themselves — from any device, with permissions that protect sensitive data.",
                "bullets": [
                    "View and update personal and banking details",
                    "Download payslips and employment documents",
                    "Check leave balances and request status",
                    "Track open requests from submit to done",
                ],
                "image": "assets/img/hrimage/ess-portal.png",
                "image_alt": "Employee portal quick actions and documents",
            },
            {
                "title": "Manager Approvals in One Place",
                "text": "Managers get clear queues for leave and profile changes — with notifications, history, and team context so decisions are fast and consistent.",
                "bullets": [
                    "Approval inbox with escalation paths",
                    "Visibility of team leave calendars",
                    "Reduced email chains and chasing",
                    "Full audit of who approved what",
                ],
                "image": "assets/img/hrimage/ess-approvals.png",
                "image_alt": "Manager approval inbox",
                "reverse": True,
            },
            {
                "title": "Secure by Design",
                "text": "Role-based access keeps employee, manager, and HR views separated. Multi-company setups stay isolated while still feeling like one HR platform.",
                "bullets": [
                    "HR, manager, and employee permission levels",
                    "Encrypted access to personal documents",
                    "Policy-aligned request forms",
                    "Mobile-responsive experience for field teams",
                ],
                "image": "assets/img/hrimage/ess-secure.png",
                "image_alt": "Role-based security for employee self-service",
            },
        ],
        "process": [
            ("Secure Sign-In", "Employees access ESS with role-based credentials."),
            ("Self-Serve", "Update details, view payslips, and submit requests."),
            ("Approve", "Managers review and approve in structured queues."),
            ("Sync", "Changes flow into HR records, leave, and payroll."),
        ],
        "capabilities": [
            ("bi-person-vcard", "Personal profile hub"),
            ("bi-receipt", "Payslip download"),
            ("bi-calendar3", "Leave visibility"),
            ("bi-folder2-open", "Document center"),
            ("bi-bell", "Smart notifications"),
            ("bi-phone", "Mobile-ready UI"),
            ("bi-shield-lock", "Privacy controls"),
            ("bi-chat-dots", "Request tracking"),
        ],
        "faqs": [
            ("Does ESS replace HR tickets?", "It dramatically reduces routine requests — payslips, balances, and profile updates — so HR focuses on higher-value work."),
            ("Can managers approve from ESS?", "Yes. Leave and selected change requests route to the right manager with full status tracking."),
            ("Is it available on mobile?", "Yes. The portal is responsive for office and field employees."),
            ("How is data protected?", "Access is role-based, and sensitive documents are only visible to authorized users."),
        ],
    },
    {
        "slug": "hrms-leave-management",
        "title": "Leave Management",
        "eyebrow": "AIVizion HRMS",
        "hero_title": "Absence Management Made Simple",
        "hero_text": "Policy-driven leave types, accruals, approvals, and team calendars — so employees know their balances and managers plan coverage with confidence.",
        "description": "AIVizion Leave Management handles annual, sick, and special leave with accruals, multi-level approvals, calendars, and payroll sync.",
        "icon": "bi-calendar-check",
        "image": "assets/img/hrimage/leave-hero.png",
        "image_alt": "Leave management absence hub dashboard",
        "trust_line": "Clear policies. Accurate balances. Faster approvals.",
        "solutions": [
            {
                "title": "Policy-Driven Leave",
                "text": "Configure leave types, accrual rules, carry-forward limits, and blackout periods once — then let the platform enforce them at request time.",
                "bullets": [
                    "Annual, sick, unpaid, and custom leave types",
                    "Automatic accruals and prorations",
                    "Carry-forward and entitlement controls",
                    "Prevention of negative or conflicting balances",
                ],
                "image": "assets/img/hrimage/leave-policy.png",
                "image_alt": "Leave types and policy configuration",
            },
            {
                "title": "Approvals & Team Planning",
                "text": "Managers see request impact against team calendars before approving — reducing coverage surprises and back-and-forth emails.",
                "bullets": [
                    "Multi-level approval workflows",
                    "Team absence calendar visibility",
                    "Attachment support for medical docs",
                    "Delegation when managers are away",
                ],
                "image": "assets/img/hrimage/leave-calendar.png",
                "image_alt": "Leave approvals and team planning",
                "reverse": True,
            },
            {
                "title": "Payroll-Connected Leave",
                "text": "Approved leave updates balances instantly and feeds payroll so unpaid leave and deductions stay accurate without manual reconciliation.",
                "bullets": [
                    "Real-time balance updates",
                    "Payroll period alignment",
                    "Absence analytics by department",
                    "Audit history for every request",
                ],
                "image": "assets/img/hrimage/leave-payroll.png",
                "image_alt": "Leave outcomes synced to payroll",
            },
        ],
        "process": [
            ("Configure", "Set leave types, accruals, and approval rules."),
            ("Request", "Employees submit leave via self-service."),
            ("Approve", "Managers review balances and team impact."),
            ("Sync", "Balances and payroll outcomes update automatically."),
        ],
        "capabilities": [
            ("bi-calendar2-week", "Leave types & policies"),
            ("bi-arrow-repeat", "Accrual engine"),
            ("bi-diagram-3", "Approval workflows"),
            ("bi-calendar-event", "Team calendars"),
            ("bi-paperclip", "Document attachments"),
            ("bi-exclamation-circle", "Policy guards"),
            ("bi-bar-chart", "Absence analytics"),
            ("bi-link-45deg", "Payroll sync"),
        ],
        "faqs": [
            ("Can we define different leave policies by company?", "Yes. Multi-company setups support company-specific leave types and entitlement rules."),
            ("How do accruals work?", "Accruals run automatically based on your configured formulas, including prorations and carry-forward limits."),
            ("Will leave affect payroll?", "Approved unpaid leave and related outcomes can sync into the payroll cycle."),
            ("Can employees see balances?", "Yes — balances and request status are available in Employee Self Service."),
        ],
    },
    {
        "slug": "hrms-employee-onboarding",
        "title": "Employee Onboarding",
        "eyebrow": "AIVizion HRMS",
        "hero_title": "Onboarding That Sets New Hires Up for Success",
        "hero_text": "Replace chaotic first weeks with guided checklists, document collection, access provisioning, and probation tracking — from offer accepted to productive.",
        "description": "AIVizion Onboarding standardizes joining with checklists, document collection, IT/HR tasks, and probation tracking.",
        "icon": "bi-person-plus",
        "image": "assets/img/hrimage/onboarding-hero.png",
        "image_alt": "Employee onboarding journey dashboard",
        "trust_line": "Faster ramp-up. Fewer missed steps. Better first impressions.",
        "solutions": [
            {
                "title": "Structured Joining Journeys",
                "text": "Launch role-based onboarding plans the moment a hire is confirmed. HR, IT, facilities, and managers each get clear tasks and due dates.",
                "bullets": [
                    "Template checklists by role or company",
                    "Pre-joining and day-one task streams",
                    "Owner assignment and due-date tracking",
                    "Progress dashboards for HR",
                ],
                "image": "assets/img/hrimage/onboarding-journey.png",
                "image_alt": "Structured onboarding checklist workflow",
            },
            {
                "title": "Documents & Compliance Early",
                "text": "Collect IDs, contracts, bank details, and compliance forms securely — with verification status so nothing blocks the first payroll.",
                "bullets": [
                    "Secure document upload",
                    "Verification workflow for HR",
                    "Complete employee master data from day one",
                    "Reduced joining-day paperwork chaos",
                ],
                "image": "assets/img/hrimage/onboarding-docs.png",
                "image_alt": "Onboarding document verification",
                "reverse": True,
            },
            {
                "title": "Access, Assets & Probation",
                "text": "Coordinate system access, equipment, induction, and probation reviews so new hires are productive — and confirmed — on time.",
                "bullets": [
                    "IT access and asset assignment tracking",
                    "Induction and training milestones",
                    "Probation reminders and reviews",
                    "Time-to-productivity visibility",
                ],
                "image": "assets/img/hrimage/onboarding-access.png",
                "image_alt": "Access provisioning and probation tracking",
            },
        ],
        "process": [
            ("Plan", "Generate onboarding checklist from hire confirmation."),
            ("Collect", "Gather documents and verify compliance forms."),
            ("Provision", "Assign systems, assets, and workspace readiness."),
            ("Activate", "Convert to employee record and track probation."),
        ],
        "capabilities": [
            ("bi-list-check", "Onboarding checklists"),
            ("bi-file-earmark-check", "Document collection"),
            ("bi-person-gear", "Profile creation"),
            ("bi-pc-display", "Access provisioning"),
            ("bi-box-seam", "Asset assignment"),
            ("bi-mortarboard", "Induction tracking"),
            ("bi-hourglass", "Probation management"),
            ("bi-speedometer2", "Onboarding KPIs"),
        ],
        "faqs": [
            ("When does onboarding start?", "As soon as hiring is confirmed — pre-joining tasks can run before day one."),
            ("Can different roles have different checklists?", "Yes. Templates can be tailored by role, department, or company."),
            ("Does onboarding connect to payroll?", "Complete profiles and documents help ensure new hires are payroll-ready on time."),
            ("Can we track probation?", "Yes. Reminders and review milestones keep confirmation decisions on schedule."),
        ],
    },
    {
        "slug": "hrms-employee-offboarding",
        "title": "Employee Offboarding",
        "eyebrow": "AIVizion HRMS",
        "hero_title": "Secure, Complete Employee Exits",
        "hero_text": "Manage resignations and terminations with clearance workflows, asset return, access revocation, and accurate final settlement — every exit audit-ready.",
        "description": "AIVizion Offboarding manages exit clearances, asset return, access revocation, knowledge handover, and final settlements.",
        "icon": "bi-person-dash",
        "image": "assets/img/hrimage/offboarding-hero.png",
        "image_alt": "Employee offboarding exit control dashboard",
        "trust_line": "Protect assets. Settle fairly. Close the loop.",
        "solutions": [
            {
                "title": "Exit Workflows That Don’t Miss Steps",
                "text": "Initiate resignation or termination once, then route clearances to IT, finance, facilities, and managers with completion tracking.",
                "bullets": [
                    "Notice period and last-day capture",
                    "Department-wise clearance checklists",
                    "Handover task assignment",
                    "Status visibility for HR",
                ],
                "image": "assets/img/hrimage/offboarding-workflow.png",
                "image_alt": "Cross-department exit clearance workflow",
            },
            {
                "title": "Assets & Access Control",
                "text": "Confirm device returns and revoke system access on schedule — reducing security and inventory risk when people leave.",
                "bullets": [
                    "Laptop, phone, and badge recovery",
                    "Email and system access shutdown",
                    "Building access coordination",
                    "Logged clearance history",
                ],
                "image": "assets/img/hrimage/offboarding-assets.png",
                "image_alt": "Asset return and access revocation",
                "reverse": True,
            },
            {
                "title": "Final Settlement & Closure",
                "text": "Calculate leave encashment, loans, and outstanding dues with payroll alignment — then issue exit documents and archive the record.",
                "bullets": [
                    "Final settlement calculation",
                    "Exit interview capture",
                    "Experience and clearance letters",
                    "Secure archival for audits",
                ],
                "image": "assets/img/hrimage/offboarding-settlement.png",
                "image_alt": "Final settlement calculation dashboard",
            },
        ],
        "process": [
            ("Initiate", "Capture exit type, notice terms, and last working day."),
            ("Clear", "Complete department clearances and asset returns."),
            ("Settle", "Calculate final dues with payroll inputs."),
            ("Close", "Revoke access, issue documents, and archive."),
        ],
        "capabilities": [
            ("bi-door-open", "Exit initiation"),
            ("bi-ui-checks", "Clearance workflow"),
            ("bi-laptop", "Asset recovery"),
            ("bi-key", "Access revocation"),
            ("bi-cash-coin", "Final settlement"),
            ("bi-chat-square-quote", "Exit interviews"),
            ("bi-file-earmark-pdf", "Exit documents"),
            ("bi-archive", "Secure archival"),
        ],
        "faqs": [
            ("What exit types are supported?", "Resignations, contract ends, and terminations — each with structured workflows."),
            ("How is final settlement handled?", "Unused leave, loans, and dues are calculated and aligned with payroll before close."),
            ("Can we track asset return?", "Yes. Assets are listed and marked recovered as part of clearance."),
            ("Is there an audit trail?", "Every clearance step and settlement action is logged."),
        ],
    },
    {
        "slug": "hrms-appraisal",
        "title": "Appraisal",
        "eyebrow": "AIVizion HRMS",
        "hero_title": "Performance Reviews That Drive Growth",
        "hero_text": "Run fair, structured appraisal cycles with goals, feedback, calibration, and development plans — turning reviews into continuous performance management.",
        "description": "AIVizion Appraisal supports goal setting, multi-rater reviews, calibration, and development plans linked to workforce growth.",
        "icon": "bi-graph-up",
        "image": "assets/img/hrimage/appraisal-hero.png",
        "image_alt": "Performance appraisal cycle dashboard",
        "trust_line": "Aligned goals. Fairer ratings. Actionable outcomes.",
        "solutions": [
            {
                "title": "Goal & KPI Frameworks",
                "text": "Set OKRs or KPIs with weights and timelines so individual work connects to team and company objectives throughout the year.",
                "bullets": [
                    "Configurable goal frameworks",
                    "Weighted objectives and milestones",
                    "Manager and employee alignment",
                    "Mid-cycle progress visibility",
                ],
                "image": "assets/img/hrimage/appraisal-goals.png",
                "image_alt": "Goals and KPI tracking dashboard",
            },
            {
                "title": "Structured Reviews & Calibration",
                "text": "Launch appraisal cycles with consistent forms, optional 360 feedback, and calibration tools that reduce bias across departments.",
                "bullets": [
                    "Self and manager review forms",
                    "Optional multi-rater input",
                    "Rating scales by grade or role",
                    "Calibration for fair outcomes",
                ],
                "image": "assets/img/hrimage/appraisal-reviews.png",
                "image_alt": "Performance reviews and calibration",
                "reverse": True,
            },
            {
                "title": "From Rating to Action",
                "text": "Connect appraisal results to development plans, training needs, promotions, and increments — with dashboards leaders can trust.",
                "bullets": [
                    "Development plan creation",
                    "Completion and distribution analytics",
                    "Links to HR outcome workflows",
                    "Continuous feedback notes",
                ],
                "image": "assets/img/hrimage/appraisal-actions.png",
                "image_alt": "Appraisal outcomes and development plans",
            },
        ],
        "process": [
            ("Launch", "Define cycle, forms, scales, and participants."),
            ("Set Goals", "Agree KPIs/OKRs with managers."),
            ("Review", "Complete evaluations and optional 360 input."),
            ("Act", "Calibrate ratings and create development plans."),
        ],
        "capabilities": [
            ("bi-bullseye", "Goal & KPI tracking"),
            ("bi-pencil-square", "Review forms"),
            ("bi-people", "360 feedback"),
            ("bi-sliders", "Calibration tools"),
            ("bi-chat-left-text", "Continuous feedback"),
            ("bi-signpost-2", "Development plans"),
            ("bi-pie-chart", "Performance analytics"),
            ("bi-link", "HR outcomes link"),
        ],
        "faqs": [
            ("Can we run annual and continuous cycles?", "Yes. Configure the cadence that fits your organization."),
            ("Is 360 feedback required?", "No — enable it only where it adds value."),
            ("How does calibration work?", "Leaders can review rating distribution before finalizing outcomes."),
            ("Can results drive promotions?", "Appraisal outcomes can feed promotion, increment, and PIP discussions."),
        ],
    },
    {
        "slug": "hrms-recruitment",
        "title": "Recruitment",
        "eyebrow": "AIVizion HRMS",
        "hero_title": "Hire Faster with a Clear Talent Pipeline",
        "hero_text": "Manage requisitions, job postings, interviews, scorecards, and offers in one place — then hand accepted candidates straight into onboarding.",
        "description": "AIVizion Recruitment manages requisitions, pipelines, interviews, evaluations, and offers with seamless onboarding handoff.",
        "icon": "bi-briefcase",
        "image": "assets/img/hrimage/recruitment-hero.png",
        "image_alt": "Recruitment talent pipeline dashboard",
        "trust_line": "Shorter time-to-hire. Better quality decisions. Seamless joining.",
        "solutions": [
            {
                "title": "Requisitions to Job Postings",
                "text": "Control headcount requests with approvals, then publish roles and collect applications into a single pipeline recruiters and managers share.",
                "bullets": [
                    "Requisition approval workflows",
                    "Job posting and source tracking",
                    "Unified candidate intake",
                    "Hiring manager collaboration",
                ],
                "image": "assets/img/hrimage/recruitment-requisition.png",
                "image_alt": "Job requisitions and headcount approvals",
            },
            {
                "title": "Screening, Interviews & Scorecards",
                "text": "Move candidates through clear stages with scheduled interviews and standardized evaluations — so comparisons stay fair and fast.",
                "bullets": [
                    "Stage-based pipeline tracking",
                    "Interview scheduling and reminders",
                    "Structured evaluation scorecards",
                    "AI-assisted shortlist support",
                ],
                "image": "assets/img/hrimage/recruitment-pipeline.png",
                "image_alt": "Interview scorecards and screening",
                "reverse": True,
            },
            {
                "title": "Offers & Onboarding Handoff",
                "text": "Issue offers, track acceptance, and push hired candidates into onboarding checklists — cutting the gap between yes and day one.",
                "bullets": [
                    "Offer generation and tracking",
                    "Acceptance status visibility",
                    "Instant onboarding handoff",
                    "Time-to-hire analytics",
                ],
                "image": "assets/img/hrimage/recruitment-offers.png",
                "image_alt": "Offer management and onboarding handoff",
            },
        ],
        "process": [
            ("Requisition", "Approve headcount and define the role."),
            ("Attract", "Publish jobs and collect applications."),
            ("Evaluate", "Screen, interview, and score candidates."),
            ("Hire", "Send offers and hand off to onboarding."),
        ],
        "capabilities": [
            ("bi-file-earmark-plus", "Requisition management"),
            ("bi-megaphone", "Job postings"),
            ("bi-kanban", "Candidate pipeline"),
            ("bi-calendar2-check", "Interview scheduling"),
            ("bi-clipboard-data", "Evaluation scorecards"),
            ("bi-envelope-check", "Offer management"),
            ("bi-robot", "AI-assisted screening"),
            ("bi-arrow-right-circle", "Onboarding handoff"),
        ],
        "faqs": [
            ("Can hiring managers collaborate in the pipeline?", "Yes. Recruiters and managers share candidate stages, feedback, and decisions."),
            ("Does recruitment connect to onboarding?", "Accepted offers can flow directly into onboarding checklists."),
            ("Can we track time-to-hire?", "Yes. Pipeline analytics highlight stage bottlenecks and cycle time."),
            ("Is AI screening available?", "AI-assisted shortlisting helps accelerate CV review while humans stay in control."),
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
              <div id="faq-{i}" class="accordion-collapse collapse{show}" data-bs-parent="#hrmsFaq">
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
  <title>{esc(m['title'])} | AIVizion HRMS</title>
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
          <a href="product-hrms.html">HRMS</a>
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
              <a href="product-hrms.html" class="hrms-btn-ghost">Explore HRMS</a>
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
            <div class="accordion hrms-faq-accordion" id="hrmsFaq" data-aos="fade-up" data-aos-delay="100">
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
            <p>Speak with our team about configuring AIVizion HRMS for your organization in Oman and the GCC.</p>
          </div>
          <div class="hrms-product-cta-group">
            <a href="index.html#contact" class="btn-primary">Book a Discovery Call</a>
            <a href="product-hrms.html" class="hrms-btn-ghost">Back to HRMS</a>
          </div>
        </div>
      </div>
    </section>

    <section class="hrms-product-related section">
      <div class="container">
        <div class="section-title text-center" data-aos="fade-up">
          <h2>More HRMS Modules</h2>
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
            <li><a href="product-hrms.html">HRMS</a></li>
            <li><a href="index.html#products">Our Products</a></li>
            <li><a href="index.html#contact">Contact</a></li>
          </ul>
        </div>
        <div class="col-lg-2 col-6 footer-links">
          <h4>HRMS Modules</h4>
          <ul>
            <li><a href="hrms-payroll.html">Payroll</a></li>
            <li><a href="hrms-leave-management.html">Leave Management</a></li>
            <li><a href="hrms-recruitment.html">Recruitment</a></li>
            <li><a href="hrms-appraisal.html">Appraisal</a></li>
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
