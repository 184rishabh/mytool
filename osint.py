import streamlit as st
import time
from datetime import datetime
import subprocess


st.set_page_config(
    page_title="OSINT App",
    page_icon="",
    layout="wide"
)

st.markdown("""
<style>
body {
    background-color: #0E1117;
}
.main {
    background-color: #0E1117;
}
h1, h2, h3, h4 {
    color: #00C8FF;
}
.stButton>button {
    background-color: #00C8FF;
    color: black;
    border-radius: 8px;
    font-weight: bold;
}
.block-container {
    padding-top: 2rem;
}
.card {
    background-color: #161B22;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 0px 10px rgba(0,200,255,0.2);
}
.footer {
    text-align: center;
    padding: 10px;
    color: gray;
    margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)


st.sidebar.title("OSINT")
menu = st.sidebar.radio("Navigation", [
    "Dashboard",
    "Username Search",
    "Email Intelligence",
    "Phone Lookup",
    "IP Scanner",
    "Reports"
])

st.sidebar.markdown("---")
st.sidebar.info("Made by Rishabh kr singh")


if menu == "Dashboard":

    st.markdown("""
    <style>
    .hero-container {
        text-align: center;
    }

    .hero-title {
        font-size: 48px;
        font-weight: bold;
        background: linear-gradient(90deg, #00C8FF, #00FFAA);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }

    .hero-subtitle {
        font-size: 20px;
        color: #AAAAAA;
        max-width: 900px;
        margin: auto;
        line-height: 1.6;
    }

    .feature-box {
        background-color: #161B22;
        padding: 30px;
        border-radius: 15px;
        margin-top: 40px;
        box-shadow: 0px 0px 20px rgba(0,200,255,0.15);
    }

    .typing {
        color: #00FFAA;
        font-family: monospace;
        font-size: 22px;
        margin-top: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero-container">
         <div class="hero-title">
         OSINT Tool
    </div>

    <div class="hero-subtitle">
        A digital intelligence platform designed to analyze and investigate 
        digital footprints across the internet. 
        <br><br>
        This system automates open-source intelligence gathering 
        through powerful reconnaissance tools integrated into a unified dashboard.
    </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="feature-box">
        <h3 style="color:#00C8FF;">🔍 What This Platform Does</h3>
        <ul style="color:#CCCCCC; font-size:18px; line-height:1.8;">
            <li><b>Username Search</b> — Discover digital footprints across platforms</li>
            <li><b>Email Intelligence</b> — Analyze exposure and reconnaissance data</li>
            <li><b>Phone Lookup</b> — Extract communication-related metadata</li>
            <li><b>IP Intelligence</b> — Perform network-level reconnaissance and geolocation</li>
        </ul>
        <p style="color:#AAAAAA;">
        Built as a cybersecurity research project, this suite demonstrates 
        automated CLI tool integration, real-time output streaming, and 
        structured intelligence analysis inside a modern web interface.
        </p>
    </div>
    """, unsafe_allow_html=True)


elif menu == "Username Search":

    st.title("👤 Username Intelligence")

    username = st.text_input("Enter Username")

    if st.button("🔍 Run Username Scan"):

        if username.strip() == "":
            st.warning("Please enter a username")
        else:
            st.subheader("📡 Live Scan Output")
            output_box = st.empty()

            command = ["user-scanner", "-u", username]

            try:
                process = subprocess.Popen(
                    command,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )

                process.stdin.write("n\n")
                process.stdin.flush()

                full_output = ""
          
                for line in iter(process.stdout.readline, ''):
                    full_output += line
                    output_box.code(full_output)

                process.wait()

                st.success("Username Scan Completed")

            except Exception as e:
                st.error(f"Error: {e}")



elif menu == "Email Intelligence":

    st.title("📧 Email Intelligence")

    email = st.text_input("Enter Email Address")

    if st.button("🔍 Run Email Scan"):

        if email.strip() == "":
            st.warning("Please enter an email")
        else:
            st.subheader("📡 Live Scan Output")
            output_box = st.empty()

            command = ["user-scanner", "-e", email]

            try:
                process = subprocess.Popen(
                    command,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )

                process.stdin.write("n\n")
                process.stdin.flush()

                full_output = ""
                for line in iter(process.stdout.readline, ''):
                    full_output += line
                    output_box.code(full_output)

                process.wait()

                st.success("Email Scan Completed")

            except Exception as e:
                st.error(f"Error: {e}")


elif menu == "Phone Lookup":

    st.title("📱 Phone Intelligence")

    phone = st.text_input("Enter Phone Number (with country code)")

    if st.button("🔍 Run Phone Scan"):

        if phone.strip() == "":
            st.warning("Please enter phone number")
        else:
            st.subheader("📡 Live Scan Output")
            output_box = st.empty()

            try:
               
                command = ["python3", "tool/tool1.py"]
                process = subprocess.Popen(
                    command,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )

                process.stdin.write("1\n")
                process.stdin.flush()

                process.stdin.write(phone + "\n")  
                process.stdin.flush()

                full_output = ""
                for line in iter(process.stdout.readline, ''):
                     full_output += line
                     output_box.code(full_output)

                process.wait()

                st.success("Phone Scan Completed")

            except Exception as e:
                st.error(f"Error: {e}")

elif menu == "IP Scanner":

    st.title("🌐 IP Intelligence Scanner")

    ip = st.text_input("Enter IP Address")

    if st.button("🔍 Run IP Scan"):

        if ip.strip() == "":
            st.warning("Please enter IP address")
        else:
            st.subheader("📡 Live Scan Output")
            output_box = st.empty()

            try:
                
                command = ["python3", "tool/tool1.py"]

                process = subprocess.Popen(
                    command,
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )

                
                process.stdin.write("2\n")
                process.stdin.flush()

                
                process.stdin.write(ip + "\n")
                process.stdin.flush()

                full_output = ""

                for line in iter(process.stdout.readline, ''):
                    full_output += line
                    output_box.code(full_output)

                process.wait()

                st.success("IP Scan Completed")

            except Exception as e:
                st.error(f"Error: {e}")


elif menu == "Reports":

    st.title("📁 Intelligence Reports")

    st.write("Generate and download investigation reports.")

    if st.button("📄 Generate Sample Report"):
        with st.spinner("Generating report..."):
            time.sleep(2)

        st.success("Report Ready")

        st.download_button(
            label="⬇ Download PDF Report",
            data=b"Sample PDF content",
            file_name="osint_report.pdf",
            mime="application/pdf"
        )


st.markdown("""
<div class="footer">
Developed By Rishabh Kr Singh | 2026
</div>
""", unsafe_allow_html=True)
