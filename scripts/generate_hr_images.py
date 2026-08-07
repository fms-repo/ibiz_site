#!/usr/bin/env python3
"""Generate AIVizion-themed HRMS dashboard mockup images.

WARNING: Running this script overwrites files in assets/img/hrimage/.
Only use when intentionally regenerating mockups from scratch.
Prefer keeping curated/high-quality images already in that folder.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "img" / "hrimage"

# AIBizs brand
BG = (3, 17, 25)
SURFACE = (27, 38, 44)
SURFACE2 = (22, 38, 47)
ACCENT = (0, 156, 220)
PRIMARY = (0, 108, 135)
HEADING = (224, 233, 242)
TEXT = (180, 198, 210)
MUTED = (110, 130, 145)
WHITE = (255, 255, 255)
SUCCESS = (46, 196, 146)
WARN = (240, 180, 41)
DANGER = (235, 87, 87)
CARD_BORDER = (40, 70, 85)

W, H = 1280, 800


def font(size: int, bold: bool = False):
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


F_TITLE = font(28, True)
F_H = font(20, True)
F_H2 = font(16, True)
F_BODY = font(14)
F_SMALL = font(12)
F_TINY = font(11)


def rr(draw, box, radius, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, value, fnt=F_BODY, fill=TEXT):
    draw.text(xy, value, font=fnt, fill=fill)


def chrome(draw, title: str, subtitle: str):
    # App shell
    rr(draw, (24, 24, W - 24, H - 24), 22, fill=SURFACE, outline=CARD_BORDER, width=2)
    # Sidebar
    rr(draw, (24, 24, 250, H - 24), 22, fill=(16, 28, 34))
    draw.rectangle((210, 24, 250, H - 24), fill=(16, 28, 34))
    text(draw, (48, 48), "AIVizion HRMS", F_H2, ACCENT)
    text(draw, (48, 74), title, F_SMALL, MUTED)

    nav = [
        ("Overview", False),
        (subtitle, True),
        ("Employees", False),
        ("Reports", False),
        ("Settings", False),
    ]
    y = 120
    for label, active in nav:
        if active:
            rr(draw, (40, y - 8, 230, y + 28), 10, fill=(0, 108, 135, 80) if False else PRIMARY)
            text(draw, (56, y), label, F_BODY, WHITE)
        else:
            text(draw, (56, y), label, F_BODY, MUTED)
        y += 46

    # Top bar
    text(draw, (280, 48), title, F_TITLE, HEADING)
    text(draw, (280, 84), subtitle, F_BODY, MUTED)
    rr(draw, (W - 220, 48, W - 48, 88), 10, fill=PRIMARY)
    text(draw, (W - 188, 58), "Run Action", F_BODY, WHITE)


def kpi_card(draw, x, y, w, h, label, value, delta, good=True):
    rr(draw, (x, y, x + w, y + h), 14, fill=SURFACE2, outline=CARD_BORDER)
    text(draw, (x + 18, y + 16), label, F_SMALL, MUTED)
    text(draw, (x + 18, y + 42), value, F_H, HEADING)
    text(draw, (x + 18, y + 72), delta, F_TINY, SUCCESS if good else WARN)


def bar_chart(draw, x, y, w, h, values, color=ACCENT):
    rr(draw, (x, y, x + w, y + h), 14, fill=SURFACE2, outline=CARD_BORDER)
    text(draw, (x + 18, y + 14), "Trend", F_SMALL, MUTED)
    max_v = max(values) or 1
    bx = x + 24
    by = y + h - 28
    bw = (w - 60) // len(values)
    for i, v in enumerate(values):
        bh = int((v / max_v) * (h - 70))
        rr(draw, (bx + i * bw, by - bh, bx + i * bw + bw - 10, by), 6, fill=color if i % 2 == 0 else PRIMARY)


def table(draw, x, y, w, h, headers, rows):
    rr(draw, (x, y, x + w, y + h), 14, fill=SURFACE2, outline=CARD_BORDER)
    col_w = (w - 36) // len(headers)
    tx = x + 18
    ty = y + 16
    for i, hdg in enumerate(headers):
        text(draw, (tx + i * col_w, ty), hdg, F_TINY, MUTED)
    draw.line((x + 14, y + 40, x + w - 14, y + 40), fill=CARD_BORDER, width=1)
    ry = y + 54
    for row in rows:
        for i, cell in enumerate(row):
            fill = HEADING if i == 0 else TEXT
            text(draw, (tx + i * col_w, ry), cell, F_SMALL, fill)
        ry += 34


def pills(draw, x, y, items):
    cx = x
    for label, color in items:
        tw = 12 + len(label) * 7
        rr(draw, (cx, y, cx + tw, y + 26), 13, fill=color)
        text(draw, (cx + 10, y + 5), label, F_TINY, WHITE)
        cx += tw + 10


def list_cards(draw, x, y, w, items):
    cy = y
    for title, meta, status, color in items:
        rr(draw, (x, cy, x + w, cy + 64), 12, fill=SURFACE2, outline=CARD_BORDER)
        text(draw, (x + 16, cy + 14), title, F_BODY, HEADING)
        text(draw, (x + 16, cy + 36), meta, F_TINY, MUTED)
        tw = 12 + len(status) * 7
        rr(draw, (x + w - tw - 16, cy + 18, x + w - 16, cy + 42), 12, fill=color)
        text(draw, (x + w - tw - 6, cy + 23), status, F_TINY, WHITE)
        cy += 76


def save(img: Image.Image, name: str):
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    img.save(path, "PNG", optimize=True)
    print(f"Wrote {path.relative_to(ROOT)}")


def base(title: str, subtitle: str):
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)
    # soft glow
    for i in range(6):
        alpha_box = (900 - i * 20, 40 + i * 10, 1260, 280)
        # approximate glow with darker teal circles via rectangles
    rr(draw, (0, 0, W, H), 0, fill=BG)
    # subtle accent orb
    draw.ellipse((980, -40, 1380, 360), fill=(0, 60, 80))
    draw.ellipse((-120, 520, 280, 920), fill=(0, 40, 55))
    chrome(draw, title, subtitle)
    return img, draw


def make_payroll():
    # Hero
    img, d = base("Payroll", "Cycle Dashboard")
    kpi_card(d, 280, 120, 220, 100, "Employees Paid", "1,248", "+36 this cycle")
    kpi_card(d, 520, 120, 220, 100, "Net Payable", "OMR 486K", "On schedule")
    kpi_card(d, 760, 120, 220, 100, "Exceptions", "12", "Needs review", good=False)
    kpi_card(d, 1000, 120, 200, 100, "Approved", "94%", "Ready to disburse")
    bar_chart(d, 280, 250, 460, 240, [40, 55, 48, 70, 62, 80, 75], ACCENT)
    table(
        d,
        760,
        250,
        440,
        240,
        ["Employee", "Dept", "Net", "Status"],
        [
            ["Sara Al Lawati", "Finance", "1,240", "Ready"],
            ["Omar Al Balushi", "Ops", "980", "Ready"],
            ["Layla Hassan", "HR", "1,105", "Hold"],
            ["Yousuf R.", "IT", "1,320", "Ready"],
            ["Huda K.", "Sales", "915", "Ready"],
        ],
    )
    list_cards(
        d,
        280,
        520,
        920,
        [
            ("March 2026 Payroll Run", "Gross-to-net completed · bank file pending", "In Review", WARN),
            ("Social Insurance Export", "Statutory contribution file generated", "Done", SUCCESS),
        ],
    )
    save(img, "payroll-hero.png")

    img, d = base("Payroll", "Salary Engine")
    text(d, (280, 120), "Pay Elements Configuration", F_H, HEADING)
    pills(d, 280, 160, [("Basic", PRIMARY), ("Housing", ACCENT), ("Transport", PRIMARY), ("Overtime", SUCCESS), ("Loan Deduction", DANGER)])
    table(
        d,
        280,
        210,
        920,
        320,
        ["Component", "Type", "Calc", "Taxable", "Active"],
        [
            ["Basic Salary", "Earning", "Fixed", "Yes", "Yes"],
            ["Housing Allowance", "Earning", "% of Basic", "Yes", "Yes"],
            ["Transport", "Earning", "Fixed", "No", "Yes"],
            ["Overtime 1.25x", "Earning", "Hourly", "Yes", "Yes"],
            ["Social Insurance", "Deduction", "Formula", "—", "Yes"],
            ["Loan Recovery", "Deduction", "Installment", "—", "Yes"],
        ],
    )
    kpi_card(d, 280, 560, 300, 100, "Pay Structures", "18", "Across 3 companies")
    kpi_card(d, 600, 560, 300, 100, "Auto Validations", "27", "Exception rules active")
    kpi_card(d, 920, 560, 280, 100, "Last Calc Time", "2.4 min", "1,248 employees")
    save(img, "payroll-cloud.png")

    img, d = base("Payroll", "HR Integration")
    text(d, (280, 120), "Inputs synced from HRMS", F_H, HEADING)
    list_cards(
        d,
        280,
        170,
        450,
        [
            ("Leave Deductions", "14 unpaid leave days this period", "Synced", SUCCESS),
            ("Overtime Entries", "326 hours from attendance", "Synced", SUCCESS),
            ("New Joiners", "8 employees payroll-ready", "Synced", SUCCESS),
            ("Loan Updates", "3 schedules adjusted", "Synced", SUCCESS),
        ],
    )
    bar_chart(d, 760, 170, 440, 280, [30, 45, 38, 60, 52, 70], PRIMARY)
    text(d, (780, 470), "Source of truth: one employee record", F_BODY, TEXT)
    table(
        d,
        760,
        510,
        440,
        160,
        ["Module", "Records", "Impact"],
        [
            ["Leave", "86", "Unpaid / balances"],
            ["Attendance", "1,248", "OT & absences"],
            ["ESS", "412", "Profile & bank"],
        ],
    )
    save(img, "payroll-integrated.png")

    img, d = base("Payroll", "Compliance")
    kpi_card(d, 280, 120, 300, 100, "Audit Trail Events", "4,812", "This cycle")
    kpi_card(d, 600, 120, 300, 100, "Approvals Complete", "3 / 3", "Finance signed off")
    kpi_card(d, 920, 120, 280, 100, "Statutory Files", "Ready", "Export available")
    table(
        d,
        280,
        250,
        920,
        300,
        ["Control", "Owner", "Status", "Timestamp"],
        [
            ["Payroll calculation lock", "HR Admin", "Passed", "06 Apr 09:12"],
            ["Exception review", "Payroll Lead", "Passed", "06 Apr 10:04"],
            ["Finance approval", "CFO Desk", "Passed", "06 Apr 11:20"],
            ["Bank file checksum", "System", "Passed", "06 Apr 11:22"],
            ["Social insurance export", "System", "Passed", "06 Apr 11:25"],
            ["Cycle archive", "System", "Queued", "—"],
        ],
    )
    pills(d, 280, 580, [("ISO-aligned logging", PRIMARY), ("Role-based access", ACCENT), ("Immutable history", SUCCESS)])
    save(img, "payroll-compliance.png")


def make_ess():
    img, d = base("Self Service", "My Workplace")
    kpi_card(d, 280, 120, 220, 100, "Leave Balance", "14 days", "Annual leave")
    kpi_card(d, 520, 120, 220, 100, "Payslips", "12", "Available to download")
    kpi_card(d, 760, 120, 220, 100, "Open Requests", "2", "In approval")
    kpi_card(d, 1000, 120, 200, 100, "Documents", "8", "HR letters")
    list_cards(
        d,
        280,
        250,
        920,
        [
            ("Payslip · March 2026", "Net OMR 1,180 · issued 01 Apr", "Download", ACCENT),
            ("Profile update · Mobile number", "Submitted to HR for verification", "Pending", WARN),
            ("Leave request · 22–24 Apr", "Manager: Fatma Al Zadjali", "In Review", WARN),
        ],
    )
    save(img, "ess-hero.png")

    img, d = base("Self Service", "Employee Portal")
    text(d, (280, 120), "Quick actions", F_H, HEADING)
    pills(d, 280, 160, [("View payslip", ACCENT), ("Request leave", PRIMARY), ("Update bank", PRIMARY), ("Documents", SUCCESS)])
    table(
        d,
        280,
        220,
        920,
        340,
        ["Item", "Category", "Updated", "Action"],
        [
            ["Personal email", "Profile", "Today", "Edit"],
            ["Emergency contact", "Profile", "2 days ago", "Edit"],
            ["Bank IBAN", "Payroll", "Verified", "View"],
            ["Employment contract", "Documents", "On file", "Download"],
            ["Policy handbook", "Documents", "2026", "Download"],
            ["Tax / SI letter", "Documents", "Mar 2026", "Download"],
        ],
    )
    save(img, "ess-portal.png")

    img, d = base("Self Service", "Approvals")
    text(d, (280, 120), "Manager approval inbox", F_H, HEADING)
    list_cards(
        d,
        280,
        170,
        920,
        [
            ("Annual leave · Ahmed Al Hinai", "3 days · team coverage OK", "Approve", SUCCESS),
            ("Profile change · Bank details", "Requires HR verification after approve", "Review", WARN),
            ("Sick leave · Noor Al Lawati", "Attachment included", "Approve", SUCCESS),
            ("Shift swap · Ops team", "Conflicts with planned leave", "Hold", DANGER),
        ],
    )
    save(img, "ess-approvals.png")

    img, d = base("Self Service", "Security")
    kpi_card(d, 280, 120, 300, 100, "Access Role", "Employee", "Least privilege")
    kpi_card(d, 600, 120, 300, 100, "Visible Records", "Own only", "Privacy enforced")
    kpi_card(d, 920, 120, 280, 100, "Session", "Protected", "SSO ready")
    table(
        d,
        280,
        250,
        920,
        280,
        ["Permission", "Employee", "Manager", "HR"],
        [
            ["Own payslips", "Yes", "Yes", "Yes"],
            ["Team leave calendar", "No", "Yes", "Yes"],
            ["Salary structures", "No", "No", "Yes"],
            ["Company documents", "Assigned", "Assigned", "All"],
            ["Approval queues", "No", "Yes", "Yes"],
        ],
    )
    save(img, "ess-secure.png")


def make_leave():
    img, d = base("Leave", "Absence Hub")
    kpi_card(d, 280, 120, 220, 100, "Pending Approvals", "18", "Across teams")
    kpi_card(d, 520, 120, 220, 100, "On Leave Today", "42", "3.4% of workforce")
    kpi_card(d, 760, 120, 220, 100, "Avg Balance", "11.6d", "Annual leave")
    kpi_card(d, 1000, 120, 200, 100, "Policy Breaches", "0", "Blocked at request")
    # calendar-like grid
    rr(d, (280, 250, 700, 620), 14, fill=SURFACE2, outline=CARD_BORDER)
    text(d, (300, 270), "Team Calendar · April", F_H2, HEADING)
    days = ["M", "T", "W", "T", "F", "S", "S"]
    for i, day in enumerate(days):
        text(d, (320 + i * 55, 310), day, F_TINY, MUTED)
    for r in range(4):
        for c in range(7):
            x0 = 310 + c * 55
            y0 = 340 + r * 60
            fill = SURFACE
            if (r, c) in {(1, 2), (1, 3), (2, 4)}:
                fill = PRIMARY
            if (r, c) in {(0, 5), (3, 1)}:
                fill = ACCENT
            rr(d, (x0, y0, x0 + 44, y0 + 44), 8, fill=fill)
    list_cards(
        d,
        720,
        250,
        480,
        [
            ("Annual · Sara", "22–24 Apr · Finance", "Pending", WARN),
            ("Sick · Omar", "06 Apr · Operations", "Approved", SUCCESS),
            ("Unpaid · Huda", "15 Apr · Sales", "Policy OK", ACCENT),
        ],
    )
    save(img, "leave-hero.png")

    img, d = base("Leave", "Policies")
    table(
        d,
        280,
        120,
        920,
        360,
        ["Leave Type", "Accrual", "Carry Forward", "Approval"],
        [
            ["Annual", "2.5 / month", "5 days max", "Manager"],
            ["Sick", "As incurred", "None", "Manager + doc"],
            ["Unpaid", "Request based", "None", "Manager + HR"],
            ["Maternity", "Policy pack", "N/A", "HR"],
            ["Hajj / Special", "Eligibility rules", "None", "HR"],
        ],
    )
    pills(d, 280, 520, [("Blackout dates", WARN), ("Negative balance blocked", DANGER), ("Auto accrual", SUCCESS)])
    save(img, "leave-policy.png")

    img, d = base("Leave", "Approvals & Planning")
    list_cards(
        d,
        280,
        120,
        920,
        [
            ("Coverage conflict detected", "2 analysts already off in same week", "Alert", WARN),
            ("Delegation active", "Manager on leave · backup approver set", "Active", ACCENT),
            ("Medical certificate required", "Sick leave > 2 days rule", "Attached", SUCCESS),
            ("Team heatmap", "Ops peak week · limit new annual leave", "Guidance", PRIMARY),
        ],
    )
    save(img, "leave-calendar.png")

    img, d = base("Leave", "Payroll Sync")
    kpi_card(d, 280, 120, 300, 100, "Unpaid Days", "27", "Ready for payroll")
    kpi_card(d, 600, 120, 300, 100, "Balance Updates", "Instant", "On approval")
    kpi_card(d, 920, 120, 280, 100, "Export Status", "Synced", "March cycle")
    bar_chart(d, 280, 250, 920, 300, [20, 35, 28, 44, 30, 50, 38], ACCENT)
    save(img, "leave-payroll.png")


def make_onboarding():
    img, d = base("Onboarding", "New Hire Journey")
    kpi_card(d, 280, 120, 220, 100, "Active Plans", "16", "Pre-joining + day-one")
    kpi_card(d, 520, 120, 220, 100, "Completion", "78%", "Average progress")
    kpi_card(d, 760, 120, 220, 100, "Blocked", "3", "Docs pending")
    kpi_card(d, 1000, 120, 200, 100, "Starts This Week", "5", "Ready track")
    list_cards(
        d,
        280,
        250,
        920,
        [
            ("Maha Al Busaidi · Analyst", "HR docs done · IT access pending", "68%", WARN),
            ("Khalid Al Farsi · Engineer", "Contract signed · assets assigned", "92%", SUCCESS),
            ("Raya N. · Sales", "Awaiting bank details", "41%", DANGER),
        ],
    )
    save(img, "onboarding-hero.png")

    img, d = base("Onboarding", "Checklists")
    table(
        d,
        280,
        120,
        920,
        400,
        ["Task", "Owner", "Due", "Status"],
        [
            ["Send offer pack", "HR", "D-7", "Done"],
            ["Collect ID & certificates", "HR", "D-3", "Done"],
            ["Create email & systems", "IT", "D-1", "In progress"],
            ["Assign laptop & badge", "Facilities", "Day 1", "Queued"],
            ["Induction session", "Manager", "Day 2", "Scheduled"],
            ["Probation goals setup", "Manager", "Week 1", "Queued"],
        ],
    )
    save(img, "onboarding-journey.png")

    img, d = base("Onboarding", "Documents")
    list_cards(
        d,
        280,
        120,
        920,
        [
            ("National ID / Passport", "Uploaded · verified by HR", "Verified", SUCCESS),
            ("Signed employment contract", "E-sign complete", "Verified", SUCCESS),
            ("Bank IBAN confirmation", "Waiting on employee", "Pending", WARN),
            ("Educational certificates", "Uploaded · under review", "Review", ACCENT),
        ],
    )
    save(img, "onboarding-docs.png")

    img, d = base("Onboarding", "Access & Probation")
    kpi_card(d, 280, 120, 300, 100, "Systems Provisioned", "84%", "On track")
    kpi_card(d, 600, 120, 300, 100, "Assets Assigned", "12 / 16", "Devices + badges")
    kpi_card(d, 920, 120, 280, 100, "Probation Reviews", "7 due", "Next 30 days")
    bar_chart(d, 280, 250, 920, 300, [25, 40, 55, 70, 68, 82, 90], PRIMARY)
    save(img, "onboarding-access.png")


def make_offboarding():
    img, d = base("Offboarding", "Exit Control")
    kpi_card(d, 280, 120, 220, 100, "Open Exits", "9", "This month")
    kpi_card(d, 520, 120, 220, 100, "Clearances Due", "4", "Before LWD")
    kpi_card(d, 760, 120, 220, 100, "Assets Pending", "6", "Devices/badges")
    kpi_card(d, 1000, 120, 200, 100, "Settlements", "3", "Ready to pay")
    list_cards(
        d,
        280,
        250,
        920,
        [
            ("Resignation · Nasser Al Habsi", "LWD 30 Apr · IT + Finance pending", "In Progress", WARN),
            ("Contract end · Contractor A", "Access revoked · settlement posted", "Closed", SUCCESS),
            ("Termination · Case # thr-14", "Legal hold · restricted archive", "Controlled", DANGER),
        ],
    )
    save(img, "offboarding-hero.png")

    img, d = base("Offboarding", "Clearance Workflow")
    table(
        d,
        280,
        120,
        920,
        360,
        ["Department", "Task", "Owner", "Status"],
        [
            ["IT", "Disable accounts & MFA", "IT Ops", "Pending"],
            ["Facilities", "Collect badge & access card", "Admin", "Done"],
            ["Finance", "Confirm loans & advances", "Payroll", "Pending"],
            ["Manager", "Knowledge handover notes", "Line Mgr", "Done"],
            ["HR", "Exit interview", "HRBP", "Scheduled"],
        ],
    )
    save(img, "offboarding-workflow.png")

    img, d = base("Offboarding", "Assets & Access")
    list_cards(
        d,
        280,
        120,
        920,
        [
            ("MacBook Pro 14", "Asset tag NB-2041", "Returned", SUCCESS),
            ("Mobile + SIM", "Asset tag PH-889", "Pending", WARN),
            ("Building access", "Door group HQ-A", "Revoked", SUCCESS),
            ("Email & SaaS apps", "Mailbox retention 30 days", "Revoked", SUCCESS),
        ],
    )
    save(img, "offboarding-assets.png")

    img, d = base("Offboarding", "Final Settlement")
    kpi_card(d, 280, 120, 300, 100, "Leave Encashment", "OMR 640", "8 days")
    kpi_card(d, 600, 120, 300, 100, "Loan Balance", "OMR 120", "Final deduction")
    kpi_card(d, 920, 120, 280, 100, "Net Settlement", "OMR 2,180", "Payroll linked")
    table(
        d,
        280,
        250,
        920,
        280,
        ["Component", "Amount", "Notes"],
        [
            ["Salary till LWD", "1,660", "Prorated"],
            ["Leave encashment", "640", "Annual balance"],
            ["Loan recovery", "-120", "Final installment"],
            ["Net payable", "2,180", "Bank file ready"],
        ],
    )
    save(img, "offboarding-settlement.png")


def make_appraisal():
    img, d = base("Appraisal", "Performance Cycle")
    kpi_card(d, 280, 120, 220, 100, "Cycle Progress", "72%", "FY2026 H1")
    kpi_card(d, 520, 120, 220, 100, "Goals Set", "1,102", "Employee + manager")
    kpi_card(d, 760, 120, 220, 100, "Reviews Due", "186", "This week")
    kpi_card(d, 1000, 120, 200, 100, "Calibrated", "41%", "Leadership")
    bar_chart(d, 280, 250, 520, 300, [12, 18, 30, 28, 22, 14, 8], ACCENT)
    table(
        d,
        820,
        250,
        380,
        300,
        ["Rating", "Count", "%"],
        [
            ["Exceeds", "148", "14%"],
            ["Meets", "690", "64%"],
            ["Develop", "180", "17%"],
            ["Below", "54", "5%"],
        ],
    )
    save(img, "appraisal-hero.png")

    img, d = base("Appraisal", "Goals & KPIs")
    list_cards(
        d,
        280,
        120,
        920,
        [
            ("Increase collections efficiency", "Weight 30% · Finance · On track", "82%", SUCCESS),
            ("Reduce average ticket time", "Weight 25% · Support · At risk", "54%", WARN),
            ("Deliver Q2 product release", "Weight 25% · Product · On track", "76%", SUCCESS),
            ("Complete compliance training", "Weight 20% · All staff · Done", "100%", ACCENT),
        ],
    )
    save(img, "appraisal-goals.png")

    img, d = base("Appraisal", "Reviews & Calibration")
    table(
        d,
        280,
        120,
        920,
        360,
        ["Employee", "Self", "Manager", "Final"],
        [
            ["Aisha Al R.", "Exceeds", "Meets", "Pending"],
            ["Hassan M.", "Meets", "Meets", "Meets"],
            ["Noor S.", "Meets", "Develop", "Calibrating"],
            ["Yahya T.", "Exceeds", "Exceeds", "Exceeds"],
            ["Lina P.", "Develop", "Develop", "PIP linked"],
        ],
    )
    pills(d, 280, 520, [("360 optional", PRIMARY), ("Bias checks", WARN), ("Fair distribution", SUCCESS)])
    save(img, "appraisal-reviews.png")

    img, d = base("Appraisal", "Outcomes")
    kpi_card(d, 280, 120, 300, 100, "Development Plans", "214", "Created this cycle")
    kpi_card(d, 600, 120, 300, 100, "Promotion Cases", "27", "In HR review")
    kpi_card(d, 920, 120, 280, 100, "Training Needs", "63", "Skills mapped")
    list_cards(
        d,
        280,
        250,
        920,
        [
            ("Leadership track nomination", "Linked from exceeds rating", "Submitted", ACCENT),
            ("Technical upskilling plan", "Cloud + security modules", "Active", SUCCESS),
            ("Performance improvement plan", "30/60/90 milestones", "Monitoring", WARN),
        ],
    )
    save(img, "appraisal-actions.png")


def make_recruitment():
    img, d = base("Recruitment", "Talent Pipeline")
    kpi_card(d, 280, 120, 220, 100, "Open Roles", "23", "Approved requisitions")
    kpi_card(d, 520, 120, 220, 100, "Candidates", "318", "Active in pipeline")
    kpi_card(d, 760, 120, 220, 100, "Interviews", "41", "This week")
    kpi_card(d, 1000, 120, 200, 100, "Time to Hire", "28d", "Rolling avg")
    # kanban columns
    stages = [
        ("Applied", ["UI Designer", "ERP Analyst", "Sales Lead"]),
        ("Screen", ["DevOps Eng.", "HRBP"]),
        ("Interview", ["Finance Mgr", "QA Lead"]),
        ("Offer", ["Data Eng."]),
    ]
    x = 280
    for title, cards in stages:
        rr(d, (x, 250, x + 220, 620), 14, fill=SURFACE2, outline=CARD_BORDER)
        text(d, (x + 16, 270), title, F_H2, HEADING)
        cy = 320
        for c in cards:
            rr(d, (x + 14, cy, x + 206, cy + 58), 10, fill=SURFACE)
            text(d, (x + 26, cy + 18), c, F_SMALL, TEXT)
            cy += 70
        x += 235
    save(img, "recruitment-hero.png")

    img, d = base("Recruitment", "Requisitions")
    table(
        d,
        280,
        120,
        920,
        360,
        ["Role", "Dept", "Headcount", "Status"],
        [
            ["Senior ERP Consultant", "Delivery", "2", "Approved"],
            ["Payroll Specialist", "HR", "1", "Open"],
            ["Cloud Engineer", "IT", "1", "Interviewing"],
            ["Sales Executive", "Commercial", "3", "Sourcing"],
            ["QHSE Officer", "Operations", "1", "Offer"],
        ],
    )
    save(img, "recruitment-requisition.png")

    img, d = base("Recruitment", "Interviews & Scorecards")
    list_cards(
        d,
        280,
        120,
        920,
        [
            ("Panel interview · Cloud Engineer", "Score 4.2 / 5 · technical strong", "Advance", SUCCESS),
            ("HR screen · Sales Executive", "Culture fit pending second call", "Schedule", WARN),
            ("Case study · ERP Consultant", "Business scenario completed", "Score", ACCENT),
            ("AI shortlist assist", "18 CVs ranked for QA Lead", "Review", PRIMARY),
        ],
    )
    save(img, "recruitment-pipeline.png")

    img, d = base("Recruitment", "Offers & Handoff")
    kpi_card(d, 280, 120, 300, 100, "Offers Sent", "11", "This month")
    kpi_card(d, 600, 120, 300, 100, "Accepted", "7", "64% accept rate")
    kpi_card(d, 920, 120, 280, 100, "To Onboarding", "7", "Auto handoff")
    table(
        d,
        280,
        250,
        920,
        280,
        ["Candidate", "Role", "Offer", "Next"],
        [
            ["Amira S.", "Data Eng.", "Accepted", "Onboarding plan"],
            ["Faisal K.", "HRBP", "Sent", "Awaiting reply"],
            ["Julia R.", "QA Lead", "Accepted", "Day-one checklist"],
            ["Omar B.", "Sales", "Declined", "Pipeline reopen"],
        ],
    )
    save(img, "recruitment-offers.png")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    make_payroll()
    make_ess()
    make_leave()
    make_onboarding()
    make_offboarding()
    make_appraisal()
    make_recruitment()
    print(f"Done. Images in {OUT}")


if __name__ == "__main__":
    main()
