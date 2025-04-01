import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

Time_Zone = [
    "UTC",
    "Asia/Karachi", 
    "America/Los_Angeles",
    "America/New_York",
    "Europe/London",
    "Australia/Sydney",
    "Africa/Cairo",
    "Asia/Tokyo",
    "Asia/Dubai",
    "Asia/Kolkata",
]

st.title("🌍 Time_Zone_App")

Select_Time_Zone = st.multiselect("Select Time-Zone", Time_Zone, default=["UTC"])
st.subheader("Select Time-Zone")

for tz in Select_Time_Zone:
    current_Time = datetime.now(ZoneInfo(tz)).strftime("%Y:%m:%d %I %H:%M:%S %p")
    st.write(f" Current Time in **{tz}** is {current_Time}")



    st.subheader("Convert Timezone Between Time")
    current_time = st.time_input( " Current Time" , value=datetime.now().time())
    from_tz = st.selectbox("From Timezone", Time_Zone , index=0)
    to_tz= st.selectbox("To Timezone",Time_Zone,index=1)

    if st.button( "Convert Timezone") :
      dt=datetime.combine(datetime.today(),current_time ,tzinfo= ZoneInfo(from_tz))
    Converted_time=dt.astimezone(ZoneInfo(to_tz))
    st.success (f"Converted Time  in { to_tz} is { Converted_time.strftime('%Y:%m:%d %I %H:%M:%S %p')}")