import streamlit as st

st.components.v1.html("""
<button id="setButton">set it</button>
<button id="getButton">get it</button>
<script>
    const set = () => {
        window.localStorage.setItem('bob', 'hi there baby')
    }
    
    const get = () => {
        alert(localStorage.getItem('bob'))
    }
    
    
    document.getElementById('setButton').addEventListener('click', set)
    document.getElementById('getButton').addEventListener('click', get)
</script>
""")
