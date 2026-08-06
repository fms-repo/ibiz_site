#!/usr/bin/env python3
"""Generate a presentable, shareable AIVizion HRMS brochure webpage."""

from __future__ import annotations

import html
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

spec = importlib.util.spec_from_file_location(
    "hrms_modules", ROOT / "scripts" / "generate_hrms_module_pages.py"
)
hrms_modules = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hrms_modules)
MODULES = hrms_modules.MODULES


def esc(text: str) -> str:
    return html.escape(text, quote=True)


def nav_items():
    items = [
        ('href="#overview"', "Overview"),
    ]
    for m in MODULES:
        items.append((f'href="#{esc(m["slug"])}"', esc(m["title"])))
    items.append(('href="#platform"', "Platform"))
    items.append(('href="#contact-cta"', "Contact"))
    return "\n".join(
        f'            <a class="hrms-brochure-nav-link" {href}>{label}</a>'
        for href, label in items
    )


def module_nav_pills():
    pills = []
    for m in MODULES:
        pills.append(
            f"""          <a class="hrms-brochure-pill" href="#{esc(m['slug'])}">
            <i class="bi {esc(m['icon'])}"></i>
            <span>{esc(m['title'])}</span>
          </a>"""
        )
    return "\n".join(pills)


def solution_grid(solutions):
    cards = []
    for s in solutions:
        bullets = "\n".join(
            f'                  <li><i class="bi bi-check2-circle"></i><span>{esc(b)}</span></li>'
            for b in s["bullets"]
        )
        cards.append(
            f"""            <div class="col-lg-4">
              <article class="hrms-brochure-solution-card">
                <div class="hrms-brochure-solution-media">
                  <img src="{esc(s['image'])}" alt="{esc(s['image_alt'])}" loading="lazy">
                </div>
                <div class="hrms-brochure-solution-body">
                  <h4>{esc(s['title'])}</h4>
                  <p>{esc(s['text'])}</p>
                  <ul>
{bullets}
                  </ul>
                </div>
              </article>
            </div>"""
        )
    return "\n".join(cards)


def process_row(steps):
    items = []
    for i, (title, desc) in enumerate(steps, start=1):
        items.append(
            f"""            <div class="col-md-6 col-xl-3">
              <div class="hrms-brochure-step">
                <span>{i:02d}</span>
                <h5>{esc(title)}</h5>
                <p>{esc(desc)}</p>
              </div>
            </div>"""
        )
    return "\n".join(items)


def capability_chips(capabilities):
    return "\n".join(
        f'              <li><i class="bi {esc(icon)}"></i><span>{esc(label)}</span></li>'
        for icon, label in capabilities
    )


def module_sections():
    sections = []
    for idx, m in enumerate(MODULES, start=1):
        tone = "light-background" if idx % 2 == 0 else ""
        sections.append(
            f"""    <section class="hrms-brochure-module section {tone}" id="{esc(m['slug'])}">
      <div class="container">
        <div class="hrms-brochure-module-head">
          <div class="row gy-4 align-items-center">
            <div class="col-lg-6" data-aos="fade-up">
              <p class="hrms-brochure-kicker"><i class="bi {esc(m['icon'])}"></i> Module {idx:02d}</p>
              <h2>{esc(m['title'])}</h2>
              <p class="hrms-brochure-lead">{esc(m['hero_text'])}</p>
              <p class="hrms-brochure-trust">{esc(m['trust_line'])}</p>
              <a class="hrms-brochure-inline-link" href="{esc(m['slug'])}.html">Open full module page <i class="bi bi-arrow-up-right"></i></a>
            </div>
            <div class="col-lg-6" data-aos="fade-left">
              <div class="hrms-brochure-hero-shot">
                <img src="{esc(m['image'])}" alt="{esc(m['image_alt'])}" loading="lazy">
              </div>
            </div>
          </div>
        </div>

        <div class="row g-4 hrms-brochure-solution-grid">
{solution_grid(m['solutions'])}
        </div>

        <div class="hrms-brochure-process">
          <h3>End-to-end process</h3>
          <div class="row g-3">
{process_row(m['process'])}
          </div>
        </div>

        <ul class="hrms-brochure-caps">
{capability_chips(m['capabilities'])}
        </ul>
      </div>
    </section>"""
        )
    return "\n\n".join(sections)


def render():
    return f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <title>AIVizion HRMS Brochure | Complete Human Resource Platform</title>
  <meta name="description" content="Presentable AIVizion HRMS brochure covering Payroll, Leave, Recruitment, Onboarding, Offboarding, Appraisal, and Employee Self Service for Oman and the GCC.">
  <meta name="author" content="AIBizs">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://aibizs.com/hrms-brochure.html">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="AIBizs">
  <meta property="og:title" content="AIVizion HRMS Brochure — Complete People Platform">
  <meta property="og:description" content="A shareable overview of AIVizion HRMS modules, dashboards, and end-to-end HR processes for Oman and the GCC.">
  <meta property="og:url" content="https://aibizs.com/hrms-brochure.html">
  <meta property="og:image" content="https://aibizs.com/assets/img/hrimage/payroll-hero.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="AIVizion HRMS Brochure">
  <meta name="twitter:description" content="Complete HRMS brochure with modules, dashboards, and process flows.">
  <meta name="twitter:image" content="https://aibizs.com/assets/img/hrimage/payroll-hero.png">

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

<body class="hrms-brochure-page">

  <header class="hrms-brochure-topbar">
    <div class="container-xl hrms-brochure-topbar-inner">
      <a href="index.html" class="hrms-brochure-brand">
        <span class="sitename">AIVizion</span>
        <small>HRMS Brochure</small>
      </a>
      <nav class="hrms-brochure-nav" aria-label="Brochure sections">
{nav_items()}
      </nav>
      <div class="hrms-brochure-top-actions">
        <button type="button" class="hrms-brochure-share" id="hrmsBrochureShare" aria-label="Copy brochure link">
          <i class="bi bi-link-45deg"></i> <span>Copy link</span>
        </button>
        <a class="btn-primary hrms-brochure-contact-btn" href="index.html#contact">Talk to us</a>
      </div>
      <button type="button" class="hrms-brochure-menu-toggle d-xl-none" id="hrmsBrochureMenuToggle" aria-label="Open module menu">
        <i class="bi bi-list"></i>
      </button>
    </div>
    <div class="hrms-brochure-mobile-nav" id="hrmsBrochureMobileNav" hidden>
{nav_items()}
    </div>
  </header>

  <main class="main">

    <section class="hrms-brochure-cover" id="cover">
      <div class="container">
        <div class="row gy-5 align-items-center">
          <div class="col-lg-6" data-aos="fade-up">
            <p class="hrms-brochure-kicker">Artificial Intelligence Business Solutions LLC</p>
            <h1>AIVizion HRMS<br>Complete People Platform</h1>
            <p class="hrms-brochure-lead">A presentable overview of our Human Resource Management System — payroll, leave, recruitment, onboarding, offboarding, appraisal, and employee self-service — built for organizations in Oman and the GCC.</p>
            <div class="hrms-brochure-cover-meta">
              <span><i class="bi bi-geo-alt"></i> Muscat, Oman</span>
              <span><i class="bi bi-building"></i> Multi-company ready</span>
              <span><i class="bi bi-shield-check"></i> Role-based &amp; audit-ready</span>
            </div>
            <div class="hrms-product-cta-group">
              <a href="#overview" class="btn-primary">Start browsing</a>
              <a href="product-hrms.html" class="hrms-btn-ghost">Product page</a>
            </div>
          </div>
          <div class="col-lg-6" data-aos="fade-left" data-aos-delay="100">
            <div class="hrms-brochure-cover-visual">
              <img src="assets/img/hrimage/payroll-hero.png" alt="AIVizion HRMS payroll dashboard" loading="eager">
              <div class="hrms-brochure-cover-stack">
                <img src="assets/img/hrimage/recruitment-hero.png" alt="Recruitment pipeline" loading="lazy">
                <img src="assets/img/hrimage/leave-hero.png" alt="Leave management dashboard" loading="lazy">
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="hrms-brochure-jump">
      <div class="container">
        <p>Jump to a module</p>
        <div class="hrms-brochure-pill-row">
{module_nav_pills()}
        </div>
      </div>
    </section>

    <section class="hrms-brochure-overview section" id="overview">
      <div class="container">
        <div class="row gy-5 align-items-center">
          <div class="col-lg-6" data-aos="fade-up">
            <p class="hrms-brochure-kicker">Platform overview</p>
            <h2>People operations, simplified</h2>
            <p class="hrms-brochure-lead">AIVizion HRMS centralizes the employee lifecycle — from hiring and onboarding to payroll, leave, performance, and offboarding — in one connected platform.</p>
            <p>HR teams get dashboards and controlled workflows. Employees get self-service. Managers get clear approvals. Finance gets payroll outputs they can trust.</p>
            <ul class="hrms-check-list">
              <li><i class="bi bi-check2-circle"></i><span>End-to-end employee lifecycle in one system</span></li>
              <li><i class="bi bi-check2-circle"></i><span>AI-assisted workflows across modules</span></li>
              <li><i class="bi bi-check2-circle"></i><span>Role-based access for HR, managers, and staff</span></li>
              <li><i class="bi bi-check2-circle"></i><span>Multi-company and multi-branch support</span></li>
            </ul>
          </div>
          <div class="col-lg-6" data-aos="fade-left">
            <div class="hrms-brochure-overview-grid">
              <img src="assets/img/hrimage/ess-hero.png" alt="Employee self service" loading="lazy">
              <img src="assets/img/hrimage/onboarding-hero.png" alt="Onboarding journey" loading="lazy">
              <img src="assets/img/hrimage/appraisal-hero.png" alt="Appraisal dashboard" loading="lazy">
              <img src="assets/img/hrimage/offboarding-hero.png" alt="Offboarding control" loading="lazy">
            </div>
          </div>
        </div>
      </div>
    </section>

{module_sections()}

    <section class="hrms-brochure-platform section light-background" id="platform">
      <div class="container">
        <div class="section-title text-center" data-aos="fade-up">
          <h2>Platform capabilities</h2>
          <p>Shared foundations across every HRMS module</p>
        </div>
        <div class="row g-4">
          <div class="col-md-4" data-aos="fade-up">
            <div class="hrms-capability-item">
              <i class="bi bi-robot"></i>
              <span>AI integration across modules</span>
            </div>
          </div>
          <div class="col-md-4" data-aos="fade-up" data-aos-delay="50">
            <div class="hrms-capability-item">
              <i class="bi bi-shield-lock"></i>
              <span>Role-based access control</span>
            </div>
          </div>
          <div class="col-md-4" data-aos="fade-up" data-aos-delay="100">
            <div class="hrms-capability-item">
              <i class="bi bi-building"></i>
              <span>Multi-company operations</span>
            </div>
          </div>
          <div class="col-md-4" data-aos="fade-up">
            <div class="hrms-capability-item">
              <i class="bi bi-diagram-3"></i>
              <span>Connected HR workflows</span>
            </div>
          </div>
          <div class="col-md-4" data-aos="fade-up" data-aos-delay="50">
            <div class="hrms-capability-item">
              <i class="bi bi-graph-up"></i>
              <span>People &amp; payroll analytics</span>
            </div>
          </div>
          <div class="col-md-4" data-aos="fade-up" data-aos-delay="100">
            <div class="hrms-capability-item">
              <i class="bi bi-phone"></i>
              <span>Self-service on any device</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="hrms-product-cta-band section" id="contact-cta">
      <div class="container" data-aos="zoom-in">
        <div class="hrms-cta-panel">
          <div>
            <h2>Ready to present AIVizion HRMS to your team?</h2>
            <p>Share this brochure link, walk through the modules, or book a live demo with our team in Muscat.</p>
          </div>
          <div class="hrms-product-cta-group">
            <a href="index.html#contact" class="btn-primary">Request a Demo</a>
            <button type="button" class="hrms-btn-ghost" id="hrmsBrochureShareBottom">Copy brochure link</button>
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
          <p>Artificial Intelligence Business Solutions LLC — AI, ERP, HRMS, and digital transformation from Muscat, Oman.</p>
        </div>
        <div class="col-lg-3 col-6 footer-links">
          <h4>Brochure</h4>
          <ul>
            <li><a href="#overview">Overview</a></li>
            <li><a href="#hrms-payroll">Payroll</a></li>
            <li><a href="#hrms-recruitment">Recruitment</a></li>
            <li><a href="product-hrms.html">HRMS product page</a></li>
          </ul>
        </div>
        <div class="col-lg-4 col-md-12 footer-contact text-center text-md-start">
          <h4>Contact</h4>
          <p>Super Plaza, Building #340, Way #480, Azaiba</p>
          <p>Muscat, Oman</p>
          <p class="mt-3"><strong>Phone:</strong> <span>+968 24 506181</span></p>
          <p><strong>Email:</strong> <span>info@aibizs.com</span></p>
        </div>
      </div>
    </div>
    <div class="container copyright text-center mt-4">
      <p>© <span>Copyright</span> <strong class="px-1 sitename">AIBizs</strong> <span>All Rights Reserved</span></p>
    </div>
  </footer>

  <div class="hrms-brochure-toast" id="hrmsBrochureToast" hidden>Link copied — ready to share</div>
  <a href="#" id="scroll-top" class="scroll-top d-flex align-items-center justify-content-center"><i class="bi bi-arrow-up-short"></i></a>
  <div id="preloader"></div>

  <script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="assets/vendor/aos/aos.js"></script>
  <script src="assets/js/main.js"></script>
  <script>
    (function () {{
      const toast = document.getElementById('hrmsBrochureToast');
      const mobileNav = document.getElementById('hrmsBrochureMobileNav');
      const menuToggle = document.getElementById('hrmsBrochureMenuToggle');

      async function copyLink() {{
        const url = window.location.href.split('#')[0];
        try {{
          await navigator.clipboard.writeText(url);
        }} catch (err) {{
          const input = document.createElement('input');
          input.value = url;
          document.body.appendChild(input);
          input.select();
          document.execCommand('copy');
          input.remove();
        }}
        if (!toast) return;
        toast.hidden = false;
        toast.classList.add('is-visible');
        setTimeout(function () {{
          toast.classList.remove('is-visible');
          toast.hidden = true;
        }}, 2200);
      }}

      document.getElementById('hrmsBrochureShare')?.addEventListener('click', copyLink);
      document.getElementById('hrmsBrochureShareBottom')?.addEventListener('click', copyLink);

      menuToggle?.addEventListener('click', function () {{
        const open = mobileNav.hasAttribute('hidden');
        if (open) mobileNav.removeAttribute('hidden');
        else mobileNav.setAttribute('hidden', '');
      }});

      mobileNav?.querySelectorAll('a').forEach(function (link) {{
        link.addEventListener('click', function () {{
          mobileNav.setAttribute('hidden', '');
        }});
      }});

      const links = document.querySelectorAll('.hrms-brochure-nav-link, .hrms-brochure-pill');
      const sections = Array.from(document.querySelectorAll('.hrms-brochure-module, #overview, #platform, #contact-cta'));
      function syncActive() {{
        let current = 'overview';
        const y = window.scrollY + 140;
        sections.forEach(function (section) {{
          if (section.offsetTop <= y) current = section.id;
        }});
        links.forEach(function (link) {{
          const href = link.getAttribute('href') || '';
          link.classList.toggle('is-active', href === '#' + current);
        }});
      }}
      window.addEventListener('scroll', syncActive, {{ passive: true }});
      syncActive();
    }})();
  </script>
</body>

</html>
"""


def main():
    path = ROOT / "hrms-brochure.html"
    path.write_text(render(), encoding="utf-8")
    print(f"Wrote {path.name}")


if __name__ == "__main__":
    main()
