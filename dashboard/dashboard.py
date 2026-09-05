import sys
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


from app.services.event_logger import EventLogger


st.set_page_config(
    page_title="Vehicle Security Monitor",
    page_icon="🚗",
    layout="wide",
)


st.title("🚗 Vehicle Security Monitor")
st.caption("Cybersecurity Event Monitoring Dashboard")


logger = EventLogger()
events = logger.get_events()


# -------------------------------------------------------------------
# SYSTEM STATUS
# -------------------------------------------------------------------

st.success("SYSTEM ONLINE")


if not events:
    st.info("No security events have been recorded yet.")
    st.stop()


# -------------------------------------------------------------------
# SECURITY METRICS
# -------------------------------------------------------------------

critical_count = sum(1 for event in events if event[5] == "CRITICAL")
high_count = sum(1 for event in events if event[5] == "HIGH")
medium_count = sum(1 for event in events if event[5] == "MEDIUM")
low_count = sum(1 for event in events if event[5] == "LOW")

total_events = len(events)

threat_count = critical_count + high_count


st.subheader("Security Overview")


col1, col2, col3, col4, col5 = st.columns(5)


with col1:
    st.metric("Total Events", total_events)


with col2:
    st.metric("Threats", threat_count)


with col3:
    st.metric("Critical", critical_count)


with col4:
    st.metric("High", high_count)


with col5:
    st.metric("Medium / Low", medium_count + low_count)


st.divider()


# -------------------------------------------------------------------
# FILTERS
# -------------------------------------------------------------------

st.subheader("Event Filters")


vehicles = ["All"] + sorted(
    set(event[1] for event in events)
)

severities = ["All"] + sorted(
    set(event[5] for event in events)
)


filter_col1, filter_col2 = st.columns(2)


with filter_col1:

    selected_vehicle = st.selectbox(
        "Vehicle",
        vehicles,
    )


with filter_col2:

    selected_severity = st.selectbox(
        "Severity",
        severities,
    )


filtered_events = events


if selected_vehicle != "All":

    filtered_events = [
        event
        for event in filtered_events
        if event[1] == selected_vehicle
    ]


if selected_severity != "All":

    filtered_events = [
        event
        for event in filtered_events
        if event[5] == selected_severity
    ]


# -------------------------------------------------------------------
# SECURITY EVENTS
# -------------------------------------------------------------------

st.subheader("Security Events")


for event in filtered_events:

    event_id = event[0]
    vehicle_id = event[1]
    event_type = event[2]
    timestamp = event[3]
    source = event[4]
    severity = event[5]
    description = event[6]

    with st.container(border=True):

        st.write(f"**Event ID:** {event_id}")

        st.write(f"**Vehicle:** {vehicle_id}")

        st.write(f"**Event Type:** {event_type}")

        st.write(f"**Severity:** {severity}")

        st.write(f"**Source:** {source}")

        st.write(f"**Timestamp:** {timestamp}")

        st.write(f"**Description:** {description}")


# -------------------------------------------------------------------
# RISK DISTRIBUTION
# -------------------------------------------------------------------

st.subheader("Risk Distribution")


risk_data = {
    "CRITICAL": critical_count,
    "HIGH": high_count,
    "MEDIUM": medium_count,
    "LOW": low_count,
}


st.bar_chart(risk_data)


# -------------------------------------------------------------------
# LATEST EVENT
# -------------------------------------------------------------------

st.subheader("Latest Event Details")


latest_event = filtered_events[0]


detail_col1, detail_col2 = st.columns(2)


with detail_col1:

    st.write(f"**Event ID:** {latest_event[0]}")

    st.write(f"**Vehicle:** {latest_event[1]}")

    st.write(f"**Event Type:** {latest_event[2]}")

    st.write(f"**Severity:** {latest_event[5]}")


with detail_col2:

    st.write(f"**Source:** {latest_event[4]}")

    st.write(f"**Timestamp:** {latest_event[3]}")

    st.write(f"**Description:** {latest_event[6]}")


st.divider()


if st.button("🔄 Refresh Events"):

    st.rerun()