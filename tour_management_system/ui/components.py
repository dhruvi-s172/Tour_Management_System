from html import escape
from math import ceil

from ui.icons import icon


def category_class(category: str) -> str:
    return "cat-" + (category or "").lower().replace(" ", "-")


def hero() -> str:
    destinations = ["Goa", "Manali", "Kashmir", "Bali", "Dubai", "Japan", "Maldives", "Spiti", "Singapore", "Kerala"]
    chips = "".join(f"<span class='dest-chip'>{escape(item)}</span>" for item in destinations * 2)
    return f"""
    <section class='hero-premium'>
      <div class='plane-float'>{icon('plane', 92)}</div>
      <div class='hero-content'>
        <div class='hero-eyebrow'>{icon('spark', 16)} Premium travel-tech demo</div>
        <h1 class='hero-title'>
          <span class='hero-word'>Explore.</span>
          <span class='hero-word'>Book.</span>
          <span class='hero-word hero-gradient'>Travel.</span>
        </h1>
        <p class='hero-subtitle'>Plan your perfect journey with smart search, seamless bookings, simulated payments, resource allocation, and real dashboard analytics.</p>
        <div class='hero-actions'>
          <a class='cta-pill' href='#popular-packages'>{icon('search', 18)} Explore Packages</a>
          <a class='ghost-pill' href='#how-it-works'>{icon('map', 18)} See Workflow</a>
        </div>
        <div class='hero-stats'>
          <div class='hero-stat'><strong>36+</strong><span>curated packages</span></div>
          <div class='hero-stat'><strong>7</strong><span>tour categories</span></div>
          <div class='hero-stat'><strong>100%</strong><span>offline demo ready</span></div>
        </div>
      </div>
    </section>
    <div class='marquee' aria-label='Featured destinations'><div class='marquee-track'>{chips}</div></div>
    """


def page_header(title: str, subtitle: str = "", icon_name: str = "spark") -> str:
    return f"""
    <div class='tm-card' style='margin-bottom:1rem;'>
      <div style='display:flex;align-items:center;gap:.85rem;'>
        <div class='metric-icon'>{icon(icon_name, 22)}</div>
        <div>
          <h1 style='margin:0'>{escape(title)}</h1>
          <div class='muted'>{escape(subtitle)}</div>
        </div>
      </div>
    </div>
    """


def kpi_card(label: str, value: str, icon_name: str = "chart", trend: str = "Live") -> str:
    return f"""
    <div class='metric-card'>
      <div class='metric-icon'>{icon(icon_name, 21)}</div>
      <div>
        <div class='label'>{escape(label)}</div>
        <div class='value'>{escape(str(value))}</div>
        <div class='metric-trend'>{escape(trend)}</div>
      </div>
    </div>
    """


def status_badge(status: str) -> str:
    cls = (status or "").lower().replace(" ", "-")
    if status == "Pending Payment":
        cls = "pending"
    return f"<span class='badge {escape(cls)}'>{escape(status or '-')}</span>"


def seat_meter(available: int, total: int) -> str:
    total = max(int(total or 0), 1)
    available = max(int(available or 0), 0)
    percent = min(100, max(0, (available / total) * 100))
    label = f"{available} of {total} seats available"
    urgency = "<span class='few-seats'>Few seats left</span>" if available < 5 else ""
    return f"<div class='seat-meter' style='--fill:{percent:.0f}%'><span></span></div><div class='tiny muted'>{escape(label)} {urgency}</div>"


def tour_card(tour) -> str:
    category = escape(tour.category or "")
    return f"""
    <article class='tour-card'>
      <div class='tour-media'>
        <span class='category-badge {category_class(tour.category)}'>{category}</span>
        <img src='{escape(tour.image_url or "")}' alt='{escape(tour.title)}' loading='lazy' onerror="this.style.opacity='0'">
        <div class='price-badge'>Rs. {float(tour.price):,.0f}</div>
      </div>
      <div class='tour-body'>
        <h3 class='tour-title'>{escape(tour.title)}</h3>
        <div class='muted'>{escape(tour.destination)}</div>
        <div class='tour-meta'>
          <span class='chip'>{icon('calendar', 14)} {tour.duration_days} days</span>
          <span class='chip'>{icon('users', 14)} {tour.available_seats} seats</span>
        </div>
        <p class='tiny'>{escape((tour.description or '')[:128])}...</p>
        {seat_meter(tour.available_seats, tour.total_seats)}
      </div>
    </article>
    """


def stepper(current_step: str) -> str:
    steps = ["Booking", "Payment", "Confirmation"]
    current_index = steps.index(current_step) if current_step in steps else 0
    html = "<div class='stepper'>"
    for index, step in enumerate(steps):
        klass = "done" if index < current_index else "active" if index == current_index else ""
        html += f"<span class='step {klass}'>{index + 1}. {escape(step)}</span>"
        if index < len(steps) - 1:
            html += "<span class='step-line'></span>"
    html += "</div>"
    return html


def timeline(status: str, payment_status: str = "") -> str:
    if status == "Cancelled":
        items = [("Booked", "done"), ("Cancelled", "active")]
    else:
        items = [
            ("Booked", "done"),
            ("Payment Confirmed", "done" if payment_status == "Paid" else "active"),
            ("Tour Confirmed", "done" if status in ["Confirmed", "Modified", "Completed"] else ""),
            ("Completed", "done" if status == "Completed" else ""),
        ]
    html = "<div class='stepper'>"
    for idx, (label, klass) in enumerate(items):
        html += f"<span class='step {klass}'>{escape(label)}</span>"
        if idx < len(items) - 1:
            html += "<span class='step-line'></span>"
    html += "</div>"
    return html


def empty_state(title: str, text: str) -> str:
    return f"""
    <div class='empty-state'>
      <div style='font-size:2.4rem'>{icon('map', 42)}</div>
      <h3>{escape(title)}</h3>
      <p class='muted'>{escape(text)}</p>
    </div>
    """


def alert(kind: str, title: str, msg: str) -> str:
    name = "check" if kind == "success" else "x" if kind == "error" else "spark"
    return f"<div class='tm-card'>{icon(name, 22)} <strong>{escape(title)}</strong><p class='muted'>{escape(msg)}</p></div>"


def price_summary(tour, travelers: int) -> str:
    subtotal = float(tour.price) * int(travelers)
    service = 0
    rows = [
        ("Price per person", f"Rs. {float(tour.price):,.0f}"),
        ("Travelers", str(travelers)),
        ("Service fee", f"Rs. {service:,.0f}"),
    ]
    row_html = "".join(f"<div style='display:flex;justify-content:space-between;margin:.45rem 0'><span>{escape(k)}</span><strong>{escape(v)}</strong></div>" for k, v in rows)
    return f"""
    <aside class='ticket-card'>
      <h3 style='margin-top:0'>{escape(tour.title)}</h3>
      <div class='muted'>{escape(tour.destination)} | {tour.duration_days} days</div>
      {row_html}
      <hr style='border:0;border-top:1px dashed #CBD5E1;margin:1rem 0'>
      <div style='display:flex;justify-content:space-between;align-items:center'><span>Total</span><strong class='price' style='font-size:1.5rem'>Rs. {subtotal + service:,.0f}</strong></div>
    </aside>
    """
