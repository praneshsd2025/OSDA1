import streamlit as st
import subprocess
from pathlib import Path

st.set_page_config(
    page_title="OS System Call Demonstrator",
    page_icon="🖥️",
    layout="centered"
)

st.title("🖥️ OS System Call Demonstrator")
st.write("Demonstration of `getpid()`, `getppid()`, and `getuid()` system calls.")

st.info(
    "The application compiles and executes the C program on the same machine/server "
    "where Streamlit is running."
)

c_file = Path(__file__).parent / "system_calls.c"
exe_file = Path(__file__).parent / "system_calls"

st.subheader("System calls used")
col1, col2, col3 = st.columns(3)
col1.metric("getpid()", "Current PID")
col2.metric("getppid()", "Parent PID")
col3.metric("getuid()", "Real UID")

if st.button("▶ Run C Program", use_container_width=True):
    try:
        compile_result = subprocess.run(
            ["gcc", str(c_file), "-o", str(exe_file)],
            capture_output=True,
            text=True,
            timeout=10
        )

        if compile_result.returncode != 0:
            st.error("Compilation failed.")
            st.code(compile_result.stderr, language="text")
        else:
            run_result = subprocess.run(
                [str(exe_file)],
                capture_output=True,
                text=True,
                timeout=10
            )

            if run_result.returncode == 0:
                st.success("Program executed successfully.")
                st.subheader("Output")
                st.code(run_result.stdout, language="text")
            else:
                st.error("Program execution failed.")
                st.code(run_result.stderr, language="text")

    except FileNotFoundError:
        st.error(
            "GCC was not found. Install GCC and make sure the `gcc` command "
            "is available in the system PATH."
        )
    except subprocess.TimeoutExpired:
        st.error("The program took too long to finish.")
    except Exception as e:
        st.error(f"Unexpected error: {e}")

st.divider()
st.subheader("Explanation")
st.markdown("""
- **getpid()** returns the process ID of the calling process.
- **getppid()** returns the process ID of the parent of the calling process.
- **getuid()** returns the real user ID of the user who owns the process.
""")

st.caption("Operating Systems Digital Assignment – System Call Demonstration")
