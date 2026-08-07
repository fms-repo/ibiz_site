#!/usr/bin/env python3
"""Generate ERP module product pages — reuse HRMS product layout classes in AIBizs theme."""

from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

MODULES = [
    {
        "slug": "erp-finance",
        "title": "Finance",
        "eyebrow": "AIBizs ERP",
        "hero_title": "Finance Control Across Every Entity",
        "hero_text": "Run journals, budgets, consolidations, and management reporting from one finance core — built for multi-company groups in Oman and the GCC that need OMR accuracy, audit trails, and real-time visibility.",
        "description": "AIBizs ERP Finance unifies journals, budgets, consolidations, and financial reporting for multi-company organizations in Oman and the GCC.",
        "icon": "bi-cash-stack",
        "image": "assets/img/erpimage/finance-hero.png",
        "image_alt": "AIBizs ERP finance control dashboard",
        "trust_line": "One finance engine for multi-company groups across Oman and the GCC",
        "solutions": [
            {
                "title": "Unified Financial Journals",
                "text": "Post, review, and reverse journals with dimension control and approval workflows — so every entity stays audit-ready without spreadsheet workarounds.",
                "bullets": [
                    "Multi-company journal entry and templates",
                    "Cost center, project, and branch dimensions",
                    "Approval workflows with full audit history",
                    "OMR and multi-currency posting support",
                ],
                "image": "assets/img/erpimage/finance-journals.png",
                "image_alt": "Financial journals and dimension posting",
            },
            {
                "title": "Statements & Consolidation",
                "text": "Produce entity and group statements from a single ledger structure. Intercompany eliminations and period locks keep consolidated numbers trustworthy.",
                "bullets": [
                    "Trial balance, P&L, and balance sheet views",
                    "Group consolidation across legal entities",
                    "Intercompany matching and eliminations",
                    "Period close controls and locks",
                ],
                "image": "assets/img/erpimage/finance-statements.png",
                "image_alt": "Financial statements and consolidation",
                "reverse": True,
            },
            {
                "title": "Budgets & Forecast Control",
                "text": "Plan budgets by company, department, and project — then track actuals versus plan with alerts that keep spending aligned to leadership targets.",
                "bullets": [
                    "Budget versions and revision history",
                    "Department and project budget allocation",
                    "Actual vs budget variance dashboards",
                    "Commitment and spend visibility",
                ],
                "image": "assets/img/erpimage/finance-budget.png",
                "image_alt": "Budget planning and variance tracking",
            },
        ],
        "process": [
            ("Configure Structures", "Set companies, chart links, dimensions, and fiscal calendars."),
            ("Capture Transactions", "Post journals from modules and manual entries with controls."),
            ("Review & Close", "Reconcile, approve, and lock periods with audit evidence."),
            ("Report & Consolidate", "Publish statements, budgets, and group consolidations."),
        ],
        "capabilities": [
            ("bi-journal-text", "Journal management"),
            ("bi-building", "Multi-company finance"),
            ("bi-currency-exchange", "OMR & multi-currency"),
            ("bi-bar-chart", "Statements & reports"),
            ("bi-diagram-3", "Group consolidation"),
            ("bi-piggy-bank", "Budget control"),
            ("bi-shield-check", "Audit trails"),
            ("bi-lock", "Period close locks"),
        ],
        "faqs": [
            ("Who is AIBizs ERP Finance for?", "Organizations in Oman and the GCC that need a unified finance core across one or many legal entities — with OMR support, consolidations, and audit-ready controls."),
            ("Does Finance connect to AP, AR, and GL?", "Yes. Sub-ledgers post into the finance core so payables, receivables, and the general ledger stay reconciled without re-keying."),
            ("Can we run multi-company consolidations?", "Yes. Manage multiple entities with shared or company-specific rules and produce group-level consolidated statements."),
            ("Is budgeting included?", "Yes. Create budget versions by company and department, then track actuals versus plan throughout the year."),
        ],
    },
    {
        "slug": "erp-accounts-payable",
        "title": "Accounts Payable",
        "eyebrow": "AIBizs ERP",
        "hero_title": "Pay Vendors with Control and Clarity",
        "hero_text": "Capture supplier invoices, match to purchase orders, schedule payments, and keep liabilities visible — so finance teams in Oman and the GCC close AP cycles without surprise overdue balances.",
        "description": "AIBizs ERP Accounts Payable manages vendor invoices, three-way matching, payment runs, and payable aging for Omani and GCC enterprises.",
        "icon": "bi-arrow-down-circle",
        "image": "assets/img/erpimage/ap-hero.png",
        "image_alt": "Accounts payable invoice and payment dashboard",
        "trust_line": "Cleaner invoice intake. Faster approvals. Predictable payment runs.",
        "solutions": [
            {
                "title": "Invoice Capture & Matching",
                "text": "Register vendor invoices against POs and receipts with exception flags — reducing duplicate payments and mismatched quantities before they hit the ledger.",
                "bullets": [
                    "PO and goods-receipt matching",
                    "Duplicate invoice detection",
                    "Tax and withholding configuration",
                    "Vendor credit note handling",
                ],
                "image": "assets/img/erpimage/ap-hero.png",
                "image_alt": "Vendor invoice capture and matching",
            },
            {
                "title": "Approval & Payment Runs",
                "text": "Route invoices through multi-level approvals, then build payment batches by due date, vendor, or company with bank-file ready outputs.",
                "bullets": [
                    "Configurable approval workflows",
                    "Scheduled and on-demand payment batches",
                    "Bank transfer file generation",
                    "Partial and advance payment support",
                ],
                "image": "assets/img/erpimage/ap-invoices.png",
                "image_alt": "AP approvals and payment batching",
                "reverse": True,
            },
            {
                "title": "Liability Visibility",
                "text": "Age payables by vendor and company, forecast cash outflows, and keep GL postings aligned so treasury and finance share one view of commitments.",
                "bullets": [
                    "Vendor aging and open-item tracking",
                    "Cash requirement forecasts",
                    "Automatic GL posting",
                    "Audit history for every payment",
                ],
                "image": "assets/img/erpimage/ap-payments.png",
                "image_alt": "Payable aging and payment history",
            },
        ],
        "process": [
            ("Receive", "Capture invoices and match to PO or contract terms."),
            ("Approve", "Route exceptions and approvals to the right owners."),
            ("Pay", "Build payment runs and issue bank files."),
            ("Reconcile", "Clear open items and post to the general ledger."),
        ],
        "capabilities": [
            ("bi-receipt", "Invoice registration"),
            ("bi-link-45deg", "PO matching"),
            ("bi-diagram-3", "Approval workflows"),
            ("bi-bank", "Payment batches"),
            ("bi-clock-history", "Aging analysis"),
            ("bi-percent", "Tax & withholding"),
            ("bi-journal-check", "GL integration"),
            ("bi-shield-check", "Duplicate controls"),
        ],
        "faqs": [
            ("Does AP support multi-company vendors?", "Yes. Vendors can be shared or company-specific, with payment runs filtered by legal entity."),
            ("Can we match invoices to purchase orders?", "Yes. Two-way and three-way matching help prevent overpayment and quantity mismatches."),
            ("How are payments issued?", "Build approved payment batches and generate bank transfer outputs for your banking partners."),
            ("Does AP post to the general ledger?", "Yes. Invoice and payment activity posts automatically into the connected GL and finance modules."),
        ],
    },
    {
        "slug": "erp-accounts-receivable",
        "title": "Accounts Receivable",
        "eyebrow": "AIBizs ERP",
        "hero_title": "Collect Faster with Clear Customer Balances",
        "hero_text": "Issue invoices, track receipts, manage credit notes, and drive collections from one receivables workspace — designed for multi-entity sales operations across Oman and the GCC.",
        "description": "AIBizs ERP Accounts Receivable handles customer invoicing, receipts, credit control, and collections for organizations in Oman and the GCC.",
        "icon": "bi-arrow-up-circle",
        "image": "assets/img/erpimage/ar-hero.png",
        "image_alt": "Accounts receivable collections dashboard",
        "trust_line": "Accurate invoices. Clear aging. Stronger cash collection.",
        "solutions": [
            {
                "title": "Customer Invoicing",
                "text": "Generate invoices from sales orders or manual billing with tax, discounts, and multi-currency options — then deliver statements customers can trust.",
                "bullets": [
                    "Sales-order and manual invoicing",
                    "OMR and multi-currency billing",
                    "Credit notes and adjustments",
                    "Customer statement generation",
                ],
                "image": "assets/img/erpimage/ar-hero.png",
                "image_alt": "Customer invoicing and statements",
            },
            {
                "title": "Receipts & Allocation",
                "text": "Record bank receipts and allocate them precisely to open invoices — including partial payments and multi-invoice settlements.",
                "bullets": [
                    "Receipt posting and allocation",
                    "Partial and advance payments",
                    "Unapplied cash tracking",
                    "Bank reconciliation support",
                ],
                "image": "assets/img/erpimage/ar-invoices.png",
                "image_alt": "Receipt allocation against open invoices",
                "reverse": True,
            },
            {
                "title": "Collections & Credit Control",
                "text": "Monitor aging buckets, credit limits, and overdue accounts so collections teams prioritize the right customers before cash risk grows.",
                "bullets": [
                    "Customer aging dashboards",
                    "Credit limit enforcement",
                    "Overdue follow-up queues",
                    "AR analytics by company and segment",
                ],
                "image": "assets/img/erpimage/ar-collections.png",
                "image_alt": "Collections and credit control workspace",
            },
        ],
        "process": [
            ("Bill", "Create and issue customer invoices with tax and terms."),
            ("Track", "Monitor open items, aging, and credit exposure."),
            ("Collect", "Allocate receipts and chase overdue balances."),
            ("Report", "Post to GL and publish AR performance views."),
        ],
        "capabilities": [
            ("bi-file-earmark-text", "Customer invoicing"),
            ("bi-cash-coin", "Receipt allocation"),
            ("bi-hourglass-split", "Aging analysis"),
            ("bi-credit-card", "Credit control"),
            ("bi-envelope", "Customer statements"),
            ("bi-graph-up", "Collections analytics"),
            ("bi-currency-exchange", "Multi-currency AR"),
            ("bi-journal-text", "GL posting"),
        ],
        "faqs": [
            ("Can AR handle multi-company customers?", "Yes. Bill and collect by legal entity while maintaining a consolidated customer view where needed."),
            ("Does it support credit notes?", "Yes. Issue credit notes and adjustments that stay linked to the original invoice trail."),
            ("How does collections work?", "Aging views and overdue queues help teams prioritize follow-ups and track resolution."),
            ("Is AR connected to CRM and sales?", "Yes. Customer and order context can flow into invoicing so billing stays aligned with commercial activity."),
        ],
    },
    {
        "slug": "erp-general-ledger",
        "title": "General Ledger",
        "eyebrow": "AIBizs ERP",
        "hero_title": "The Ledger Your Enterprise Runs On",
        "hero_text": "Maintain a single, controlled chart of accounts with sub-ledger integration, period close discipline, and audit-ready history — the financial backbone for multi-company ERP in Oman and the GCC.",
        "description": "AIBizs ERP General Ledger provides chart of accounts control, sub-ledger integration, period close, and audit-ready financial history.",
        "icon": "bi-journal-text",
        "image": "assets/img/erpimage/gl-hero.png",
        "image_alt": "General ledger and chart of accounts dashboard",
        "trust_line": "One chart. Clean postings. Disciplined period close.",
        "solutions": [
            {
                "title": "Chart of Accounts Control",
                "text": "Design a scalable chart structure for single or multi-entity groups — with account types, dimensions, and mapping rules that stay consistent as you grow.",
                "bullets": [
                    "Flexible chart of accounts design",
                    "Account hierarchies and mapping",
                    "Dimension and segment control",
                    "Company-specific or shared charts",
                ],
                "image": "assets/img/erpimage/gl-hero.png",
                "image_alt": "Chart of accounts structure",
            },
            {
                "title": "Sub-Ledger Integration",
                "text": "Receive postings from AP, AR, inventory, payroll, and projects into the GL with clear source references — eliminating end-of-month reconciling chaos.",
                "bullets": [
                    "Automated module-to-GL posting",
                    "Source document drill-down",
                    "Recurring and reversing journals",
                    "Suspense and exception handling",
                ],
                "image": "assets/img/erpimage/gl-coa.png",
                "image_alt": "Sub-ledger postings into general ledger",
                "reverse": True,
            },
            {
                "title": "Period Close & Audit",
                "text": "Run checklists, lock periods, and retain immutable history so auditors and leadership can trust every closing balance.",
                "bullets": [
                    "Period open/close workflows",
                    "Close checklists and owner tasks",
                    "Immutable posting history",
                    "Trial balance and account inquiry",
                ],
                "image": "assets/img/erpimage/gl-close.png",
                "image_alt": "Period close and audit controls",
            },
        ],
        "process": [
            ("Structure", "Define chart, dimensions, and posting rules."),
            ("Post", "Accept sub-ledger and manual journal activity."),
            ("Reconcile", "Clear exceptions and validate trial balances."),
            ("Close", "Complete checklists and lock the period."),
        ],
        "capabilities": [
            ("bi-list-columns", "Chart of accounts"),
            ("bi-arrow-left-right", "Sub-ledger sync"),
            ("bi-calendar-check", "Fiscal calendars"),
            ("bi-lock", "Period locks"),
            ("bi-search", "Account inquiry"),
            ("bi-file-earmark-bar-graph", "Trial balance"),
            ("bi-clock-history", "Audit history"),
            ("bi-building", "Multi-entity GL"),
        ],
        "faqs": [
            ("Can one GL serve multiple companies?", "Yes. Run separate ledgers or a shared structure with entity-level controls and consolidations."),
            ("How do modules post to the GL?", "AP, AR, inventory, and other modules post with source references so you can drill from balance to document."),
            ("Is period close controlled?", "Yes. Use close checklists and period locks so late postings cannot alter closed books."),
            ("Does the GL support OMR reporting?", "Yes. Maintain OMR as a base currency with multi-currency posting and reporting options."),
        ],
    },
    {
        "slug": "erp-treasury",
        "title": "Treasury",
        "eyebrow": "AIBizs ERP",
        "hero_title": "Cash, Banks, and Liquidity in One View",
        "hero_text": "Manage bank accounts, cash positions, transfers, and forecasts so finance leaders see liquidity across entities — not scattered spreadsheets and email balances.",
        "description": "AIBizs ERP Treasury centralizes cash management, bank operations, transfers, and liquidity forecasting for Oman and GCC enterprises.",
        "icon": "bi-bank",
        "image": "assets/img/erpimage/treasury-hero.png",
        "image_alt": "Treasury cash and banking dashboard",
        "trust_line": "Real-time cash visibility. Controlled bank operations. Better forecasts.",
        "solutions": [
            {
                "title": "Cash Position Management",
                "text": "See available cash by bank, company, and currency. Combine AP/AR outlooks with treasury balances for a practical daily liquidity picture.",
                "bullets": [
                    "Multi-bank cash position views",
                    "Company and currency breakdowns",
                    "Inflow and outflow forecasts",
                    "Liquidity alerts and thresholds",
                ],
                "image": "assets/img/erpimage/treasury-hero.png",
                "image_alt": "Cash position by bank and company",
            },
            {
                "title": "Banking Operations",
                "text": "Record bank receipts, payments, and transfers with reconciliation tools that keep book balances aligned to bank statements.",
                "bullets": [
                    "Bank account master control",
                    "Internal and intercompany transfers",
                    "Bank statement reconciliation",
                    "Cheque and transfer tracking",
                ],
                "image": "assets/img/erpimage/treasury-cash.png",
                "image_alt": "Banking operations and transfers",
                "reverse": True,
            },
            {
                "title": "Bank Connectivity & Control",
                "text": "Organize payment files, approvals, and bank relationships with role-based access — so treasury actions stay secure and auditable.",
                "bullets": [
                    "Payment file coordination with AP",
                    "Treasury approval workflows",
                    "Bank relationship records",
                    "Audit logs for cash movements",
                ],
                "image": "assets/img/erpimage/treasury-bank.png",
                "image_alt": "Bank connectivity and treasury controls",
            },
        ],
        "process": [
            ("Position", "Review cash by bank, entity, and currency."),
            ("Move", "Execute transfers and coordinate payment batches."),
            ("Reconcile", "Match statements to book balances."),
            ("Forecast", "Project liquidity using AP/AR and treasury inputs."),
        ],
        "capabilities": [
            ("bi-wallet2", "Cash positioning"),
            ("bi-bank2", "Bank account control"),
            ("bi-arrow-left-right", "Transfers"),
            ("bi-clipboard-check", "Bank reconciliation"),
            ("bi-graph-up", "Liquidity forecasts"),
            ("bi-shield-lock", "Treasury approvals"),
            ("bi-currency-exchange", "Multi-currency cash"),
            ("bi-building", "Multi-entity treasury"),
        ],
        "faqs": [
            ("Does Treasury work with AP and AR?", "Yes. Payment runs and collections feed treasury visibility so cash forecasts reflect real open items."),
            ("Can we manage multiple bank accounts?", "Yes. Maintain accounts across banks and companies with consolidated cash views."),
            ("Is bank reconciliation included?", "Yes. Match statements to book transactions and clear differences with audit history."),
            ("Can treasury support multi-currency?", "Yes. Track balances and movements in OMR and other currencies used across the GCC."),
        ],
    },
    {
        "slug": "erp-inventory-management",
        "title": "Inventory Management",
        "eyebrow": "AIBizs ERP",
        "hero_title": "Stock Control You Can Trust",
        "hero_text": "Track items across warehouses, manage receipts and issues, and keep inventory valuation tied to finance — so operations and accounting share one stock truth.",
        "description": "AIBizs ERP Inventory Management provides real-time stock tracking, warehouse control, valuation, and inventory workflows for Oman and GCC businesses.",
        "icon": "bi-box-seam",
        "image": "assets/img/erpimage/inventory-hero.png",
        "image_alt": "Inventory management stock dashboard",
        "trust_line": "Accurate stock. Controlled warehouses. Finance-aligned valuation.",
        "solutions": [
            {
                "title": "Real-Time Stock Visibility",
                "text": "Know what you have, where it sits, and what is reserved — across warehouses and companies — before you promise delivery or reorder.",
                "bullets": [
                    "Multi-warehouse stock on hand",
                    "Reservations and availability checks",
                    "Batch and serial tracking options",
                    "Reorder level and shortage alerts",
                ],
                "image": "assets/img/erpimage/inventory-hero.png",
                "image_alt": "Real-time stock visibility across warehouses",
            },
            {
                "title": "Warehouse Operations",
                "text": "Run receipts, issues, transfers, and adjustments with documented reasons — keeping warehouse teams fast and auditors satisfied.",
                "bullets": [
                    "Goods receipt and issue workflows",
                    "Inter-warehouse transfers",
                    "Stock adjustments with reasons",
                    "Cycle count and inventory checks",
                ],
                "image": "assets/img/erpimage/inventory-stock.png",
                "image_alt": "Warehouse receipts issues and transfers",
                "reverse": True,
            },
            {
                "title": "Valuation & Warehouse Control",
                "text": "Keep inventory costs aligned to the ledger with valuation methods and warehouse policies that support manufacturing and project consumption.",
                "bullets": [
                    "Inventory valuation methods",
                    "Automatic GL inventory postings",
                    "Warehouse and bin organization",
                    "Consumption for projects and production",
                ],
                "image": "assets/img/erpimage/inventory-warehouse.png",
                "image_alt": "Inventory valuation and warehouse control",
            },
        ],
        "process": [
            ("Receive", "Post goods into warehouses against POs or transfers."),
            ("Store", "Organize locations, batches, and availability."),
            ("Issue", "Fulfill sales, production, and project demand."),
            ("Value", "Update costs and post inventory to the ledger."),
        ],
        "capabilities": [
            ("bi-box", "Stock on hand"),
            ("bi-building", "Multi-warehouse"),
            ("bi-upc-scan", "Batch & serial"),
            ("bi-arrow-repeat", "Transfers"),
            ("bi-clipboard-data", "Cycle counts"),
            ("bi-cash-stack", "Valuation"),
            ("bi-exclamation-triangle", "Reorder alerts"),
            ("bi-link-45deg", "Finance sync"),
        ],
        "faqs": [
            ("Can inventory span multiple warehouses?", "Yes. Track stock by warehouse and company with transfer workflows between locations."),
            ("Does inventory post to finance?", "Yes. Valuation and stock movements can post automatically into the general ledger."),
            ("Is batch or serial tracking supported?", "Yes. Enable batch and serial controls where products require traceability."),
            ("How does inventory connect to manufacturing?", "BOMs and production issues consume stock with visibility back to warehouse balances."),
        ],
    },
    {
        "slug": "erp-operation-management",
        "title": "Operation Management",
        "eyebrow": "AIBizs ERP",
        "hero_title": "Run Daily Operations with Connected Workflows",
        "hero_text": "Coordinate operational processes, task ownership, and performance KPIs across departments — so day-to-day execution stays aligned with ERP data, not side systems.",
        "description": "AIBizs ERP Operation Management streamlines day-to-day business workflows, process ownership, and operational KPI tracking.",
        "icon": "bi-gear",
        "image": "assets/img/erpimage/operations-hero.png",
        "image_alt": "Operation management workflow dashboard",
        "trust_line": "Clear workflows. Owned tasks. Measurable operational performance.",
        "solutions": [
            {
                "title": "Operational Workflow Control",
                "text": "Standardize recurring operational processes with defined steps, owners, and escalations — reducing handoff gaps between teams.",
                "bullets": [
                    "Configurable operational workflows",
                    "Owner and due-date assignment",
                    "Escalation and reminder rules",
                    "Cross-department handoff tracking",
                ],
                "image": "assets/img/erpimage/operations-hero.png",
                "image_alt": "Operational workflow control board",
            },
            {
                "title": "Process Execution Hub",
                "text": "Give supervisors a single place to monitor open work, bottlenecks, and exceptions tied to inventory, orders, and service activity.",
                "bullets": [
                    "Live operational work queues",
                    "Bottleneck and exception views",
                    "Links to inventory and order status",
                    "Mobile-friendly task updates",
                ],
                "image": "assets/img/erpimage/operations-workflow.png",
                "image_alt": "Process execution and work queues",
                "reverse": True,
            },
            {
                "title": "KPI & Performance Tracking",
                "text": "Measure what matters — cycle times, completion rates, and SLA adherence — so leadership can improve operations with evidence.",
                "bullets": [
                    "Operational KPI dashboards",
                    "SLA and cycle-time tracking",
                    "Department performance views",
                    "Trend analysis for continuous improvement",
                ],
                "image": "assets/img/erpimage/operations-kpi.png",
                "image_alt": "Operations KPI and performance dashboards",
            },
        ],
        "process": [
            ("Define", "Configure workflows, owners, and success metrics."),
            ("Execute", "Run daily tasks with status and handoff control."),
            ("Monitor", "Spot bottlenecks and escalate exceptions."),
            ("Improve", "Use KPI trends to refine operating procedures."),
        ],
        "capabilities": [
            ("bi-diagram-3", "Workflow builder"),
            ("bi-person-check", "Task ownership"),
            ("bi-bell", "Escalations"),
            ("bi-kanban", "Work queues"),
            ("bi-speedometer2", "KPI dashboards"),
            ("bi-hourglass", "Cycle-time tracking"),
            ("bi-phone", "Field-friendly updates"),
            ("bi-link", "ERP module links"),
        ],
        "faqs": [
            ("What is Operation Management for?", "Teams that need structured day-to-day execution across departments while staying connected to ERP inventory, orders, and service data."),
            ("Can workflows differ by company?", "Yes. Multi-company setups can use shared or entity-specific operational processes."),
            ("Does it replace project management?", "No — it focuses on recurring operational execution; projects are handled in the Project Management module."),
            ("Can we track KPIs?", "Yes. Dashboards highlight cycle times, completion rates, and SLA performance."),
        ],
    },
    {
        "slug": "erp-crm",
        "title": "Customer Relationship Management",
        "eyebrow": "AIBizs ERP",
        "hero_title": "Win, Serve, and Grow Customer Relationships",
        "hero_text": "Manage leads, opportunities, accounts, and service interactions in one CRM connected to ERP orders and receivables — built for commercial teams across Oman and the GCC.",
        "description": "AIBizs ERP CRM manages customer interactions, sales pipelines, accounts, and service workflows connected to enterprise operations.",
        "icon": "bi-person-heart",
        "image": "assets/img/erpimage/crm-hero.png",
        "image_alt": "CRM sales and service dashboard",
        "trust_line": "Clear pipelines. Stronger service. Revenue tied to operations.",
        "solutions": [
            {
                "title": "Account & Contact Hub",
                "text": "Keep a complete view of customers, contacts, and history — so sales and service teams never work from outdated email threads.",
                "bullets": [
                    "Account and contact master data",
                    "Interaction and activity history",
                    "Multi-company customer contexts",
                    "Segmentation for targeted follow-up",
                ],
                "image": "assets/img/erpimage/crm-hero.png",
                "image_alt": "Customer account and contact hub",
            },
            {
                "title": "Sales Pipeline Management",
                "text": "Move opportunities through defined stages with forecasts, quotes, and conversion tracking that leadership can trust.",
                "bullets": [
                    "Stage-based opportunity pipelines",
                    "Quote and proposal tracking",
                    "Win/loss reasons and forecasts",
                    "Handoff into orders and billing",
                ],
                "image": "assets/img/erpimage/crm-pipeline.png",
                "image_alt": "Sales pipeline and opportunity stages",
                "reverse": True,
            },
            {
                "title": "Customer Service Continuity",
                "text": "Log service cases, assign owners, and close loops with visibility that protects relationships after the sale.",
                "bullets": [
                    "Service case logging and SLAs",
                    "Assignment and escalation rules",
                    "Customer communication history",
                    "Service performance analytics",
                ],
                "image": "assets/img/erpimage/crm-service.png",
                "image_alt": "Customer service case management",
            },
        ],
        "process": [
            ("Capture", "Log leads, accounts, and customer interactions."),
            ("Qualify", "Progress opportunities through the sales pipeline."),
            ("Convert", "Hand off wins into orders, delivery, and AR."),
            ("Serve", "Manage cases and renewals with full history."),
        ],
        "capabilities": [
            ("bi-people", "Account management"),
            ("bi-funnel", "Sales pipelines"),
            ("bi-file-earmark-richtext", "Quotes"),
            ("bi-headset", "Service cases"),
            ("bi-graph-up", "Forecasting"),
            ("bi-bell", "Follow-up reminders"),
            ("bi-link-45deg", "Order & AR link"),
            ("bi-bar-chart", "CRM analytics"),
        ],
        "faqs": [
            ("Does CRM connect to ERP billing?", "Yes. Won opportunities and customer data can flow into orders and accounts receivable."),
            ("Can multiple teams share one customer view?", "Yes. Sales and service work from shared account history with role-based access."),
            ("Is pipeline forecasting available?", "Yes. Stage-based pipelines support forecast views and conversion analytics."),
            ("Does it support multi-company sales?", "Yes. Manage customer relationships across legal entities with clear commercial context."),
        ],
    },
    {
        "slug": "erp-srm",
        "title": "Supplier Relation Management",
        "eyebrow": "AIBizs ERP",
        "hero_title": "Procurement Relationships Under Control",
        "hero_text": "Qualify suppliers, manage contracts, and run procurement processes with visibility from requisition to receipt — strengthening supply assurance for Oman and GCC operations.",
        "description": "AIBizs ERP Supplier Relation Management covers supplier qualification, contracts, procurement processes, and supplier performance.",
        "icon": "bi-truck",
        "image": "assets/img/erpimage/srm-hero.png",
        "image_alt": "Supplier relation and procurement dashboard",
        "trust_line": "Trusted suppliers. Controlled contracts. Smoother procurement.",
        "solutions": [
            {
                "title": "Supplier Lifecycle",
                "text": "Onboard and qualify suppliers with documents, categories, and risk notes — then keep master data current for purchasing and AP teams.",
                "bullets": [
                    "Supplier onboarding and qualification",
                    "Category and risk classification",
                    "Document and compliance records",
                    "Approved supplier lists",
                ],
                "image": "assets/img/erpimage/srm-hero.png",
                "image_alt": "Supplier onboarding and qualification",
            },
            {
                "title": "Procurement Execution",
                "text": "Drive requisitions, RFQs, and purchase orders with approval paths that keep spend controlled before goods arrive.",
                "bullets": [
                    "Purchase requisitions and approvals",
                    "RFQ comparison and award",
                    "Purchase order management",
                    "Goods receipt coordination",
                ],
                "image": "assets/img/erpimage/srm-procurement.png",
                "image_alt": "Procurement requisitions and purchase orders",
                "reverse": True,
            },
            {
                "title": "Contracts & Performance",
                "text": "Track contract terms, renewals, and supplier scorecards so procurement decisions stay evidence-based — not relationship-only.",
                "bullets": [
                    "Supplier contract repositories",
                    "Renewal and expiry alerts",
                    "Delivery and quality scorecards",
                    "Spend analysis by supplier",
                ],
                "image": "assets/img/erpimage/srm-contracts.png",
                "image_alt": "Supplier contracts and performance scorecards",
            },
        ],
        "process": [
            ("Qualify", "Onboard suppliers and approve categories."),
            ("Source", "Run requisitions, RFQs, and awards."),
            ("Order", "Issue POs and track deliveries."),
            ("Review", "Score performance and manage contracts."),
        ],
        "capabilities": [
            ("bi-person-check", "Supplier qualification"),
            ("bi-cart-check", "Purchase orders"),
            ("bi-clipboard-data", "RFQ comparison"),
            ("bi-file-earmark-text", "Contract control"),
            ("bi-star", "Performance scorecards"),
            ("bi-box-seam", "Receipt coordination"),
            ("bi-cash", "Spend visibility"),
            ("bi-link", "AP integration"),
        ],
        "faqs": [
            ("How does SRM connect to Accounts Payable?", "Approved receipts and supplier invoices align with AP so procurement and finance stay reconciled."),
            ("Can we manage supplier contracts?", "Yes. Store terms, track renewals, and alert owners before expiry."),
            ("Does it support multi-company purchasing?", "Yes. Requisitions and POs can follow company-specific approval and supplier rules."),
            ("Can we score supplier performance?", "Yes. Track delivery, quality, and commercial performance for better sourcing decisions."),
        ],
    },
    {
        "slug": "erp-vendor-portal",
        "title": "Vendor Portal",
        "eyebrow": "AIBizs ERP",
        "hero_title": "Self-Service for Your Supplier Network",
        "hero_text": "Give vendors a secure portal to view orders, submit invoices, track payment status, and update profile details — cutting email noise while improving procurement collaboration.",
        "description": "AIBizs ERP Vendor Portal provides suppliers a self-service space for orders, invoices, payment status, and profile updates.",
        "icon": "bi-door-open",
        "image": "assets/img/erpimage/vendor-hero.png",
        "image_alt": "Vendor portal supplier self-service dashboard",
        "trust_line": "Fewer emails. Faster vendor responses. Clear order status.",
        "solutions": [
            {
                "title": "Secure Vendor Access",
                "text": "Onboard suppliers with controlled login and permissions so each vendor sees only their company data — nothing more.",
                "bullets": [
                    "Role-based vendor user access",
                    "Company-isolated data views",
                    "Profile and banking detail updates",
                    "Secure document exchange",
                ],
                "image": "assets/img/erpimage/vendor-hero.png",
                "image_alt": "Secure vendor portal access",
            },
            {
                "title": "Orders & Acknowledgements",
                "text": "Vendors view purchase orders, acknowledge lines, and flag delivery issues early — improving fulfillment reliability.",
                "bullets": [
                    "Purchase order visibility",
                    "Order acknowledgement workflows",
                    "Delivery date updates",
                    "Exception and query logging",
                ],
                "image": "assets/img/erpimage/vendor-portal.png",
                "image_alt": "Vendor order acknowledgement workspace",
                "reverse": True,
            },
            {
                "title": "Invoices & Payment Status",
                "text": "Let vendors submit invoice details and track payment progress without calling AP — while finance keeps approval control inside ERP.",
                "bullets": [
                    "Invoice submission from the portal",
                    "Payment status transparency",
                    "Reduced AP inquiry volume",
                    "Audit trail of vendor actions",
                ],
                "image": "assets/img/erpimage/vendor-orders.png",
                "image_alt": "Vendor invoices and payment status",
            },
        ],
        "process": [
            ("Invite", "Provision vendor users with secure access."),
            ("Collaborate", "Share POs and receive acknowledgements."),
            ("Submit", "Vendors send invoices and supporting documents."),
            ("Track", "Both sides monitor payment and order status."),
        ],
        "capabilities": [
            ("bi-shield-lock", "Secure vendor login"),
            ("bi-bag-check", "PO visibility"),
            ("bi-check2-square", "Acknowledgements"),
            ("bi-receipt", "Invoice submission"),
            ("bi-cash-coin", "Payment status"),
            ("bi-folder2-open", "Document exchange"),
            ("bi-bell", "Status notifications"),
            ("bi-person-gear", "Profile self-update"),
        ],
        "faqs": [
            ("Who can use the Vendor Portal?", "Approved suppliers with provisioned users — each limited to their own orders and documents."),
            ("Can vendors see payment status?", "Yes. Payment progress is visible after invoices enter the AP workflow."),
            ("Does the portal replace AP approvals?", "No. Approvals remain inside ERP; the portal improves collaboration and status transparency."),
            ("Is data isolated between vendors?", "Yes. Vendors only see their own company information and transactions."),
        ],
    },
    {
        "slug": "erp-e-invoicing",
        "title": "E-Invoicing",
        "eyebrow": "AIBizs ERP",
        "hero_title": "Electronic Invoicing Built for Compliance",
        "hero_text": "Generate, validate, and submit electronic invoices with PEPPOL/OTA-ready pathways — helping organizations in Oman and the GCC meet digital invoicing requirements without breaking ERP workflows.",
        "description": "AIBizs ERP E-Invoicing supports electronic invoice generation, validation, PEPPOL/OTA-aligned submission, and compliance tracking for Oman and the GCC.",
        "icon": "bi-receipt",
        "image": "assets/img/erpimage/einvoice-hero.png",
        "image_alt": "E-invoicing compliance and submission dashboard",
        "trust_line": "PEPPOL/OTA-ready. Validated invoices. Compliance you can prove.",
        "solutions": [
            {
                "title": "Electronic Invoice Generation",
                "text": "Create structured e-invoices from ERP billing and AP/AR documents — with the fields and formats required for digital exchange.",
                "bullets": [
                    "Structured e-invoice generation",
                    "Source documents from AR and AP",
                    "Buyer and seller data validation",
                    "Tax and line-item completeness checks",
                ],
                "image": "assets/img/erpimage/einvoice-hero.png",
                "image_alt": "Electronic invoice generation from ERP",
            },
            {
                "title": "Submission & Exchange",
                "text": "Submit invoices through PEPPOL/OTA-aligned channels and track acknowledgement status so finance knows what cleared and what needs correction.",
                "bullets": [
                    "PEPPOL/OTA-aligned submission paths",
                    "Transmission status tracking",
                    "Acknowledgement and rejection handling",
                    "Resubmission workflows",
                ],
                "image": "assets/img/erpimage/einvoice-submit.png",
                "image_alt": "E-invoice submission and acknowledgement status",
                "reverse": True,
            },
            {
                "title": "Compliance & Audit Evidence",
                "text": "Retain submission history, validation results, and document archives so compliance teams can demonstrate control during reviews.",
                "bullets": [
                    "Validation rule enforcement",
                    "Immutable submission archives",
                    "Compliance status dashboards",
                    "Audit-ready document trail",
                ],
                "image": "assets/img/erpimage/einvoice-compliance.png",
                "image_alt": "E-invoicing compliance and audit archive",
            },
        ],
        "process": [
            ("Prepare", "Generate structured invoices from ERP documents."),
            ("Validate", "Run schema and business-rule checks."),
            ("Submit", "Send via PEPPOL/OTA-aligned channels."),
            ("Archive", "Store acknowledgements and compliance evidence."),
        ],
        "capabilities": [
            ("bi-file-earmark-code", "Structured e-invoices"),
            ("bi-send-check", "PEPPOL/OTA submit"),
            ("bi-shield-check", "Validation rules"),
            ("bi-arrow-repeat", "Resubmission"),
            ("bi-archive", "Compliance archive"),
            ("bi-graph-up", "Status dashboards"),
            ("bi-link-45deg", "AR/AP integration"),
            ("bi-lock", "Audit evidence"),
        ],
        "faqs": [
            ("Is e-invoicing PEPPOL/OTA ready?", "Yes. Submission pathways are designed for PEPPOL/OTA-aligned electronic invoice exchange relevant to Oman and the GCC."),
            ("Does it connect to AR and AP?", "Yes. E-invoices are generated from ERP billing and payable documents to avoid dual entry."),
            ("What happens if an invoice is rejected?", "Rejection details are captured so teams can correct and resubmit with a full history."),
            ("Can we keep compliance archives?", "Yes. Validation results, submissions, and acknowledgements are retained for audit."),
        ],
    },
    {
        "slug": "erp-human-resource-management",
        "title": "Human Resource Management",
        "eyebrow": "AIBizs ERP",
        "hero_title": "People Data Connected to the Enterprise",
        "hero_text": "Manage employee master data, organizational structures, and HR processes inside ERP — with payroll-ready records and links to projects, costing, and self-service.",
        "description": "AIBizs ERP Human Resource Management covers employee master data, organization structures, HR processes, and payroll-ready workforce records.",
        "icon": "bi-people-fill",
        "image": "assets/img/erpimage/hr-hero.png",
        "image_alt": "Human resource management employee dashboard",
        "trust_line": "One employee record. Clear org structures. Payroll-ready data.",
        "solutions": [
            {
                "title": "Employee Master & Organization",
                "text": "Maintain complete employee profiles, grades, departments, and reporting lines across companies — the foundation for HR and costing accuracy.",
                "bullets": [
                    "Employee master data management",
                    "Org charts and reporting lines",
                    "Multi-company workforce structures",
                    "Contracts and employment history",
                ],
                "image": "assets/img/erpimage/hr-hero.png",
                "image_alt": "Employee master and organization structures",
            },
            {
                "title": "HR Operations",
                "text": "Run core HR processes — transfers, promotions, and status changes — with approvals and an audit trail that keeps records trustworthy.",
                "bullets": [
                    "Transfers and promotions",
                    "Employment status workflows",
                    "Document and record tracking",
                    "HR action approval trails",
                ],
                "image": "assets/img/erpimage/hr-employees.png",
                "image_alt": "HR operations and employee lifecycle actions",
                "reverse": True,
            },
            {
                "title": "Payroll & Cost Integration",
                "text": "Keep workforce data ready for payroll and project costing so finance and HR share consistent headcount and labor numbers.",
                "bullets": [
                    "Payroll-ready employee records",
                    "Cost center and project assignment",
                    "Headcount and workforce reports",
                    "Links to ESS and payroll modules",
                ],
                "image": "assets/img/erpimage/hr-payroll.png",
                "image_alt": "HR payroll readiness and cost assignment",
            },
        ],
        "process": [
            ("Structure", "Define companies, departments, and job grades."),
            ("Maintain", "Keep employee records and HR actions current."),
            ("Assign", "Link people to cost centers and projects."),
            ("Enable", "Feed payroll, ESS, and workforce reporting."),
        ],
        "capabilities": [
            ("bi-person-vcard", "Employee master"),
            ("bi-diagram-3", "Org structures"),
            ("bi-arrow-left-right", "Transfers & promotions"),
            ("bi-folder2", "HR documents"),
            ("bi-wallet2", "Payroll readiness"),
            ("bi-pie-chart", "Workforce reports"),
            ("bi-building", "Multi-company HR"),
            ("bi-person-badge", "ESS connectivity"),
        ],
        "faqs": [
            ("Is this a full HRMS replacement?", "It provides ERP-connected HR foundations. For deeper HR lifecycle modules, AIBizs also offers AIVizion HRMS."),
            ("Does HR connect to payroll?", "Yes. Employee and assignment data stay payroll-ready and can integrate with payroll processing."),
            ("Can we manage multi-company workforces?", "Yes. Maintain structures and employees across legal entities from one platform."),
            ("How does HR link to projects?", "Employees can be assigned to cost centers and projects for accurate labor costing."),
        ],
    },
    {
        "slug": "erp-manufacturing",
        "title": "Manufacturing",
        "eyebrow": "AIBizs ERP",
        "hero_title": "Plan and Execute Production with Precision",
        "hero_text": "Define BOMs, plan production orders, and track execution against inventory — so manufacturing teams deliver on schedule with cost and material visibility.",
        "description": "AIBizs ERP Manufacturing supports bill of materials, production planning, manufacturing execution, and inventory-connected shop-floor control.",
        "icon": "bi-cpu",
        "image": "assets/img/erpimage/mfg-hero.png",
        "image_alt": "Manufacturing production planning dashboard",
        "trust_line": "Clear BOMs. Controlled production. Inventory-aware execution.",
        "solutions": [
            {
                "title": "Bill of Materials & Routing",
                "text": "Define product structures and process steps once — then reuse them across production orders with version control.",
                "bullets": [
                    "Multi-level bill of materials",
                    "Routing and work-center definitions",
                    "BOM version control",
                    "Component availability checks",
                ],
                "image": "assets/img/erpimage/mfg-hero.png",
                "image_alt": "Bill of materials and routing setup",
            },
            {
                "title": "Production Planning",
                "text": "Create and schedule production orders based on demand, capacity, and material readiness — reducing last-minute shortages.",
                "bullets": [
                    "Production order management",
                    "Material requirement visibility",
                    "Capacity and schedule planning",
                    "Priority and due-date control",
                ],
                "image": "assets/img/erpimage/mfg-bom.png",
                "image_alt": "Production planning and order scheduling",
                "reverse": True,
            },
            {
                "title": "Manufacturing Execution",
                "text": "Issue materials, record completions, and capture scrap or variances — keeping inventory and costing aligned as products are finished.",
                "bullets": [
                    "Material issue to production",
                    "Operation and completion booking",
                    "Scrap and variance capture",
                    "Finished goods receipt to stock",
                ],
                "image": "assets/img/erpimage/mfg-execution.png",
                "image_alt": "Manufacturing execution and completions",
            },
        ],
        "process": [
            ("Define", "Set BOMs, routings, and work centers."),
            ("Plan", "Create production orders against demand."),
            ("Execute", "Issue materials and book operations."),
            ("Receive", "Post finished goods and cost outcomes."),
        ],
        "capabilities": [
            ("bi-diagram-2", "BOM management"),
            ("bi-signpost-2", "Routings"),
            ("bi-calendar3", "Production planning"),
            ("bi-tools", "Shop-floor booking"),
            ("bi-box-arrow-in-down", "Material issues"),
            ("bi-box-seam", "Finished goods"),
            ("bi-exclamation-circle", "Scrap & variance"),
            ("bi-cash-stack", "Production costing"),
        ],
        "faqs": [
            ("Does manufacturing connect to inventory?", "Yes. Component issues and finished goods receipts update warehouse stock in real time."),
            ("Can we use multi-level BOMs?", "Yes. Define nested product structures with version control."),
            ("How is production cost tracked?", "Material and completion activity supports costing visibility tied to ERP finance."),
            ("Is it suitable for multi-plant setups?", "Yes. Plan and execute production across companies and locations with shared or separate masters."),
        ],
    },
    {
        "slug": "erp-project-management",
        "title": "Project Management",
        "eyebrow": "AIBizs ERP",
        "hero_title": "Deliver Projects with Cost and Resource Clarity",
        "hero_text": "Plan timelines, assign resources, track progress, and control project budgets — connecting delivery teams to inventory, HR, and finance for Oman and GCC project organizations.",
        "description": "AIBizs ERP Project Management plans, tracks, and controls projects with resources, timelines, budgets, and enterprise cost integration.",
        "icon": "bi-kanban",
        "image": "assets/img/erpimage/project-hero.png",
        "image_alt": "Project management planning dashboard",
        "trust_line": "On-time delivery. Controlled budgets. Resource clarity.",
        "solutions": [
            {
                "title": "Project Planning",
                "text": "Structure projects with phases, tasks, milestones, and dependencies so delivery teams share one plan — not scattered trackers.",
                "bullets": [
                    "Phases, tasks, and milestones",
                    "Dependency and timeline planning",
                    "Project templates by type",
                    "Status and progress tracking",
                ],
                "image": "assets/img/erpimage/project-hero.png",
                "image_alt": "Project phases tasks and milestones",
            },
            {
                "title": "Resource & Schedule Control",
                "text": "Assign people and capacity to work, monitor utilization, and spot overloads before deadlines slip.",
                "bullets": [
                    "Resource assignment and calendars",
                    "Utilization visibility",
                    "Workload balancing",
                    "Timesheet and effort capture",
                ],
                "image": "assets/img/erpimage/project-plan.png",
                "image_alt": "Project resource and schedule control",
                "reverse": True,
            },
            {
                "title": "Budget & Cost Tracking",
                "text": "Connect project spend to budgets and actuals from inventory, AP, and labor — so commercial and delivery leaders see the same numbers.",
                "bullets": [
                    "Project budget vs actual",
                    "Cost from inventory and AP",
                    "Labor and timesheet costing",
                    "Project profitability views",
                ],
                "image": "assets/img/erpimage/project-resources.png",
                "image_alt": "Project budget and cost tracking",
            },
        ],
        "process": [
            ("Initiate", "Create the project structure and budget."),
            ("Plan", "Define tasks, milestones, and resources."),
            ("Execute", "Track progress, effort, and material use."),
            ("Control", "Compare actuals to budget and close the project."),
        ],
        "capabilities": [
            ("bi-kanban", "Task boards"),
            ("bi-flag", "Milestones"),
            ("bi-people", "Resource planning"),
            ("bi-clock", "Timesheets"),
            ("bi-cash", "Budget control"),
            ("bi-box", "Material costing"),
            ("bi-graph-up", "Profitability"),
            ("bi-building", "Multi-company projects"),
        ],
        "faqs": [
            ("Can project costs pull from inventory and AP?", "Yes. Material issues and supplier costs can roll into project actuals."),
            ("Does it support resource timesheets?", "Yes. Capture effort against tasks for utilization and labor costing."),
            ("Can we run multi-company projects?", "Yes. Structure projects by entity with shared visibility where needed."),
            ("How does this differ from Operation Management?", "Projects are time-bound initiatives; Operation Management focuses on recurring operational workflows."),
        ],
    },
    {
        "slug": "erp-employee-self-service",
        "title": "Employee Self Service",
        "eyebrow": "AIBizs ERP",
        "hero_title": "Employee Self-Service Inside the Enterprise",
        "hero_text": "Give employees a secure portal for profiles, requests, and HR-related services connected to ERP — reducing admin load while keeping workforce data accurate.",
        "description": "AIBizs ERP Employee Self Service provides a secure portal for profiles, requests, and workforce self-service connected to enterprise HR data.",
        "icon": "bi-person-badge",
        "image": "assets/img/erpimage/ess-hero.png",
        "image_alt": "Employee self-service ERP portal",
        "trust_line": "Fewer admin tickets. Faster employee requests. Accurate workforce data.",
        "solutions": [
            {
                "title": "Employee Portal",
                "text": "A clear self-service workspace where employees view profiles, submit requests, and access permitted documents without waiting on email chains.",
                "bullets": [
                    "Personal profile visibility",
                    "Request submission and tracking",
                    "Document access with permissions",
                    "Mobile-responsive experience",
                ],
                "image": "assets/img/erpimage/ess-hero.png",
                "image_alt": "Employee self-service portal home",
            },
            {
                "title": "Requests & Approvals",
                "text": "Route employee requests to managers and HR with status tracking — so nothing gets lost between inbox folders.",
                "bullets": [
                    "Structured request forms",
                    "Manager and HR approval queues",
                    "Status notifications",
                    "Full request history",
                ],
                "image": "assets/img/erpimage/ess-portal.png",
                "image_alt": "ESS requests and approval queues",
                "reverse": True,
            },
            {
                "title": "Secure Workforce Self-Service",
                "text": "Role-based access keeps employee, manager, and HR views separated while syncing approved changes back into ERP HR records.",
                "bullets": [
                    "Role-based data protection",
                    "Approved changes sync to HR",
                    "Multi-company access isolation",
                    "Reduced routine HR admin",
                ],
                "image": "assets/img/erpimage/ess-requests.png",
                "image_alt": "Secure ESS requests and profile updates",
            },
        ],
        "process": [
            ("Sign In", "Employees access ESS with role-based credentials."),
            ("Self-Serve", "Update permitted details and submit requests."),
            ("Approve", "Managers and HR clear queues with audit trails."),
            ("Sync", "Approved changes update ERP workforce records."),
        ],
        "capabilities": [
            ("bi-person-vcard", "Profile hub"),
            ("bi-chat-dots", "Request tracking"),
            ("bi-check2-square", "Approvals"),
            ("bi-folder2-open", "Documents"),
            ("bi-bell", "Notifications"),
            ("bi-phone", "Mobile-ready UI"),
            ("bi-shield-lock", "Privacy controls"),
            ("bi-link-45deg", "HR data sync"),
        ],
        "faqs": [
            ("Does ESS reduce HR tickets?", "Yes. Routine profile and request tasks move to self-service so HR focuses on higher-value work."),
            ("Can managers approve in ESS?", "Yes. Selected requests route to manager and HR queues with status tracking."),
            ("Is ESS connected to ERP HR?", "Yes. Approved changes sync into human resource management records."),
            ("Is it available on mobile devices?", "Yes. The portal is responsive for office and field employees."),
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
              <div id="faq-{i}" class="accordion-collapse collapse{show}" data-bs-parent="#erpFaq">
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
  <title>{esc(m['title'])} | AIBizs ERP</title>
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
          <a href="product-erp.html">ERP</a>
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
              <a href="product-erp.html" class="hrms-btn-ghost">Explore ERP</a>
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
            <div class="accordion hrms-faq-accordion" id="erpFaq" data-aos="fade-up" data-aos-delay="100">
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
            <p>Speak with our team about configuring AIBizs ERP for your organization in Oman and the GCC.</p>
          </div>
          <div class="hrms-product-cta-group">
            <a href="index.html#contact" class="btn-primary">Book a Discovery Call</a>
            <a href="product-erp.html" class="hrms-btn-ghost">Back to ERP</a>
          </div>
        </div>
      </div>
    </section>

    <section class="hrms-product-related section">
      <div class="container">
        <div class="section-title text-center" data-aos="fade-up">
          <h2>More ERP Modules</h2>
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
            <li><a href="product-erp.html">ERP</a></li>
            <li><a href="index.html#products">Our Products</a></li>
            <li><a href="index.html#contact">Contact</a></li>
          </ul>
        </div>
        <div class="col-lg-2 col-6 footer-links">
          <h4>ERP Modules</h4>
          <ul>
            <li><a href="erp-finance.html">Finance</a></li>
            <li><a href="erp-inventory-management.html">Inventory</a></li>
            <li><a href="erp-crm.html">CRM</a></li>
            <li><a href="erp-manufacturing.html">Manufacturing</a></li>
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
