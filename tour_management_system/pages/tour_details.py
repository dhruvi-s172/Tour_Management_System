import streamlit as st

from auth import require_role
from config import ROLES
from services.booking_service import get_tour
from ui.components import seat_meter
from utils.helpers import money


def render():
    if not require_role(ROLES["CUSTOMER"]):
        return
    tour_id = st.session_state.get("selected_tour_id")
    if not tour_id:
        st.warning("Select a tour package first.")
        if st.button("Go to Search"):
            st.session_state.page = "Search Tours"
            st.rerun()
        return
    tour = get_tour(tour_id)
    if not tour:
        st.error("Selected tour package was not found.")
        return

    st.markdown(
        f"""
        <section class='hero-premium' style="min-height:420px;background:linear-gradient(90deg, rgba(11,31,58,.88), rgba(18,53,107,.45)), url('{tour.image_url}'); background-size:cover; background-position:center;">
          <div class='hero-content'>
            <div class='hero-eyebrow'>{tour.category}</div>
            <h1 class='hero-title' style='font-size:clamp(2.5rem,5vw,4.7rem)'>{tour.title}</h1>
            <p class='hero-subtitle'>{tour.destination} | {tour.duration_days} days | {money(tour.price)} per person</p>
          </div>
        </section>
        """,
        unsafe_allow_html=True,
    )
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Destination", tour.destination)
    c2.metric("Duration", f"{tour.duration_days} days")
    c3.metric("Price", money(tour.price))
    c4.metric("Seats", f"{tour.available_seats}/{tour.total_seats}")
    st.markdown(seat_meter(tour.available_seats, tour.total_seats), unsafe_allow_html=True)

    st.markdown("### Overview")
    st.write(tour.description)
    st.markdown("### Day-wise Itinerary")
    for line in tour.itinerary.splitlines():
        st.markdown(f"- {line}")
    st.markdown("### Included Facilities")
    st.write("Hotel stay, guided sightseeing, selected meals, local transport, booking support, and a simulated digital payment receipt.")
    st.markdown("### Booking Information")
    st.info("Bookings reserve seats immediately and remain Pending Payment until the demo payment gateway confirms payment.")

    if st.button("Book Now", type="primary", use_container_width=True, disabled=tour.available_seats <= 0):
        st.session_state.page = "Booking"
        st.rerun()
