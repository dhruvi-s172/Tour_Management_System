import plotly.express as px
import streamlit as st

from auth import require_role
from config import ROLES
from services.report_service import chart_frames, dashboard_metrics
from ui.charts import polish
from utils.helpers import metric_card, money


def render():
    if not require_role(ROLES["ADMIN"]):
        return
    st.markdown("<div class='tm-card'><h1 style='margin:0'>Admin Dashboard</h1><p class='muted'>Live booking, revenue, package and customer analytics.</p></div>", unsafe_allow_html=True)
    metrics = dashboard_metrics()
    cols = st.columns(6)
    with cols[0]:
        metric_card("Customers", metrics["total_customers"])
    with cols[1]:
        metric_card("Packages", metrics["total_tours"])
    with cols[2]:
        metric_card("Bookings", metrics["total_bookings"])
    with cols[3]:
        metric_card("Confirmed", metrics["confirmed"])
    with cols[4]:
        metric_card("Cancelled", metrics["cancelled"])
    with cols[5]:
        metric_card("Revenue", money(metrics["revenue"]))

    frames = chart_frames()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("<div class='chart-card'><div class='chart-title'><strong>Bookings by Month</strong><span class='chip'>Trend</span></div>", unsafe_allow_html=True)
        st.plotly_chart(polish(px.bar(frames["monthly_bookings"], x="Month", y="Bookings"), "Bookings by Month"), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='chart-card'><div class='chart-title'><strong>Revenue by Month</strong><span class='chip'>Paid only</span></div>", unsafe_allow_html=True)
        st.plotly_chart(polish(px.line(frames["monthly_revenue"], x="Month", y="Revenue", markers=True), "Revenue by Month"), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    c3, c4 = st.columns(2)
    with c3:
        st.markdown("<div class='chart-card'><div class='chart-title'><strong>Popular Destinations</strong><span class='chip'>Leaderboard</span></div>", unsafe_allow_html=True)
        st.plotly_chart(polish(px.bar(frames["destinations"], x="Destination", y="Bookings"), "Popular Destinations"), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    with c4:
        st.markdown("<div class='chart-card'><div class='chart-title'><strong>Status Distribution</strong><span class='chip'>Mix</span></div>", unsafe_allow_html=True)
        st.plotly_chart(polish(px.pie(frames["status"], names="Booking Status", values="Count", hole=.45), "Booking Status Distribution"), use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div class='chart-card'><div class='chart-title'><strong>Tour Category Distribution</strong><span class='chip'>Catalog</span></div>", unsafe_allow_html=True)
    st.plotly_chart(polish(px.pie(frames["categories"], names="Category", values="Packages", hole=.5), "Tour Category Distribution"), use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)
